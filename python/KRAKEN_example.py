import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pyat.env as at
from pyat.readwrite import *

os.environ['PATH'] = os.environ['PATH'].replace(':/opt/build/at/bin', '')+":/opt/build/at/bin"

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

Title = "Pekeris profile example"

### Build Environment File
##########################

# Environmental parameters
cw = 1500                                                                      # water sound speed [m/s]
pw = 1                                                                         # density of water [g/cm^3]
aw = 0                                                                         # attenuation of water [units determined below]
cb = 1600                                                                      # bottom sound speed
pb = 1.8                                                                       # density of bottom [g/cm^3]
ab = 0.2                                                                       # attenuation of bottom [units determined below]

# Position object
sd = 20                                                                        # source depth [m]
Z = np.arange(0, 200, .5)                                                      # depth of recievers [m]
X = np.arange(0, 10, .01)                                                      # range of receivers [km]
s = at.Source(sd)
r = at.Dom(X, Z)
pos = at.Pos(s,r)
pos.s.depth = [sd]
pos.r.depth = Z
pos.r.range = X
pos.Nsd = 1                                                                    # number of source depths
pos.Nrd = len(Z)                                                               # number of reciever depths

# Sound Speed Object
bottom_depth = 200 # m
z1 = np.linspace(0, bottom_depth, 1000)                                        # depth [m]
alphaR	=	cw*np.ones(z1.shape)                                               # p-wave speed in water
betaR	=	0.0*np.ones(z1.shape)                                              # s-wave speed in water
rho		=	pw*np.ones(z1.shape)                                               # density of water [g/cm^3]
alphaI	=	aw*np.ones(z1.shape)                                               # p-wave attenuation [units are determined by Opt (below)]
betaI	=	0.0*np.ones(z1.shape)                                              # s-wave attenuation [units are determined by Opt (below)]

# create raw sound speed object - package of all arrays above
ssp1 = at.SSPraw(z1, alphaR, betaR, rho, alphaI, betaI)                           

# Sound Speed Layer Specifications
depth   = [0, bottom_depth]                                                    # depth array for layers
NMedia	= 1
Opt		= 'CVW'                                                                # C-linear interpolation, Vaccuum top boundary, attenuation in dB/wavelength

# more detailed information about these options see Kraken User Manual p.83
N	  =	[z1.size]                                                              # array with num points in each layer, don't include one for halfpace
sigma =	[.5,.5]	                                                               # roughness at each layer. only effects attenuation (imag part)

# create sound speed object
ssp   = at.SSP([ssp1], depth, NMedia, Opt, N, sigma)                              

# Define Boundary Conditions
hs = at.HS(alphaR=cb, betaR=0, rho = pb, alphaI=ab, betaI=0)                   # create halph space object for the bottom
Opt = 'A'                                                                      # acousto-elastic half space, 
bottom = at.BotBndry(Opt, hs)                                                  # create Bottom Boundary Object
top = at.TopBndry('CVW')                                                       # create Top Boundary Object
bdy = at.Bndry(top, bottom)                                                    # create boundary object for both top and bottom

# Write Environment File
class Empty:
    def __init__(self):
        return

cInt = Empty()
cInt.High = 999999999
cInt.Low = 0                                                                   # compute automatically
RMax = 100
freq = 400
write_env('py_env.env', 'KRAKEN', Title, freq, ssp, bdy, pos, [], cInt, RMax)
write_fieldflp('py_env', 'R', pos)                                             # Build .flp file

### Run Kraken
##############
os.system('kraken.exe py_env')
os.system('field.exe py_env')

### Read the .env, .mod and .shd files
######################################
fname = 'py_env.mod'
options = {'fname':fname, 'freq':0}
modes = read_modes(**options)
[PlotTitle, PlotType, freqVec, atten,Pos1,pressure]= read_shd('py_env.shd')
env = read_env('py_env.env', 'KRAKEN')

### Plots
#########
at.plot_lvl(X, Z, pressure, PlotTitle, vmin=-120, vmax=0)
at.plot_ssp(ssp, PlotTitle)
at.plot_mod(modes, 10, PlotTitle)

plt.show()

