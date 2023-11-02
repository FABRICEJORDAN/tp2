from typing import Optional

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="SPCM",
    page_icon="📝",
)

impression = pd.read_csv('impressions.csv',sep=",")
clic = pd.read_csv('clics.csv',sep=",")
achat = pd.read_csv('achats.csv',sep=",")

st.markdown(f'<h1 style="color:#ff000a;font-size:30px; text-align: center;text-decoration: underline">{"Les tables utilisés pour le dashboard"}</h1>', unsafe_allow_html=True)

tables = st.radio(
        "Sélectionner la table à afficher 👇",
        ["Impressions", "Clicks", "Achats"],
        key="visibility",
        horizontal=True,
    )
if tables == 'Impressions':
    st.write(impression)
elif tables == 'Clicks':
    st.write(clic)
else:
    st.write(achat)