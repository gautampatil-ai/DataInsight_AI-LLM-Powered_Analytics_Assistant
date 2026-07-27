import sys
from pathlib import Path

# Fix import path for modular resolution
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
import pandas as pd
import numpy as np
from utils.helpers import load_css, render_header, render_kpi

# -----------------------------------------------------------------------------
# 1. Page & Layout Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Dataset Studio | InsightAI",
    page_icon="📂",
    layout="wide"
)
load_css()

render_header(
    "Data Engineering & Ingestion Workbench", 
    "High-throughput data ingestion, schema inspection, and automated ETL transformation engine."
)

# Initialize Session States
if "df" not in st.session_state:
    st.session_state["df"] = None

# -----------------------------------------------------------------------------
# 2. File Upload & Ingestion Section
# -----------------------------------------------------------------------------
st.markdown("### 📥 Dataset Ingestion")

with st.container():
    uploaded_file = st.file_uploader(
        "Upload Analytical Dataset (Supported formats: CSV, XLSX)",
        type=["csv", "xlsx", "xls"],
        help="Drag and drop or browse your local file. Maximum file size: 200MB."
    )

if uploaded_file is not None:
    try:
        with st.spinner("Ingesting and parsing payload..."):
            if uploaded_file.name.endswith(".csv"):
                df_raw = pd.read_csv(uploaded_file)
            else:
                df_raw = pd.read_excel(uploaded_file)

            # Store loaded data in session state if not already set or changed
            if st.session_state["df"] is None or st.sidebar.button("Reload Original File"):
                st.session_state["df"] = df_raw
                st.toast(f"Successfully ingested {uploaded_file.name}", icon="✅")

    except Exception as e:
        st.error(f"Execution Error: Ingestion failed due to file parsing anomaly: {str(e)}")

# -----------------------------------------------------------------------------
# 3. Data Overview & Advanced ETL Workbench
# -----------------------------------------------------------------------------
df = st.session_state.get("df", None)

if df is not None:
    st.markdown("---")
    
    # KPI Metrics
    st.markdown("### 📊 Metadata & Telemetry")
    m1, m2, m3, m4, m5 = st.columns(5)
    
    memory_size_mb = round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)
    missing_cells = df.isna().sum().sum()
    duplicate_rows = df.duplicated().sum()
    
    with m1: render_kpi("Total Records", f"{len(df):,}", "📄")
    with m2: render_kpi("Total Features", f"{df.shape[1]}", "⚙️")
    with m3: render_kpi("Missing Cells", f"{missing_cells:,}", "⚠️")
    with m4: render_kpi("Duplicate Rows", f"{duplicate_rows:,}", "👥")
    with m5: render_kpi("Memory Allocation", f"{memory_size_mb} MB", "💾")

    # Data Preview & Column Health Inspection Tabs
    st.markdown("---")
    st.markdown("### 🔍 Schema Inspection & Exploratory Analytics")
    
    tab_preview, tab_schema, tab_cleaner = st.tabs([
        "📋 Data Preview", 
        "🧬 Data Types & Schema", 
        "🛠️ Automated Data Cleaning Engine"
    ])

    # TAB 1: PREVIEW
    with tab_preview:
        col_ctrl1, col_ctrl2 = st.columns([1, 4])
        with col_ctrl1:
            rows_to_show = st.slider("Display Records", min_value=5, max_value=100, value=15, step=5)
        with col_ctrl2:
            search_query = st.text_input("🔍 Quick Search / Filter Preview Rows", "")

        df_display = df
        if search_query:
            # Filter rows where search string matches any text column
            mask = df.astype(str).apply(lambda row: row.str.contains(search_query, case=False).any(), axis=1)
            df_display = df[mask]

        st.dataframe(df_display.head(rows_to_show), use_container_width=True)

    # TAB 2: SCHEMA & TYPES
    with tab_schema:
        schema_df = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": [str(dtype) for dtype in df.dtypes],
            "Non-Null Count": df.notnull().sum().values,
            "Null Count": df.isnull().sum().values,
            "Null Ratio (%)": np.round((df.isnull().sum().values / len(df)) * 100, 2),
            "Unique Values": [df[col].nunique() for col in df.columns]
        })
        st.dataframe(schema_df, use_container_width=True)

    # TAB 3: DATA CLEANING WORKBENCH
    with tab_cleaner:
        st.markdown("##### ⚙️ Pipeline ETL Operations")
        c_clean1, c_clean2 = st.columns(2)

        with c_clean1:
            st.markdown("**Handling Missing Values**")
            impute_strategy = st.selectbox(
                "Imputation Strategy for Numeric Attributes",
                options=["None", "Impute with Mean", "Impute with Median", "Drop Rows with Nulls"]
            )
            
            st.markdown("**Deduplication**")
            remove_dupes = st.checkbox("Remove Duplicate Rows", value=False)

        with c_clean2:
            st.markdown("**Date Type Conversion**")
            date_cols = st.multiselect("Select columns to parse into Datetime", df.columns)

            st.markdown("**Type Casting**")
            col_to_cast = st.selectbox("Select column to cast", ["None"] + list(df.columns))
            target_type = st.selectbox("Target Data Type", ["string", "int64", "float64", "category", "bool"])

        if st.button("🚀 Apply Transformations", type="primary"):
            cleaned_df = df.copy()

            # Deduplication
            if remove_dupes:
                before_cnt = len(cleaned_df)
                cleaned_df = cleaned_df.drop_duplicates()
                st.info(f"Deduplication complete: Removed {before_cnt - len(cleaned_df)} rows.")

            # Missing Values Imputation
            if impute_strategy == "Impute with Mean":
                num_cols = cleaned_df.select_dtypes(include=[np.number]).columns
                cleaned_df[num_cols] = cleaned_df[num_cols].fillna(cleaned_df[num_cols].mean())
            elif impute_strategy == "Impute with Median":
                num_cols = cleaned_df.select_dtypes(include=[np.number]).columns
                cleaned_df[num_cols] = cleaned_df[num_cols].fillna(cleaned_df[num_cols].median())
            elif impute_strategy == "Drop Rows with Nulls":
                cleaned_df = cleaned_df.dropna()

            # Date Parsing
            for d_col in date_cols:
                try:
                    cleaned_df[d_col] = pd.to_datetime(cleaned_df[d_col])
                except Exception as ex:
                    st.warning(f"Could not parse `{d_col}` to Datetime: {str(ex)}")

            # Type Casting
            if col_to_cast != "None":
                try:
                    cleaned_df[col_to_cast] = cleaned_df[col_to_cast].astype(target_type)
                except Exception as ex:
                    st.error(f"Failed to cast `{col_to_cast}` to `{target_type}`: {str(ex)}")

            # Update Session State
            st.session_state["df"] = cleaned_df
            st.success("ETL Transformation pipeline executed successfully!")
            st.rerun()

    # Data Export Options
    st.markdown("---")
    st.markdown("### 📤 Export Processed Data")
    
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Cleaned Dataset (CSV)",
        data=csv_data,
        file_name="cleaned_dataset_export.csv",
        mime="text/csv"
    )

else:
    st.info("👆 Please upload a CSV or Excel dataset above to open the analysis workbench.")
