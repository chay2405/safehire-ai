# 🛡️ SafeHire AI – AI-Powered Internship Scam Detector

SafeHire AI is an AI-powered web application that helps students and job seekers identify fraudulent internship and job offers using **Google Gemini**, **real-world hiring logic**, and **structured risk analysis**.

Unlike traditional keyword-based scam detectors, SafeHire AI evaluates offers using **contextual reasoning**, **temporal validation**, and **behavioral scam patterns** to generate an evidence-based verdict.

---

## 🌟 Why SafeHire AI?

Every year, thousands of students lose money or share sensitive information because of fake internship offers.

Common scam techniques include:

- 💰 Asking candidates to pay registration or training fees
- 📧 Fake HR email addresses
- 🏢 Impersonating well-known companies
- ⏳ Creating fake urgency
- 🎯 Offering jobs without interviews
- 📄 Fake offer letters and onboarding messages

SafeHire AI helps users verify these messages before they become victims.

---

# 🚀 Key Features

- 🤖 AI-powered internship & job scam detection
- 📊 Risk Score (0–100)
- ✅ Verdict (Legitimate / Suspicious / Scam)
- 🔍 Evidence-based reasoning
- 🚨 Scam signal identification
- 💡 Personalized safety recommendations
- 📅 Real-time hiring timeline validation
- 🎨 Clean, user-friendly Streamlit interface
- ☁️ Cloud deployment using Streamlit Cloud

---

# 🧠 How It Works

```text
User Message
      │
      ▼
Streamlit Web Interface
      │
      ▼
Google Gemini AI
      │
      ▼
Contextual Reasoning
      │
      ▼
Hiring Timeline Validation
      │
      ▼
Scam Pattern Analysis
      │
      ▼
Structured Risk Assessment
      │
      ▼
Risk Score + Verdict + Advice
```

---

# 🏗️ System Architecture

```text
                +----------------+
                |     User       |
                +----------------+
                        │
                        ▼
            Streamlit Web Interface
                        │
                        ▼
            Prompt Engineering Layer
                        │
                        ▼
            Google Gemini 2.5 Flash
                        │
                        ▼
      Contextual Hiring Logic Evaluation
                        │
                        ▼
        Structured Response Generation
                        │
                        ▼
        Response Parsing & UI Rendering
                        │
                        ▼
          Risk Score • Verdict • Advice
```

---

# 🔍 What SafeHire AI Checks

The AI evaluates multiple scam indicators, including:

- Payment requests
- Company legitimacy
- Email domain authenticity
- Hiring workflow realism
- Interview process
- Urgency tactics
- Joining timeline plausibility
- Offer consistency
- Behavioral scam patterns
- General recruitment authenticity

Instead of relying on keywords, SafeHire AI reasons about the **entire hiring context**.

---

# 📅 Intelligent Timeline Validation

Large Language Models do not automatically understand today's date.

SafeHire AI solves this by grounding every analysis with the current date.

Hiring timeline rules include:

- ✅ 0–18 months → Normal
- ✅ 18–24 months → Acceptable
- ⚠️ More than 24 months → Suspicious

This significantly reduces false positives caused by future internship dates.

---

# 🎯 Sample Output

```text
🟢 SAFE

Risk Score: 5 / 100

Why?

• Official company domain
• Standard hiring workflow
• No payment requests

What should you do?

• Continue through official recruitment channels.
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| AI Model | Google Gemini 2.5 Flash |
| Frontend | Streamlit |
| Environment | python-dotenv |
| Deployment | Streamlit Cloud |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
safehire-ai/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .env                   # API Key (local only)
├── README.md              # Project documentation
└── .gitignore
```

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/chay2405/safehire-ai.git

cd safehire-ai
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure API Key

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

---

# 🌐 Live Demo

👉 https://safehire-ai.streamlit.app/

---

# 💻 GitHub Repository

👉 https://github.com/chay2405/safehire-ai

---

# 📈 Performance Highlights

- ⚡ Response time: **300–500 ms**
- 👥 Supports **30+ concurrent users**
- 📊 Structured Risk Score (0–100)
- ☁️ Fully cloud deployed
- 🔒 Stateless request handling

---

# ⚙️ Engineering Highlights

This project demonstrates:

- Prompt Engineering
- AI System Design
- Contextual Reasoning
- Temporal Grounding
- Structured Response Parsing
- Stateless Architecture
- Cloud Deployment
- User-Centered AI Interface

---

# 🚧 Current Limitations

- Depends on Gemini reasoning quality
- Does not analyze email headers
- No OCR support for screenshots
- No phishing URL database integration
- Intended for educational and awareness purposes

---

# 🚀 Future Enhancements

- Browser Extension
- OCR for Offer Letters
- Email Header Verification
- Phishing URL Detection
- Company Reputation Database
- Multi-language Scam Detection
- PDF Report Generation
- Confidence Calibration

---

# 📚 Learning Outcomes

While building SafeHire AI, I gained hands-on experience with:

- Google Gemini API
- Prompt Engineering
- AI-powered Risk Analysis
- Streamlit Deployment
- Python Application Development
- Context-Aware AI Systems
- Temporal Validation
- Cloud Deployment
- UI Design for AI Applications

---

# ⚠️ Disclaimer

SafeHire AI provides AI-assisted scam analysis for educational and awareness purposes.

The application should **not** be considered a substitute for professional legal, cybersecurity, or employment verification services.

Users should always verify internship and job offers through official company websites and recruitment channels.

---

# 👨‍💻 Author

**Chaitanya Peddiboyina**

- GitHub: https://github.com/chay2405
- LinkedIn: https://linkedin.com/in/chaitanya-peddiboyina

---

## ⭐ If you found this project useful, consider giving it a star!
