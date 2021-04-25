from montpellier_biking.model import G
import numpy as np
import networkx as nx
from scipy import sparse
import time


class Counter():
    """An eco-counter of Montpellier

    ecrire un texte

    :param coordinates: Point # the real coordinate
    :type coordinates: type tuple
    :param node: graph node, the nearest node from the counter
    :type node: type numpy.int64
    :param bikes: number of bike passing
    :type bikes: type int
    :param name: counter's name
    :type name: type string
    :param out: True if the counter is out of Montpellier city
    :type out: type boolean
    """
    bike_distribution = [0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.5,
                         5, 9, 7, 7, 6, 6, 6, 6, 6, 9, 9, 8, 5, 4, 3, 2, 1]

    def __init__(self, coordinates, node, name, bikes=0, out=False):
        """construction method

        """
        self.coordinates = coordinates
        self.node = node
        self.bikes = bikes
        self.name = name
        self.out = out

    def x_node(self):
        """Gives a x coordinate on the graph.

        text?

        :return: the x coordinate on the graph.
        :rtype: float

        :Example:

        >>> import montpellier_biking as mb
        >>> mb.counters.Lattes.x_node()
        3.904615

        """
        return G.nodes[self.node]['x']

    def y_node(self):
        """Gives a y coordinate on the graph.

        :return: the y coordinate on the graph.
        :rtype: float

        :Example:

        >>> import montpellier_biking as mb
        >>> mb.counters.Lattes.y_node()
        43.5915408

        """
        return G.nodes[self.node]['y']

    def x_list(counter_list):
        """Give a list of x coordinates of a counter list

        :param counter_list: list of Counter
        :return: list of x node coordinate
        :rtype: list

        :Example:

        >>> import montpellier_biking as mb
        >>> mb.counters.Counter.x_list([mb.counters.Celleneuve,
                                        mb.counters.Lattes,
                                        mb.counters.Vieille_poste])
        [3.8344038, 3.904615, 3.9095831]

        """
        x_list = []
        for counter in counter_list:
            x_list.append(counter.x_node())
        return x_list

    def y_list(counter_list):
        """Give a list of y coordinates of a counter list

        :param counter_list: list of Counter
        :return: list of y node coordinate
        :rtype: list

        :Example:

        >>> import montpellier_biking as mb
        >>> mb.counters.Counter.y_list([mb.counters.Celleneuve,
                                        mb.counters.Lattes,
                                        mb.counters.Vieille_poste])
        [43.6146128, 43.5915408, 43.6155189]

        """
        y_list = []
        for counter in counter_list:
            y_list.append(counter.y_node())
        return y_list

    def generate_random_route(self):
        """Generate a random route that goes through the counter

        :return: list of nodes and lengh of route
        :rtype: tuple

        :Example:

        >>> import montpellier_biking as mb
        >>> mb.counters.Celleneuve.generate_random_route()
        ([280711163,
          280935801,
          280935470,
          287874356,
          ...
          279924936,
          1433327041,
          2994872551],
         60)

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
        """Transform a list of node into a list of (x,y) plot coordinates

        :param route: a list of node
        :return: list of plot coordinates
        :rtype: list

        :Example:

        >>> import montpellier_biking as mb
        >>> mb.counters.Counter.route_to_scatter([280711163, 280935801,
                                                  280935470, 287874356])
        [[3.8121647, 43.6352595],
         [3.8106809, 43.635287],
         [3.8093811, 43.6359382],
         [3.8095079, 43.6395812]]

        """
        if len(route) != 0:
            scatter_list = []
            for j in range(len(route)):
                scatter = [G.nodes[route[j]]['x'], G.nodes[route[j]]['y']]
                scatter_list.append(scatter)
            return scatter_list

    def set_matrix(self, quality=2880):
        """set passing bike matrix for one day

        :return: each raw is a frame, each colum is a route.
        :rtype: scipy.sparse.csr.csr_matrix

        :Example:

        >>> import montpellier_biking as mb
        >>> mb.counters.Vieille_poste.set_matrix()
        (1, 0)	      286656311.0
        (2, 0)	      282458029.0
        (3, 0)	      286656296.0
        ...
        (2878, 721)   3667338829.0
        (2878, 2280)  3667338829.0
        (2878, 2291)  3667338829.0

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
        """Set the simulation for each counter

        :param: list of counter
        :return anim_list: list of node list,
        all nodes who need to be plotted at time i
        :return count_list: list of list that contain the number of bike,
        passed at the time i
        :rtype: list

        :Example:

        >>> import montpellier_biking as mb
        >>> mb.counters.Counter.list_for_ani(mb.counters.counter_list)
        array([1.48140357e+09, 2.57227978e+09, 6.33348707e+09, 2.83308307e+08,
                2.05966087e+09, 1.93483920e+09, 2.95351676e+08, 2.46625431e+08,
                2.46623648e+08, 5.21426316e+08, 2.44208890e+08, 2.12274145e+0
                ...
              ]
        array([...])
        ...

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
