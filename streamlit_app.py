import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.image('./images/UNOSAT_Logo.png', width=100)
# Customize page title
st.title("UNOSAT - Streamlit Dashboard")

st.markdown(
    """
    This Streamlit application presents geospatial data from various sources.
    """
)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
