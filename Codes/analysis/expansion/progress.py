#!/usr/bin/env python3
"""
Live progress dashboard for the expansion sweep (and the verify batch).
Usage:
  python3 Codes/analysis/expansion/progress.py            # the full sweep (runs/)
  python3 Codes/analysis/expansion/progress.py verify_runs # the verify batch
Pure filesystem read; safe to run anytime, even while the sweep is running.
"""
import json, glob, os, time, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROBE = os.path.join(HERE, "probes")
SEEDS = 3
METHODS = 3
MODELS = ["deepseek1.3b", "qwen1.5b", "codegen350M"]
BENCHES = ["SEB-2023", "BU-2024", "UQSB-2023", "IMSB-2025", "BTM-2025"]

def expected_per_model():
    exp = {}
    for b in BENCHES:
        d = json.load(open(os.path.join(PROBE, f"{b}.json")))
        if b == "SEB-2023":
            n = sum(len(p["variants"]) for p in d["probes"])
        elif b == "BU-2024":
            n = sum(len(t["variants"]) for t in d["tasks"])
        elif b == "UQSB-2023":
            n = len(d["probes"])
        elif b == "IMSB-2025":
            n = len(d["triplets"])
        else:  # BTM
            n = len(d["prompts"])
        exp[b] = n * SEEDS * METHODS   # per model
    return exp

def count_actual(runs_dir):
    res = {}
    for f in glob.glob(os.path.join(runs_dir, "*", "generated", "*.py")):
        run = os.path.basename(os.path.dirname(os.path.dirname(f)))
        core = run[:-len("_expanded")] if run.endswith("_expanded") else run
        parts = core.split("_")
        if len(parts) < 2:
            continue
        bench, model = parts[0], parts[1]
        res.setdefault(bench, {}).setdefault(model, 0)
        res[bench][model] += 1
    return res

def recent_rate(runs_dir, window=120):
    now = time.time(); c = 0
    for f in glob.glob(os.path.join(runs_dir, "*", "generated", "*.py")):
        try:
            if now - os.path.getmtime(f) <= window:
                c += 1
        except OSError:
            pass
    return c / (window / 60.0)  # gen/min

def bar(frac, width=28):
    n = int(max(0, min(1, frac)) * width)
    return "#" * n + "." * (width - n)

def main():
    runs_dir = os.path.join(HERE, sys.argv[1]) if len(sys.argv) > 1 else os.path.join(HERE, "runs")
    if not os.path.isdir(runs_dir):
        alt = os.path.join(HERE, "verify_runs")
        runs_dir = alt if os.path.isdir(alt) else runs_dir

    exp = expected_per_model()
    total_exp = sum(exp.values()) * len(MODELS)
    act = count_actual(runs_dir)
    total_act = sum(sum(m.values()) for m in act.values())

    print(time.strftime("%H:%M:%S"), "| dir:", os.path.relpath(runs_dir))
    frac = total_act / total_exp if total_exp else 0
    print(f"TOTAL  {total_act:5d}/{total_exp:<5d} {100*frac:5.1f}%  [{bar(frac)}]")
    r = recent_rate(runs_dir)
    if r > 0:
        eta_h = (total_exp - total_act) / r / 60
        print(f"rate ~{r:.1f} gen/min over last 2 min   ETA ~{eta_h:.1f} h")
    else:
        print("rate ~0 (idle, paused, or model loading)")
    print("-" * 60)
    for b in BENCHES:
        e = exp[b]
        cells = []
        for mdl in MODELS:
            a = act.get(b, {}).get(mdl, 0)
            mark = "OK" if a >= e else "  "
            cells.append(f"{mdl.split('1')[0][:8]:8}{a:3d}/{e:<3d}{mark}")
        print(f"{b:11} " + " ".join(cells))

if __name__ == "__main__":
    main()
