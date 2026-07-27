import sys
from pathlib import Path

# Fix import paths
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
import pandas as pd
from utils.helpers import load_css, render_header, render_kpi

# Config
st.set_page_config(page_title="Dataset Studio", layout="wide")
load_css()

render_header("Dataset Workspace", "Upload, inspect, and clean your analytical datasets.")

# File Uploader
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Load Data
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        # Store in Streamlit session state
        st.session_state["df"] = df
        st.success(f"Successfully loaded `{uploaded_file.name}`!")

    except Exception as e:
        st.error(f"Error loading file: {str(e)}")

# Display active dataset stats
df = st.session_state.get("df", None)

if df is not None:
    st.markdown("### 📊 Dataset Overview")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: 
        render_kpi("Rows", f"{len(df):,}", "📄")
    with c2: 
        render_kpi("Columns", f"{df.shape[1]}", "📊")
    with c3: 
        render_kpi("Missing Cells", f"{df.isna().sum().sum():,}", "⚠️")
    with c4: 
        render_kpi("Memory Size", f"{round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)} MB", "💾")

    st.markdown("---")
    st.markdown("### 🔍 Raw Data Preview")
    st.dataframe(df.head(100), use_container_width=True)

    # Simple Cleaning Trigger
    st.markdown("---")
    st.markdown("### 🧹 Quick Clean")
    if st.button("Drop Duplicate Rows"):
        old_count = len(df)
        df = df.drop_duplicates()
        st.session_state["df"] = df
        st.success(f"Removed {old_count - len(df)} duplicate rows!")
        st.rerun()
else:
    st.info("👆 Please upload a file above to begin your analysis.")
