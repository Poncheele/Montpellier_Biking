from montpellier_biking.model import G
import numpy as np
import networkx as nx
from scipy import sparse
import time


class Counter():
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
    bike_distribution = [0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.5,
                         5, 9, 7, 7, 6, 6, 6, 6, 6, 9, 9, 8, 5, 4, 3, 2, 1]

    def __init__(self, coordinates, node, name, bikes=0, out=False):
        """
        construction method
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
        # if len(route) > 120:
        #     route = route[len(route)-110:]
        lengh = len(route)
        if self.out is False:
            path = False
            end = np.random.choice(G.nodes)
            while path is False:
                try:
                    route.extend(nx.shortest_path(G,
                                 self.node, end)[1:])
                    path = True
                except Exception:
                    end = np.random.choice(G.nodes)
        return route, lengh

    def route_to_scatter(route):
        """
        Transform a list of node into a list of (x,y) plot coordinates
        Parameters
        ----------
        route: list of node
        Returns
        -------
        scatter list: list of plot coordinates
        """
        if len(route) != 0:
            scatter_list = []
            for j in range(len(route)):
                scatter = [G.nodes[route[j]]['x'], G.nodes[route[j]]['y']]
                scatter_list.append(scatter)
            return scatter_list

    def set_matrix(self, quality=2880):
        """
        Set passing bike matrix for one day
        Parameters
        ----------
        Counter
        Returns
        -------
        numpy matrix: each raw is a frame, each colum is a route.
        """
        M1 = np.zeros((quality, quality))
        for j in range(24):
            i = 0
            while i <= Counter.bike_distribution[j]*self.bikes/100:
                route, lengh = Counter.generate_random_route(self)
                try:  # random bike passing time
                    random_pass = np.random.randint(low=120*j+lengh,
                                                    high=120*(j+1))
                    M1[random_pass-(lengh):random_pass+len(route)-lengh,
                       i+j*120] = route
                except Exception:  # last hour can't exceed 2880
                    random_pass = np.random.randint(low=min(len(route)+120*j,
                                                    120*(j+1)-1),
                                                    high=120*(j+1))
                    M1[random_pass-len(route):random_pass, i+j*120] = route
                i += 1
        return sparse.csr_matrix(M1)

    def list_for_ani(c_list):
        """
        Set the simulation for each counter
        Parameters
        ----------
        list of counter
        Returns
        -------
        anim_list: list of node list,
        all nodes who need to be plotted at time i
        count_list: list of list that contain the number of bike,
        passed at the time i
        """
        anim_list = []
        # set list for the first counter
        M = Counter.set_matrix(c_list[0])
        for i in range(M.shape[0]):
            anim_list.append(M[i].data)
        # extends lists with other counters
        for c in c_list[1:]:
            t = time.time()
            M = Counter.set_matrix(c)
            for i in range(M.shape[0]):
                anim_list[i] = np.hstack((anim_list[i], M[i].data))
            print(time.time()-t)
        return anim_list




import osmnx as ox
Albert1er = Counter(coordinates=(43.61620945549243,
                    3.874408006668091),
                    node=ox.distance.get_nearest_node(G,
                    (43.61620945549243, 3.874408006668091)),
                    bikes=500, name="Albert1er")

Counter.generate_random_route(Albert1er)

t= time.time()
Counter.set_matrix(Albert1er)
print(time.time()-t)

help(nx.general_random_intersection_graph)