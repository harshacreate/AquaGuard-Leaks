# AquaGuard-Leaks — Water Network Leak Detection Prototype

**Sector:** Water utilities  
**Task:** Binary classification: synthetic leak window

Identifies generated leak windows from pressure, flow, acoustic level, pipe age, night demand, and vibration. Pipe segments are held out by group.

## Data and provenance

The offline demo uses a deterministic synthetic generator in `aquaguard/data.py`. It does not use or download real records, and no external data license applies. Synthetic output is only a benchmark for this simulator, not evidence of real-world performance.

## Method

- **Baseline:** majority-class prior classifier.
- **Stronger model:** histogram gradient-boosting classifier.
- **Split:** grouped holdout by machine, pipe, camera, or contractor (IDs are excluded from the model inputs).
- **Metrics:** accuracy, balanced accuracy, macro F1, confusion matrix, ROC-AUC, average precision, precision, and recall.
- **Error analysis:** confusion matrix and total misclassification count.

## Limitations

The leak signal is injected by a simulator and is more regular than field telemetry. Outputs cannot replace field inspection or operator review.

## Run

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -e ".[test]"
    python -m aquaguard.train --seed 42 --samples 2400 --json
    python -m pytest -q

`make setup`, `make train`, and `make test` are shortcuts. Python 3.9 or newer is required.

## Layout and license

- `aquaguard/data.py`: synthetic generator and validation.
- `aquaguard/split.py`: entity-group split.
- `aquaguard/model.py`: baseline, stronger model, metrics, and subgroup diagnostics.
- `aquaguard/train.py`: CLI.
- `tests/`: data, split, model, metric, and CLI checks.
- `.github/workflows/ci.yml`: CI.

No code license has been selected for this new project; default copyright rules apply. Choose a license before public distribution.
