import streamlit as st
import pandas as pd
from pathlib import Path

def load_css():
    """Injects custom CSS styling for dark theme if available."""
    css = """
    <style>
    body {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    .header-container {
        background: linear-gradient(135deg, #7C3AED 0%, #2563EB 100%);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
    }
    .kpi-card {
        background: #1E293B;
        border: 1px solid #334155;
        padding: 1.5rem;
        border-radius: 12px;
    }
    .kpi-title {
        font-size: 0.875rem;
        color: #94A3B8;
        text-transform: uppercase;
    }
    .kpi-value {
        font-size: 1.875rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-top: 0.5rem;
    }
    .glass-container {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_header(title: str, subtitle: str):
    """Renders a styled gradient header."""
    st.markdown(
        f"""
        <div class="header-container">
            <h1 style="margin:0; font-size:2.2rem; font-weight:800;">{title}</h1>
            <p style="margin:0.5rem 0 0 0; opacity:0.9; font-size:1.05rem;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_kpi(label: str, value: str, icon: str = "📊"):
    """Renders a metric card."""
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
    """Helper to retrieve dataset stored in Streamlit session state."""
    return st.session_state.get("df", None)
