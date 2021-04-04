import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
ox.config(use_cache=True, log_console=True)

import osmnx as ox
G = ox.graph_from_place('montpellier, France','bike')


albert1er_point = (43.61620945549243, 3.874408006668091)
albert1er_node = ox.distance.get_nearest_node(G, (43.61620945549243, 3.874408006668091))
point = (43.61465,3.8336)
x_node = ox.distance.get_nearest_node(G, (43.61465,3.8336))
comedie = ox.geocoder.geocode('137 avenue de Lodève, Montpellier, France')
comedie_node = ox.distance.get_nearest_node(G, comedie)

Beracasa = (43.60969924926758, 3.896939992904663)
Celleneuve = (43.61465, 3.8336)
Delmas = (43.6266977, 3.8956288)
Gerhardt = (43.6138841, 3.8684671)
Lattes = (43.57883, 3.8684671)
Laverune = (43.5907, 3.81324)
Vielle_poste = (43.6157418, 3.9096322)

l = [Beracasa, Celleneuve, Delmas, Gerhardt, Lattes, Laverune, Vielle_poste, albert1er_point]
nodes = []
routes = []
for i in range (7): 
    nodes.append(ox.distance.get_nearest_node(G, l[i]))
    routes.append(nx.shortest_path(G,nodes[i], comedie_node))

from matplotlib.animation import FuncAnimation
# from IPython.display import HTML
# from matplotlib import rc
# import ffmpeg

fig, ax = ox.plot_graph_routes(G, routes, node_size = 0, show=False, close=False)

route0 = list(routes)[0]
route1 = list(routes)[1]
x_r= G.nodes[route0[0]]['x']
y_r = G.nodes[route0[0]]['y']

pic = ax.scatter(G.nodes[route0[0]]['x'] , G.nodes[route0[0]]['y']
                , s=20,
               c='y', alpha=1, edgecolor='none', zorder=4)

def animate(i):
    # inspired by code source of https://github.com/gboeing/osmnx/blob/master/osmnx/plot.py 
    pic.set_offsets((G.nodes[route0[i+1]]['x'] , G.nodes[route0[i+1]]['y']))
    return pic 
    

ani = FuncAnimation(fig, animate, frames=len(route0)-1, interval = 100, repeat=True)
plt.show()