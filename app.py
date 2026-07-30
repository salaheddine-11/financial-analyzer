import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Statement Analyzer",
    layout="wide"
)

st.title("Financial Statement Analyzer")
st.success("Phase 0 complete: environment is working.")

st.write("This is a prototype for Project 1.")

uploaded_file = st.file_uploader(
    "Upload a financial statement CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Uploaded data preview")
    st.dataframe(df.head(20))

    st.subheader("Basic information")
    st.write(f"Number of rows: {len(df)}")
    st.write(f"Number of columns: {len(df.columns)}")

else:
    st.info("No file uploaded yet. Try uploading data/sample_company.csv.")