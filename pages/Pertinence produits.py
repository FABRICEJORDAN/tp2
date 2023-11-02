from typing import Optional

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="SPCM",
    page_icon="📝",
)

achat = pd.read_csv('achats.csv',sep=",")
nbr_achat = achat['timestamp'].count()
st.markdown(f'<h1 style="color:#ff000a;font-size:30px; text-align: center;text-decoration: underline">{"Nombre achat par Produit"}</h1>', unsafe_allow_html=True)
achat_produit= achat.groupby("product_id", as_index=False)["timestamp"].count()
fig = px.bar(achat_produit,x='product_id',y='timestamp',color='product_id',height=400, text='timestamp', labels={'timestamp': 'Nombre achats effectués'})
st.plotly_chart(fig)

col1, col2, col3 = st.columns(3)
with col1:
    st.write("Le Nombre totale d'achats est de:")
with col2:
    st.write(nbr_achat)
