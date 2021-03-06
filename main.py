import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.stats.weightstats as sm

test_data = None


class HypothesisTest:
    def __init__(self, test_type, num_samples, num_tails, function, function_extra):
        self.test_type = test_type
        self.num_samples = num_samples
        self.num_tails = num_tails
        self.set_function()

    def get_num_samples(self):
        return self.num_samples

    def get_num_tails(self):
        return self.num_tails

    def get_test_type(self):
        return self.test_type

    def set_num_samples(self, num_samples):
        self.num_samples = num_samples

    def set_num_tails(self, num_tails):
        self.num_tails = num_tails

    def set_test_type(self, test_type):
        self.test_type = test_type

    def do_test(self):
        population_mean = st.text_input("Enter Population Mean of Null Hypothesis: ")
        sig_level = st.text_input("Enter Significance Level (Ex: 0.05): ")
        if population_mean and sig_level:
            zstat, pvalue = eval(
                self.function + "(test_data.tolist()," + self.function_extra + "=float(population_mean))")
            st.metric(label="Z Statistic", value=zstat)
            st.metric(label="P-value for Z-test", value=pvalue)

            if pvalue < float(sig_level):
                st.write("We reject the null hypothesis at the ", sig_level, " significance level.")
            else:
                st.write("We DO NOT reject the null hypothesis at the ", sig_level, " significance level.")

    def set_function(self):
        if self.test_type == 'Z-test':
            self.function = 'sm.ztest'
            self.function_extra = 'value'
        elif self.test_type == 'T-test':
            self.function = 'stats.ttest_1samp'
            self.function_extra = 'popmean'


def upload_file():
    uploaded_file = st.file_uploader("Choose a CSV file")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Dataframe Display")
        st.dataframe(df)
        what_do(df)


def what_do(df):
    st.write("What do you want to do?")
    if st.button('Data Visualization'):
        vizType = st.radio("What type of visualization do you want?", ('Histogram', 'Scatterplot'))
        if vizType == 'Histogram':
            column = st.text_input('Dataframe Column For Histogram')
            histogram(df, column)
        if vizType == 'Scatterplot':
            x = st.text_input('X-axis column')
            y = st.text_input('Y-axis column')
            scatterplot(df, x, y)

    elif st.button('Statistics'):
        statType = st.radio("What type of statistics do you want to perform?",
                            ('Summary Statistics', 'Hypothesis Testing', 'Regression'))
        if statType == 'Summary Statistics':
            column = st.text_input('Dataframe Column For Summary Statistics')
            summarystats(df, column)
        if statType == 'Hypothesis Testing':
            test_type = st.radio("What type of test do you want to perform?", ('Z-test', 'T-test', 'ANOVA'))
            num_samples = st.radio("1-sample or 2-sample test", ('1-sample', '2-sample'))
            num_tails = st.radio("1-tailed or 2-tailed test", ('1-tailed', '2-tailed'))
            test = HypothesisTest(test_type, num_samples, num_tails, None, None)
            column = st.text_input('Dataframe Column For Hypothesis Test')
            if column:
                global test_data
                test_data = df[column]
                test.do_test()


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


if __name__ == '__main__':
    st.write("""
    # DATA 515 Project - Statistics for Dummies
    """)
    upload_file()