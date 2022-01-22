import numpy as np
import pandas as pd
import pandas_profiling
import streamlit as st
import streamlit_pandas_profiling

# main application frame title
st.markdown('''
# **Machine Intelligence Experiment**
---
''')

# data upload application frame
with st.sidebar.header('Experiment CSV Upload'):
    dfile = st.sidebar.file_uploader("select file", type=["csv"])

if dfile is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(dfile)
        return csv
    df = load_csv()

    # create profile report
    pr = pandas_profiling.ProfileReport(df, explorative=True)

    # present data and profile
    st.header('**Input Data**')
    st.write(df)
    st.write('---')
    st.header('**Exploratory Data Analysis Report**')
    streamlit_pandas_profiling.st_profile_report(pr)

