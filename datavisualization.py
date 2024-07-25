import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Interactive Data Visualization")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the dataset
    st.write("Dataset Preview:")
    st.write(df.head())
    
    # Sidebar for user input
    st.sidebar.title("Visualization Settings")
    plot_type = st.sidebar.selectbox("Select Plot Type", ["Scatter", "Histogram", "Boxplot"])
    
    if plot_type == "Scatter":
        x_axis = st.sidebar.selectbox("X-axis", df.columns)
        y_axis = st.sidebar.selectbox("Y-axis", df.columns)
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=x_axis, y=y_axis)
        st.pyplot(plt)

    elif plot_type == "Histogram":
        column = st.sidebar.selectbox("Column", df.columns)
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True)
        st.pyplot(plt)

    elif plot_type == "Boxplot":
        column = st.sidebar.selectbox("Column", df.columns)
        plt.figure(figsize=(10, 6))
        sns.boxplot(y=column, data=df)
        st.pyplot(plt)
else:
    st.write("Please upload a CSV file to get started.")
