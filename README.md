# 🔐 Phishing Website Detector

A simple machine learning tool that detects phishing websites based on the URL structure. Built using Python, scikit-learn, and Streamlit.

---

## 🚀 Features

- Paste any URL and get an instant prediction
- Detects phishing indicators like:
  - IP addresses in URLs
  - Suspicious keywords (e.g., "login", "verify", "gift")
  - Missing HTTPS
  - Abnormally long URLs
- Lightweight, fast, and runs offline

---

## 🛠️ Technologies Used

- Python
- scikit-learn
- Streamlit
- pandas
- joblib

---

## 📁 Dataset

A simple dataset of phishing and legitimate URLs with features:
- `having_ip_address`
- `url_length`
- `https_token`
- `suspicious_words`

See `dataset.csv`.

---

## 📦 Installation

git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector
pip install -r requirements.txt

🧠 Train the Model
python -c "from utils import train_model; train_model()"

🖥️ Run the App
streamlit run app.py
