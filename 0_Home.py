import streamlit as st

from utils.session import (
    load_dataset,
    get_dataset,
    has_dataset,
    clear_dataset,
    dataset_info
)

st.title("📊 DataPilot AI")

st.markdown("""
### 🚀 Professional AI Powered Data Analytics Platform

Upload your dataset once and use it across all modules.

---
""")

# ==========================================
# Upload Dataset
# ==========================================

uploaded = st.file_uploader(
    "📂 Upload CSV or Excel Dataset",
    type=["csv", "xlsx"]
)

if uploaded is not None:
    load_dataset(uploaded)

# ==========================================
# Dataset Information
# ==========================================

if has_dataset():

    st.success("✅ Dataset Loaded Successfully")

    info = dataset_info()

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", info["Rows"])
    col2.metric("Columns", info["Columns"])
    col3.metric("Missing Values", info["Missing Values"])

    col4, col5, col6 = st.columns(3)

    col4.metric("Duplicate Rows", info["Duplicate Rows"])
    col5.metric("Numeric Columns", info["Numeric Columns"])
    col6.metric("Categorical Columns", info["Categorical Columns"])

    st.info(
        f"Memory Usage : {info['Memory Usage (KB)']} KB"
    )

    if st.button("🗑 Remove Dataset"):

        clear_dataset()

        st.success("Dataset Removed Successfully")

        st.rerun()

else:

    st.warning("⚠ No dataset uploaded.")

# ==========================================
# Feature Cards
# ==========================================

st.divider()

st.header("🚀 Available Modules")

c1, c2 = st.columns(2)

with c1:

    st.info("""
### 📊 EDA

✔ Dataset Preview

✔ Missing Values

✔ Duplicate Rows

✔ Summary Statistics
""")

    st.info("""
### 📈 Dashboard

✔ KPI Cards

✔ Interactive Charts

✔ Filters

✔ Downloads
""")

    st.info("""
### 📉 Visualization Studio

✔ Bar Chart

✔ Scatter Plot

✔ Pie Chart

✔ Histogram

✔ Heatmap
""")

with c2:

    st.info("""
### 🤖 AI Analytics Center

✔ Business Insights

✔ SQL Generator

✔ Pandas Generator

✔ Recommendations
""")

    st.info("""
### 📄 Report Generator

✔ PDF Report

✔ Excel Export

✔ Business Summary
""")

    st.info("""
### 💻 Technologies

✔ Python

✔ Streamlit

✔ Pandas

✔ Plotly

✔ ReportLab
""")

st.divider()

st.markdown(
"""
### 📌 Instructions

1️⃣ Upload your dataset from this page.

2️⃣ Navigate to **EDA**.

3️⃣ Explore the **Dashboard**.

4️⃣ Create custom charts in **Visualization Studio**.

5️⃣ Use **AI Analytics Center** for insights.

6️⃣ Generate a professional report.

---
Made with ❤️ using Streamlit.
"""
)