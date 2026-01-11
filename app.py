import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
# No changes needed, the imports are already correct and sufficient.
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ----------------- CONFIG -----------------
st.set_page_config(page_title="SafeHire AI", layout="centered")

st.title("🛡️ SafeHire AI – Internship Scam Detector")
st.write("Paste an internship or job message below to check if it is a scam.")

# ----------------- API KEY -----------------
API_KEY = os.getenv("GEMINI_API_KEY")

# These variables and the subsequent conditional logic handle API key and model initialization errors.
genai_configured = False
model = None

if not API_KEY:
    st.error("GEMINI_API_KEY environment variable not set. Please set it to use the app.")
else:
    try:
        genai.configure(api_key=API_KEY)
        genai_configured = True
    except Exception as e:
        st.error(f"Failed to configure Gemini API: {e}. Please check your API key.")

if genai_configured:
    try:
        model = genai.GenerativeModel(
            model_name="models/gemini-2.5-flash",
            system_instruction="""
    You are SafeHire AI, an internship scam detector.

Analyze messages and output:

Risk Score:
Verdict:
Evidence:
Scam Signals:
Advice:

Use web search to verify companies, domains, and scam reports.
Be strict and factual.
    """
        )
    except Exception as e:
        st.error(f"Failed to initialize Gemini model: {e}. Please check the model name or API key permissions.")

# ----------------- UI -----------------
user_input = st.text_area("Paste internship or job message here:")
# This variable dynamically disables the button if the API key or model setup failed.
analyze_button_disabled = not genai_configured or model is None

if st.button("Analyze", disabled=analyze_button_disabled):
    if user_input.strip() == "":
        st.warning("Please paste a message first.")
    else:
        if model: # Ensure model is available before attempting to use it
            # This try-except block handles potential errors during the API call itself.
            with st.spinner("Analyzing with SafeHire AI..."):
                try:
                    response = model.generate_content(user_input)
                    st.markdown("### 🔍 Analysis Result")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}. Please try again.")
        else:
            st.error("Gemini model is not initialized. Please check API key and configuration.")
