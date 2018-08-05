import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000: 
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# [90 to -90, 180 to -180]
map = folium.Map(location=[35, -82], zoom_start=4, tiles="Mapbox Bright")

# Make a feature group in order to customize the layer control
# This FG is to read the Volcanoes CSV and list an Icon depending on 
# their elevations.
fgv = folium.FeatureGroup(name='Volcanoes')

# Read elevation information from csv file and pastes a circle icon on the map
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" Meters", 
    fill_color=color_producer(el), color='grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

# Displays a certain color on the map depending on population amount
# reads information from Json file
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Initializes map opbject for each feature group
map.add_child(fgv)
map.add_child(fgp)

# This adds the layor control Icon to the map
# Must be after the map has been initialized
map.add_child(folium.LayerControl())



map.save("Map1.html")

