# Project notes

## Current version
- Uses the UCI Machine Learning Repository's Default of Credit Card Clients dataset (ID 350).
- Data is retrieved at runtime through `ucimlrepo`; raw customer-level records are not committed.
- The notebook and training script are intended to generate the visualizations and metrics on execution.
- No model performance figures should be documented until the current code has been run and the metrics reproduced.

## Reproducibility checklist
- [ ] Install dependencies from `requirements.txt`.
- [ ] Run the notebook from top to bottom with internet access.
- [ ] Run `python src/train_model.py` from the repository root.
- [ ] Confirm generated chart files and record environment/package versions.
- [ ] Record the exact split, metrics, and any deviations in this report.

## Interpretation cautions
The dataset is historical Taiwanese credit-card client data from 2005. The models are educational baselines and are not validated for current lending decisions. Accuracy alone is insufficient; report class-specific precision/recall, balanced accuracy, ROC-AUC, and confusion matrices. See `docs/ethics_and_limitations.md`.
