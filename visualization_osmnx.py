import osmnx as ox
import pandas as pd
import matplotlib.pyplot as plt
from osmnx import footprints_from_place
import folium
ox.config(log_console=True, use_cache=True)
ox.__version__


adress_name = "3 Rue Joseph Delteil, 34000 Montpellier, France" #specify the adress
graph = ox.graph_from_address(adress_name)#Fetch OSM street network from the locatio
gdf = ox.project_graph(graph)#the street network
type(graph)#Verifing the that the type is networkx.classes.multidigraph.MultiDiGraph
#Plot the street

#Next we will retrive the extent of our location 
#area = ox.geometries_from_address(adress_name,tags = tags)
buildings = ox.geometries.geometries_from_address(adress_name,tags= {'amenity':True, 'landuse':['retail','commercial'], 'highway':'bus_stop'}, dist=400)
#osmnx.io.load_graphml(filepath, node_dtypes=None, edge_dtypes=None)
type(buildings)

map = ox.plot_graph(graph)
l = ox.io.save_graph_shapefile(graph, filepath="C:/Users/wiam chaoui/Desktop/projetdevlog/Montpellier_Biking")
cspn = ox.utils_graph.count_streets_per_node(graph)
map.save("mapMntp")
