import arlpy.uwapm as pm
import numpy as np
import os 
import matplotlib.pyplot as plt

os.environ['PATH'] = os.environ['PATH'].replace(':/opt/build/at/bin', '')+":/opt/build/at/bin"

pm.models()

Title = "Example"

## Environment
##############

bathy = [
    [0, 20],    # 30 m water depth at the transmitter
    [300, 30],  # 20 m water depth 300 m away
    [1000, 15]  # 25 m water depth at 1 km
    
]

surface = np.array([[r, 0.75+0.75*np.sin(2*np.pi*0.05*r)] for r in np.linspace(0,1000,1001)])

ssp = [
    [ 0, 1532],  # 1540 m/s at the surface
    [10, 1525],  # 1530 m/s at 10 m depth
    [20, 1527],  # 1532 m/s at 20 m depth
    [25, 1526],  # 1533 m/s at 25 m depth
    [30, 1525]   # 1535 m/s at the seabed
]

beampattern = np.array([
    [-180,  10], [-170, -10], [-160,   0], [-150, -20], [-140, -10], [-130, -30],
    [-120, -20], [-110, -40], [-100, -30], [-90 , -50], [-80 , -30], [-70 , -40],
    [-60 , -20], [-50 , -30], [-40 , -10], [-30 , -20], [-20 ,   0], [-10 , -10],
    [  0 ,  10], [ 10 , -10], [ 20 ,   0], [ 30 , -20], [ 40 , -10], [ 50 , -30],
    [ 60 , -20], [ 70 , -40], [ 80 , -30], [ 90 , -50], [100 , -30], [110 , -40],
    [120 , -20], [130 , -30], [140 , -10], [150 , -20], [160 ,   0], [170 , -10],
    [180 ,  10]
])

env = pm.create_env2d(
    depth=bathy,
    soundspeed=ssp,
    bottom_soundspeed=1450,
    bottom_density=1200,
    bottom_absorption=1.0,
    tx_depth=15,
    rx_depth=10,
    tx_directionality=beampattern,
    surface=surface
)

pm.print_env(env)

## Run Bellhop
##############

rays     = pm.compute_rays(env)
eigrays  = pm.compute_eigenrays(env)
arrivals = pm.compute_arrivals(env)
ir       = pm.arrivals_to_impulse_response(arrivals, fs=96000)
pm.plot_rays(eigrays, env=env, Title=Title)

env['rx_range'] = np.linspace(0, 1000, 1001)
env['rx_depth'] = np.linspace(0, 30, 301)
tloss    = pm.compute_transmission_loss(env, mode='incoherent')
pm.plot_transmission_loss(tloss, env=env, Title=Title, vmin=-60, vmax=-10)


plt.show()