import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import re

SUSPICIOUS_KEYWORDS = ["login", "verify", "update", "secure", "account", "bank", "free", "gift"]

def extract_features(url):
    has_ip = 1 if re.match(r"^http[s]?://\d+\.\d+\.\d+\.\d+", url) else 0
    url_len = len(url)
    has_https = 1 if "https" in url else 0
    suspicious = 1 if any(word in url.lower() for word in SUSPICIOUS_KEYWORDS) else 0
    return [has_ip, url_len, has_https, suspicious]

def train_model():
    df = pd.read_csv("dataset.csv")
    X = df.drop(columns=["URL", "label"])
    y = df["label"].map({"legitimate": 0, "phishing": 1})

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "phishing_model.pkl")
    return model
