import osmnx as ox
import time

t = time.time()
G = ox.graph_from_place('Montpellier, France', 'bike')
print('time to load graph: ', time.time()-t)
