
import Network_Module as nm
import osmnx as ox
import matplotlib.pyplot as plt
import numpy as np
from Network_Module.counters import Counter
# from matplotlib import animation
# from matplotlib import rc


G = nm.model.G

counters = nm.model.counters.counter_list



listx = nm.counters.Counter.x_list(counters)
listy = nm.counters.Counter.y_list(counters)
pic = ax.scatter(listx,listyx , s=20,
                 c='y', alpha=1, edgecolor='none', zorder=4)

plt.show()

route_list = []

for i in range(len(counters)):
    if i !=5:
        route_list.append(generate_random_route(counters[i]))
    
fig, ax = ox.plot_graph(G, node_size=0, show=False)
pic = ax.scatter(listx,listy , s=20,
                 c='y', alpha=1, edgecolor='none', zorder=4)
def animate(i):
    lx = []
    ly = []
    for j in range(len(route_list)):
        lx.append(G.nodes[route_list[j][i]]['x'])
        ly.append(G.nodes[route_list[j][i]]['y'])
    pic.set_offsets((lx,ly))
    return pic

ani = FuncAnimation(fig, animate, frames=100, interval=100)

plt.show()

def generate_random_route(self):
    """
    Generate a random route that goes through the counter
    Parameters
    ----------
    Counter :
    Counter : a Montpellier_Biking Counter
    Returns
    -------
    Path : list of nodes
    """
    start = np.random.choice(G.nodes)
    end = np.random.choice(G.nodes)
    route = nx.shortest_path(G, start, self.node)
    if self.out == False:
            route.extend(nx.shortest_path(G, self.node, end)[1:])
    return route

generate_random_route(counters[5])

