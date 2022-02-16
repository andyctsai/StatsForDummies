import streamlit as st
import pandas as pd

st.write("""
# DATA 515 Project - Statistics for Dummies
""")

uploaded_file = st.file_uploader("Choose a file")
st.dataframe(data=uploaded_file, width=None, height=None)