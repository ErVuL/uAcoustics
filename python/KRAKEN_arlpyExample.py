import arlpy.uwapm as pm
import numpy as np
import pyat.env as at


if __name__ == '__main__':
    
    Title = "Example"
    
    ############
    ### Grid ###
    ############
    
    x = np.linspace(0, 2000, 1000)
    z = np.linspace(0, 100,  1000)
    
    #############
    ### Bathy ###
    #############
    
    bathy = [
        [x[0],  90],  
        [100, 75],
        [200, 80],  
        [1000, 85], 
        [x[-1], 100]  
    ]
    
    ###############
    ### Surface ###
    ###############
    
    surface = np.array([[r, 1+1*np.sin(2*np.pi*0.05*r)] for r in x])
    
    ###################################
    ### Sound speed in water column ###
    ###################################
    
    ssp_depth = [0, 25, 75, 90, z[-1]] # Must start at 0
    ssp_range = [0, 100]
    
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
    
    tx_depth  = 50
    frequency = 250
    
    beampattern = np.array([
        [-180,  10], [-170, -10], [-160,   0], [-150, -20], [-140, -10], [-130, -30],
        [-120, -20], [-110, -40], [-100, -30], [-90 , -50], [-80 , -30], [-70 , -40],
        [-60 , -20], [-50 , -30], [-40 , -10], [-30 , -20], [-20 ,   0], [-10 , -10],
        [  0 ,  10], [ 10 , -10], [ 20 ,   0], [ 30 , -20], [ 40 , -10], [ 50 , -30],
        [ 60 , -20], [ 70 , -40], [ 80 , -30], [ 90 , -50], [100 , -30], [110 , -40],
        [120 , -20], [130 , -30], [140 , -10], [150 , -20], [160 ,   0], [170 , -10],
        [180 ,  10]
    ])
    
    #######################
    ### Bottom settings ###
    #######################
    
    bottom_sdepth = [75, 100]
    bottom_absorption = [10, 15]
    
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
        model                      = 'KRAKEN',
        depth                      = bathy,
        surface                    = surface,
        soundspeed                 = soundspeed,
        soundspeed_range           = ssp_range,
        soundspeed_depth           = ssp_depth,
        soundspeed_interp          = 'c-linear',
        top_boundary               = 'vacuum',
        bottom_soundspeed          = bottom_soundspeed,
        bottom_density             = bottom_density,
        bottom_absorption          = bottom_absorption,
        bottom_sdepth              = bottom_sdepth,        
        bottom_roughness_interface = 10,
        bottom_boundary            = 'rigid',
        frequency                  = frequency,
        tx_depth                   = tx_depth,
        tx_directionality          = beampattern,
        rx_depth                   = z,
        rx_range                   = x,  
        nmedia                     = 3 # water, bottom1, bottom2
    )
    
    ###############
    ### Compute ###
    ###############

    tloss = pm.compute_transmission_loss(env, debug=True)
    modes = pm.compute_modes(env, debug=True) 
    
    ############
    ### Plot ###
    ############
    
    at.plot_mod(modes, 5, Title)
    