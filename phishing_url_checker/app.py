import streamlit as st
import joblib
from utils import extract_features

model = joblib.load("phishing_model.pkl")

st.title("🔗 Paste a Website URL to Check for Phishing")

url = st.text_input("Enter Website URL", "http://example.com")

if st.button("Check"):
    features = extract_features(url)
    prediction = model.predict([features])[0]
    st.markdown("### Result:")
    if prediction == 1:
        st.error("🚨 This is likely a **Phishing** website!")
    else:
        st.success("✅ This is likely a **Legitimate** website.")
