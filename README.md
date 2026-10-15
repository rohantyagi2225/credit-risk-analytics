# Credit Risk Analytics & Risk Modelling

An educational data analytics and baseline machine-learning project exploring credit-risk patterns using Python. The repository includes a reproducible notebook, a command-line training script, and a synthetic dataset.

> [!IMPORTANT]
> **Synthetic-data demonstration only.** The bundled dataset and its target labels are artificially generated. Results demonstrate a coding workflow, not real-world predictive performance. Do not use this project for lending, eligibility, pricing, or other real credit decisions.

## Project highlights

- Data quality checks, summary statistics, and exploratory analysis
- Visualizations of target distribution, feature distributions, and numeric correlations
- Preprocessing pipelines for numeric and categorical features
- Baseline Logistic Regression and Random Forest classifiers
- Classification reports, confusion matrices, ROC-AUC, and ROC curves
- Saved chart outputs in `visualizations/`

## Technology stack

Python · Pandas · NumPy · Matplotlib · scikit-learn · Jupyter Notebook

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
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting started

### Option A: Google Colab

1. Open [the project notebook](notebooks/credit_risk_analysis.ipynb).
2. Download the repository as a ZIP using GitHub's **Code → Download ZIP** option, then upload and extract it in Colab, or clone the repository in a Colab cell.
3. Run the notebook cells from top to bottom from the repository root.

### Option B: Run locally

Requires Python 3.10 or newer.

```bash
git clone https://github.com/rohantyagi2225/credit-risk-analytics.git
cd credit-risk-analytics
python -m venv .venv
```

Activate the environment, then install dependencies:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/train_model.py
```

**macOS/Linux**
```bash
source .venv/bin/activate
pip install -r requirements.txt
python src/train_model.py
```

Open `notebooks/credit_risk_analysis.ipynb` in Jupyter to run the EDA and chart generation workflow. The notebook writes generated figures to `visualizations/`.

## Dataset

The file `data/credit_risk_synthetic.csv` contains 1,200 generated records. Its columns are:

| Column | Description |
|---|---|
| `applicant_id` | Synthetic demonstration ID |
| `age` | Synthetic age |
| `annual_income` | Illustrative annual income units |
| `loan_amount` | Illustrative loan amount units |
| `credit_score` | Synthetic credit-score-like value |
| `employment_years` | Synthetic years employed |
| `debt_to_income` | Illustrative debt-to-income ratio |
| `loan_purpose` | Generated purpose category |
| `default` | Artificial binary label (1 = positive demo label) |

The label was generated from an illustrative formula with noise; it is not based on actual defaults. See [DATASET_NOTICE.txt](data/DATASET_NOTICE.txt).

## Modelling approach

1. Separate features from the synthetic target.
2. Split the data into stratified training and test sets.
3. Impute missing numeric and categorical values.
4. Scale numeric features and one-hot encode categorical features.
5. Fit Logistic Regression and Random Forest baselines.
6. Report precision, recall, F1-score, confusion matrices, and ROC-AUC.

When interpreting classification results, inspect positive-class recall and precision alongside accuracy. The default decision threshold may not reflect the trade-offs required in a real credit setting.

## Limitations and responsible use

- Synthetic patterns and metrics are not evidence of real-world performance.
- No fairness, regulatory, stability, or out-of-time validation is claimed.
- A real-world study would require lawful data access, documented provenance, leakage checks, robust validation, calibration, explainability, fairness assessment, and expert review.
- Never commit personal, confidential, or identifiable financial records to a public repository.

## Potential next steps

- Replace demo data with an appropriately licensed and documented dataset.
- Add cross-validation and probability calibration.
- Compare threshold-dependent precision/recall trade-offs.
- Evaluate model stability and fairness with appropriate safeguards.
- Add a dashboard only after the analysis and data are validated.

## Author

**Rohan Tyagi**  
B.Tech, Computer Science and Engineering — Data Science & Machine Learning
