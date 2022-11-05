# App 1: web mapping with python
# interactive mapping of population and volcanoes

import folium
import pandas

# loading data using pandas
data = pandas.read_csv("python_course/python_apps/App1_Web_Mapping_with_Python/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# adding a marker to the map
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el)+" m",parse_html=True), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)

map.save("python_course/python_apps/App1_Web_Mapping_with_Python/map.html")