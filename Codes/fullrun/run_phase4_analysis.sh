#!/usr/bin/env bash
# Run the frozen Phase-4 analysis scripts over the FULL-RUN extractions.
#
# WHY THIS WRAPPER EXISTS
# -----------------------
# analyze_expansion.py, threshold_sensitivity.py, majority_vote.py and
# per_model_pass.py all honour --runs for INPUT but hard-code their OUTPUT to
# Codes/analysis/expansion/out/. Pointing them at the full run therefore
# overwrites the frozen Phase-4 CSVs that the current 30-page draft cites.
#
# This script stashes those frozen files, runs the analysis, moves the results
# into Codes/fullrun/out/, and puts the frozen files back. The frozen numbers
# stay quotable; the full-run numbers land somewhere separate.
#
# Usage:  ./run_phase4_analysis.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXP="$HERE/../analysis/expansion"
# The four scripts write to TWO different frozen output dirs, neither of which
# honours --runs: analyze_expansion -> expansion/out, threshold_sensitivity /
# majority_vote / per_model_pass -> analysis/out. Both must be protected.
FROZEN_DIRS=("$EXP/out" "$HERE/../analysis/out")
STASH="$(mktemp -d)"
DEST="$HERE/out"
mkdir -p "$DEST"

if [ ! -d "$HERE/runs_clean" ]; then
  echo "No runs_clean/. Run: python run_full.py && python extract_and_score.py" >&2
  exit 1
fi

for i in "${!FROZEN_DIRS[@]}"; do
  mkdir -p "$STASH/$i"
  cp -a "${FROZEN_DIRS[$i]}/." "$STASH/$i/"
done
echo "Stashed frozen Phase-4 outputs -> $STASH"

restore() {
  echo "Restoring frozen Phase-4 outputs"
  for i in "${!FROZEN_DIRS[@]}"; do
    for f in "$STASH/$i"/*; do
      [ -f "$f" ] && cat "$f" > "${FROZEN_DIRS[$i]}/$(basename "$f")"
    done
  done
}
trap restore EXIT

cd "$EXP"
for script in analyze_expansion.py threshold_sensitivity.py majority_vote.py per_model_pass.py; do
  echo "=== $script ==="
  python3 "$script" --runs "$HERE/runs_clean" || echo "  ($script failed; continuing)"
done

echo "Collecting full-run results -> $DEST"
for i in "${!FROZEN_DIRS[@]}"; do
  for f in "${FROZEN_DIRS[$i]}"/*; do
    [ -f "$f" ] || continue
    base="$(basename "$f")"
    # anything that changed relative to the stash is a full-run result
    if ! cmp -s "$f" "$STASH/$i/$base"; then
      cp "$f" "$DEST/full_$base"
      echo "  full_$base"
    fi
  done
done

echo
echo "Full-run analysis in $DEST"
echo "Frozen Phase-4 CSVs are unchanged."
