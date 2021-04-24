#%%
import pytest
import osmnx as ox
import montpellier_biking as mb
from montpellier_biking import counters
from montpellier_biking import animation

#%%

anim = animation.Animation()
def test_counter_matrix():
    for c in anim.list_counter():
        nbrebike=0
        test = counters.Counter.set_matrix(c).toarray()
        for i in range(2880):
            nbrebike = nbrebike + list(test[i,:]).count(c.node)
        print(nbrebike)
        assert(nbrebike <= c.bikes*1.05 and nbrebike >= c.bikes*0.95)

#%%
test_counter_matrix()

