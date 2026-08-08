import streamlit as st
import pandas as pd
from utils.session import get_dataset

st.title("📊 Exploratory Data Analysis (EDA)")

df = get_dataset()


def section(title, description):
    """Render a consistent section heading and description."""
    st.markdown(f"## {title}\n\n{description}")

if df is None:

    st.info("""
## 📂 No Dataset Loaded

Upload a CSV or Excel dataset from the **Home** page.

Once uploaded, you'll unlock:

✅ Exploratory Data Analysis

✅ Interactive Dashboard

✅ Visualization Studio

✅ AI Analytics

✅ Professional Reports
""")

    st.stop()

st.success("✅ Dataset Loaded Successfully")

# ============================================
# Dataset Overview
# ============================================

section(
    "📊 Statistical Summary",
    "View descriptive statistics for all dataset columns."
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Missing", int(df.isnull().sum().sum()))
col4.metric("Duplicates", int(df.duplicated().sum()))

st.divider()

# ============================================
# Dataset Preview
# ===========================================

section(
    "📈 Correlation Analysis",
    "Explore relationships between numeric variables."
)

rows = st.slider(
    "Rows to Display",
    5,
    min(100, len(df)),
    10
)

st.dataframe(df.head(rows), use_container_width=True)

st.divider()

# ============================================
# Data Types
# ============================================

st.markdown("""
## 🧾 Column Data Types
""")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(dtype_df, use_container_width=True)

st.divider()

# ============================================
# Missing Values
# ============================================

st.markdown("""
## ❌ Missing Values Analysis
""")

missing = df.isnull().sum()

missing = missing[missing > 0]

if len(missing) == 0:

    st.success("No Missing Values Found ✅")

else:

    st.dataframe(
        missing.rename("Missing Count"),
        use_container_width=True
    )

st.divider()

# ============================================
# Duplicate Rows
# ============================================

st.markdown("""
## 🔁 Duplicate Records Analysis

Identify repeated records that may affect data quality.
""")

duplicates = df.duplicated().sum()

st.metric(
    "Duplicate Rows",
    duplicates
)

st.divider()

# ============================================
# Summary Statistics
# ============================================

st.markdown("""
## 📊 Statistical Summary

View descriptive statistics for all dataset columns.
""")

st.dataframe(
    df.describe(include="all"),
    use_container_width=True
)

st.divider()

# ============================================
# Correlation Matrix
# ============================================

st.markdown("""
## 📈 Correlation Analysis

Explore relationships between numeric variables.
""")

numeric = df.select_dtypes(include="number")

if numeric.shape[1] >= 2:

    st.dataframe(
        numeric.corr(),
        use_container_width=True
    )

else:

    st.info("Need at least two numeric columns.")

st.divider()

# ============================================
# Column Information
# ============================================

st.markdown("""
## 📋 Column Information

Review column names, data types, and structure.
""")

selected = st.selectbox(
    "Select Column",
    df.columns
)

st.write("### Sample Values")

st.write(df[selected].head(10))

st.write("### Unique Values")

st.write(df[selected].nunique())

st.divider()

# ============================================
# Download Dataset
# ============================================

st.markdown("""
## 📥 Export Dataset

Download the processed dataset in your preferred format.
""")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    "dataset.csv",
    "text/csv"
)

buffer = pd.ExcelWriter(
    "temp.xlsx",
    engine="openpyxl"
)

df.to_excel(buffer, index=False)

buffer.close()

with open("temp.xlsx", "rb") as f:

    st.download_button(
        "📥 Download Excel",
        f,
        "dataset.xlsx"
    )