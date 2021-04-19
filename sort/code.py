# Pour pouvoir utiliser osmnx il faut télécharger son package.
# Pour cela il faut executer les commandes suivantes dans le terminal anaconda prompt:
#        conda config --prepend channels conda-forge
#        conda create -n ox --strict-channel-priority osmnx
#        conda activate ox
# %%
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
import plotly_express as px
import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
import Network_Module as nm

ox.config(use_cache=True, log_console=True)

# %%

G = ox.graph_from_place('montpellier, France', 'bike')

# %%

df = nm.Load_db.Load_db().save_as_df("Albert 1er")
df

# %%
# Consolidate intersections (combine complex nodes)
G_proj = ox.project_graph(G)
intersections = ox.consolidate_intersections(
    G_proj, rebuild_graph=True, tolerance=15, dead_ends=False
)
# %%
G2 = ox.consolidate_intersections(G_proj, rebuild_graph=True, tolerance=15,
                                  dead_ends=False)

# %%
fig, ax = ox.plot_graph(G2, node_color="w")

# %%
# show which nodes we'd remove if we simplify it (yellow)
nc = ["r" if ox.simplification._is_endpoint(G2, node)
      else "y" for node in G2.nodes()]
fig, ax = ox.plot_graph(G2, node_color=nc)
# %%
G3 = ox.simplify_graph(G2)
# %%
ox.plot_graph(G, figsize=(15, 10), node_size=0, edge_color='w')
# %%

# %%
albert1er_point = (43.61620945549243, 3.874408006668091)
albert1er_node = ox.distance.get_nearest_node(G, (43.61620945549243,
                                                  3.874408006668091))
point = (43.61465, 3.8336)
x_node = ox.distance.get_nearest_node(G, (43.61465, 3.8336))
comedie = ox.geocoder.geocode('137 avenue de Lodève, Montpellier, France')
comedie_node = ox.distance.get_nearest_node(G, comedie)
# %%
# orig = list(G)[7299660144]
# dest = list(G)[120]
# orig1 = list(G2)[985]
# dest1 = list(G2)[12]
route = ox.shortest_path(G, albert1er_node, x_node, weight="length")
fig, ax = ox.plot_graph_route(G, route, route_color="y", route_linewidth=6,
                              node_size=0)
# %%
gdf_edges = ox.graph_to_gdfs(G2, nodes=False)
# %%
Beracasa = (43.60969924926758, 3.896939992904663)
Celleneuve = (43.61465, 3.8336)
Delmas = (43.6266977, 3.8956288)
Gerhardt = (43.6138841, 3.8684671)
Lattes = (43.57883, 3.8684671)
Laverune = (43.5907, 3.81324)
Vielle_poste = (43.6157418, 3.9096322)
# %%
liste = [Beracasa, Celleneuve, Delmas, Gerhardt, Lattes, Laverune,
         Vielle_poste, albert1er_point]
nodes = []
routes = []
for i in range(len(liste)):
    nodes.append(ox.distance.get_nearest_node(G, liste[i]))
    routes.append(nx.shortest_path(G, nodes[i], comedie_node))

# %%
fig, ax = ox.plot_graph_routes(G, routes, route_colors="y", node_size=0)

# %%
route = nx.shortest_path(G, nodes[5], comedie_node, weight="length")
# fig, ax = ox.plot_graph_route(G, route, route_color="y", route_linewidth=6,
#                               node_size=0)
# %%
node_start = []
node_end = []
X_to = []
Y_to = []
X_from = []
Y_from = []
length = []
travel_time = []

for u, v in zip(route[:-1], route[1:]):
    node_start.append(u)
    node_end.append(v)
    length.append(round(G.edges[(u, v, 0)]['length']))
    # travel_time.append(round(G.edges[(u, v, 0)]['travel_time']))
    X_from.append(G.nodes[u]['x'])
    Y_from.append(G.nodes[u]['y'])
    X_to.append(G.nodes[v]['x'])
    Y_to.append(G.nodes[v]['y'])
# %%
df = pd.DataFrame(list(zip(node_start, node_end, X_from, Y_from,  X_to, Y_to,
                           length, travel_time)),
                  columns=["node_start", "node_end", "X_from", "Y_from",
                           "X_to", "Y_to", "length", "travel_time"])
df.head()
# %%
fig, ax = ox.plot_graph_routes(G, routes, node_size=0, show=False,
                               close=False)
x_r = (G.nodes[267851583]['x'], G.nodes[6255493123]['x'])
y_r = (G.nodes[267851583]['y'], G.nodes[6255493123]['y'])
ax.scatter(x_r, y_r, s=100, c='y', alpha=0.5, edgecolor='none', zorder=4)

plt.show()

# %%
from matplotlib.collections import LineCollection
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from matplotlib import rc
import ffmpeg
fig, ax = ox.plot_graph_routes(G, routes, node_size=0, show=False,
                               close=False)
route0 = list(routes)[0]
route1 = list(routes)[1]
x_r = G.nodes[route0[0]]['x']
y_r = G.nodes[route0[0]]['y']
plt.legend(frameon=False)

def init():
    pic = ax.scatter(x_r, y_r, s=100, c='y', alpha=0.5,
                     edgecolor='none', zorder=4)

def animate(i):
# inspired by code source of https://github.com/gboeing/osmnx/blob/master/osmnx/plot.py 
    pic.set_offsets(G.nodes[route0[i+1]]['x'], G.nodes[route0[i+1]]['y'])
    
    

ani = FuncAnimation(fig, animate, init_func=init , frames=32,
                    interval=100)
plt.show()
# %%
fig, ax = ox.plot_graph_routes(G, routes, node_size=0, show=False, 
                               close=False)
route0 = list(routes)[0]
x_r = G.nodes[route0[0]]['x']
y_r = G.nodes[route0[0]]['y']
ax.scatter(x_r, y_r, s=100, c='y', alpha=0.5, edgecolor='none',
           zorder=4)

plt.show()
# %%
ani
# %%
fig, ax = ox.plot_graph_routes(G, routes, node_size=0, show=False,
                               close=False)
for i in range(len(route0)):
    ax.scatter(G.nodes[route0[i]]['x'], G.nodes[route0[i]]['y'], s=100,
               c='y', alpha=0.5, edgecolor='none', zorder=4)
    plt.show()
# %%
import numpy as np
np.random.rand(2)
# %%

# %%
