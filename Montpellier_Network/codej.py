Pour pouvoir utiliser osmnx il faut télécharger son package.
Pour cela il faut executer les commandes suivantes dans le terminal anaconda prompt:
       conda config --prepend channels conda-forge
       conda create -n ox --strict-channel-priority osmnx
       conda activate ox


#%%
import osmnx as ox

G = ox.graph_from_place('montpellier, France', network_type='bike')
#ox.plot_graph(G)
origin = ox.utils.geocode('Place Eugène Bataillon, Montpellier, France')
destination = ox.utils.geocode('Maison du Lez, Montpellier, France')

origin_node = ox.get_nearest_node(G, origin)
destination_node = ox.get_nearest_node(G, destination)

print(origin)
print(destination)
route = nx.shortest_path(G, origin_node, destination_node)
# %%
import Network_Module as nm

df=nm.Load_db.Load_db().save_as_df("Albert 1er")
df
# %%
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
G.add_edge('D', 'A', weight=2)

my_seed = 42
nx.draw_networkx(G, with_labels=True, 
                 pos=nx.spring_layout(G, seed=my_seed))
labels = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G, seed=my_seed), 
                            edge_labels=labels)


nx.draw_networkx_edges(G, pos=nx.spring_layout(G, seed=my_seed), 
                     wight=list(labels.value()))

plt.axis('off')
plt.show()

# %%
#matrice d'adjacence
A = nx.adjacency_matrix(G)
print(A.todense())