import numpy as np
import arlpy.uwa as uwa
import sys
from os import system
from matplotlib import pyplot as plt
from matplotlib import rc
from pyat.env import *
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
s            = Source(sd)
r            = Dom(X, Z)
pos          = Pos(s,r)
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
ssp1 = SSPraw(z1, alphaR, betaR, rho, alphaI, betaI)


### Sound-speed layer specifications
####################################

# Sound-speed layer 1 specifications
raw    = [ssp1]
NMedia = 1
Opt	   = 'CVW'	
N      = [0, 0]	
sigma  = [0, 0]	
raw[0]
ssp    = SSP(raw, depth, NMedia, Opt, N, sigma)

# Sound-speed layer 2 specifications
alphaR  = 1600 		                                                           # p wave speed in sediment
betaR   = 0     	                                                           # no shear wave
alphaI  = .5   		                                                           # p wave atten
betaI   = 0     	                                                           # s wave atten
rhob    = 1600

# Define Boundary Conditions
hs     = HS(alphaR, betaR, rhob, alphaI, betaI)
Opt    = 'A'
bottom = BotBndry(Opt, hs)
top    = TopBndry('CVW')
bdy    = Bndry(top, bottom)


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

# Bathy
bathy = np.array([
    [0, 500],    
    [65, 3000],  
    [80, 1000]
])

# Surface
surface = np.array([
    [0, 0],    
    [65, 500],  
    [80, 0]
])

# Directivity
directivity = np.array([
    [0, 30],    
    [40, 200],  
    [80, 20]
])

# Write Bathy, Surface and Directivity files
#
# TODO      - Take it into account for computation
#           - Plot function
#           - Units ?
write_bathy("py_env.bty", bathy)
write_ati("py_env.ati", surface, interp='C')
write_sbp("py_env.sbp", directivity)
    
### Run Bellhop
###############

# Compute incoherent TL
run_type = 'I'
beam     = Beam(RunType=run_type, Nbeams=nbeams, alpha=alpha, box=box, deltas=deltas)
write_env('py_env.env', 'BELLHOP', Title, freq, ssp, bdy, pos, beam, cInt, RMax)
system("bellhop.exe py_env")
[PlotTitle, PlotType, freqVec, atten, ppos, pressure] = read_shd("py_env.shd")

# Generate a ray file
run_type = 'R'
beam     = Beam(RunType=run_type, Nbeams=nbeams, alpha=alpha, box=box, deltas=deltas)
write_env('py_env.env', 'BELLHOP', Title, freq, ssp, bdy, pos, beam, cInt, RMax)
system("bellhop.exe py_env")
rays = "py_env.ray"

### Generate arrivals file
run_type = 'A'
beam     = Beam(RunType=run_type, Nbeams=nbeams, alpha=alpha, box=box, deltas=deltas)
write_env('py_env.env', 'BELLHOP', Title, freq, ssp, bdy, pos, beam, cInt, RMax)
system("bellhop.exe py_env")
arrival_list, pos = read_arrivals_asc_alt("py_env.arr")


### Plots
#########
plot_lvl(X, Z, pressure, PlotTitle, vmin=-60, vmax=0)
plot_ssp(ssp, PlotTitle)
plot_ray(rays, PlotTitle)
plot_cir(arrival_list[357], PlotTitle)
plot_ellipse(arrival_list[357], PlotTitle)

plt.show()

