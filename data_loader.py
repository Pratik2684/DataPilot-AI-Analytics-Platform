import streamlit as st
import pandas as pd


def load_data():
    """
    Upload a CSV or Excel file and store it in Streamlit Session State.
    This uploader should be called only once (preferably from Home page).
    """

    uploaded_file = st.sidebar.file_uploader(
        "📂 Upload CSV or Excel File",
        type=["csv", "xlsx"],
        help="Upload a dataset to use across the application."
    )

    if uploaded_file is not None:

        try:

            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)

            else:
                df = pd.read_excel(uploaded_file)

            # Save dataset in session state
            st.session_state["dataset"] = df

            st.sidebar.success("✅ Dataset Loaded Successfully!")

            return df

        except Exception as e:

            st.sidebar.error(f"Error loading dataset:\n{e}")

            return None

    # Return previously uploaded dataset if available
    if "dataset" in st.session_state:
        return st.session_state["dataset"]

    return None


def get_data():
    """
    Returns the uploaded dataset from session state.
    """

    return st.session_state.get("dataset", None)


def clear_data():
    """
    Removes dataset from session state.
    """

    if "dataset" in st.session_state:
        del st.session_state["dataset"]

        st.sidebar.success("Dataset Cleared!")