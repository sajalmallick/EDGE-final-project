import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

MODEL_PATH = "saved_model/model.pkl"

def train_model(csv_path):
    df = pd.read_csv(csv_path)

    # Assume last column is the target
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Encode categorical targets if needed
    if y.dtype == 'object':
        le = LabelEncoder()
        y = le.fit_transform(y)
        joblib.dump(le, "saved_model/label_encoder.pkl")
    else:
        le = None

    clf = RandomForestClassifier()
    clf.fit(X, y)

    os.makedirs("saved_model", exist_ok=True)
    joblib.dump(clf, MODEL_PATH)

def predict_with_model(q):
    clf = joblib.load(MODEL_PATH)
    le = joblib.load("saved_model/label_encoder.pkl") if os.path.exists("saved_model/label_encoder.pkl") else None

    # Parse input question as CSV row
    import ast
    query_data = pd.DataFrame([ast.literal_eval(q)])  # e.g. "[5.1, 3.5, 1.4, 0.2]"

    pred = clf.predict(query_data)
    return le.inverse_transform(pred)[0] if le else pred[0]
