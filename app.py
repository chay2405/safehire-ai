import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# ---------------- CONFIG ----------------
st.set_page_config(page_title="SafeHire AI", layout="centered")
st.title("🛡️ SafeHire AI – Internship Scam Detector")
st.write("Paste an internship or job message below to check if it is a scam.")

# ---------------- API KEY ----------------
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY is not set in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=API_KEY)

# ---------------- DATE GROUNDING ----------------
today = datetime.now().strftime("%B %d, %Y")

SYSTEM_PROMPT = f"""
You are SafeHire AI, an internship and job scam detector.

Today's date is {today}.

When analyzing messages:
• Treat future joining dates as normal unless they are unrealistic or inconsistent
• Never flag something as suspicious only because it is in the future
• Verify companies, domains, and scam patterns using reasoning
• Use real-world hiring logic

Output in this exact format:

Risk Score:
Verdict:
Evidence:
Scam Signals:
Advice:
"""

# ---------------- MODEL ----------------
try:
    model = genai.GenerativeModel(
        model_name="models/gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT
    )
except Exception as e:
    st.error(f"❌ Gemini model failed to load: {e}")
    st.stop()

# ---------------- UI ----------------
user_input = st.text_area("Paste internship or job message here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please paste a message first.")
    else:
        with st.spinner("Analyzing with SafeHire AI..."):
            try:
                response = model.generate_content(user_input)
                st.markdown("### 🔍 Analysis Result")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Analysis failed: {e}")
