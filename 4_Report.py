import streamlit as st


import pandas as pd

from io import BytesIO

from utils.session import get_dataset
from utils.insights import generate_insights
from utils.report import create_pdf_report

st.markdown("""
# 📄 Report Center

Generate professional business reports.
""")

df = get_dataset()

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

# ==========================================
# KPI Cards
# ==========================================

st.subheader("Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Missing", int(df.isnull().sum().sum()))
c4.metric("Duplicates", int(df.duplicated().sum()))

st.divider()

# ==========================================
# Preview
# ==========================================

st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.divider()

# ==========================================
# Statistics
# ==========================================

st.subheader("Summary Statistics")

st.dataframe(
    df.describe(include="all"),
    use_container_width=True
)

st.divider()

# ==========================================
# Business Insights
# ==========================================

st.subheader("Business Insights")

insights = generate_insights(df)

for insight in insights:
    st.info(insight)

st.divider()

# ==========================================
# Download CSV
# ==========================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download CSV",
    csv,
    "dataset.csv",
    "text/csv"
)

# ==========================================
# Download Excel
# ==========================================

buffer = BytesIO()

with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
    df.to_excel(writer, index=False)

st.download_button(
    "📥 Download Excel",
    buffer.getvalue(),
    "dataset.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.divider()

# ==========================================
# PDF Report
# ==========================================

st.subheader("Generate PDF Report")

if st.button("📄 Generate Professional PDF"):

    pdf = create_pdf_report(df)

    st.download_button(
        "⬇ Download PDF Report",
        pdf,
        "DataPilot_Report.pdf",
        mime="application/pdf"
    )

st.divider()

st.success("🎉 Report Ready")