from typing import Optional
from plotly import graph_objs as go
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="SPCM",
    page_icon="📝",
)

impression = pd.read_csv('impressions.csv',sep=",")
impression['external_site_id'] = impression['external_site_id'].apply(str)
clic = pd.read_csv('clics.csv',sep=",")

st.markdown(f'<h1 style="color:#ff000a;font-size:30px; text-align: center;text-decoration: underline">{"Nombre de clique et publicités par site"}</h1>', unsafe_allow_html=True)

impre_clic = pd.merge(impression, clic, on='cookie_id') #je joins la table clic et impression
nbclic_site= impre_clic.groupby("external_site_id", as_index=False)["cookie_id"].count() #Je compte les clics
pub_site= impression.groupby("external_site_id", as_index=False)["timestamp"].count()
pcs = pd.merge(nbclic_site, pub_site, on='external_site_id')
pcs['taux de pertinence'] = (pcs["cookie_id"]/pcs["timestamp"])*100
#je tris par ordre décroissant pour afficher les 5 premiers sites
first=pcs.sort_values(by='cookie_id', ascending=False)[:7]
first.columns = first.columns.str.replace('external_site_id', 'site_id')
first.columns = first.columns.str.replace('cookie_id', 'nombre clics')
first.columns = first.columns.str.replace('timestamp', 'nombre publicités')
#j'affiche sur un graphe en barre
fig = px.bar(first,x='site_id',y='nombre clics',color='site_id',height=400)
data = [
    go.Scatter(x = first['site_id'], y=first["nombre clics"], name='Nombre de clics', text=first["nombre clics"]),
    go.Bar(x = first['site_id'], y = first["nombre publicités"], name='Nombre de publicités', text=first["nombre publicités"])
]
fig = go.Figure(data=data)
st.plotly_chart(fig)
st.write('Le site le plus pertinent est le 772983. Voir le tableau recap pour plus de détail!')
agree = st.checkbox('Voir le tableau récapitulatif')

if agree:
    st.write(first)

