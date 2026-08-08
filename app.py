import streamlit as st

st.set_page_config(
    page_title="DataPilot AI",
    page_icon="📊",
    layout="wide"
)

home = st.Page(
    "pages/0_Home.py",
    title="Home",
    icon="🏠",
    default=True
)

eda = st.Page(
    "pages/1_EDA.py",
    title="EDA",
    icon="📊"
)

dashboard = st.Page(
    "pages/2_Dashboard.py",
    title="Dashboard",
    icon="📈"
)

visualization = st.Page(
    "pages/5_Visualization.py",
    title="Visualization",
    icon="📉"
)

ai = st.Page(
    "pages/3_AI_Assistant.py",
    title="AI Analytics",
    icon="🤖"
)

report = st.Page(
    "pages/4_Report.py",
    title="Report",
    icon="📄"
)

pg = st.navigation(
    [
        home,
        eda,
        dashboard,
        visualization,
        ai,
        report
    ]
)

pg.run()