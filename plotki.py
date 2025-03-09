### https://matplotlib.org/

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('_mpl-gallery')

# trajectory
n = 1000
xs = np.linspace(0, 1, n)
ys = np.sin(xs * 10 * np.pi)
zs = np.cos(xs * 10 * np.pi)

# place the planet
center_x=0
center_y=0
center_z=0.5
planet_radius=0.3

# planet
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 30)
sphere_x = center_x + planet_radius * np.outer(np.cos(u), np.sin(v))
sphere_y = center_y + planet_radius * np.outer(np.sin(u), np.sin(v))    
sphere_z = center_z + planet_radius * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"projection": "3d"})
ax.plot(zs, ys, xs, label="Trajectory")
ax.plot_surface(sphere_x, sphere_y, sphere_z, color="orange", label="Planet")
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
ax.set_xlim([-0.7, 0.7])
ax.set_ylim([-0.7, 0.7])
ax.set_zlim([0, 1])

plt.legend()
plt.show()