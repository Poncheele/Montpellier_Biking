# %%
# Introduction :
# 1st try :
# First :
#  using OSMnx package we obtain Montpellier's
#  Network-graph (representation of a street-network from OpenStreetMap )
#  We will then  pick the nearest osm-node for each coordonate tha we are interested in ,as well as the shortest paths between them
# Second :
#  Modeling the events with  Casymda and SimPy
# Last :
#  Visualize with Leaflet.js


# importing ncessary packages 
import osmnx as ox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from osmnx import footprints_from_place
from IPython.display import Image
import folium
ox.config(log_console=True, use_cache=True)
ox.__version__
# %% 
#Montpellier's map (graph) 
graph = ox.graph_from_place('montpellier, France', network_type='all') #Fetch OSM street network from the location
gdf = ox.project_graph(graph) #the street network
type(graph)#Verifing the that the type is networkx.classes.multidigraph.MultiDiGraph
#Plot the street
type(gdf)
# %%
                                         
#Test : a map with one route 
img_folder = 'images'
extension = 'png'
size = 600
dpi = 800
street_widths = {'footway':0.5,
                'steps ': 0.5,
                'path' : 0.5,
                'track': 0.5,
                'service': 1,
                'residential': 1,
                'primary' : 3}
place = 'montpellier, France'
city = ox.geocode_to_gdf('montpellier, France')
ax = ox.project_gdf(city).plot()
fig, ax = ox.plot_figure_ground(address=place , dist= 3000,network_type='bike',
                                       street_widths=street_widths , dpi = dpi)
Image('{}/{}.{}'.format(img_folder, place, extension), height=size, width=size)

fig, ax = ox.plot_graph_route(graph, route, route_linewidth=6, node_size=0, bgcolor='k',route_alpha=0.1)

l = ox.io.save_graph_shapefile(G, filepath="C:/Users/wiam chaoui/Desktop/projetdevlog/Montpellier_Biking")

cspn = ox.utils_graph.count_streets_per_node(graph)# nodes in our graph 
# %%
import networkx as nx 
g = nx.Graph(graph)
# %% 

nod = list(g.nodes().keys())
len(cspn)

pos = ((43.60969924926758,3.896939992904663),(43.5907,3.81324),(43.61465,3.8336),(43.57926,3.93327),(43.57883,3.93324,),(43.6157418,3.9096322),(43.6138841,3.8684671),(43.61620945549243,3.874408006668091),(43.6266977,3.8956288),(43.6266977,3.8956288), (43.614660,3.833050), (43.615400,3.873950),(43.612690,3.895570),(43.626300,3.895110),(43.613880,3.868470), (43.5806384,3.9300896),(43.58639,3.80611),(43.617,3.911),())
compt_nod = np.arange(start = 0 , stop = len(pos) ,dtype=np.int64)
for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18] :
        compt_nod[i]= ox.distance.get_nearest_node(graph ,pos[i])
        print(compt_nod) #the nearest nod to every coordinate we interesting in 

ox.distance.get_nearest_node(graph ,pos[0])#Test 
import random
#Get a list of lists of routes between the nodes that correspond to the nodes of compt_nod
routes = np.arange(start = 0 , stop = 10 ,dtype=list)
routes = []
r = list([0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
random.shuffle(r)
routes.append(ox.shortest_path(graph,compt_nod[2],compt_nod[7]))
for i in r :
    routes.append(ox.shortest_path(graph,compt_nod[i],compt_nod[i+1]))
    print(routes)
routes = list(routes)
len(routes)

ox.plot_graph_route(graph,node_size=0.5, route = ox.shortest_path(graph,compt_nod[0],compt_nod[5]))
ox.plot_graph_routes(graph,routes,node_size=0.5, route_colors='white',route_linewidth=3,bgcolor='k' ,route_alpha=0.1)

#Make geodataframes from graph data
nodes, edges = ox.graph_to_gdfs(graph, nodes=True, edges=True)

# Folium 

# Creat a function 
# Try to generate an image for every t (an time intervall that we can choose )
#https://medium.com/udacity/creating-map-animations-with-python-97e24040f17b(to start with)
#https://python-visualization.github.io/folium/modules.html
#https://stackoverflow.com/questions/9018607/python-library-for-animated-map-visualization (Forum question
# #https://waterprogramming.wordpress.com/2016/03/01/making-movies-of-time-evolving-global-maps-with-python/)


# Get an image on one date and then next do a loop for all the date we are interested in .

# Preparing data 
# we need data that contains 4 colimns 1 for week days 2 number of bicycles passing 3 longitude and 4 latitude
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd
from folium import MarkerCluster
#Data processing :
data = pd.read_csv('bdata.csv',sep =';')
data

#Define marker for every density 
# blue for n< 90
# green for  90> n <200
# yellow for  200 >500
# orange for 500>1000
# red for < 1000
ox.simplification.simplify_graph(graph)
def color(c) : 
    if (c<90) : 
        return('blue')
    elif(90 <= c < 200) : 
        return('green')
    elif(200<=c<500) :
        return('yellow')
    elif(500<=c<100):
        return('orange')
    else : 
        return('red')

def radius(c) : 
        return(c * 0.3)


_radius=list()
for i in np.arange(start = 0,stop= len(byciclesnumb)-1) : 
    _radius.append(radius(byciclesnumb[i]))

_colors = list()
for i in np.arange(start = 0,stop= len(byciclesnumb)-1) : 
    _colors.append(color(byciclesnumb[i]))

# For a day d in a week we will creat a function that takes as argument a day in a week and gives for return a graph represinting 
#"La moyenne des vélos" that had passed in that day by each station 
# and then we will creat an image for each day
# For that first we need to 

map = ox.plot_graph_folium(graph)

folium.vector_layers.CircleMarker(location=Beracasa,popup = None , radius = 10).add_to(graph1)
plt.map(graph1)
loc= data.Column3

Marker_ = folium.CircleMarker(locations=loc,radius = _radius,color = _colors).add_to(graph1)
m = 'map.html'
folium.map.save(m)
