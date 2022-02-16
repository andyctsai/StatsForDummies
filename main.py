import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def upload_file:
    uploaded_file = st.file_uploader("Choose a CSV file")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Dataframe Display")
        st.dataframe(df)
        what_do(df)

def what_do(df):
    whatDo = st.radio("What do you want to do?", ('Data Visualization', 'Statistics'))
    if whatDo == 'Data Visualization':
        vizType = st.radio("What type of visualization do you want?", ('Histogram','Scatterplot'))
        if vizType == 'Histogram':
            column = st.text_input('Dataframe Column For Histogram')
            histogram(df, column)
        if vizType == 'Scatterplot':
            x = st.text_input('X-axis column')
            y = st.text_input('Y-axis column')
            scatterplot(df, x, y)

    elif whatDo == 'Statistics':
        statType = st.radio("What type of statistics do you want to perform?", ('Summary Statistics','Hypothesis Testing', 'Regression'))
        if statType == 'Summary Statistics':
            column = st.text_input('Dataframe Column For Summary Statistics')
            summarystats(df, column)
        if statType == 'Hypothesis Testing':
            testType = st.radio("What type of test do you want to perform?", ('Z-test', 'T-test', 'ANOVA'))
            if testType == 'Z-test' or testType == 'T-test':
                one_or_two_sample()
                one_or_two_tailed()
                column = st.text_input('Dataframe Column For 1-sample Two-tailed T-test')
                population_mean = st.text_input("Enter Population Mean of Null Hypothesis: ")
                if column and population_mean:
                    tstat, pvalue = stats.ttest_1samp(df[column].tolist(), popmean=float(population_mean))
                    st.metric(label="T Statistic", value=tstat)
                    st.metric(label="P-value", value=pvalue)



def histogram(df, column):
    if column:
        fig = plt.figure(figsize=(10, 4))
        plt.hist(df[column])
        st.pyplot(fig)


def scatterplot(df, x, y):
    if x and y:
        fig = plt.figure(figsize=(10, 4))
        plt.scatter(df[x], df[y])
        st.pyplot(fig)


def summarystats(df, column):
    if column:
        mean = df[column].mean()
        sd = df[column].std()
        st.metric(label="Mean", value=mean)
        st.metric(label="Standard Deviation", value=sd)


def one_or_two_sample():
    st.radio("1-sample or 2-sample test", ('1-sample', '2-sample'))


def one_or_two_tailed():
    st.radio("1-tailed or 2-tailed test", ('1-tailed', '2-tailed'))


if __name__ == '__main__':
    st.write("""
    # DATA 515 Project - Statistics for Dummies
    """)
    upload_file()