import arlpy.uwapm as pm
import numpy as np

if __name__ == '__main__':

    Title = "Example"

    ############
    ### Grid ###
    ############
    
    x = np.linspace(0, 35000, 10)
    z = np.linspace(0, 3000,  10)
    
    #############
    ### Bathy ###
    #############
    
    bathy = np.array([
        [0,     2500],  
        [10000, 3000],
        [20000, 2000],  
        [30000, 2500], 
        [x[-1], 3000]  
    ])
    
    ###############
    ### Surface ###
    ###############
    
    surface = np.array([[r, 1+1*np.sin(2*np.pi*0.05*r)] for r in x])
    
    ###################################
    ### Sound speed in water column ###
    ###################################
    
    ssp_depth = [0, 1000, 2000, 2500, z[-1]]
    ssp_range = [0, x[-1]]
    
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
    frequency = 5000
    
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
    
    bottom_sdepth = np.array([2500, 3000])
    bottom_srange = np.array([0,   10000])
    
    bottom_absorption = np.array([
        [10, 12],
        [15, 11]
    ])
    bottom_soundspeed = np.array([
        [1600, 1550],
        [1700, 1650]
    ])
    bottom_density = np.array([
        [1200, 1700],
        [1500, 1650]
    ])
    
    ##########################
    ### Init Bellhop class ###
    ##########################
    
    Bellhop = pm.bellhop()
    
    ####################
    ### Generate env ###
    ####################
    
    Bellhop.create_env(
        mode               = 'coherent', 
        depth              = bathy,
        surface            = surface,
        soundspeed         = soundspeed,
        soundspeed_depth   = ssp_depth,
        soundspeed_range   = ssp_range,
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
    
    # Transmission Loss
    Bellhop.compute_tranmission_loss(debug=True)