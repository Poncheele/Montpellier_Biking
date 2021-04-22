# import matplotlib.pyplot as plt
import matplotlib.animation as ma
import osmnx as ox
import Montpellier_Biking as nm
import time

start_time = time.time()

G = nm.model.G
print(time.time() - start_time)

anim_list = nm.counters.Counter.list_for_ani(nm.counters.counter_list)
fig, ax = ox.plot_graph(G, node_size=0, show=False)
fig.set_size_inches(20, 20)
pic = ax.scatter(nm.counters.Counter.x_node(nm.counters.Albert1er),
                 nm.counters.Counter.y_node(nm.counters.Albert1er), s=10,
                 c='b', alpha=1, edgecolor='none', zorder=4)


def animate(i):
    pic.set_offsets(nm.counters.Counter.route_to_scatter(anim_list[i]))
    return pic


ani = ma.FuncAnimation(fig, animate, frames=2880,
                       interval=100, blit=False, repeat=False)


# plt.show()
f = r"animation.avi"
writervideo = ma.FFMpegWriter(fps=20)
ani.save(f, writer=writervideo)
