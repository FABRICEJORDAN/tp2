from ctypes.wintypes import SIZE
from typing import Optional

import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objs as go
st.set_page_config(
    page_title="SPCM",
    page_icon="📝",
)

impression = pd.read_csv('impressions.csv',sep=",")
clic = pd.read_csv('clics.csv',sep=",")
achat = pd.read_csv('achats.csv',sep=",")

st.markdown(f'<h1 style="color:#ff000a;font-size:30px; text-align: center;text-decoration: underline">{"Chiffre affaire et publicités par Campagne"}</h1>', unsafe_allow_html=True)

pub_campagne= impression.groupby("campaign_id",as_index=False)["timestamp"].count()
impre_achat = pd.merge(impression, achat, on='cookie_id') #je joins la table achat et impression
chif_campagne= impre_achat.groupby("campaign_id", as_index=False)["price"].sum() #Je fais la somme des prix par campaign_id
pcc = pd.merge(pub_campagne, chif_campagne, on='campaign_id')
pcc['campaign_id'] = pcc['campaign_id'].apply(str)
pcc['taux de pertinence'] = (pcc["price"]/pcc["timestamp"])*100
data = [
    go.Scatter(x = pcc['campaign_id'], y=pcc["timestamp"], name='Nombre de publicités', text=pcc["timestamp"]),
    go.Bar(x = pcc['campaign_id'], y = pcc["price"], name='Chiffre affaire généré', text=pcc["price"])
]
fig = go.Figure(data=data)

st.plotly_chart(fig)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(pcc['campaign_id'])
with col2:
    st.write(pcc['taux de pertinence'])
with col3:
    st.write('La campagne la plus rentable est la campagne 2')