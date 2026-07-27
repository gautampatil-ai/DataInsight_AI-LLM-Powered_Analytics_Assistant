import sys
from pathlib import Path

# Fix Streamlit Cloud Path Resolution
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
import pandas as pd

# Safe dynamic import
try:
    from utils.helpers import load_css, render_header, render_kpi, get_current_dataset
except ModuleNotFoundError as e:
    st.error(f"❌ Could not load 'utils' module. Path: {ROOT_DIR}")
    st.error(f"Detailed Error: {str(e)}")
    st.stop()

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

# 5. Main Dashboard View
if df is None:
    st.markdown("---")
    st.info("👈 **Welcome!** Select a page from the sidebar to upload your dataset or begin analysis.")
    
    st.markdown("### 🛠️ Keyless Capabilities")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class="glass-container">
                <h3>📊 Visual Analytics</h3>
                <p>Interactive charts, custom plot generators, and correlation matrix maps.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col2:
        st.markdown(
            """
            <div class="glass-container">
                <h3>🤖 Local AI Chat</h3>
                <p>Natural language data queries computed entirely offline without API keys.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col3:
        st.markdown(
            """
            <div class="glass-container">
                <h3>⚡ Report Generator</h3>
                <p>Export executive statistical reports directly in downloadable PDF format.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.markdown("### 📈 Executive Dataset Summary")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        render_kpi("Total Records", f"{len(df):,}", "📄")
    with c2:
        render_kpi("Total Attributes", f"{df.shape[1]}", "📊")
    with c3:
        render_kpi("Missing Values", f"{df.isna().sum().sum():,}", "⚠️")
    with c4:
        render_kpi("Memory Size", f"{round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)} MB", "💾")

    st.markdown("---")
    st.markdown("### 🔍 Preview")
    st.dataframe(df.head(10), use_container_width=True)
