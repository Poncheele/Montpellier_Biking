#%%
import matplotlib.pyplot as plt
import matplotlib.animation as ma
import osmnx as ox
import montpellier_biking as mb
import numpy as np
import time
import datetime


start_time = time.time()
megal = mb.counters.Counter.list_for_ani(mb.counters.counter_list)
print(time.time() - start_time)
mega = megal[1500:]

start_time = time.time()
fig, ax = ox.plot_graph(mb.counters.G, node_size=0, show=False)
# fig.set_size_inches(15, 15)
pic = ax.scatter(mb.counters.Counter.x_node(mb.counters.Albert1er),
                 mb.counters.Counter.y_node(mb.counters.Albert1er), s=10,
                 c='b', alpha=1, edgecolor='none', zorder=4)
count_list = [0, 0, 0, 0, 0, 0, 0, 0]
count_str_list = ["Albert1er:     ",
                  "Beracasa:     ",
                  "Celleneuve:  ",
                  "Delmas:        ",
                  "Gerhardt:      ",
                  "Lattes:          ",
                  "Laverune:     ",
                  "Vielle_poste: "]
text_list = []
hour = ax.text(3.8075, 43.57, "00:00:00", c='w')
for i in range(len(count_list)):
    text_list.append(ax.text(3.903, 43.57+0.0025*i,
                     count_str_list[i]+str(0), c='w'))


def animate(i):
    pic.set_offsets(mb.counters.Counter.route_to_scatter(mega[i]))
    hour.set_text(str(datetime.timedelta(seconds=i*30)))
    for j in range(len(text_list)):
        count_list[j] += np.count_nonzero(mega[i]
                                          == mb.counters.counter_list[j].node)
        text_list[j].set_text(count_str_list[j]+str(count_list[j]))
    return pic, hour


ani = ma.FuncAnimation(fig, animate, frames=100,
                       interval=100, blit=False, repeat=True)


plt.show()

# f = r"testtamere.avi"
# writervideo = animation.FFMpegWriter(fps=1)
# ani.save(f, writer=writervideo)
# %%
