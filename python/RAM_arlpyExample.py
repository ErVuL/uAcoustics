import arlpy.uwapm as pm
import numpy as np
import os 
import matplotlib.pyplot as plt
from matplotlib import rc
os.environ['PATH'] = os.environ['PATH'].replace(':/opt/build/at/bin', '')+":/opt/build/at/bin"

Title = "Example"
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


############
### Grid ###
############

x = np.linspace(0, 35000, 1250)
z = np.linspace(0, 3000,  1500)

#############
### Bathy ###
#############

bathy = [
    [x[0],  2500],  
    [10000, 3000],
    [20000, 2000],  
    [30000, 2500], 
    [x[-1], 3000]  
]

###############
### Surface ###
###############

surface = np.array([[r, 1+1*np.sin(2*np.pi*0.05*r)] for r in x])

###################################
### Sound speed in water column ###
###################################

ssp_depth = [z[0], 1000, 2000, 2500, z[-1]]
ssp_range = [0, 10000]

soundspeed = [
    [1527,  1532],
    [1400,  1400],
    [1540,  1600], 
    [1526,  1526],
    [1525,  1525]  
]

####################
### Source specs ###
####################

tx_depth  = 500
frequency = 500

beampattern = [
    [-180, -60],
    [-5,     0],
    [0,    -60],
    [5,      0],
    [180,  -60],
]

#######################
### Bottom settings ###
#######################

bottom_sdepth = [2500, 3000]
bottom_srange = [0,   10000]

bottom_absorption = [
    [10, 12],
    [15, 11]
]
bottom_soundspeed = [
    [1600, 1550],
    [1700, 1650]
]
bottom_density = [
    [1200, 1700],
    [1500, 1650]
]

####################
### Generate env ###
####################

env = pm.create_env2d(
    depth              = bathy,
    surface            = surface,
    soundspeed         = soundspeed,
    soundspeed_range   = ssp_range,
    soundspeed_depth   = ssp_depth,
    bottom_soundspeed  = bottom_soundspeed,
    bottom_density     = bottom_density,
    bottom_absorption  = bottom_absorption,
    bottom_sdepth      = bottom_sdepth,        
    bottom_srange      = bottom_srange,
    frequency          = frequency,
    tx_depth           = tx_depth,
    tx_directionality  = beampattern,
    rx_depth           = z,
    rx_range           = x  
)

########################
### Compute and plot ###
########################

# Bellhop for comparison
env['model'] = 'BELLHOP'
tloss =  pm.compute_transmission_loss(env, mode='coherent') 
pm.plot_transmission_loss(tloss, env, Title, vmin=-120, vmax=0)
pm.plot_soundspeed(env, Title, vmin=1400, vmax=1700)
pm.plot_absorption(env, Title)
pm.plot_density(env, Title)
pm.plot_beam(env, Title)

# RAM
env['model'] = 'RAM'
tloss = pm.compute_transmission_loss(env)
pm.plot_transmission_loss(tloss, env, Title, vmin=-120, vmax=0)
pm.plot_soundspeed(env, Title, vmin=1400, vmax=1700)
pm.plot_absorption(env, Title)
pm.plot_density(env, Title)
pm.plot_beam(env, Title)

plt.show()