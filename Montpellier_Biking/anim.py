# %%
# import pandas as pd
# import geopandas as gpd
# from shapely.geometry import Point
# from shapely.geometry import LineString
import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ox.config(use_cache=True, log_console=True)

# %%
G = ox.graph_from_place('Montpellier, France', 'bike')
# %%

Albert1er_point = (43.61620945549243, 3.874408006668091)
Albert1er_node = ox.distance.get_nearest_node(G, Albert1er_point)
point = (43.61465, 3.8336)
x_node = ox.distance.get_nearest_node(G, point)
Comedie = ox.geocoder.geocode('Place de la comédie, Montpellier, France')
Comedie_node = ox.distance.get_nearest_node(G, Comedie)

Beracasa = (43.60969924926758, 3.896939992904663)
Celleneuve = (43.61465, 3.8336)
Delmas = (43.6266977, 3.8956288)
Gerhardt = (43.6138841, 3.8684671)
Lattes = (43.57883, 3.8684671)
Laverune = (43.5907, 3.81324)
Vielle_poste = (43.6157418, 3.9096322)

liste = [Beracasa, Celleneuve, Delmas, Gerhardt, Lattes, Laverune,
         Vielle_poste, Albert1er_point]
nodes = []
routes = []


# %%
############################ for consol ############################
for i in range(len(liste)):
    nodes.append(ox.distance.get_nearest_node(G, liste[i]))
    routes.append(nx.shortest_path(G, nodes[i], Comedie_node))
    fig, ax = ox.plot_graph_routes(G, routes, node_size=0, show=False,
                                   close=False)

    route0 = list(routes)[0]
    route1 = list(routes)[1]
    x_r = G.nodes[route0[0]]['x']
    y_r = G.nodes[route0[0]]['y']

    pic = ax.scatter(G.nodes[route0[0]]['x'], G.nodes[route0[0]]['y'],
                     s=20, c='y', alpha=1, edgecolor='none', zorder=4)

# inspired by code source of https://github.com/gboeing/osmnx/blob/master/osmnx/plot.py 
    def animate(i):
        pic.set_offsets((G.nodes[route0[i+1]]['x'], G.nodes[route0[i+1]]['y']))
        return pic


    ani = FuncAnimation(fig, animate, frames=len(route0)-1, interval=100,
                        repeat=True)
    plt.show()
# %%
############################ for jupyter ############################
from IPython.display import HTML
from matplotlib import animation
from matplotlib import rc
#import ffmpeg

fig, ax = ox.plot_graph_routes(G, routes, 'blue', node_size=0, show=False,
                               close=False)
pic = ax.scatter(G.nodes[routes[2][0]]['x'], G.nodes[routes[2][0]]['y'], s=20,
                 c='y', alpha=1, edgecolor='none', zorder=4)

for i in range(len(liste)):
    nodes.append(ox.distance.get_nearest_node(G, liste[i]))
    routes.append(nx.shortest_path(G, nodes[i], Comedie_node))
    

    def animate(i):
        pic.set_offsets(((G.nodes[routes[2][i]]['x'],
                          G.nodes[routes[2][i]]['y']),
                         (G.nodes[routes[3][i]]['x'],
                          G.nodes[routes[3][i]]['y']),
                         (G.nodes[routes[4][i]]['x'],
                          G.nodes[routes[4][i]]['y'])))
        return pic

    ani = FuncAnimation(fig, animate, frames=len(routes[4]), interval=100)

rc('animation', html='jshtml')
ani
# %%
