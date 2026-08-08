import streamlit as st
import pandas as pd
from io import BytesIO

from utils.session import get_dataset
from utils.dashboard import get_kpis
from utils.charts import (
    bar_chart,
    pie_chart,
    histogram,
    scatter,
    box_plot,
    heatmap
)
from utils.insights import generate_insights

# ==========================================
# Page Config
# ==========================================

st.title("📈 Interactive Dashboard")

st.caption(
    "Analyze your uploaded dataset with KPIs, charts, filters and AI insights."
)

# ==========================================
# Load Dataset
# ==========================================

df = get_dataset()

if df is None:

    st.info("""
## 📂 No Dataset Loaded

Please upload a dataset from the **Home** page.

Supported Formats

- CSV
- Excel (.xlsx)
""")

    st.stop()

# ==========================================
# Sidebar Filters
# ==========================================

st.sidebar.title("🎯 Filters")

st.sidebar.caption(
    "Filters are generated automatically from your dataset."
)

filtered_df = df.copy()

categorical_cols = filtered_df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

for col in categorical_cols:

    unique_values = sorted(
        filtered_df[col].dropna().unique().tolist()
    )

    # Skip huge columns
    if len(unique_values) > 50:
        continue

    selected = st.sidebar.multiselect(
        label=col,
        options=unique_values,
        default=unique_values
    )

    filtered_df = filtered_df[
        filtered_df[col].isin(selected)
    ]

st.sidebar.divider()

st.sidebar.success(
    f"Rows after filtering : {filtered_df.shape[0]}"
)

# ==========================================
# KPI Cards
# ==========================================

kpis = get_kpis(filtered_df)

st.markdown("## 📊 Dashboard Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Rows",
    f"{kpis['rows']:,}"
)

c2.metric(
    "Columns",
    kpis["columns"]
)

c3.metric(
    "Missing Values",
    kpis["missing"]
)

c4.metric(
    "Duplicate Rows",
    kpis["duplicates"]
)

c5, c6, c7 = st.columns(3)

c5.metric(
    "Numeric Columns",
    kpis["numeric"]
)

c6.metric(
    "Categorical Columns",
    kpis["categorical"]
)

c7.metric(
    "Memory (KB)",
    kpis["memory"]
)

# ==========================================
# Optional KPIs
# ==========================================

if kpis["avg_salary"] is not None:

    col1, col2 = st.columns(2)

    col1.metric(
        "Average Salary",
        f"₹{kpis['avg_salary']:,.0f}"
    )

    col2.metric(
        "Highest Salary",
        f"₹{kpis['max_salary']:,.0f}"
    )

if kpis["avg_experience"] is not None:

    st.metric(
        "Average Experience",
        f"{kpis['avg_experience']} Years"
    )

st.divider()

# ==========================================
# Tabs
# ==========================================

tab1, tab2, tab3 = st.tabs(
    [
        "📊 Dashboard",
        "📈 Charts",
        "📄 Dataset"
    ]
)
# ==========================================
# TAB 1 - Dashboard
# ==========================================

with tab1:

    st.markdown("## 💡 AI Business Insights")

    insights = generate_insights(filtered_df)

    for insight in insights:
        st.info(insight)

    st.divider()

    st.markdown("## 📈 Dataset Health")

    q1, q2, q3 = st.columns(3)

    q1.metric(
        "Quality Score",
        f"{kpis['quality_score']}%"
    )

    q2.metric(
        "Missing Values",
        kpis["missing"]
    )

    q3.metric(
        "Duplicate Rows",
        kpis["duplicates"]
    )

# ==========================================
# TAB 2 - Charts
# ==========================================

