import streamlit as st
import pandas as pd

st.write("""
# DATA 515 Project - Statistics for Dummies
""")

uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Table")
    st.dataframe(df)

whatDo = st.radio("What do you want to do?", ('Data Visualization', 'Statistics'))
if whatDo == 'Data Visualization':
    vizType = st.radio("What type of visualization do you want?", ('Scatterplot', 'Bar Chart'))
elif whatDo == 'Statistics':
    statType = st.radio("What type of statistics do you want to perform?", ('Hypothesis Testing', 'Regression'))
    if statType == 'Hypothesis Testing':
        testType = st.radio("What type of test do you want to perform?", ('Z-test', 'T-test', 'ANOVA'))
        if testType == 'Z-test':
             st.radio("1-sample or 2-sample Z-test", ('1-sample', '2-sample', 'ANOVA'))
        if testType == 'T-test':
             st.radio("1-sample or 2-sample Z-test", ('1-sample', '2-sample', 'ANOVA'))
if st.button('Click Me to Celebrate!'):
    st.balloons()
