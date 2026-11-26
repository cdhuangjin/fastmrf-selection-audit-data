"""Recompute cohort means from the deposited per-pair measurements."""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent

def groups(filename, *keys):
    out = defaultdict(list)
    with (ROOT / filename).open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            out[tuple(row[k] for k in keys)].append(row)
    return out

def average(rows, field):
    return mean(float(row[field]) for row in rows)

print("Corrected baseline: descriptor, n, NN and MRF geodesic, NN and MRF Dirichlet, Dirichlet increases")
for (desc,), rows in sorted(groups("baseline.csv", "descriptor").items()):
    print(desc, len(rows), *(f"{average(rows,k):.6f}" for k in
          ("nn_geodesic","new_mrf_geodesic","nn_dirichlet","new_mrf_dirichlet")),
          sum(float(r["new_mrf_dirichlet"]) > float(r["nn_dirichlet"]) for r in rows))

arms = groups("selection.csv", "dataset", "proposer", "arm")
print("Expanded minus binary: cohort, proposer, pairs, attainable, realized, location, label, mandatory")
for ds, proposer in sorted({key[:2] for key in arms}):
    a, b = arms[ds,proposer,"plus_top4"], arms[ds,proposer,"binary"]
    assert [(r["source"],r["target"],r["edits"]) for r in a] == [(r["source"],r["target"],r["edits"]) for r in b]
    print(ds, proposer, len(a), *(f"{average(a,k)-average(b,k):+.9f}" for k in
          ("at_most","observed","location","label","mandatory_edits")))

print("Joint gate: cohort, n, geodesic vs open, geodesic vs single, Dirichlet vs single")
for (ds,), rows in sorted(groups("gating.csv", "dataset").items()):
    print(ds,len(rows), *(f"{average(rows,k)-average(rows,k+'_Baseline-'+comp):+.6f}" for k,comp in
          (("geodesic","Ungated"),("geodesic","Single"),("dirichlet","Single"))))
