import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

st.title("Data Visualizer App 📈 📉")

# File uploader

file = st.file_uploader("Upload Excel or PDF file", type=["xlsx", "xls", "pdf"])

if file is not None:

    file_ext = file.name.split(".")[-1]

    

    if file_ext in ["xlsx", "xls"]:

        # Read Excel file

        df = pd.read_excel(file)

    elif file_ext == "pdf":

        # Read PDF file

        df = pd.read_pdf(file)

    else:

        st.error("Unsupported file format.")

        st.stop()

    

    # Perform data processing and visualization

    st.subheader("Data Summary")

    st.write(df.head())

    column_selectbox = st.selectbox("Select a column for visualization", df.columns)

    # Group data by selected column and count occurrences

    data_counts = df[column_selectbox].value_counts()

    st.subheader("Bar Chart")

    plt.figure(figsize=(10, 6))

    plt.bar(data_counts.index, data_counts.values)

    plt.xlabel(column_selectbox)

    plt.ylabel("Count")

    plt.xticks(rotation=45)

    st.pyplot()

