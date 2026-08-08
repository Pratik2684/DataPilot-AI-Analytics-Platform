import streamlit as st


import pandas as pd

from utils.session import get_dataset
from utils.visualization import create_chart

st.title("📊 Visualization Studio")

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

st.divider()

# ============================================
# Chart Selection
# ============================================

st.markdown("""
## 📊 Visualization Studio

Create interactive charts instantly.
""")

chart_type = st.selectbox(
    "Chart Type",
    [
        "Bar Chart",
        "Line Chart",
        "Scatter Plot",
        "Pie Chart",
        "Histogram",
        "Box Plot",
        "Heatmap"
    ]
)

columns = list(df.columns)

numeric_cols = list(df.select_dtypes(include="number").columns)

categorical_cols = list(df.select_dtypes(exclude="number").columns)

# ============================================
# Axis Selection
# ============================================

x = None
y = None

if chart_type == "Pie Chart":

    x = st.selectbox(
        "Category",
        categorical_cols if categorical_cols else columns
    )

elif chart_type == "Histogram":

    x = st.selectbox(
        "Numeric Column",
        numeric_cols
    )

elif chart_type == "Heatmap":

    st.info("Heatmap will automatically use all numeric columns.")

else:

    col1, col2 = st.columns(2)

    with col1:

        x = st.selectbox(
            "X Axis",
            columns
        )

    with col2:

        y = st.selectbox(
            "Y Axis",
            numeric_cols
        )

st.divider()

# ============================================
# Generate Chart
# ============================================
if st.button("🚀 Generate Interactive Chart"):

    fig = create_chart(
        df,
        chart_type,
        x,
        y
    )

    if fig:

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.success("Chart Generated Successfully!")

st.divider()

# ============================================
# Dataset Preview
# ============================================

st.markdown("""
## 📋 Dataset Preview
""")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.divider()

# ============================================
# Dataset Information
# ============================================

st.header("📋 Dataset Information")

c1, c2, c3 = st.columns(3)

c1.metric("Rows", df.shape[0])

c2.metric("Columns", df.shape[1])

c3.metric(
    "Numeric Columns",
    len(numeric_cols)
)

st.divider()

# ============================================
# Chart Recommendations
# ============================================

st.markdown("""
## 🤖 AI Chart Recommendations
""")

recommendations = []

for col in numeric_cols:

    recommendations.append(
        f"📈 Histogram is recommended for **{col}**"
    )

    recommendations.append(
        f"📦 Box Plot is recommended for **{col}**"
    )

for col in categorical_cols:

    recommendations.append(
        f"📊 Bar Chart is recommended for **{col}**"
    )

    recommendations.append(
        f"🥧 Pie Chart is recommended for **{col}**"
    )

for item in recommendations:

    st.info(item)