import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

from orbitplot import Plotter
fig, ax = plt.subplots(1, figsize=(25, 25))


# a = np.linspace(7000,150000, 10000)

orbits = {'orbit_1': {
    'semi_major_axis': 2000, 'eccentricity': 0.1,
    'orbit_color': 'orange',
    # 'start_angle':0, 'end_angle': 2, 'orbit_resolution':1000
    },
}
orbit_values = Plotter(ax, 'Earth', **orbits)

plt.style.use('seaborn-pastel')

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.seet_ddata([], [])
    return line


def animate(i):
    x, y = Plotter.get_orbit_plot_points('orbit_0')
    print(x,y)

animate(1)


# orbit_plt, orbit_ax = orbit_values.plot_orbit()
# orbit_plt.show()
