#%%
import json
import pandas as pd


#%%
with open('caca.json') as json_file:  # open a json file as a DF
    data = pd.read_json(json_file,lines=True)
data
# %%
import requests
import json
data = json.loads(requests.get('https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json'))
# %%
import pandas as pd
import json
import urllib.request

import urllib, json
from urllib.request import urlopen
url = 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json'
import urllib2
import json
req = urllib2.Request(url)
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
#%%
with open('C2.json', 'w') as outfile:
    json.dump(data, outfile)

with open('C2.json') as json_file:  # open a json file as a DF
    data = pd.read_json(json_file,lines=True) 
data
#df = pd.read_json(data)
#%%
# save it as a json file

with open('oui.json', 'w') as outfile:
    json.dump(data, outfile)
#%%
with open('caca.json') as json_file:  # open a json file as a DF
    df = json.loads(json_file.read(),lines=True) 

df = pd.read_json(data,lines=True)
# %%

import wget
url = 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json'
#fs = wget.download(url,'caca.json')
 
df = pd.read_json(open('caca.json'),lines=True,nrows=1) # open a json file as a DF
df
# %%
# %%
