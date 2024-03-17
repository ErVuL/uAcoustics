import arlpy.uwapm as pm
import numpy as np
import matplotlib.pyplot as plt


# Acousto-elastic boundary condition recommended values (GPT info not verified)
#####################################################################################################################################################################################################
# | Element            | Sound Speed (m/s) | Density (g/cm³) | P-wave Speed (m/s)  | S-wave Speed (m/s)  | P-wave Attn (dB/wavelength)  | S-wave Attn (dB/wavelength)  | Absorption (dB/wavelength) |
# |--------------------|-------------------|-----------------|---------------------|---------------------|------------------------------|------------------------------|----------------------------|
# | Air                | 343               | 0.0012          | -                   | -                   | 0.0001                       | 0.0001                       | 0.0001                     |
# | Asphalt            | 2500              | 1.6             | 2500                | 1250                | 0.012                        | 0.012                        | 0.007                      |
# | Basalt             | 5750              | 2.75            | 5750                | 3500                | 0.018                        | 0.018                        | 0.009                      |
# | Clay               | 1600              | 1.85            | 1600                | 900                 | 0.0085                       | 0.0085                       | 0.0035                     |
# | Clayey Sand        | 1600              | 1.75            | 1600                | 900                 | 0.0075                       | 0.0075                       | 0.0025                     |
# | Concrete           | 4500              | 2.25            | 4500                | 2250                | 0.0175                       | 0.0175                       | 0.008                      |
# | Coral              | 1800              | 1.75            | 1800                | 900                 | 0.0095                       | 0.0095                       | 0.004                      |
# | Coral Reef         | 1700              | 1.75            | 1700                | 900                 | 0.0095                       | 0.0095                       | 0.004                      |
# | Fiberglass         | 3000              | 1.75            | 3000                | 1500                | 0.0135                       | 0.0135                       | 0.008                      |
# | Gravel             | 3250              | 2.25            | 3250                | 1750                | 0.0175                       | 0.0175                       | 0.008                      |
# | Granite            | 6500              | 2.75            | 6500                | 3500                | 0.0175                       | 0.0175                       | 0.009                      |
# | Grass              | 3250              | 0.375           | 3250                | 1750                | 0.006                        | 0.006                        | 0.0025                     |
# | Ice                | 3400              | 0.915           | 3400                | 1700                | 0.0045                       | 0.0045                       | 0.0015                     |
# | Limestone          | 6500              | 2.5             | 6500                | 4000                | 0.0225                       | 0.0225                       | 0.0125                     |
# | Marble             | 3150              | 2.65            | 3150                | 1650                | 0.0135                       | 0.0135                       | 0.008                      |
# | Metal              | 6500              | 7.8             | 6500                | 3500                | 0.0275                       | 0.0275                       | 0.0175                     |
# | Mud                | 1600              | 1.35            | 1600                | 800                 | 0.007                        | 0.007                        | 0.0025                     |
# | Peat               | 1500              | 0.75            | 1500                | 650                 | 0.006                        | 0.006                        | 0.0025                     |
# | Plastic            | 2500              | 1.25            | 2500                | 1250                | 0.0125                       | 0.0125                       | 0.0075                     |
# | Pumice             | 750               | 0.3             | 750                 | -                   | 0.0015                       | -                            | 0.00075                    |
# | Quartz             | 5900              | 2.65            | 5900                | 3300                | 0.0175                       | 0.0175                       | 0.009                      |
# | Rubber             | 1750              | 1.2             | 1750                | 750                 | 0.009                        | 0.009                        | 0.005                      |
# | Sand               | 1600              | 1.65            | 1600                | 900                 | 0.007                        | 0.007                        | 0.0025                     |
# | Sandstone          | 3250              | 2.25            | 3250                | 1750                | 0.0175                       | 0.0175                       | 0.008                      |
# | Silt               | 1600              | 1.5             | 1600                | 700                 | 0.007                        | 0.007                        | 0.0025                     |
# | Soil               | 1600              | 1.5             | 1600                | 850                 | 0.0075                       | 0.0075                       | 0.0025                     |
# | Water (Fresh)      | 1435              | 1.0             | 1482                | 0                   | 0.125                        | 0.125                        | 0.06                       |
# | Water (Salt)       | 1570              | 1.03            | 1570                | 0                   | 0.125                        | 0.125                        | 0.06                       |
# | Wood               | 3500              | 0.65            | 3500                | 1750                | 0.0125                       | 0.0125                       | 0.0075                     |
#####################################################################################################################################################################################################


if __name__ == '__main__':

    Title = "Example"

    ####################
    ### Results grid ###
    ####################
    
    x = np.linspace(-10000, 15000, 1080)
    z = np.linspace(-15, 3100,  720)
                    
    ###############
    ### Surface ###
    ###############
    
    surfaceWaveHeight = 3 # m
    surfaceWaveLength = 7 # m
    top_range         = np.array([-10000, 1000, 5000, 10000])
    top_interface     = surfaceWaveHeight*np.sin(2*np.pi/surfaceWaveLength*top_range)
    
    #############
    ### Bathy ###
    #############
    
    bot_range     = np.array([-10000, -500, 5000, 7000, 10000])
    bot_interface = np.array([2500, 1900, 2800, 3000, 2700])

    ###################################
    ### Sound speed in water column ###
    ###################################
    
    ###################################
    ### Sound speed in water column ###
    ###################################
    
    ssp_range = np.array([-10000, 2500, 5000])
    ssp_depth = np.array([500, 1000, 2000, 2500])
    ssp       = np.array([[1200,  1532, 1500],
                          [1430,  1200, 1200],
                          [1540,  1300, 1200], 
                          [1525,  1700, 1500]])
    
    ####################
    ### Source specs ###
    ####################
    
    tx_freq   = 25
    tx_depth  = 250
    
    #######################
    ### Bottom settings ###
    #######################
    
    bot_xrange = np.array([-1000, 0, 10000])
    bot_xdepth = np.array([np.min(bot_interface), np.max(bot_interface)])
    
    bot_absorption = np.array([
        [0.01, 0.015, 0.012],
        [0.02, 0.007, 0.011]
    ])
    bot_ssp = np.array([
        [6500, 5660, 6000],
        [7000, 6600, 5900]
    ])
    bot_density = np.array([
        [2.7, 2.3, 2.5],
        [2.5, 1.8, 2.0]
    ])
    
    ####################
    ### Generate env ###
    ####################
    
    env = pm.make_env2d(
        
        name            = Title,
        
        rx_depth        = z,
        rx_range        = x,  
        
        top_interface   = np.column_stack((top_range,top_interface)),
        
        ssp_range       = ssp_range,
        ssp_depth       = ssp_depth,
        ssp             = ssp,
        
        bot_interface   = np.column_stack((bot_range,bot_interface)), 
        
        bot_range       = bot_xrange,
        bot_depth       = bot_xdepth,
        bot_ssp         = bot_ssp,
        bot_density     = bot_density,
        bot_absorption  = bot_absorption,

        tx_freq         = tx_freq,
        tx_depth        = tx_depth,
        
        pad_inputData   = True,
    )
    
    ###############
    ### Compute ###
    ###############
    
    RAM     = pm.RAM(env)
    
    tl        = RAM.compute_transmission_loss(debug=True)
    fig, ax   = RAM.plot_transmission_loss()