with tab2:

    st.markdown("## 📈 Interactive Charts")

    if filtered_df.empty:

        st.warning("No data available after applying filters.")

    else:

        col1, col2 = st.columns(2)

        # ------------------------
        # Bar Chart
        # ------------------------

        with col1:

            fig = bar_chart(filtered_df)

            if fig is not None:

                fig.update_layout(
                    template="plotly_white",
                    height=450
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:

                st.info("Bar Chart not available.")

        # ------------------------
        # Pie Chart
        # ------------------------

        with col2:

            fig = pie_chart(filtered_df)

            if fig is not None:

                fig.update_layout(
                    template="plotly_white",
                    height=450
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:

                st.info("Pie Chart not available.")

        st.divider()

        col3, col4 = st.columns(2)

        # ------------------------
        # Histogram
        # ------------------------

        with col3:

            fig = histogram(filtered_df)

            if fig is not None:

                fig.update_layout(
                    template="plotly_white",
                    height=450
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:

                st.info("Histogram not available.")

        # ------------------------
        # Scatter Plot
        # ------------------------

        with col4:

            fig = scatter(filtered_df)

            if fig is not None:

                fig.update_layout(
                    template="plotly_white",
                    height=450
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:

                st.info("Scatter Plot not available.")

        st.divider()

        # ------------------------
        # Box Plot
        # ------------------------

        fig = box_plot(filtered_df)

        if fig is not None:

            fig.update_layout(
                template="plotly_white",
                height=450
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.info("Box Plot not available.")

        # ------------------------
        # Heatmap
        # ------------------------

        fig = heatmap(filtered_df)

        if fig is not None:

            fig.update_layout(
                height=600
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.info("Correlation Heatmap not available.")
            
            # ==========================================
# TAB 3 - Dataset
# ==========================================

with tab3:

    st.markdown("## 📋 Dataset Preview")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=450
    )

    st.divider()

    # ======================================
    # Dataset Information
    # ======================================

    st.markdown("## 📊 Dataset Information")

    info1, info2, info3, info4 = st.columns(4)

    info1.metric(
        "Rows",
        f"{filtered_df.shape[0]:,}"
    )

    info2.metric(
        "Columns",
        filtered_df.shape[1]
    )

    info3.metric(
        "Missing Values",
        int(filtered_df.isnull().sum().sum())
    )

    info4.metric(
        "Duplicate Rows",
        int(filtered_df.duplicated().sum())
    )

    st.divider()

    # ======================================
    # Data Types
    # ======================================

    st.markdown("## 📑 Column Information")

    column_info = pd.DataFrame({

        "Column": filtered_df.columns,

        "Data Type": filtered_df.dtypes.astype(str),

        "Missing Values": filtered_df.isnull().sum().values,

        "Unique Values": filtered_df.nunique().values

    })

    st.dataframe(
        column_info,
        use_container_width=True
    )

    st.divider()

    # ======================================
    # Summary Statistics
    # ======================================

    st.markdown("## 📈 Summary Statistics")

    st.dataframe(
        filtered_df.describe(include="all"),
        use_container_width=True
    )

    st.divider()

    # ======================================
    # Download Section
    # ======================================

    st.markdown("## 📥 Export Dataset")

    csv = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(

            label="📄 Download CSV",

            data=csv,

            file_name="filtered_dataset.csv",

            mime="text/csv",

            use_container_width=True

        )

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        filtered_df.to_excel(
            writer,
            index=False
        )

    with col2:

        st.download_button(

            label="📊 Download Excel",

            data=output.getvalue(),

            file_name="filtered_dataset.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

            use_container_width=True

        )

    st.divider()

    # ======================================
    # Dataset Memory
    # ======================================

    memory = round(
        filtered_df.memory_usage(deep=True).sum() / 1024,
        2
    )

    st.success(
        f"💾 Dataset Memory Usage : {memory} KB"
    )
    
    # ==========================================
# Footer
# ==========================================

st.divider()

st.caption(
    "📊 DataPilot AI | Interactive Dashboard | Built with Python, Streamlit & Plotly"
)

    
    
    
    
    
    
    
    
    
    
    
    
    
