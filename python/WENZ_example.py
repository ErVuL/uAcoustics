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

# Settings
##########
Fmin           = 1        # Minimum frequency in Hz
Fmax           = 100000   # Maximum frequency in Hz
wind_speed     = 5        # Wind speed in knots
water_depth    = 'deep'   # 'shallow' or 'deep' 
shipping_level = 'low'    # 'no, 'low', 'medium', or 'high'
rain_rate      = 'light'  # 'no', 'light', 'moderate', 'heavy', or 'veryheavy'
Fxx            = np.linspace(Fmin, Fmax, Fmax-Fmin)

# Compute noise levels
######################
NL = pm.compute_wenz(Fxx, wind_speed, rain_rate, water_depth, shipping_level)

# Plot
######
pm.plot_wenz(Fxx, NL, wind_speed, rain_rate, water_depth, shipping_level)
plt.show()