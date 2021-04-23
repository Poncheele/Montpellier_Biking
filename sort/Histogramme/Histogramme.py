## A Histogramme from the data
import pandas
import matplotlib.pyplot as plt

#Fisrt Histogramme
y1 = [1022,1139,1205,1126,982,1009,1077]
x1 = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

plt.hist(y1)
plt.title(" Compt_name daily average ")
#plt.savefig("compt_name dialy average")
plt.show()