#%%
import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

ox.config(use_cache=True, log_console=True)

# %%
G = ox.graph_from_place('Montpellier, France', 'bike')

# %%
    
Beracasa = (43.60969924926758, 3.896939992904663)
Celleneuve = (43.61465, 3.8336)
Delmas = (43.6266977, 3.8956288)
Gerhardt = (43.6138841, 3.8684671)
Lattes = (43.57883, 3.8684671)
Laverune = (43.5907, 3.81324)
Vielle_poste = (43.6157418, 3.9096322)
Albert1er_point = (43.61620945549243, 3.874408006668091)

liste = [Beracasa, Celleneuve, Delmas, Gerhardt, Lattes, Laverune,
         Vielle_poste, Albert1er_point]

#orig_points = []
#for i in liste:
#    x, y = i.xy
#    x = x[0]
#    y = y[0]
#    orig_points.append((y, x))



# %%
############################ for jupyter ############################
from IPython.display import HTML
from matplotlib import animation
from matplotlib import rc


Comedie = ox.geocoder.geocode('Place de la comédie, Montpellier, France')
Comedie_node = ox.distance.get_nearest_node(G, Comedie)
#%%
nodes = []
routes = []
for i in range(len(liste)):
    nodes.append(ox.distance.get_nearest_node(G, liste[i]))
    routes.append(nx.shortest_path(G, nodes[i], Comedie_node))
#%%
#orig_points = []
#for j in range(0,len(routes)):
#    x= G.nodes[routes[j][0]]['x']
#    y = G.nodes[routes[j][0]]['y']
#    orig_points.append((y, x))
#
#dest_points = []
#for j in range(0,len(routes)):
#    x= G.nodes[routes[j][-1]]['x']
#    y = G.nodes[routes[j][-1]]['y']
#    dest_points.append((y, x))
#
#orig_nodes = []
#for orig_point in orig_points:
#    orig_nodes.append(ox.get_nearest_node(G, orig_point))
#    
#dest_nodes = []
#for dest_point in dest_points:
#    dest_nodes.append(ox.get_nearest_node(G, dest_point))

#%%

route_coorindates = []

for i in routes:
    points = []
    for j in i:
        x = G.nodes[j]['x']
        y = G.nodes[j]['y']
        points.append([x, y])
    route_coorindates.append(points)
    
n_routes = len(route_coorindates)
max_route_len = max([len(x) for x in route_coorindates])
#%%


fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.patch.set_facecolor('black')

scatter_list = []
for j in range(n_routes):
    scatter_list.append(ax.scatter(route_coorindates[j][0][0],
                                   route_coorindates[j][0][1],
                                   s=10, c='blue', marker = '.' ))
scatter_list1 = []
for j in range(n_routes):
    scatter_list1.append(ax.scatter(route_coorindates[j][0][0],
                                   route_coorindates[j][0][1],
                                   s=10, c='blue', marker = '.', alpha=0.7 ))

scatter_list2 = []
for j in range(n_routes):
    scatter_list2.append(ax.scatter(route_coorindates[j][0][0],
                                   route_coorindates[j][0][1],
                                   s=10, c='blue', marker = '.', alpha=0.4))

scatter_list3 = []
for j in range(n_routes):
    scatter_list3.append(ax.scatter(route_coorindates[j][0][0],
                                   route_coorindates[j][0][1],
                                   s=10, c='blue', marker = '.', alpha=0.2))


#%%

def animate(i):
    for j in range(n_routes):
        # Some routes are shorter than others
        # Therefore we need to use try except with continue construction
        try:
            # Try to plot a scatter plot
            x_j = route_coorindates[j][i][0]
            y_j = route_coorindates[j][i][1]
            x_j1 = route_coorindates[j][i-1][0]
            y_j1 = route_coorindates[j][i-1][1] 
            x_j2 = route_coorindates[j][i-2][0]
            y_j2 = route_coorindates[j][i-2][1] 
            x_j3 = route_coorindates[j][i-3][0]
            y_j3 = route_coorindates[j][i-3][1] 
            scatter_list[j].set_offsets(np.c_[x_j, y_j])
            scatter_list1[j].set_offsets(np.c_[x_j1, y_j1])
            scatter_list2[j].set_offsets(np.c_[x_j2, y_j2])
            scatter_list3[j].set_offsets(np.c_[x_j3, y_j3])
        except:
            # If i became > len(current_route) then continue to the next route
            continue

ani = FuncAnimation(fig, animate, frames=max_route_len)

ani.save('animation.mp4', dpi=300)
# %%
