import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def what_do():
    whatDo = st.radio("What do you want to do?", ('Data Visualization', 'Statistics'))
    if whatDo == 'Data Visualization':
        vizType = st.radio("What type of visualization do you want?", ('Histogram','Scatterplot', 'Bar Chart'))
    elif whatDo == 'Statistics':
        statType = st.radio("What type of statistics do you want to perform?", ('Summary Statistics','Hypothesis Testing', 'Regression'))
        if statType == 'Hypothesis Testing':
            testType = st.radio("What type of test do you want to perform?", ('Z-test', 'T-test', 'ANOVA'))
            if testType == 'Z-test':
                 st.radio("1-sample or 2-sample Z-test", ('1-sample', '2-sample'))
            if testType == 'T-test':
                 st.radio("1-sample or 2-sample T-test", ('1-sample', '2-sample'))
    if st.button('Click Me to Celebrate!'):
        st.balloons()


if __name__ == '__main__':
    st.write("""
    # DATA 515 Project - Statistics for Dummies
    """)

    uploaded_file = st.file_uploader("Choose a CSV file")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Data Table")
        st.dataframe(df)
        what_do()