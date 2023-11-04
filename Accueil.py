
from typing import Optional
from PIL import Image

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

st.title("Bienvenue sur le SPCM")
st.markdown(f'<h1 style="color:#ff000a;font-size:30px; text-align: center">{"Suivi Performance Campagne Marketing"}</h1>', unsafe_allow_html=True)

#image = Image.open('logo.PNG')
#st.image(image, width=250)
st.markdown(f'<h1 style="text-align: center; text-decoration: underline;font-size:24px">{"Les chiffres clés"}</h1>', unsafe_allow_html=True)

nbr_publicite = impression['timestamp'].count()
nbr_client = achat['cookie_id'].nunique()
nbr_campagne = impression['campaign_id'].nunique()
nbr_visiteur = clic['cookie_id'].nunique()
nbr_site = impression['external_site_id'].nunique()
nbr_produit = achat['product_id'].nunique()
ca = achat['price'].sum()

data = {
  "Chiffre d'affaire": [ca],
  "Nombre de campagne marketing": [nbr_campagne],
  "Nombre de client": [nbr_client],
  "Nombre de produit vendu": [nbr_produit],
  "Nombre de sites atteints": [nbr_site],
}
df = pd.DataFrame(data)
st.table(df)
