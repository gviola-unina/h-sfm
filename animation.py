import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

with open('X.npy', 'rb') as f:
    X = np.load(f)

mask = [item for sublist in [[i * 6 +1, i * 6 ] for i in range(int(X.shape[1] / 6))] for item in sublist]

coord = np.zeros((2,int(X.shape[1]/6),X.shape[0]))

m = X[:,mask]

for t in range(X.shape[0]):
    for n in range(int(X.shape[1]/6)):
        coord[:,n,t] = m[t,[n,n+1]]


groupi = np.zeros(int(X.shape[1] / 6))
radii = np.ones(int(X.shape[1] / 6))*0.39



fig, ax = plt.subplots(1, 1, figsize=(35, 5))

scatter = ax.scatter(coord[0, :, 0], coord[1, :, 0], c='b', s=0.81)
agents, = ax.plot([],[], 'bo', ms=6)
plt.xlim(-25, 25.0)

plt.ylim(-25, 25.0)
def init():

    return scatter

def animation_func(i):
    scatter.set_offsets(np.transpose(coord[:, :, i]))
    # Set sizes...
    scatter.set_sizes(radii*100)
    # Set colors..
    scatter.set_array(groupi)




animation = FuncAnimation(fig, animation_func, init_func=init, frames=500, interval = 100)
plt.show()

