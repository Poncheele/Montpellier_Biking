#%%
import pytest
import montpellier_biking as mb
from montpellier_biking import counters
#%%

def test_counter_matrix():
    for c in counters.counter_list:
        nbrebike=0
        test = counters.Counter.set_matrix(c).toarray()
        for i in range(2880):
            nbrebike = nbrebike + list(test[i,:]).count(c.node)
        assert(nbrebike <= c.bikes*1.05 and  nbrebike >= c.bikes*0.95)

#%%
print(type(counters.Counter.node(counter_list(Vieille_poste))))


# %%
