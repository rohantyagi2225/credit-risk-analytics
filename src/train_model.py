"""Train baseline educational models on the bundled synthetic credit-risk dataset."""
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "credit_risk_synthetic.csv"
TARGET = "default"

def main():
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=[TARGET, "applicant_id"])
    y = df[TARGET]
    numeric = X.select_dtypes(include=["number"]).columns.tolist()
    categorical = X.select_dtypes(exclude=["number"]).columns.tolist()
    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocess = ColumnTransformer([
        ("numeric", numeric_pipe, numeric),
        ("categorical", categorical_pipe, categorical),
    ])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, class_weight="balanced"),
        "Random Forest": RandomForestClassifier(
            n_estimators=250, random_state=42, class_weight="balanced"
        ),
    }
    for name, model in models.items():
        pipe = Pipeline([("preprocess", preprocess), ("model", model)])
        pipe.fit(X_train, y_train)
        predictions = pipe.predict(X_test)
        probabilities = pipe.predict_proba(X_test)[:, 1]
        print(f"\n=== {name} ===")
        print(classification_report(y_test, predictions, zero_division=0))
        print(f"ROC-AUC: {roc_auc_score(y_test, probabilities):.3f}")
        print("Reminder: these are synthetic-data demonstration metrics, not real-world evidence.")

if __name__ == "__main__":
    main()
