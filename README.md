# Credit Risk Analytics & Risk Modelling

A portfolio-ready educational project demonstrating exploratory analysis and a baseline machine-learning workflow for credit-risk data.

> **Important:** The included dataset is synthetic demonstration data generated for this repository. It is not real customer or lender data. The target label is artificially generated and model metrics are not evidence of real-world performance. Do not use this project to make lending decisions.

## Project goals
- Inspect and clean structured credit-risk data.
- Explore distributions, default rates, and relationships between variables.
- Build baseline classification models for learning purposes.
- Evaluate models using precision, recall, F1-score, ROC-AUC, and a confusion matrix.
- Keep the workflow reproducible and transparent.

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, Jupyter Notebook.

## Repository structure
```text
credit-risk-analytics/
├── data/
│   ├── credit_risk_synthetic.csv
│   └── DATASET_NOTICE.txt
├── notebooks/
│   └── credit_risk_analysis.ipynb
├── src/
│   └── train_model.py
├── reports/
│   └── PROJECT_NOTES.md
├── visualizations/
│   └── .gitkeep
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally or in Google Colab
1. Download or clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `notebooks/credit_risk_analysis.ipynb` in Jupyter or upload it to Google Colab.
4. Run cells from top to bottom.

To run the script:
```bash
python src/train_model.py
```
The script expects the CSV at `data/credit_risk_synthetic.csv` relative to the project root.

## Data dictionary
| Column | Description |
|---|---|
| `applicant_id` | Synthetic demonstration identifier |
| `age` | Applicant age in the synthetic data |
| `annual_income` | Annual income, in illustrative currency units |
| `loan_amount` | Requested loan amount, in illustrative currency units |
| `credit_score` | Synthetic credit-score-like value |
| `employment_years` | Years employed |
| `debt_to_income` | Illustrative debt-to-income ratio |
| `loan_purpose` | Synthetic loan purpose category |
| `default` | Artificially generated binary target (1 = demo default label) |

## Methodology
- Data quality checks and summary statistics
- Exploratory data analysis (EDA)
- Stratified train/test split
- Preprocessing with imputation, scaling, and one-hot encoding
- Logistic Regression and Random Forest baselines
- Classification metrics and confusion matrix

## Limitations and responsible use
This is a learning template, not a validated credit-risk model. Synthetic data can make the workflow runnable but cannot establish useful real-world performance. Credit models can have serious fairness, privacy, regulatory, and explainability implications. Before any real-world research, use a lawful, documented dataset, assess data quality and bias, validate out of time and across relevant groups, and obtain appropriate expert review. Avoid uploading confidential or personally identifiable financial information to public repositories.

## Next improvements
- Replace the synthetic CSV with an appropriately licensed, documented dataset.
- Add feature definitions and data provenance.
- Add cross-validation and calibration analysis.
- Add explainability and fairness evaluation where appropriate.
- Add a dashboard only after the data and analysis are validated.

## Author
Rohan Tyagi
