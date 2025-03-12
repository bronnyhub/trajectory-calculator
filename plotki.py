import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from skyfield.api import load
import datetime as dt

#satellite data
ts = load.timescale()
satellites = load.tle_file("satelity.txt")
satellite = satellites[0]  #!!!zmienić na to, aby można było wybrać satelitę z listy

#time range
now = dt.datetime.utcnow()
time_steps = ts.utc(now.year, now.month, now.day, np.linspace(0, 24, 144))
positions = satellite.at(time_steps).position.km 

#coordinates
x = positions[0]
y = positions[1]
z = positions[2]

#satellite trajectory
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=30, azim=220)

#Earth !!! zmienić, aby można było wybrać planetę z układu słonecznego
earth_radius = 6371
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 30)
earth_x = earth_radius * np.outer(np.cos(u), np.sin(v))
earth_y = earth_radius * np.outer(np.sin(u), np.sin(v))
earth_z = earth_radius * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(earth_x, earth_y, earth_z, alpha=0.5, zorder=1)
ax.set_aspect('equal')
ax.view_init(elev=20, azim=130)

#satellite path
ax.plot(x, y, z, label="Satellite Trajectory", color="orange", zorder=2, linewidth=2)
#current position
ax.scatter(x[0], y[0], z[0], color="red", label="Current Position", s=50, zorder=3)

#legend
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.set_title(f"Satellite Trajectory (UTC: {dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')})")
ax.legend()
plt.show()
