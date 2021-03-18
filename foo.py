#%%
import json
import pandas as pd


#%%
with open('caca.json') as json_file:  # open a json file as a DF
    data = pd.read_json(json_file, lines=True)
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
import requests
import json

#%%
with open('C2.json', 'w') as outfile:
    json.dump(data, outfile)
#%%
with open('C2.json') as json_file:  # open a json file as a DF
    data = pd.read_json(json_file, lines=True) 
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
print(os.path.isfile('caca.json'))
df = pd.read_json(open('caca.json'),lines=True) # open a json file as a DF
df
# %%
import wget
url = 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042632_archive.json'
file=('caca.json')
def dowload_json(file):
    if os.path.isfile(file):
        os.remove(file)
    fs = wget.download(url,'caca.json')

dowload_json(file)
#%%
def fixjson(txt):
    file = open(txt, "r")
    newfile = open("caca.json",'x')
    for line in file:
        newfile.write(line.replace('}{','}\n{'))
    os.remove(txt)
fixshit('caca.json')

# %%
df = pd.read_json(open('caca2.json'),lines=True) # open a json file as a DF
df

# %%
import wget
import os
url_db = url_db = ['https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json', 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042632_archive.json', 
'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042633_archive.json', 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042634_archive.json', 
'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042635_archive.json', 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063161_archive.json', 
'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063162_archive.json', 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_XTH19101158_archive.json', 
'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063163_archive.json', 'https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063164_archive.json']


name = ['Beracasa.json', 'Laverune.json','Celleneuve.json','Lattes 2.json','Lattes 1.json','Vieille-Poste.json','Gerhardt.json','Albert 1er.json','Delmas 1.json','Delmas 2.json']
i=0
for url in url_db:
    path_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Montpellier_Network/Network_Module", "data", name[i])
    if os.path.isfile(path_target):
        os.remove(path_target)    
    fs = wget.download(url, path_target)
    i += 1
# %%

for i in range(len(url_db)):
    print(url_db[i])
    fs = wget.download(url_db[i])
# %%
