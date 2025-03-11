import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import datetime as dt
import math as m

from skyfield.api import load

ts = load.timescale()
satellites = load.tle_file("satelity.txt")
satellite = satellites[0]  # Pick the first satellite

orb = satellite.at(ts.now())  # Compute the satellite’s position
plt.style.use('_mpl-gallery')

#file with satellites data - skróć ten link
ADDR = "satelity.txt"
TLE = open(ADDR,"r").readlines()

#constants for Earth = change for other planets!!!
mu = 398600.4418
r = 6781
D = 24*0.997269

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

# Plot trajectory
def plot_tle(data):
    fig = plt.figure()
    ax = plt.axes(projection='3d', computed_zorder=False)

    # Initialize `orb` to avoid UnboundLocalError
    orb = {"t": dt.datetime.now()}  # Default time if no valid TLE data is found

    for i in range(len(data)//2):
        if data[i*2][0] != "1":
            print("Wrong TLE format at line "+str(i*2)+". Lines ignored.")
            continue
        if int(data[i*2][18:20]) > int(dt.date.today().year%100):
            orb = {"t": dt.datetime.strptime("19"+data[i*2][18:20]+" "+data[i*2][20:23]+" "+
                                             str(int(24*float(data[i*2][23:33])//1))+" "+
                                             str(int(((24*float(data[i*2][23:33])%1)*60)//1))+" "+
                                             str(int((((24*float(data[i*2][23:33])%1)*60)%1)//1)), "%Y %j %H %M %S")}
        else:
            orb = {"t": dt.datetime.strptime("20"+data[i*2][18:20]+" "+data[i*2][20:23]+" "+
                                             str(int(24*float(data[i*2][23:33])//1))+" "+
                                             str(int(((24*float(data[i*2][23:33])%1)*60)//1))+" "+
                                             str(int((((24*float(data[i*2][23:33])%1)*60)%1)//1)), "%Y %j %H %M %S")}
        orb.update({"name": data[i*2+1][2:7], "e": float("."+data[i*2+1][26:34]),
                    "a": (mu/((2*m.pi*float(data[i*2+1][52:63])/(D*3600))**2))**(1./3),
                    "i": float(data[i*2+1][9:17])*m.pi/180,
                    "RAAN": float(data[i*2+1][17:26])*m.pi/180,
                    "omega": float(data[i*2+1][34:43])*m.pi/180})

    plt.title("Orbits plotted in the ECE frame as of " + orb["t"].strftime("%m %Y"))
    plt.show()

#file with satellites data  
ADDR = "satelity.txt"
TLE = open(ADDR,"r").readlines()
plot_tle(TLE), orb