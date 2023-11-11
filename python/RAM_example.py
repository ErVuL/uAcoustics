import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pyram.PyRAM as ram

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


Title = "Random profile example"

RMAX = 15000
ZMAX = 1000
RAMenv = dict(
    
    ### SOURCE SETTINGS and RECEIVER POSITION
    freq  = 20,                                                # Source frequency (Hz) => Max: 500
    zs    = 600,                                               # Source depth (m)
    zr    = 50,                                                # Receiver depth for the line plot (m) 
    c0    = 1540,                                              # Reference sound speed (m/s)
    
    ### GRID MODEL SETTINGS
    rmax  = RMAX,                                              # Maximum range for mathematical model (m)
    dr    = 9,                                                 # Range step for mathematical model (m)
    dz    = 3,                                                 # Depth grid spacing for mathematical model (m) 
    zmplt = ZMAX,                                              # Maximum depth of output to tlgrid
    
    ### SOUND SPEED PROFILE IN WATER COLUMN
    rp_ss = np.array([0, 10000, 12000]),                       # Range for sound speed profile update (m)
    z_ss  = np.array([0, 250, 500, ZMAX]),                     # Sound speed profile depth point (m)
    
                        #rp_ss1   rp_ss2   ...                                                                                                      
    cw    = np.array([[1530,   1540,    1550],   # z_ss1       # Sound speed in water column (m/s)
                      [1200,   1200,    1200],   # z_ss2
                      [1480,   1530,    1550],   # ...
                      [1500,   1490,    1510]]),   
    
    ### SEDIMENT PROPRIETIES
    rp_sb = np.array([0, 7000]),                               # Range of sediment profile update (m) 
    z_sb  = np.array([-750, -600, -500]),                      # Depth of sediment profile point (m) counted from max(zb)
                           
                     # rp_sb1   rp_sb2   ...
    cb    = np.array([[1700,   1650],   # z_sb1                # Sound speed in sediment (m/s)
                      [1680,   1750],   # z_sb2
                      [2000,   2300]]), # ...                               
    
                     # rp_sb1   rp_sb2  ...
    rhob  = np.array([[1.5,    2],     # z_sb1                 # Density in sediment (g/cc)
                      [2,      2.5],   # z_sb2
                      [2.3,    1.7]]), # ...              
        
                    # rp_sb1   rp_sb2  ...
    attn  = np.array([[0.5,    0.6],   # z_sb1                 # Attenuation in sediment (dB/wavLength)
                      [0.6,    0.8],   # z_sb2
                      [0.65,   0.7]]), # ...                                    
                                                 
    ### BATHYMETRY
                     # rb     zb
    rbzb  = np.array([[0,     1000],                           # Range and corresponding Z bathymetry point (m)
                      [5000,  900],
                      [7400,  950],
                      [7500,  750],
                      [10000, 50],
                      [RMAX,  100]])
)         

### Compute RAM
###############
ram_out = ram.ram(**RAMenv).run()

### Plots
#########
ram.plot_tline(ram_out, Title=Title, **RAMenv)
ram.plot_tl(ram_out, Title=Title, vmin = 0, vmax = 120, **RAMenv)
ram.plot_rhob(Title=Title, vmin=0.3, vmax=3, Nxy=200, **RAMenv)
ram.plot_ssp(Nxy=200, Title=Title, **RAMenv)
ram.plot_atn(Nxy=200, Title=Title, vmin=0, vmax=1, **RAMenv)

plt.show()
