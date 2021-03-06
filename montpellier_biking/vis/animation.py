# import matplotlib.pyplot as plt
import matplotlib.animation as ma
import osmnx as ox
import montpellier_biking as mb
from montpellier_biking.model.counters import Counter
import numpy as np
import time
import datetime

G = mb.counters.G


class Animation():
    """This class generate a video of the bike traffic in montpellier in a day.
    Need to use 'lauch_anim()' method.
    """
    def __init__(self, bike_list=[1523, 1701, 694, 745, 1065, 455, 426, 292],
                 date=str(datetime.date(2021, 4, 20))):
        """Parameters
           ----------
           bike_list: int list of numbers of bike passed at
           the counters in the day
        """
        self.date = date
        self.bikes = bike_list
        self.Albert1er = Counter(coordinates=(43.61620945549243,
                                              3.874408006668091),
                                 node=ox.distance.get_nearest_node(G,
                                 (43.61620945549243, 3.874408006668091)),
                                 bikes=self.bikes[0], name="Albert1er")

        self.Beracasa = Counter(coordinates=(43.60969924926758,
                                             3.896939992904663),
                                node=ox.distance.get_nearest_node(G,
                                (43.60969924926758, 3.896939992904663)),
                                bikes=self.bikes[1], name="Beracasa")
        self.Celleneuve = Counter(coordinates=(43.61465, 3.8336),
                                  node=ox.distance.get_nearest_node(G,
                                  (43.61465, 3.8336)), bikes=self.bikes[2],
                                  name="Celleneuve")
        self.Delmas = Counter(coordinates=(43.6266977, 3.8956288),
                              node=ox.distance.get_nearest_node(G,
                              (43.6266977, 3.8956288)),
                              bikes=self.bikes[3], name="Delmas", out=True)
        self.Gerhardt = Counter(coordinates=(43.6138841, 3.8684671),
                                node=ox.distance.get_nearest_node(G,
                                (43.6138841, 3.8684671)),
                                bikes=self.bikes[4], name="Gerhardt")
        self.Lattes = Counter(coordinates=(43.5915, 3.90473),
                              node=ox.distance.get_nearest_node(G,
                              (43.5915, 3.90473)),
                              bikes=self.bikes[5], name="Lattes", out=True)
        self.Laverune = Counter(coordinates=(43.5907, 3.81324),
                                node=ox.distance.get_nearest_node(G,
                                (43.5907, 3.81324)),
                                bikes=self.bikes[6], name="Laverune", out=True)
        self.Vieille_poste = Counter(coordinates=(43.6157418, 3.9096322),
                                     node=ox.distance.get_nearest_node(G,
                                     (43.6157418, 3.9096322)),
                                     bikes=self.bikes[7],
                                     name="Vielle_poste", out=True)

        self.counter_list = [self.Albert1er, self.Beracasa, self.Celleneuve,
                             self.Delmas, self.Gerhardt, self.Lattes,
                             self.Laverune, self.Vieille_poste]
        self.counter_list = self.counter_list

    def list_counter(self):
        """Returns the counter list (montpellier_biking's Countr)
        """
        return (self.counter_list)

    def set_anim(self):
        """Set Self.anim_list
        use Counter.list_for_ani from montpellier_biking.model.counters.Counter
        """
        self.anim_list = Counter.list_for_ani(
                                  self.counter_list)

    def animate(self, i):
        """Animation function,
        plot scatter points of each bike presents at the frame i.
        """
        self.pic.set_offsets(Counter.route_to_scatter(
                             self.anim_list[i]))
        self.hour.set_text(str(self.date)+" "+str(datetime.timedelta(
                                                  seconds=i*30)))
        for j in range(len(self.text_list)):
            self.count_list[j] += np.count_nonzero(
                                  self.anim_list[i]
                                  == self.counter_list[j].node)
            self.text_list[j].set_text(self.count_str_list[j]+str(
                                       self.count_list[j]))
        return self.pic, self.hour

    def launch_anim(self):
        """Generate animation and save it as a mp4 file. Can be long
        """
        self.set_anim()
        start_time = time.time()
        self.fig, self.ax = ox.plot_graph(G, node_size=0, show=False)
        self.pic = self.ax.scatter(Counter.x_node(self.Albert1er),
                                   Counter.y_node(self.Albert1er), s=10,
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
        self.hour = self.ax.text(3.8075, 43.57,
                                 str(self.date)+" 00:00:00", c='w')
        for i in range(len(self.count_list)):
            self.text_list.append(self.ax.text(3.903, 43.57+0.0025*i,
                                  self.count_str_list[i]+str(0), c='w'))
        ani = ma.FuncAnimation(self.fig, self.animate, frames=2880,
                               interval=100, blit=False, repeat=False)
        # plt.show()
        f = r""+str(self.date)+".avi"
        writervideo = ma.FFMpegWriter(fps=10)
        ani.save(f, writer=writervideo)
        print('time to make video: ', time.time()-start_time)


if __name__ == "__main__":
    app = Animation()
