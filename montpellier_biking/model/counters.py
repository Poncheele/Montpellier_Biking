from Montpellier_Biking.model import G
import osmnx as ox
import numpy as np
import networkx as nx


class Counter():

    bike_distribution = [0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.5,
                         5, 9, 7, 7, 6, 6, 6, 6, 6, 9, 9, 8, 5, 4, 3, 2, 1]

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
        if len(route) > 120:
            route = route[len(route)-110:]
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

    def set_matrix(self):
        """
        set passing bike matrix for one day
        Parameters
        ----------
        Counter
        Returns
        -------
        numpy matrix: each raw is a frame, each colum is a route.
        """
        M1 = np.zeros((2880, 2880))
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
                    random_pass = np.random.randint(low=min(len(route)+120*23,
                                                    120*24-1), high=120*24)
                    M1[random_pass-len(route):random_pass, i+j*120] = route
                i += 1
        return M1

    def list_for_ani(c_list):
        """
        Set the simulation for each counter
        Parameters
        ----------
        list of counter
        Returns
        -------
        list of node list
        """
        anim_list = []
        # set list for the first counter
        M = Counter.set_matrix(c_list[0])
        for i in range(len(M)):
            anim_list.append(M[i, :][M[i, :] > 0])
        # extends lists with other counters
        for c in c_list[1:]:
            M = Counter.set_matrix(c)
            for i in range(len(M)):
                anim_list[i] = np.hstack((anim_list[i], M[i, :][M[i, :] > 0]))
        return anim_list


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
Lattes = Counter(coordinates=(43.5915, 3.90473),
                 node=ox.distance.get_nearest_node(G,
                 (43.5915, 3.90473)),
                 bikes=648, name="Lattes", out=True)
Laverune = Counter(coordinates=(43.5907, 3.81324),
                   node=ox.distance.get_nearest_node(G,
                   (43.5907, 3.81324)),
                   bikes=302, name="Laverune", out=True)
Vielle_poste = Counter(coordinates=(43.6157418, 3.9096322),
                       node=ox.distance.get_nearest_node(G,
                       (43.6157418, 3.9096322)),
                       bikes=283, name="Vielle_poste", out=True)

counter_list = [Albert1er, Beracasa, Celleneuve, Delmas, Gerhardt, Lattes,
                Laverune, Vielle_poste]