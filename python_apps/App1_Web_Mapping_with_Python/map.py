# App 1: web mapping with python
# interactive mapping of population and volcanoes

import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

# adding a marker to the map
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi i am a marker", icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("map.html")