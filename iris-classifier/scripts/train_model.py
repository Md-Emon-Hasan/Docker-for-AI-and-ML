from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main():
    iris = load_iris()
    x_train, _, y_train, _ = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    # Resolve the output from this script's location, not the caller's working directory.
    project_root = Path(__file__).resolve().parents[1]
    model_path = project_root / "models" / "iris_model.pkl"
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Saved trained Iris model to {model_path}")


if __name__ == "__main__":
    main()
