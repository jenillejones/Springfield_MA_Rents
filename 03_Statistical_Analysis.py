import os
import streamlit as st
from copy import deepcopy
#from streamlit_lottie import st_lottie
import helpers as hp
from config import token

# # User dependent variables - ORIGINAL
# raw_data_path = "./data/raw/georef-switzerland-kanton.geojson"
# proc_data_path = "./data/processed/rents_with_coords_clean.csv"

# User dependent variables - RE-Defined using Absolute Paths
raw_data_path = os.path.abspath(os.path.join("../.", "data/raw/", "georef-switzerland-kanton.geojson"))
proc_data_path = os.path.abspath(os.path.join("../.", "data/processed/", "rents_with_coords_clean.csv"))

# Secrets (accessed via st.secrets())
#mapbox_access_token = st.secrets["MAPBOX_ACCESS_TOKEN"]

#mapbox_access_token = st.secrets['mapbox']['MAPBOX_ACCESS_TOKEN']
#token = "pk.eyJ1IjoiampvbmVzMSIsImEiOiJjbDdzaG9xcTkwODM0M3BtbXp2OW5oa29mIn0.d1NUWF43CRbDcCZ4B-V7UA"
mapbox_token = token

# Load the data
df_proc, cantons = hp.load_data(raw_data_path, proc_data_path)
df_plotting = deepcopy(df_proc)

# Sidebar
# Lottie icon
# lottie_url = "https://assets3.lottiefiles.com/packages/lf20_fgne1q0e.json"
# lottie_pin = hp.load_lottieurl(lottie_url)
# with st.sidebar:
#     st_lottie(lottie_pin, speed=1, height=100)

st.dataframe(df_plotting)
