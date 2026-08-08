import streamlit as st
import pandas as pd


SESSION_KEY = "uploaded_dataset"


def load_dataset(uploaded_file):
    """
    Load CSV or Excel dataset and store it in Streamlit session state.
    """

    if uploaded_file is None:
        return None

    try:

        if uploaded_file.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif uploaded_file.name.lower().endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        else:
            st.error("Unsupported file type.")
            return None

        st.session_state[SESSION_KEY] = df

        return df

    except Exception as e:

        st.error(f"Error loading dataset: {e}")

        return None


def get_dataset():
    """
    Returns uploaded dataframe.
    """

    return st.session_state.get(SESSION_KEY)


def has_dataset():

    return SESSION_KEY in st.session_state


def clear_dataset():

    if SESSION_KEY in st.session_state:
        del st.session_state[SESSION_KEY]


def dataset_info():

    df = get_dataset()

    if df is None:
        return None

    info = {

        "Rows": df.shape[0],

        "Columns": df.shape[1],

        "Missing Values": int(df.isnull().sum().sum()),

        "Duplicate Rows": int(df.duplicated().sum()),

        "Numeric Columns":
            len(df.select_dtypes(include="number").columns),

        "Categorical Columns":
            len(df.select_dtypes(exclude="number").columns),

        "Memory Usage (KB)":
            round(df.memory_usage(deep=True).sum() / 1024, 2)

    }

    return info