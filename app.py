import streamlit as st
import re

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="PhishShield AI",
    page_icon="🛡️",
    layout="centered"
)

# ------------------------------
# HEADER
# ------------------------------
st.title("🛡️ PhishShield AI")
st.subheader("AI-powered Phishing Email Detection")
st.write("Paste an email below to check if it looks **safe or suspicious**.")

st.markdown("---")

# ------------------------------
# INPUT
# ------------------------------
email_text = st.text_area(
    "Paste the email content here:",
    height=220,
    placeholder="Example: Urgent! Verify your account immediately..."
)

# ------------------------------
# PHISHING DETECTION LOGIC
# ------------------------------
def analyze_email(text: str):
    phishing_keywords = [
        "urgent",
        "verify",
        "password",
        "click here",
        "login",
        "account suspended",
        "confirm",
        "bank",
        "limited time",
        "reset"
    ]

    score = 0
    matched_words = []

    for word in phishing_keywords:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            score += 1
            matched_words.append(word)

    if score >= 3:
        verdict = "⚠️ Likely Phishing"
        confidence = "High"
    elif score == 2:
        verdict = "⚠️ Suspicious"
        confidence = "Medium"
    else:
        verdict = "✅ Looks Safe"
        confidence = "Low"

    return verdict, confidence, matched_words

# ------------------------------
# ANALYZE BUTTON
# ------------------------------
if st.button("Analyze Email"):
    if not email_text.strip():
        st.warning("Please paste an email first.")
    else:
        verdict, confidence, matches = analyze_email(email_text)

        st.markdown("### 🧠 Analysis Result")
        st.success(f"**Verdict:** {verdict}")
        st.info(f"**Confidence Level:** {confidence}")

        if matches:
            st.markdown("**Suspicious keywords found:**")
            for m in matches:
                st.write(f"- {m}")
        else:
            st.write("No common phishing keywords detected.")

# ------------------------------
# FOOTER
# ------------------------------
st.markdown("---")
st.caption("PhishShield AI • Educational phishing detection tool")
