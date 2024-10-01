import streamlit as st
import os.path
import numpy as np
import pandas as pd
from urllib.request import urlretrieve

# Dataset list
options =  {"dataset": ["basic1","basic2","basic3", "basic4", "basic5", "box", "boxes", "boxes2", "boxes3"],
            "url": ["https://drive.google.com/file/d/1AwBoHW59poWfOEzzpTdFJmIqJeeYRHjQ/view?usp=share_link",
                      "https://drive.google.com/file/d/1T2gRzWnqU4xvTCOI6f3Lwwhrv4Z8fIej/view?usp=share_link",
                      "https://drive.google.com/file/d/1rT688DY90G14Cpj5Hd9wNy7LFFFEVNLO/view?usp=share_link",
                      "https://drive.google.com/file/d/1NmR-SnqxyQEJMAX7IP-4Le2fs4SfkwHD/view?usp=share_link",
                      "https://drive.google.com/file/d/1q_br5XJoUaj2OGmss924CoMIrMsjw0bG/view?usp=share_link",
                      "https://drive.google.com/file/d/1gCiqfCMYlVxeQS9iesIZIuTbASXYpLxs/view?usp=share_link",
                      "https://drive.google.com/file/d/16qcmAHdIBzk-7hYoRUrIEpi4hjonCOE9/view?usp=share_link",
                      "https://drive.google.com/file/d/1KcDtDA458CwCXxUGLBRxsCX7WMCkEGLP/view?usp=share_link",
                      "https://drive.google.com/file/d/1peoKUk2Gt02JKThVdIDO1K9laXV6BrEx/view?usp=share_link"]}

@st.cache_data
def load_df(url):
    if url:
        url='https://drive.google.com/uc?id=' + url.split('/')[-2]
        filename = 'ds.csv'
        urlretrieve(url, filename)
        df = pd.read_csv(filename)
        return df
    return None

options_df = pd.DataFrame(options, columns=["dataset", "url"])
# st.write(options_df)
# Seleccionamos el Dataseet que se usará
selected_ds = st.sidebar.selectbox("Seleccione un Dataset", options=options_df["dataset"].values[:])
selected_url = options_df.where(options_df["dataset"] == selected_ds).dropna()

# Cargamos los datos (descarga de la url y se carga el dataset)
df = load_df(selected_url['url'].values[0])

# Mostramos la información seleccionada
st.subheader(selected_url['dataset'].values[0])
st.write("URL:",selected_url['url'].values[0])
st.write(df.head())
st.session_state.df = df


