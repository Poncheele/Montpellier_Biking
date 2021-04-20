from Montpellier_Biking.model import G
import osmnx as ox
import networkx as nx
import numpy as np


class Counter():

    def __init__(self, coordinates, node, name, bikes=0, out=False):
        """
        An eco-counter of Montpellier

        Parameters
        ----------
        coordinates : Point # the real coordinate
        node : graph node, the nearest node from the counter
        bikes : int, number of bike passing
        name : string, counter's name
        out : bool, True if the counter is out of Montpellier city
        """
        self.coordinates = coordinates
        self.node = node
        self.bikes = bikes
        self.name = name
        self.out = out

    def x_node(self):
        """
        returns the x coordinate on the graph
        """
        return G.nodes[self.node]['x']

    def y_node(self):
        """
        returns the y coordinate on the graph
        """
        return G.nodes[self.node]['y']

    @staticmethod
    def x_list(counter_list):
        """
        Returns a list of x coordinates of a counter list

        Parameters
        ----------
        counter_list : list of Counter

        Return
        ------
        x_list : list of x node coordinate
        """
        x_list = []
        for counter in counter_list:
            x_list.append(counter.x_node())
        return x_list

    def y_list(counter_list):
        """
        Returns a list of y coordinates of a counter list

        Parameters
        ----------
        counter_list : list of Counter

        Return
        ------
        y_list : list of y node coordinate
        """
        y_list = []
        for counter in counter_list:
            y_list.append(counter.y_node())
        return y_list

    def generate_random_route(self):
        """
        Generate a random route that goes through the counter
        Parameters
        ----------
        Counter : a Montpellier_Biking Counter
        Returns
        -------
        Path : list of nodes
        """
        path = False
        start = np.random.choice(G.nodes)
        while path is False:
            try:
                route = nx.shortest_path(G, start, self.node)
                path = True
            except Exception:
                start = np.random.choice(G.nodes)
        if self.out is False:
            end = np.random.choice(G.nodes)
            while path is False:
                try:
                    route.append(nx.shortest_path(G, end, self.node))
                    path = True
                except Exception:
                    end = np.random.choice(G.nodes)
        return route

    def route_to_scatter(route):
        scatter_list = []
        for j in range(len(route)):
            scatter = [G.nodes[route[j]]['x'], G.nodes[route[j]]['y']]
            scatter_list.append(scatter)
        return scatter_list


# Number of bike the 04-15

Albert1er = Counter(coordinates=(43.61620945549243,
                    3.874408006668091),
                    node=ox.distance.get_nearest_node(G,
                    (43.61620945549243, 3.874408006668091)),
                    bikes=1569, name="Albert1er")

Beracasa = Counter(coordinates=(43.60969924926758, 3.896939992904663),
                   node=ox.distance.get_nearest_node(G,
                   (43.60969924926758, 3.896939992904663)),
                   bikes=1376, name="Beracasa")
Celleneuve = Counter(coordinates=(43.61465, 3.8336),
                     node=ox.distance.get_nearest_node(G,
                     (43.61465, 3.8336)), bikes=638,
                     name="Celleneuve")
Delmas = Counter(coordinates=(43.6266977, 3.8956288),
                 node=ox.distance.get_nearest_node(G,
                 (43.6266977, 3.8956288)),
                 bikes=725, name="Delmas", out=True)
Gerhardt = Counter(coordinates=(43.6138841, 3.8684671),
                   node=ox.distance.get_nearest_node(G,
                   (43.6138841, 3.8684671)),
                   bikes=1109, name="Gerhardt")
Lattes = Counter(coordinates=(43.5728796, 3.9460064),
                 node=ox.distance.get_nearest_node(G,
                 (43.5728796, 3.9460064)),
                 bikes=648, name="Lattes", out=True)
Laverune = Counter(coordinates=(43.5907, 3.81324),
                   node=ox.distance.get_nearest_node(G,
                   (43.5907, 3.81324)),
                   bikes=302, name="Laverune", out=True)
Vielle_poste = Counter(coordinates=(43.6157418, 3.9096322),
                       node=ox.distance.get_nearest_node(G,
                       (43.6157418, 3.9096322)),
                       bikes=283, name="Vielle_poste", out=True)

counter_list = [Albert1er, Beracasa, Celleneuve, Delmas, Gerhardt,  # Lattes,
                Laverune, Vielle_poste]

bike_distribution = [0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.5,
                     5, 9, 7, 7, 6, 6, 6, 6, 6, 9, 9, 8, 5, 4, 3, 2, 1]

M1 = np.zeros((2000, 2000))


for i in range(Albert1er.bikes):
    route = Counter.generate_random_route(Albert1er)
    M1[i:i+len(route), i] = route

############### VIS_TEST #################

fig, ax = ox.plot_graph(G, node_size=0, show=False)
pic = ax.scatter(Counter.x_node(Albert1er), Counter.y_node(Albert1er), s=20,
                 c='y', alpha=1, edgecolor='none', zorder=4)


def animate(i):
    pic.set_offsets(Counter.route_to_scatter(M1[i, :][M1[i, :] > 0]))
    return pic


ani = FuncAnimation(fig, animate, frames=Albert1er.bikes,
                    interval=10, blit=False)

plt.show()

