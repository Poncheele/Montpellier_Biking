Pour pouvoir utiliser osmnx il faut télécharger son package.
Pour cela il faut executer les commandes suivantes dans le terminal anaconda prompt:
       conda config --prepend channels conda-forge
       conda create -n ox --strict-channel-priority osmnx
       conda activate ox


#%%
import osmnx as ox
ox.plot_graph(ox.graph_from_place('montpellier, France'))

# %%
