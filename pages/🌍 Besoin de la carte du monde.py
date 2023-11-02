from typing import Optional

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="SPCM",
    page_icon="📝",
)

DATE_COLUMN = "date/time"
DATA_URL = ("https://s3-us-west-2.amazonaws.com/"
            "streamlit-demo-data/uber-raw-data-sep14.csv.gz")


@st.cache_data(persist=True)
def load_data(nrows: Optional[int]) -> pd.DataFrame:
    """ Load dataset

    nrows: Number of rows of file to read. Useful for reading pieces of large files.

    Returns:
         pd.DataFrame: pandas's dataframe with `nrows` rows
    """
    data = pd.read_csv(DATA_URL, nrows=nrows)
    cols_lowercase = lambda x: str(x).lower()
    data.rename(cols_lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


st.markdown(f'<h1 style="color:#ff000a;font-size:30px; text-align: center;text-decoration: underline">{"Localisation"}</h1>', unsafe_allow_html=True)

data_load_state = st.text("Loading data...")
data = load_data(10)
data_load_state.text("La carte du monde")

filtered_data = data[data[DATE_COLUMN].dt.hour == 17]
# display Map

st.map(filtered_data)  # Use the st.map() function to plot the data
