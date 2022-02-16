import streamlit as st
import pandas as pd

st.write("""
# DATA 515 Project - Statistics for Dummies
""")

uploaded_file = st.file_uploader("Choose a file")
df = pd.read_excel(uploaded_file)
if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.dataframe(df)
    st.table(df)

whatDo = st.radio("What do you want to do?", ('Data Visualization', 'Statistics'))
if whatDo == 'Data Visualization':
     st.write('What type of visualization do you want?')
elif whatDo == 'Statistics':
     st.write("What type of statistics do you want to perform?")