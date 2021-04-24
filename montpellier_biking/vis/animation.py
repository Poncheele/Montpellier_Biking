import matplotlib.pyplot as plt
import matplotlib.animation as ma
import osmnx as ox
import montpellier_biking as mb
import numpy as np
import time
import datetime

G = mb.counters.G

class Animation():

    def __init__(self, bike_list=[1523, 1701, 694, 745, 1065, 455, 426, 292]):
        self.bikes = bike_list
        self.Albert1er = mb.counters.Counter(coordinates=(43.61620945549243,
                    3.874408006668091),
                    node=ox.distance.get_nearest_node(G,
                    (43.61620945549243, 3.874408006668091)),
                    bikes=self.bikes[0], name="Albert1er")

        self.Beracasa = mb.counters.Counter(coordinates=(43.60969924926758, 3.896939992904663),
                           node=ox.distance.get_nearest_node(G,
                           (43.60969924926758, 3.896939992904663)),
                           bikes=self.bikes[1], name="Beracasa")
        self.Celleneuve = mb.counters.Counter(coordinates=(43.61465, 3.8336),
                             node=ox.distance.get_nearest_node(G,
                             (43.61465, 3.8336)), bikes=self.bikes[2],
                             name="Celleneuve")
        self.Delmas = mb.counters.Counter(coordinates=(43.6266977, 3.8956288),
                         node=ox.distance.get_nearest_node(G,
                         (43.6266977, 3.8956288)),
                         bikes=self.bikes[3], name="Delmas", out=True)
        self.Gerhardt = mb.counters.Counter(coordinates=(43.6138841, 3.8684671),
                           node=ox.distance.get_nearest_node(G,
                           (43.6138841, 3.8684671)),
                           bikes=self.bikes[4], name="Gerhardt")
        self.Lattes = mb.counters.Counter(coordinates=(43.5915, 3.90473),
                         node=ox.distance.get_nearest_node(G,
                         (43.5915, 3.90473)),
                         bikes=self.bikes[5], name="Lattes", out=True)
        self.Laverune = mb.counters.Counter(coordinates=(43.5907, 3.81324),
                           node=ox.distance.get_nearest_node(G,
                           (43.5907, 3.81324)),
                           bikes=self.bikes[6], name="Laverune", out=True)
        self.Vieille_poste = mb.counters.Counter(coordinates=(43.6157418, 3.9096322),
                                node=ox.distance.get_nearest_node(G,
                                (43.6157418, 3.9096322)),
                                bikes=self.bikes[7], name="Vielle_poste", out=True)

        self.Counter_list = [self.Albert1er, self.Beracasa, self.Celleneuve,
                             self.Delmas, self.Gerhardt, self.Lattes,
                             self.Laverune, self.Vieille_poste]
        t = time.time()
        self.set_anim()
        print('time to set anim', time.time()-t)
        self.launch_anim()

    def set_anim(self):
        self.anim_list = mb.counters.Counter.list_for_ani(
                                  self.Counter_list)
        self.anim_list = self.anim_list[1500:]

    def animate(self,i):
        self.pic.set_offsets(mb.counters.Counter.route_to_scatter(self.anim_list[i]))
        self.hour.set_text(str(datetime.timedelta(seconds=i*30)))
        for j in range(len(self.text_list)):
            self.count_list[j] += np.count_nonzero(self.anim_list[i]
                                              == self.Counter_list[j].node)
            self.text_list[j].set_text(self.count_str_list[j]+str(self.count_list[j]))
        return self.pic, self.hour

    
    def launch_anim(self):
        start_time = time.time()
        self.fig, self.ax = ox.plot_graph(G, node_size=0, show=False)
        # fig.set_size_inches(15, 15)
        self.pic = self.ax.scatter(mb.counters.Counter.x_node(self.Albert1er),
                         mb.counters.Counter.y_node(self.Albert1er), s=10,
                         c='b', alpha=1, edgecolor='none', zorder=4)
        self.count_list = [0, 0, 0, 0, 0, 0, 0, 0]
        self.count_str_list = ["Albert1er:     ",
                          "Beracasa:     ",
                          "Celleneuve:  ",
                          "Delmas:        ",
                          "Gerhardt:      ",
                          "Lattes:          ",
                          "Laverune:     ",
                          "Vieille_poste: "]
        self.text_list = []
        self.hour = self.ax.text(3.8075, 43.57, "00:00:00", c='w')
        for i in range(len(self.count_list)):
            self.text_list.append(self.ax.text(3.903, 43.57+0.0025*i,
                             self.count_str_list[i]+str(0), c='w'))
        ani = ma.FuncAnimation(self.fig, self.animate, frames=100,
                               interval=100, blit=False, repeat=True)
        plt.show()
        print(time.time()-start_time)
    
    # f = r"testtamere.avi"
    # writervideo = animation.FFMpegWriter(fps=1)
    # ani.save(f, writer=writervideo)


if __name__ == "__main__":
    app = Animation()
