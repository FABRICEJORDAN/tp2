from typing import Optional

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="SPCM",
    page_icon="📝",
)

ac = pd.read_json("http://127.0.0.1:8000/get_data")

st.markdown(f'<h3 style="color:#ff000a;font-size:30px; text-align: center;text-decoration: underline">{"Les données de fASTAPI"}</h3>', unsafe_allow_html=True)
st.markdown(f'<h3 style="color:black;font-size:30px; text-align: center;text-decoration: underline">{"Voici la table contenant toutes les tables fusionnées"}</h3>', unsafe_allow_html=True)
st.write(ac)
