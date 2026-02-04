# 📄 Contract Analysis & Risk Assessment Bot

## 🧠 Overview
The **Contract Analysis & Risk Assessment Bot** is a GenAI-powered legal assistant designed to help **small and medium business owners (SMEs)** understand complex contracts in **simple business language**.

The system analyzes contracts clause by clause, identifies potential legal risks, highlights unfavorable terms, and presents insights using **clear visuals, risk indicators, and plain-English explanations**.  
It prioritizes **explainability, usability, and confidentiality**, not legal advice.

---

## 🎯 Problem Statement
Business owners often struggle to understand lengthy and complex contracts such as employment agreements, vendor contracts, service agreements, and NDAs. This can lead to hidden risks, unfair obligations, and legal liabilities.

This project solves the problem by:
- Breaking contracts into readable clauses
- Identifying legal risks and imbalances
- Explaining clauses in simple business language
- Providing visual risk indicators and downloadable reports

---

## 🚀 Key Features

### 📂 Supported Input Formats
- PDF (text-based)
- DOC / DOCX
- Plain Text (.txt)

---

### 🧩 Core Analysis Capabilities
- Clause & sub-clause extraction
- Named entity recognition:
  - Parties
  - Dates & duration
  - Financial amounts
  - Jurisdiction & governing law
- Obligation, right, and prohibition identification
- Clause-level and contract-level risk scoring
- Rule-based risk detection

---

### ⚠️ Risk Detection Includes
- Unilateral termination clauses
- Non-compete restrictions
- Confidentiality & NDA obligations
- Indemnity and liability exposure
- Auto-renewal and lock-in periods
- Intellectual Property (IP) ownership & assignment
- Jurisdiction and governing law risks

---

### 📊 Visual & User-Friendly Outputs
- Overall contract risk indicator (Low / Medium / High)
- Clause-wise risk summary table
- Risk distribution bar chart
- Expandable clause cards
- Icon-based, plain-English explanations
- Downloadable PDF risk report

---

### 🌐 Multilingual Handling
- English and Hindi contract support
- Hindi contracts are internally normalized to English for NLP processing
- Output explanations are provided in **simple business English**

---

## 🛠️ Technology Stack

| Component | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| NLP | spaCy, rule-based NLP |
| File Parsing | pdfplumber, python-docx |
| Language Detection | langdetect |
| Reporting | ReportLab |
| Storage | Local file system |

---

## 📁 Project Structure
```

contract-risk-analysis-bot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── input_handler.py
│   ├── language_handler.py
│   ├── clause_extractor.py
│   ├── ner_extractor.py
│   ├── obligation_identifier.py
│   ├── risk_engine.py
│   ├── scorer.py
│   └── report_generator.py
│
├── data/
│   ├── uploads/
│   └── outputs/
│
└── audit_logs/

````

---

## ▶️ How to Run Locally

### 1️⃣ Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🌍 Live Deployment

**Live App URL:**

---

## 🔐 Confidentiality & Disclaimer

* No external legal databases or APIs are used
* No contract data is permanently stored
* All processing is local and session-based
* This tool does **not provide legal advice**
* Intended for awareness and risk identification only

---

## ⚠️ Limitations

* Scanned PDFs are not supported (no OCR)
* Indian currency and party names may need further tuning
* Compliance checks are heuristic, not statutory validation

---

## 📌 Future Enhancements

* Improved party and financial entity extraction
* Advanced IP clause classification
* GPT-based clause explanations and rewrites
* Enhanced PDF formatting with tables and highlights
* Optional OCR support for scanned documents

---

## 🏁 Conclusion

This project demonstrates how **GenAI and NLP** can be applied responsibly to legal text analysis by focusing on **clarity, explainability, and user understanding**, making it useful for SMEs and a strong portfolio project for AI and Data Science roles.


Just say what’s next.
```
