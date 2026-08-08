import streamlit as st


from utils.session import get_dataset
from utils.insights import generate_insights
from utils.sql_generator import generate_sql
from utils.pandas_generator import generate_pandas

st.markdown("""
# 🤖 AI Analytics Center

Generate insights, SQL queries and Pandas code using AI.
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

st.success("✅ Dataset Ready")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "💬 Business Insights",
        "🗄 SQL Generator",
        "🐼 Pandas Generator",
        "📊 Dataset Summary",
        "📈 Chart Suggestions"
    ]
)

# =====================================================
# BUSINESS INSIGHTS
# =====================================================

with tab1:

    st.subheader("AI Business Insights")

    insights = generate_insights(df)

    for item in insights:
        st.info(item)

# =====================================================
# SQL GENERATOR
# =====================================================

with tab2:

    st.subheader("Natural Language ➜ SQL")

    question = st.text_area(
        "Describe the SQL query",
        placeholder="Example: Show employees with salary greater than 50000"
    )

    if st.button("🗄 Generate SQL Query"):

        sql = generate_sql(question)

        st.code(sql, language="sql")

# =====================================================
# PANDAS GENERATOR
# =====================================================

with tab3:

    st.subheader("Natural Language ➜ Pandas")

    prompt = st.text_area(
        "Describe the pandas operation",
        placeholder="Example: Remove missing values"
    )

    if st.button("🐼 Generate Pandas Code"):

        code = generate_pandas(prompt)

        st.code(code, language="python")

# =====================================================
# DATASET SUMMARY
# =====================================================

with tab4:

    st.subheader("Dataset Overview")

    c1, c2 = st.columns(2)

    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])

    c3, c4 = st.columns(2)

    c3.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

    c4.metric(
        "Duplicate Rows",
        int(df.duplicated().sum())
    )

    st.divider()

    st.subheader("Column Types")

    st.write(df.dtypes)

# =====================================================
# CHART RECOMMENDATIONS
# =====================================================

with tab5:

    st.subheader("Recommended Charts")

    numeric = df.select_dtypes(include="number").columns

    categorical = df.select_dtypes(exclude="number").columns

    for col in numeric:

        st.success(f"📈 Histogram → {col}")

        st.success(f"📦 Box Plot → {col}")

    for col in categorical:

        st.info(f"📊 Bar Chart → {col}")

        st.info(f"🥧 Pie Chart → {col}")

st.divider()

st.caption("🚀 DataPilot AI • AI Analytics Center")