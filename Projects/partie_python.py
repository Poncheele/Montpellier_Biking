Pour pouvoir utiliser osmnx il faut télécharger son package.
Pour cela il faut executer la commande:
        conda install -c conda-forge shapely #sinon la commande d'apres ne marche pas
        pip install pyproj #idem
        python -m pip install osmnx

#%%
import osmnx as ox
#ox.plot_graph(ox.graph_from_place('Modena, Italy'))

# %%
