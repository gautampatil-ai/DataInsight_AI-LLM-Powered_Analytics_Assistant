import streamlit as st
import pandas as pd

def load_css():
    """Injects high-end Data Science Studio Dark UI with micro-animations & glowing effects."""
    css = """
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* Global Dark Canvas */
    .stApp {
        background: #090D16 !important;
        color: #F8FAFC !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Sidebar Modernization */
    section[data-testid="stSidebar"] {
        background-color: #060911 !important;
        border-right: 1px solid #1E293B !important;
    }

    /* Animated Multi-Color Header Banner */
    @keyframes subtleGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .header-container {
        background: linear-gradient(-45deg, #1E1B4B, #312E81, #4C1D95, #1E3A8A);
        background-size: 300% 300%;
        animation: subtleGradient 10s ease infinite;
        padding: 2.5rem;
        border-radius: 24px;
        color: #FFFFFF;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px -10px rgba(99, 102, 241, 0.35);
        border: 1px solid rgba(255, 255, 255, 0.12);
    }

    /* Premium Glowing KPI Cards */
    .kpi-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(16px);
        border: 1px solid #1E293B;
        padding: 1.5rem;
        border-radius: 20px;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }

    .kpi-card:hover {
        transform: translateY(-5px);
        border-color: #6366F1;
        box-shadow: 0 12px 30px -5px rgba(99, 102, 241, 0.4);
    }

    .kpi-title {
        font-size: 0.75rem;
        font-weight: 700;
        color: #818CF8;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    .kpi-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 0.3rem;
        letter-spacing: -0.02em;
    }

    /* HIGH-End Animated Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 50%, #4338CA 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 14px !important;
        padding: 0.7rem 1.8rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.02em !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35) !important;
        width: 100%;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.01) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.6) !important;
        border-color: #A5B4FC !important;
    }

    div.stButton > button:active {
        transform: translateY(0px) scale(0.98) !important;
    }

    /* Glassmorphic File Uploader */
    div[data-testid="stFileUploader"] {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 2px dashed #312E81 !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stFileUploader"]:hover {
        border-color: #6366F1 !important;
        background: rgba(30, 27, 75, 0.4) !important;
    }

    /* Modern Tabs Styling */
    div[data-baseweb="tab-list"] {
        background-color: #0F172A !important;
        border-radius: 16px !important;
        padding: 5px !important;
        gap: 5px !important;
        border: 1px solid #1E293B !important;
    }

    button[data-baseweb="tab"] {
        border-radius: 12px !important;
        color: #94A3B8 !important;
        font-weight: 600 !important;
        padding: 0.5rem 1.2rem !important;
        transition: all 0.2s ease !important;
    }

    button[aria-selected="true"] {
        background-color: #1E1B4B !important;
        color: #A5B4FC !important;
        border: 1px solid #4338CA !important;
    }

    /* Modern Dark Table Container */
    div[data-testid="stDataFrame"] {
        background: #0F172A !important;
        border: 1px solid #1E293B !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
    }

    /* Styled Chat Input Bar */
    div[data-testid="stChatInput"] {
        border-radius: 16px !important;
        border: 1px solid #312E81 !important;
        background-color: #0F172A !important;
    }

    div[data-testid="stChatInput"]:focus-within {
        border-color: #6366F1 !important;
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.4) !important;
    }

    /* Hide Top Native Padding */
    .block-container {
        padding-top: 1.8rem !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_header(title: str, subtitle: str):
    """Renders an animated gradient banner header."""
    st.markdown(
        f"""
        <div class="header-container">
            <h1 style="margin:0; font-size:2.4rem; font-weight:800; letter-spacing:-0.03em;">{title}</h1>
            <p style="margin:0.5rem 0 0 0; opacity:0.9; font-size:1.05rem; font-weight:400;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_kpi(label: str, value: str, icon: str = "⚡"):
    """Renders a modern glowing metric card."""
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
