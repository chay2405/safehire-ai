import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- CONFIG ----------------
st.set_page_config(page_title="SafeHire AI", layout="centered")

st.markdown("## 🛡️ SafeHire AI")
st.caption("Check internship or job messages for scam risk in seconds.")

# ---------------- API KEY ----------------
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY is not set. Please configure Streamlit secrets.")
    st.stop()

genai.configure(api_key=API_KEY)

# ---------------- DATE GROUNDING ----------------
today = datetime.now().strftime("%B %d, %Y")

SYSTEM_PROMPT = f"""
You are SafeHire AI, an AI system for detecting internship and job scams.

Today's date is {today}.

Your task is to analyze job or internship messages using real-world hiring practices.

Rules:
- Future dates alone are NOT suspicious.
- Hiring timelines:
  • 0–18 months → normal
  • 18–24 months → acceptable
  • >24 months → suspicious
- Evaluate domains, payment requests, company presence, urgency, and process realism.

You MUST respond in the EXACT format below:

Risk Score: <number from 0 to 100>
Verdict: <Legitimate | Suspicious | Scam>
Evidence:
- <point>
- <point>
Scam Signals:
- <point>
- <point>
Advice:
- <point>
- <point>

Do not add or remove sections.
"""

# ---------------- MODEL ----------------
try:
    model = genai.GenerativeModel(
        model_name="models/gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT
    )
except Exception as e:
    st.error(f"❌ Failed to load Gemini model: {e}")
    st.stop()

# ---------------- INPUT ----------------
user_input = st.text_area(
    "📋 Paste internship or job message here",
    height=180,
    placeholder="Paste the full message or email content..."
)

# ---------------- HELPERS ----------------
def extract_section(text, header):
    if header not in text:
        return ""
    return text.split(header, 1)[1].split("\n", 1)[1].strip()

def extract_risk_score(text):
    for line in text.splitlines():
        if line.startswith("Risk Score"):
            return int("".join(filter(str.isdigit, line)))
    return 0

def bullet_points(text, limit=3):
    return [line.replace("-", "").strip() for line in text.splitlines() if line.strip()][:limit]

# ---------------- ANALYZE ----------------
if st.button("🔍 Check Message"):
    if not user_input.strip():
        st.warning("Please paste a message to analyze.")
    else:
        with st.spinner("Analyzing message..."):
            try:
                response = model.generate_content(user_input)
                result = response.text

                risk = extract_risk_score(result)
                verdict = extract_section(result, "Verdict:")
                evidence = extract_section(result, "Evidence:")
                signals = extract_section(result, "Scam Signals:")
                advice = extract_section(result, "Advice:")

                st.divider()

                # ---------------- COLOR CARD ----------------
                if risk >= 70:
                    st.error("🚨 **UNSAFE — SCAM DETECTED**")
                elif risk >= 40:
                    st.warning("⚠️ **CAUTION — SUSPICIOUS**")
                else:
                    st.success("✅ **SAFE — LIKELY LEGITIMATE**")

                st.markdown(f"### Risk Score: **{risk} / 100**")
                st.progress(risk / 100)

                # ---------------- WHY ----------------
                st.markdown("### 🤔 Why this result?")
                for point in bullet_points(signals):
                    st.markdown(f"• {point}")

                # ---------------- ACTION ----------------
                st.markdown("### ✅ What should you do?")
                for step in bullet_points(advice):
                    st.markdown(f"• {step}")

                # ---------------- DETAILS ----------------
                with st.expander("🔍 View detailed analysis"):
                    st.markdown("**Evidence**")
                    for item in bullet_points(evidence, limit=5):
                        st.markdown(f"• {item}")

            except Exception as e:
                st.error(f"❌ Analysis failed: {e}")
