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
You are SafeHire AI, an AI system for detecting internship and job scams.

Today's date is {today}.

Your task is to analyze job or internship messages using real-world hiring practices and web-based reasoning.

Rules:
- Future joining dates are normal.
- Do NOT flag something as suspicious just because it is in the future.
- Hiring timelines:
  • 0–18 months ahead → normal
  • 18–24 months ahead → acceptable
  • More than 24 months ahead → suspicious
- Always evaluate email domains, company reputation, payment requests, and hiring process.
- Use logical, real-world recruiting behavior in every decision.

You MUST output the result in the following EXACT format and NEVER change it:

Risk Score: <number from 0 to 100>
Verdict: <Legitimate | Suspicious | Scam>
Evidence:
- <bullet point>
- <bullet point>
Scam Signals:
- <bullet point>
- <bullet point>
Advice:
- <bullet point>
- <bullet point>

Do NOT omit any section.
Always include a numeric Risk Score.
Do not add extra text outside this format.
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
