import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure(figsize=(7,7))
ax = plt.axes(xlim=(0,20),ylim=(0,20))

scatter = ax.scatter((0,0))

def update(frame_number):
    for i in range(10):
        scatter.set_offsets((i,i*2))
    return scatter

anim = FuncAnimation(fig, update,frames=10 interval=10)
plt.show()