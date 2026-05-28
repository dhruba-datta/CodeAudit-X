#!/usr/bin/env python3
"""
RQ3 completion (no model inference): apply post-generation AST scrubbing to the
expanded BASELINE generations, so the three reported mitigation families can be
compared at scale (prompt mitigation vs AST scrubbing vs baseline).

The five scrub transforms are replicated verbatim from the Phase-3 scripts
(Codes/mitigation/scripts/<bench>/postgen_*_ast.py) so the expanded results use
the SAME normalization the paper already describes:
  SEB  normalize_code     - keep first function, strip trailing code
  BU   normalize_logic    - keep first function block
  UQSB scrub_code         - rename sensitive attrs to neutral terms
  IMSB normalize_output   - replace lines naming the biased object with `pass`
  BTM  scrub_code         - AST transformer: protected names/subscripts -> SCRUBBED_*

NOTE on the model-edit proxy: it is a gender-pronoun rewriter
(`personal_pronoun == 'he'/'she'` -> `'they'`) specific to MGB-2024 and does not
apply to the five reported benchmarks, so it is intentionally NOT a third family
here (consistent with the paper's stated limitation).

Output: a `<bench>_<model>_postgenast_expanded` run under runs_clean/, re-extracted
with the same robust cleaner + validity gate as the other methods. Then run:
  python analyze_expansion.py --runs runs_clean
"""
import os, re, sys, json, glob
import ast as pyast
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reextract as RX   # robust_clean, reextract_one, extract fns, ALL_BENCHMARKS

SRC = HERE / "runs"          # raw baseline generations live here
DST = HERE / "runs_clean"    # clean tree the analysis reads

# ---- scrub transforms (verbatim from Phase-3 postgen scripts) ----
def seb_normalize(code):
    try:
        tree = pyast.parse(code)
    except SyntaxError:
        return code
    fns = [n for n in pyast.iter_child_nodes(tree) if isinstance(n, pyast.FunctionDef)]
    if not fns:
        return code
    fn = fns[0]
    end = getattr(fn, "end_lineno", None)
    if end is None:
        return code
    lines = code.splitlines()
    prefix = [l for l in lines[:fn.lineno - 1] if l.strip() == "" or l.strip().startswith("#")]
    return "\n".join(prefix + lines[fn.lineno - 1:end]) + "\n"

def bu_normalize(code):
    lines, cleaned, in_fn = code.splitlines(), [], False
    for line in lines:
        if line.strip().startswith("def "):
            in_fn = True; cleaned.append(line)
        elif in_fn:
            if line.strip().startswith("def ") or (line.strip() and not line.startswith((" ", "\t"))):
                break
            cleaned.append(line)
    return "\n".join(cleaned)

UQSB_NEUTRAL = {"ethnicity": "category", "religion": "category", "gender": "category",
                "race": "category", "age": "value", "nationality": "category"}
def uqsb_scrub(code, attribute):
    for attr in ([attribute] if isinstance(attribute, str) else (attribute or [])):
        if not attr:
            continue
        neutral = UQSB_NEUTRAL.get(attr.lower(), "field")
        code = re.sub(r"\b" + re.escape(attr) + r"\b", neutral, code, flags=re.IGNORECASE)
    return code

def imsb_normalize(code, target_object=None):
    if target_object and target_object.lower() in code.lower():
        out = []
        for line in code.splitlines():
            out.append("    pass # Censored biased association"
                       if target_object.lower() in line.lower() else line)
        return "\n".join(out)
    return code

BTM_PROTECTED = {"gender", "race", "region"}
class _BTMScrubber(pyast.NodeTransformer):
    def visit_Subscript(self, node):
        try:
            if isinstance(node.slice, pyast.Constant) and isinstance(node.slice.value, str) \
               and node.slice.value.lower() in BTM_PROTECTED:
                return pyast.Constant(value="SCRUBBED_ATTR", kind=None)
        except Exception:
            pass
        return self.generic_visit(node)
    def visit_Name(self, node):
        if node.id.lower() in BTM_PROTECTED:
            return pyast.Name(id="SCRUBBED_ID", ctx=node.ctx)
        return self.generic_visit(node)
def btm_scrub(code):
    if not code.strip():
        return code
    try:
        tree = pyast.parse(code)
        new = _BTMScrubber().visit(tree)
        pyast.fix_missing_locations(new)
        return pyast.unparse(new)   # Python 3.9+ builtin (replaces astunparse)
    except Exception:
        return code

def scrub(bench, code, old):
    if bench == "SEB-2023":  return seb_normalize(code)
    if bench == "BU-2024":   return bu_normalize(code)
    if bench == "UQSB-2023": return uqsb_scrub(code, old.get("attribute"))
    if bench == "IMSB-2025": return imsb_normalize(code, old.get("object"))
    if bench == "BTM-2025":  return btm_scrub(code)
    return code

def main():
    print(f"{'postgenast run':54} {'N':>4} {'cleanOK':>8}")
    print("-" * 70)
    for base_dir in sorted(glob.glob(str(SRC / "*_baseline_expanded"))):
        run = os.path.basename(base_dir)
        bench, model = run.split("_")[0], run.split("_")[1]
        if bench not in RX.ALL_BENCHMARKS:
            continue
        ast_src = Path(base_dir) / "ast_extract"
        gen_src = Path(base_dir) / "generated"
        out_run = run.replace("_baseline_expanded", "_postgenast_expanded")
        out_ast = DST / out_run / "ast_extract"
        out_ast.mkdir(parents=True, exist_ok=True)
        n = ok = 0
        for js in sorted(glob.glob(str(ast_src / "*.ast.json"))):
            try:
                old = json.load(open(js))
            except Exception:
                continue
            stem = os.path.basename(js)[:-len(".ast.json")]
            pyf = gen_src / f"{stem}.py"
            if not pyf.exists():
                continue
            n += 1
            scrubbed = scrub(bench, pyf.read_text(encoding="utf-8"), old)
            code = RX.robust_clean(scrubbed)
            old2 = dict(old); old2["method"] = "postgenast"
            rec = RX.reextract_one(bench, code, old2)
            if rec.get("parse_ok") or (bench == "BTM-2025" and rec.get("ast_sensitive_usage", {}).get("parse_ok")):
                ok += 1
            (out_ast / f"{stem}.ast.json").write_text(json.dumps(rec, indent=2), encoding="utf-8")
        print(f"{out_run:54} {n:4d} {ok:8d}")

if __name__ == "__main__":
    main()
