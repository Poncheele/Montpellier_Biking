
import Montpellier_Biking as mb
import osmnx as ox
import matplotlib.pyplot as plt
import numpy as np
from Montpellier_Biking.model.counters import Counter
from matplotlib.animation import FuncAnimation
import networkx as nx
from scipy.sparse import coo_matrix
# from matplotlib import animation
# from matplotlib import rc


G = mb.model.G

counters = mb.model.counters.counter_list
listx = mb.counters.Counter.x_list(counters)
listy = mb.counters.Counter.y_list(counters)

fig, ax = ox.plot_graph(G, node_size=0, show=False)

pic = ax.scatter(listx, listy, s=20,
                 c='y', alpha=1, edgecolor='none', zorder=4)

plt.show()

route_list = []

for i in range(len(counters)):
    if i != 5:
        route_list.append(Counter.generate_random_route(counters[i]))
    

fig, ax = ox.plot_graph(G, node_size=0, show=False)
fig.set_size_inches(18.5, 10.5)
pic = ax.scatter(listx, listy , s=20,
                 c='y', alpha=1, edgecolor='none', zorder=4)




def animate(i):
    lx = []
    ly = []
    data = []
    route = Counter.generate_random_route(counters[0])
    for j in range(len(route_list)):
        l = [G.nodes[route_list[j][i]]['x'], G.nodes[route_list[j][i]]['y']]
        data.append(l)

    pic.set_offsets(data)
    return pic


ani = FuncAnimation(fig, animate, frames=200, interval=10, blit=False)

plt.show()



a = [0, 1, 0, 1, 0, 0, 0, 0]
nonzeroind = np.nonzero(a)[0] # the return is a little funny so I use the [0]
print(nonzeroind)


