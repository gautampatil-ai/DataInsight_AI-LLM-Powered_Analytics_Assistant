import streamlit as st
from utils.helpers import load_css, render_header, get_current_dataset
from utils.report import ReportGenerator

st.set_page_config(page_title="PDF Report Studio", layout="wide")
load_css()

render_header("Executive Report Generator", "Download fully automated PDF summary reports generated locally without API keys.")

df = get_current_dataset()

if df is None:
    st.warning("Please upload a dataset first.")
else:
    if st.button("Generate & Export PDF Report"):
        with st.spinner("Generating PDF locally..."):
            pdf_path = ReportGenerator.generate_pdf(df)
            
            with open(pdf_path, "rb") as file:
                st.download_button(
                    label="📥 Download PDF Report",
                    data=file,
                    file_name="Dataset_Executive_Report.pdf",
                    mime="application/pdf"
                )
