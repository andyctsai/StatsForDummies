import streamlit as st
import pandas as pd

st.write("""
# DATA 515 Project - Statistics for Dummies
""")

uploaded_file = st.file_uploader("Upload a CSV file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Table")
    st.dataframe(df)

whatDo = st.radio("What do you want to do?", ('Data Visualization', 'Statistics'), index=None)
if whatDo == 'Data Visualization':
    vizType = st.radio("What type of visualization do you want?", ('Scatterplot', 'Bar Chart'), index=None)
elif whatDo == 'Statistics':
    statType = st.radio("What type of statistics do you want to perform?", ('Hypothesis Testing', 'Regression'), index=None)
    if statType == 'Hypothesis Testing':
        testType = st.radio("What type of test do you want to perform?", ('Z-test', 'T-test', 'ANOVA'), index=None)