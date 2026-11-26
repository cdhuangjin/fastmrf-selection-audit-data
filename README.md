# Fixed-budget shape matching: per-pair audit data

Run `python reproduce.py` with Python 3.8 or later. The script uses the standard library and reads the CSV files relative to its own directory.

- **baseline.csv** contains 190 FAUST descriptor–pair records: 100 ULRSSM, 45 WKS and 45 SHOT. The columns give nearest-neighbor and orientation-corrected FastMRF outcomes.
- **selection.csv** contains paired binary and expanded arms for two proposal sources on the same 37 FAUST and 20 SCAPE pairs. Expanded pools have four distinct non-base alternatives per vertex. Each arm uses the same local score and matched edit count within a pair. The script reports how expansion changes attainable and realized losses and the location, label and mandatory-edit components.
- **gating.csv** contains 100 FAUST, 20 SCAPE and 37 reconstructed TOPFAUST pairs under joint ULRSSM gating. Single and Ungated columns refer to corrected single-descriptor FastMRF and unrestricted mixing at the matched allowance.

Geodesic error is normalized by target diameter. Dirichlet energy measures map smoothness. Lower values favor the evaluated map. Rows sharing shapes are dependent. Counts across these files concern overlapping experimental conditions. This deposit reproduces the main aggregate comparisons from frozen measurements. Meshes, model weights, external solver code, per-vertex maps and additional sensitivity experiments are outside its scope.
