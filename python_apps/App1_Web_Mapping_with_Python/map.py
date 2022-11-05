# App 1: web mapping with python
# interactive mapping of population and volcanoes

import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
map.save("map.html")