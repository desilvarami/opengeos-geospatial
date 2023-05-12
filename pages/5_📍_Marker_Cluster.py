import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: <https://streamlit.geemap.org>
    - GitHub repository: <https://github.com/giswqs/streamlit-geospatial>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Qiusheng Wu: <https://wetlands.io>
    [GitHub](https://github.com/giswqs) | [Twitter](https://twitter.com/giswqs) | [YouTube](https://www.youtube.com/c/QiushengWu) | [LinkedIn](https://www.linkedin.com/in/qiushengwu)
    """
)

st.title("Marker Cluster")

m = leafmap.Map(center=[0, 0], zoom=2)
#cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
#regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'
hotspots = './data/modis.csv'
countries = './data/world.geojson'

m.add_geojson(countries, layer_name='Countries')
m.add_points_from_xy(
    hotspots,
    x="LONGITUDE",
    y="LATITUDE",
    #x="longitude",
    #y="latitude",
    #color_column='CONFIDENCE',
    #icon_names=['gear', 'map', 'leaf', 'globe'],
    #spin=True,
    #add_legend=True,
)

m.to_streamlit(height=700)
