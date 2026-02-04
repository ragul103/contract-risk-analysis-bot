import streamlit as st
import os

from src.input_handler import extract_text
from src.language_handler import normalize_text
from src.clause_extractor import extract_clauses
from src.ner_extractor import extract_entities
from src.obligation_identifier import identify_obligations
from src.risk_engine import detect_risks
from src.scorer import score_risk
from src.report_generator import generate_pdf


st.set_page_config(page_title="Contract Risk Analysis Bot", layout="wide")


def risk_badge(level):
    if level == "High":
        st.error("🔴 HIGH RISK")
    elif level == "Medium":
        st.warning("🟠 MEDIUM RISK")
    else:
        st.success("🟢 LOW RISK")


st.markdown(
    """
    <h1 style="text-align:center;">📄 Contract Risk Analysis Bot</h1>
    <p style="text-align:center;">Simple visual understanding of contract risks</p>
    """,
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(
    "Upload Contract (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"],
    key="file_uploader"
)


if uploaded_file:

    upload_dir = "data/uploads"
    output_dir = "data/outputs"
    os.makedirs(upload_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    raw_text = extract_text(file_path, uploaded_file.name.split(".")[-1])
    normalized = normalize_text(raw_text)
    clauses = extract_clauses(normalized["normalized_text"])

    st.markdown("## 📊 Overall Contract Risk")

    contract_risks = []
    report_lines = []

    for clause in clauses:
        risks = detect_risks(clause["text"])
        risk_level = score_risk(risks)
        contract_risks.append(risk_level)

        report_lines.append(f"{clause['clause_id']} - Risk: {risk_level}")
        report_lines.append(clause["text"])
        for r in risks:
            report_lines.append(f"- {r}")
        report_lines.append("")

    overall_risk = "Low"
    if "High" in contract_risks:
        overall_risk = "High"
    elif "Medium" in contract_risks:
        overall_risk = "Medium"

    risk_badge(overall_risk)

    risk_percent = {"Low": 30, "Medium": 65, "High": 90}[overall_risk]
    st.progress(risk_percent)

    st.markdown("---")

    st.markdown("## 📋 Clause Risk Summary")

    table_data = []
    for clause in clauses:
        risks = detect_risks(clause["text"])
        table_data.append({
            "Clause": clause["clause_id"],
            "Risk Level": score_risk(risks)
        })

    st.table(table_data)

    st.markdown("---")

    st.markdown("## 📈 Risk Distribution")

    low = sum(1 for r in contract_risks if r == "Low")
    medium = sum(1 for r in contract_risks if r == "Medium")
    high = sum(1 for r in contract_risks if r == "High")

    st.bar_chart({
        "Low Risk": low,
        "Medium Risk": medium,
        "High Risk": high
    })

    st.markdown("---")
    st.markdown("## 📌 Clause-by-Clause Details")

    for clause in clauses:
        risks = detect_risks(clause["text"])
        risk_level = score_risk(risks)
        entities = extract_entities(clause["text"])
        obligations = identify_obligations(clause["text"])

        with st.expander(f"📄 {clause['clause_id']}"):
            st.markdown("### Clause Text")
            st.write(clause["text"])

            risk_badge(risk_level)

            st.markdown("### 🔍 Key Information")

            if entities["DATE"]:
                st.write("📅 Dates:", ", ".join(entities["DATE"]))
            if entities["MONEY"]:
                st.write("💰 Amounts:", ", ".join(entities["MONEY"]))
            if entities["GPE"]:
                st.write("📍 Jurisdiction:", ", ".join(entities["GPE"]))

            st.markdown("### 🧾 Obligations & Restrictions")

            for o in obligations["obligations"]:
                st.write(f"✔ {o}")
            for r in obligations["rights"]:
                st.write(f"➡ {r}")
            for p in obligations["prohibitions"]:
                st.write(f"⛔ {p}")

            st.markdown("### 🧠 What this means (Simple)")

            text = clause["text"].lower()

            if "terminate" in text:
                st.write("❗ One party can end the contract easily.")
            if "non-compete" in text:
                st.write("🚫 Future work or business may be restricted.")
            if "indemnify" in text:
                st.write("💸 You may have to cover losses or legal costs.")

    st.markdown("---")

    if st.button("📄 Generate PDF Report"):
        report_path = os.path.join(output_dir, "Contract_Risk_Report.pdf")
        generate_pdf(report_lines, report_path)

        with open(report_path, "rb") as pdf:
            st.success("PDF generated successfully")
            st.download_button(
                "⬇️ Download PDF",
                pdf,
                file_name="Contract_Risk_Report.pdf",
                mime="application/pdf"
            )

    if st.button("🔄 Upload Another Contract"):
        st.session_state.clear()
        st.rerun()
