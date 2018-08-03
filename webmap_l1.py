import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

# [90 to -90, 180 to -180]
map = folium.Map(location=[35, -82], zoom_start=4, tiles="Mapbox Bright")



fg = folium.FeatureGroup(name="MyMap")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Marker 1", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

