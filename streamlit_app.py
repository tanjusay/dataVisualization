import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

from io import BytesIO

# Streamlit app

st.title("📈 Data Visuals 📊")

# Upload Excel file

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file is not None:

    try:

        # Read data from Excel file

        df = pd.read_excel(uploaded_file)

        # Display data

        st.subheader("Raw Data")

        st.dataframe(df)

        # Plot options

        plot_type = st.selectbox("Select Plot Type", ["Linear", "Bar"])

        # Plot the data

        st.subheader("Data Visualization")

        if plot_type == "Linear":

            plt.plot(df.iloc[:, 0], df.iloc[:, 1])

            plt.xlabel(df.columns[0])

            plt.ylabel(df.columns[1])

            plt.title('Data Trend')

            st.pyplot()

        elif plot_type == "Bar":

            plt.bar(df.iloc[:, 0], df.iloc[:, 1])

            plt.xlabel(df.columns[0])

            plt.ylabel(df.columns[1])

            plt.title('Data Comparison')

            st.pyplot()

        # Conclusion

        st.subheader("Conclusion")

        if df.iloc[:, 1].sum() > 5000:

            st.write("The total data indicates a positive trend.")

        else:

            st.write("The total data indicates a stagnant or negative trend.")

    except Exception as e:

        st.error("Error: Unable to read the Excel file. Please make sure it is in the correct format.")

 
