"""Baseline credit-default analysis using the official UCI dataset.

Run from the repository root:
    python src/train_model.py

The script downloads UCI dataset 350 at runtime; internet access is required.
This is a retrospective educational example, not a lending decision system.
"""
from __future__ import annotations

import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    ConfusionMatrixDisplay,
    roc_auc_score,
    roc_curve,
    balanced_accuracy_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
VISUALS_DIR = ROOT / "visualizations"
TARGET = "default_next_month"
RANDOM_STATE = 42

# These fields are coded categories in the source and are treated categorically
# rather than assuming that each code is a continuous numeric measurement.
CATEGORICAL_COLUMNS = [
    "SEX", "EDUCATION", "MARRIAGE",
    "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6",
]

def load_uci_data() -> pd.DataFrame:
    """Download UCI dataset 350 and normalize its columns."""
    dataset = fetch_ucirepo(id=350)
    X = dataset.data.features.copy()
    y = dataset.data.targets.copy()
    X.columns = [str(c).strip() for c in X.columns]
    y.columns = [str(c).strip() for c in y.columns]
    target_col = y.columns[0]
    df = X.copy()
    df[TARGET] = y[target_col].reset_index(drop=True)
    # UCI feature names are normally descriptive; this handles alternate exports.
    aliases = {
        "X1": "LIMIT_BAL", "X2": "SEX", "X3": "EDUCATION",
        "X4": "MARRIAGE", "X5": "AGE", "X6": "PAY_0",
        "X7": "PAY_2", "X8": "PAY_3", "X9": "PAY_4",
        "X10": "PAY_5", "X11": "PAY_6", "X12": "BILL_AMT1",
        "X13": "BILL_AMT2", "X14": "BILL_AMT3", "X15": "BILL_AMT4",
        "X16": "BILL_AMT5", "X17": "BILL_AMT6", "X18": "PAY_AMT1",
        "X19": "PAY_AMT2", "X20": "PAY_AMT3", "X21": "PAY_AMT4",
        "X22": "PAY_AMT5", "X23": "PAY_AMT6",
    }
    df = df.rename(columns=aliases)
    # Some exports expose the target with its original descriptive name.
    if TARGET not in df.columns:
        raise ValueError(f"Target column {TARGET!r} was not created.")
    df[TARGET] = pd.to_numeric(df[TARGET], errors="raise").astype(int)
    return df

def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    categorical = [c for c in CATEGORICAL_COLUMNS if c in X.columns]
    numeric = [c for c in X.columns if c not in categorical]
    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])
    return ColumnTransformer([
        ("numeric", numeric_pipe, numeric),
        ("categorical", categorical_pipe, categorical),
    ])

def main() -> None:
    VISUALS_DIR.mkdir(parents=True, exist_ok=True)
    df = load_uci_data()
    print(f"Dataset shape: {df.shape}")
    print(f"Missing cells: {int(df.isna().sum().sum())}")
    print(f"Duplicate rows: {int(df.duplicated().sum())}")
    print("\nTarget distribution:")
    print(df[TARGET].value_counts(normalize=True).sort_index().rename("proportion"))

    # Do not use the row identifier as a predictor.
    X = df.drop(columns=[TARGET, "ID"], errors="ignore")
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )

    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=2000, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=300, class_weight="balanced",
            random_state=RANDOM_STATE, n_jobs=-1
        ),
    }

    fig, ax = plt.subplots(figsize=(7, 5))
    for name, estimator in models.items():
        pipe = Pipeline([
            ("preprocess", build_preprocessor(X_train)),
            ("model", estimator),
        ])
        pipe.fit(X_train, y_train)
        predictions = pipe.predict(X_test)
        probabilities = pipe.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, probabilities)
        print(f"\n=== {name} ===")
        print(classification_report(y_test, predictions, zero_division=0))
        print(f"ROC-AUC: {auc:.3f}")
        print(f"Balanced accuracy: {balanced_accuracy_score(y_test, predictions):.3f}")
        ConfusionMatrixDisplay.from_predictions(y_test, predictions, values_format="d")
        plt.title(f"{name} — UCI historical data")
        plt.tight_layout()
        plt.savefig(VISUALS_DIR / f"confusion_matrix_{name.lower().replace(' ', '_')}.png", dpi=160)
        plt.close()
        fpr, tpr, _ = roc_curve(y_test, probabilities)
        ax.plot(fpr, tpr, label=f"{name} (AUC={auc:.3f})")

    ax.plot([0, 1], [0, 1], "--", label="Chance baseline")
    ax.set(title="ROC curves — UCI Default of Credit Card Clients",
           xlabel="False positive rate", ylabel="True positive rate")
    ax.legend()
    fig.tight_layout()
    fig.savefig(VISUALS_DIR / "roc_curves_real_data.png", dpi=160)
    plt.close(fig)
    print(f"\nCharts saved in: {VISUALS_DIR}")
    print("Reminder: retrospective educational results only; not validated for lending decisions.")

if __name__ == "__main__":
    main()
