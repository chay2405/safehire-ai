# 🛡️ SafeHire AI – Internship Scam Detector

SafeHire AI is a **RAG-powered AI web application** that helps students identify fake internship and job offers using **Gemini AI with live web verification**.

It analyzes emails, WhatsApp messages, and job posts to detect scams such as:
- Payment-for-job fraud
- Fake HR emails
- Fake companies
- Urgency-based traps
- No-interview offers

---

## 🚀 How it Works

User Message
↓
Streamlit Web App
↓
Gemini AI (LLM)
↓
Google Search Grounding (RAG)
↓
Scam Evidence + Fraud Signals
↓
Risk Score, Verdict & Advice

yaml
Copy code

The AI retrieves **real-world web evidence** (company websites, scam reports, email domains) before making a decision.

---

## 🧠 Features

- **Live Scam Detection**
- **Risk Score (0–100)**
- **Evidence-backed verdict**
- **Fraud pattern recognition**
- **Student safety advice**
- **Web-based UI**

---

## 🛠 Tech Stack

- **Google Gemini API**
- **Google Search Grounding (RAG)**
- **Streamlit**
- **Python**

---

## 🧪 How to Run Locally

1. Clone the repository  
git clone https://github.com/YOUR_USERNAME/safehire-ai
cd safehire-ai

cpp
Copy code

2. Create virtual environment  
python -m venv venv
venv\Scripts\activate

markdown
Copy code

3. Install dependencies  
pip install streamlit google-generativeai python-dotenv

markdown
Copy code

4. Create `.env` file  
GEMINI_API_KEY=your_api_key_here

markdown
Copy code

5. Run the app  
streamlit run app.py

yaml
Copy code

---

## ⚠ Disclaimer

This tool provides **AI-based analysis** and should not be considered legal advice.  
Always verify offers independently.

---

## 📌 Project Purpose

Built to help **students and freshers** avoid fake internship scams using **modern AI and retrieval-based verification**.

---