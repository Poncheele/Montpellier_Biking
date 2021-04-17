from Network_Module.model import G
import osmnx as ox
import networkx as nx
import random
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
        Counter :
        Counter : a Montpellier_Biking Counter

        Returns
        -------
        Path : list of nodes
        """
        start = np.random.choice(G.nodes)
        end = np.random.choice(G.nodes)
        route = nx.shortest_path(G, start, self)
        if self.out == False:
            route = route.append(nx.shortest_path(G, self, end))
        return route


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

counter_list = [Albert1er, Beracasa, Celleneuve, Delmas, Gerhardt,# Lattes,
                Laverune, Vielle_poste]
