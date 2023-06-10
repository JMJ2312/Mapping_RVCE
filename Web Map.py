import folium
import pandas

data = pandas.read_csv("Applications\App1\Data.csv")
lat = list(data["Lat"])
lon = list(data["Lon"])
type = list(data["Type"])
names = list(data["Name"])
status = list(data["Status"])

map = folium.Map(location=[12.923177868020359, 77.49928786068105], zoom_start = 20)

fg = folium.FeatureGroup(name="RVCE")

for latt,long,ty,name,state in zip(lat, lon, type, names, status):
    if ty == "Department":
        colour = "blue"
    elif ty=="Eatery":
        colour = "orange"
    elif ty=="Administration":
        colour = "blue"
    elif ty=="POI":
        colour = "green"
    elif ty=="Hostel":
        colour = "gray"
    elif ty=="Services":
        colour = "purple"

    if state == "Under Construction":
        colour = "red"
        name= str(name)+" (Under Construction)"
    if ty==" ":
        ty="Click Me!"
    fg.add_child(folium.Marker(location=(latt, long), popup=name, icon=folium.Icon(color=colour), tooltip=ty))

fg.add_child(folium.GeoJson(data=open('Applications\App1\world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 50000000 
                                                       else 'orange' if x['properties']['POP2005'] < 100000000 else 'red'}))

map.add_child(fg)
map.save("Applications\App1\Map1.html")