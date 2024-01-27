#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import arlpy.uwapm as pm
import numpy as np
import os 
import matplotlib.pyplot as plt
from matplotlib import rc
os.environ['PATH'] = os.environ['PATH'].replace(':/opt/build/at/bin', '')+":/opt/build/at/bin"
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


if __name__ == '__main__':
    
    """
        Table 1-1. Beaufort Wind Force and Sea State Numbers Vs Wind Speed
                   ("AMBIENT NOISE IN THE SEA" R.J.URICK, 1984)
                                                 Wind Speed
        Beaufort Number     Sea State       Knots       Meters/Sec
        0                   0               <1          0 - 0.2
        1                   1/2             1 - 3       0.3 - 1.5
        2                   1               4 - 6       1.6 - 3.3
        3                   2               7 - 10      3.4 - 5.4
        4                   3               11 - 16     5.5 - 7.9
        5                   4               17 - 21     8.0 - 10.7
        6                   5               22 - 27     10.8 - 13.8
        7                   6               28 - 33     13.9 - 17.1
        8                   6               34 - 40     17.2 - 20.7
    """
    
    # Settings
    ##########
    Fmin           = 1           # Min freq in Hz
    Fmax           = 1e5         # Max recommended value 1e5 Hz
    wind_speed     = 10          # Wind speed in knots
    water_depth    = 'deep'      # 'shallow' or 'deep' 
    shipping_level = 'low'       # 'no, 'low', 'medium', or 'high'
    rain_rate      = 'light'     # 'no', 'light', 'moderate', 'heavy', or 'veryheavy'
    Fxx            = np.linspace(Fmin, Fmax, int(Fmax-Fmin)) 
    
    # Compute noise levels
    ######################
    NL = pm.compute_wenz(Fxx, wind_speed, rain_rate, water_depth, shipping_level)
    
    # Plot
    ######
    pm.plot_wenz(Fxx, NL, wind_speed, rain_rate, water_depth, shipping_level)
    plt.show()