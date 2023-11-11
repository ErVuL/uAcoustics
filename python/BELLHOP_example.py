import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pyat.env as at
from pyat.readwrite import *

os.environ['PATH'] = os.environ['PATH'].replace(':/opt/build/at/bin', '')+":/opt/build/at/bin"

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

Title = "Munk profile example"

### Build Environment File
##########################

rr = 2.5

# Environmental parameters
cw = 1500                                                                      # water sound speed [m/s]
pw = 1                                                                         # density of water [g/cm^3]
aw = 0                                                                         # attenuation of water [units determined below]
cb = 1600                                                                      # bottom sound speed
pb = 1.5                                                                       # density of bottom [g/cm^3]
ab = 0.5                                                                       # attenuation of bottom [units determined below]

# Position object
sd           = 2500                                                            # source depth [m]
Z            = np.linspace(1, 5000, 201)                                       # depth of recievers [m]
X            = np.arange(1, 100, .1)                                           # range of receivers [km]
s            = at.Source(sd)
r            = at.Dom(X, Z)
pos          = at.Pos(s,r)
pos.s.depth  = [sd]
pos.r.depth  = Z
pos.r.range  = X
pos.Nsd      = 1                                                               # number of source depths
pos.Nrd      = len(X)                                                          # number of reciever depths

# Sound Speed Object
depth  = [0, 5000]                                                             # m    
z1     = [0.0,  200.0,  250.0,  400.0,  600.0,  800.0, 1000.0, 1200.0, 1400.0, 1600.0, 1800.0, 2000.0, 2200.0, 2400.0, 2600.0, 2800.0, 3000.0, 3200.0, 3400.0, 3600.0, 3800.0, 4000.0, 4200.0, 4400.0, 4600.0, 4800.0, 5000.0] # depth [m]
alphaR = [1548.52,1530.29,1526.69,1517.78,1509.49,1504.30,1501.38,1500.14,1500.12,1501.02,1502.57,1504.62,1507.02,1509.69,1512.55,1515.56,1518.67,1521.85,1525.10,1528.38,1531.70,1535.04,1538.39,1541.76,1545.14,1548.52,1551.91] # p-wave speed in water
betaR  = 0.0*np.array([1]*len(z1))                                             # s-wave speed in water	
rho	   = pw*np.array([1]*len(z1))		                                       # density of water [g/cm^3]
alphaI = aw*np.array([1]*len(z1))		                                       # p-wave attenuation [units are determined by Opt (below)]
betaI  = 0.0*np.array([1]*len(z1))                                             # s-wave attenuation [units are determined by Opt (below)]

# create raw sound speed object - package of all arrays above
ssp1 = at.SSPraw(z1, alphaR, betaR, rho, alphaI, betaI)


### Sound-speed layer specifications
####################################

# Sound-speed layer 1 specifications
raw    = [ssp1]
NMedia = 1
Opt	   = 'CVW'	
N      = [0, 0]	
sigma  = [0, 0]	
raw[0]
ssp    = at.SSP(raw, depth, NMedia, Opt, N, sigma)

# Sound-speed layer 2 specifications
alphaR  = 1600 		                                                           # p wave speed in sediment
betaR   = 0     	                                                           # no shear wave
alphaI  = .5   		                                                           # p wave atten
betaI   = 0     	                                                           # s wave atten
rhob    = 1600


# Define Boundary Conditions
hs     = at.HS(alphaR, betaR, rhob, alphaI, betaI)                                                               
bottom = at.BotBndry('A', hs)                                                  # Analytic bottom boundary condition (add * for use of bty file)
top    = at.TopBndry('CVW')                                                    # C: Interpolate sound speed, V: Standard vacuum condition for ocean surface, W: Attenuation in dB/lambda
bdy    = at.Bndry(top, bottom)


low  = 1400
high = 1e9
cInt = cInt(low, high)
RMax = max(X)
freq = 3000

# Beam params
nbeams   = 100
alpha    = np.linspace(-20,20, 100)
box      = Box(5500, 100)
deltas   = 0

# Bathy (range in km, depth in m)
bathy = np.array(
[   #range  depth
    [0,     2000],    
    [65,    100],  
    [80,    3000]
])

# Surface (range in km, depth in m)
surface = np.array(
[   #range  depth
    [0,     0],    
    [65,    50],  
    [80,    0]
])

# Directivity
directivity = np.array(
[   #theta   power
    [0,      -20],    
    [40,     -30],  
    [80,     10]
])

# Write Bathy, Surface and Directivity files
#
# TODO      - Take it into account for computation
#           - Plot function
#           - Units ?
write_bathy("py_env.bty", bathy, interp='L')                                   # Piecewise linear fit
write_ati("py_env.ati", surface, interp='C')                                   # Curvilinear fit
write_sbp("py_env.sbp", directivity)                                           # Source directivity pattern 
    
### Run Bellhop
###############

# Compute incoherent TL with Geometric Gaussian beams in Cartesian coordinates using beam pattern file *.sbp
run_type = 'IB*'                                                              
beam     = Beam(RunType=run_type, Nbeams=nbeams, alpha=alpha, box=box, deltas=deltas)
write_env('py_env.env', 'BELLHOP', Title, freq, ssp, bdy, pos, beam, cInt, RMax)
os.system("bellhop.exe py_env")
[PlotTitle, PlotType, freqVec, atten, ppos, pressure] = read_shd_bin("py_env.shd")

# Generate a ray file with Geometric Gaussian beams in Cartesian coordinates using beam pattern file *.sbp
run_type = 'RB*'
beam     = Beam(RunType=run_type, Nbeams=nbeams, alpha=alpha, box=box, deltas=deltas)
write_env('py_env.env', 'BELLHOP', Title, freq, ssp, bdy, pos, beam, cInt, RMax)
os.system("bellhop.exe py_env")
rays = "py_env.ray"

### Generate arrivals file with Geometric Gaussian beams in Cartesian coordinates using beam pattern file *.sbp
run_type = 'AB*'
beam     = Beam(RunType=run_type, Nbeams=nbeams, alpha=alpha, box=box, deltas=deltas)
pos.r.range = [65] # km
pos.r.depth = [50] # m
write_env('py_env.env', 'BELLHOP', Title, freq, ssp, bdy, pos, beam, cInt, RMax)
os.system("bellhop.exe py_env")
arrival_list, pos = read_arrivals_asc_alt("py_env.arr")


### Plots
#########
at.plot_lvl(X, Z, pressure, PlotTitle, vmin=-60, vmax=0)
at.plot_ssp(ssp, PlotTitle)
at.plot_ray(rays, PlotTitle)
at.plot_cir(arrival_list[0], PlotTitle)
at.plot_elp(arrival_list[0], PlotTitle)

plt.show()

