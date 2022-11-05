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
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", 
    fill_color=color_producer(el), color='grey',fill=True, fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('python_course/python_apps/App1_Web_Mapping_with_Python/world.json', mode='r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)

map.save("python_course/python_apps/App1_Web_Mapping_with_Python/map.html")