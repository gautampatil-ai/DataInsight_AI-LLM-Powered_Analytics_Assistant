import streamlit as st
import pandas as pd

def load_css():
    """Injects high-end Data Science Studio dark CSS with CSS animations."""
    css = """
    <style>
    /* Global Background & Typography */
    .stApp {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Sidebar Dark Styling */
    section[data-testid="stSidebar"] {
        background-color: #0B0F19 !important;
        border-right: 1px solid #1E293B !important;
    }

    /* Animated Gradient Header */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .header-container {
        background: linear-gradient(-45deg, #4F46E5, #7C3AED, #2563EB, #06B6D4);
        background-size: 400% 400%;
        animation: gradientShift 12s ease infinite;
        padding: 2.2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px -10px rgba(124, 58, 237, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Animated KPI Cards */
    .kpi-card {
        background: #1E293B;
        border: 1px solid #334155;
        padding: 1.5rem;
        border-radius: 16px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }

    .kpi-card:hover {
        transform: translateY(-6px);
        border-color: #7C3AED;
        box-shadow: 0 12px 25px -5px rgba(124, 58, 237, 0.4);
    }

    .kpi-card::before {
        content: '';
        position: absolute;
        top: 0; left: -100%;
        width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.05), transparent);
        transition: 0.5s;
    }

    .kpi-card:hover::before {
        left: 100%;
    }

    .kpi-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .kpi-value {
        font-size: 2rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 0.4rem;
        background: linear-gradient(135deg, #FFFFFF 0%, #CBD5E1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Glassmorphic Containers */
    .glass-container {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        transition: border 0.3s ease;
    }

    .glass-container:hover {
        border-color: #3B82F6;
    }

    /* Primary Button Styling */
    div.stButton > button {
        background: linear-gradient(135deg, #7C3AED 0%, #2563EB 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.4rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 14px 0 rgba(124, 58, 237, 0.39) !important;
    }

    div.stButton > button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 6px 20px 0 rgba(124, 58, 237, 0.6) !important;
    }

    /* Custom Dataframe Styling */
    div[data-testid="stDataFrame"] {
        background-color: #1E293B;
        border-radius: 12px;
        border: 1px solid #334155;
        overflow: hidden;
    }

    /* Hide default Streamlit padding at top */
    .block-container {
        padding-top: 2rem !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_header(title: str, subtitle: str):
    """Renders an animated gradient banner header."""
    st.markdown(
        f"""
        <div class="header-container">
            <h1 style="margin:0; font-size:2.3rem; font-weight:800; letter-spacing:-0.02em;">{title}</h1>
            <p style="margin:0.6rem 0 0 0; opacity:0.92; font-size:1.05rem; font-weight:400;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_kpi(label: str, value: str, icon: str = "📊"):
    """Renders an animated glowing metric card."""
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">{icon} {label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def get_current_dataset() -> pd.DataFrame | None:
    """Safely fetch active dataset stored in Streamlit state."""
    return st.session_state.get("df", None)
