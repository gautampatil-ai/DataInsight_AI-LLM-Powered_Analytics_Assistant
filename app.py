import streamlit as st
import pandas as pd
from utils.helpers import load_css, render_header, render_kpi, get_current_dataset

# 1. Page Configuration
st.set_page_config(
    page_title="InsightAI Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject Custom Dark Theme Styles
load_css()

# 3. Main Application Header
render_header(
    title="InsightAI Studio",
    subtitle="Keyless Enterprise AI Platform for Interactive Data Analytics & AutoML"
)

# 4. Fetch Current Dataset from Session State
df = get_current_dataset()

# 5. Dashboard View Logic
if df is None:
    st.markdown("---")
    st.info("👈 **Welcome!** To get started, navigate to the **Dataset** tab in the sidebar and upload a CSV or Excel file.")
    
    # Feature Overview Cards for First-Time Users
    st.markdown("### 🛠️ Platform Capabilities")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class="glass-container">
                <h3>📊 Visual Analytics & SQL</h3>
                <p>Generate interactive Plotly charts, perform correlation analysis, and execute DuckDB SQL queries directly on your data.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col2:
        st.markdown(
            """
            <div class="glass-container">
                <h3>🤖 Keyless AI Assistant</h3>
                <p>Ask natural language questions about your dataset locally. No external LLM API keys or subscription fees required.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col3:
        st.markdown(
            """
            <div class="glass-container">
                <h3>⚡ AutoML Workbench</h3>
                <p>Train and benchmark multiple machine learning models (RandomForest, XGBoost, LightGBM) automatically.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    # KPI Metrics Banner
    st.markdown("### 📈 Executive Dataset Summary")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        render_kpi("Total Records", f"{len(df):,}", "📄")
    with c2:
        render_kpi("Total Attributes", f"{df.shape[1]}", "📊")
    with c3:
        render_kpi("Missing Values", f"{df.isna().sum().sum():,}", "⚠️")
    with c4:
        render_kpi("Memory Usage", f"{round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)} MB", "💾")

    st.markdown("---")
    
    # Quick Preview Table
    st.markdown("### 🔍 Dataset Quick Preview")
    st.dataframe(df.head(10), use_container_width=True)
    
    # Statistical Overview
    st.markdown("### 📉 Numerical Features Overview")
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        st.dataframe(numeric_df.describe().T, use_container_width=True)
    else:
        st.write("No numeric columns found in the dataset.")
