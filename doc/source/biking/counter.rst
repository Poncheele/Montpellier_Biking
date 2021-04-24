The class methods (to play with data)
======================================

.. autoclass:: montpellier_biking.model.counters.Counter
   :members:

In addition
============

Throughout the project, we need counters which are defined as follows:  

**Example:**

::

      Albert1er = Counter(coordinates=(43.61620945549243,
                          3.874408006668091),
                          node=ox.distance.get_nearest_node(G,
                          (43.61620945549243, 3.874408006668091)),
                          bikes=1569, name="Albert1er")


We have the coordinates, nodes, number of bicycles passed at this counter,
the name of counter, and to finish with is the counter is in Montpellier or not.

The list of all counters are:

::

      counter_list = [Albert1er, Beracasa, Celleneuve, Delmas, Gerhardt, Lattes, 
                      Laverune, Vieille_poste]
