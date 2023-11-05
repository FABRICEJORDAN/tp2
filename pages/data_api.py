from typing import Optional

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="SPCM",
    page_icon="📝",
)

ac = pd.read_csv("http://127.0.0.1:8000/get_data")


st.markdown(f'<h1 style="color:#ff000a;font-size:30px; text-align: center;text-decoration: underline">{"Les données de fASTAPI"}</h1>', unsafe_allow_html=True)

st.table(ac)
