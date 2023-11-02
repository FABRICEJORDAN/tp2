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
nbr_visiteur = clic['cookie_id'].nunique()
nbr_site = impression['external_site_id'].nunique()
nbr_publicite = impression['timestamp'].count()
nbr_campagne = impression['campaign_id'].nunique()
nbr_per = impression['cookie_id'].nunique()
nbr_achat = achat['timestamp'].count()
nbr_client = achat['cookie_id'].nunique()
nbr_produit = achat['product_id'].nunique()

st.markdown(f'<h1 style="color:#ff000a;font-size:30px; text-align: center;text-decoration: underline">{"Les statistiques sur les tables utilisées"}</h1>', unsafe_allow_html=True)

tables = st.radio(
        "Sélectionner la table dont vous voulez afficher 👇 les statistiques",
        ["Impressions", "Clicks", "Achats"],
        key="visibility",
        horizontal=True,
    )
if tables == 'Impressions':
    st.write("Le nombre de publicités:")
    st.write(nbr_publicite)
    st.write("Le nombre de site publicitaires")
    st.write(nbr_site)
    st.write("Le nombre de campagne publicitaires")
    st.write(nbr_campagne)
    st.write("Le nombre d'observateurs de publicités")
    st.write(nbr_per)
elif tables == 'Clicks':
    st.write("nombres totales de cliques sur les publiccités:")
    st.write(nbr_visiteur)
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(achat['price'].describe())
    with col2:
        st.write(achat['age'].describe())
    with col3:
        st.write("Le nombre d'achats totale effectués:")
        st.write(nbr_achat)
        st.write("Le nombre de clients:")
        st.write(nbr_client)
        st.write("Le nombre de produits achetés:")
        st.write(nbr_produit)
