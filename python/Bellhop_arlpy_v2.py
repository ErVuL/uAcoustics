import arlpy.uwapm as pm
import numpy as np

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

    ####################
    ### Results grid ###
    ####################
    
    x = np.linspace(-15000, 15000, 100)
    z = np.linspace(-15, 3100,  100)
                    
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
    
    bot_range     = np.array([-1000, -500, 5000, 7000, 10000])
    bot_interface = np.array([2500, 1900, 2800, 3000, 2700])
    
    ###################################
    ### Sound speed in water column ###
    ###################################
    
    ssp_range = np.array([-10000, 10000])
    ssp_depth = np.array([500, 1000, 2000, 2500])
    ssp       = np.array([[1527,  1532],
                          [1430,  1400],
                          [1540,  1600], 
                          [1525,  1700]])
    
    ####################
    ### Source specs ###
    ####################
    
    tx_freq  = 5000
    tx_depth = 500
    tx_angle = np.linspace(-180, 180 , 10)
    tx_level = 10*np.sin(2*np.pi*4*tx_angle/360)  
        
    ####################
    ### Generate env ###
    ####################
    
    env = pm.make_env2d(
        
        auto_xSettings  = True,                                    
        auto_xBox       = True,                                                
        
        name            = 'Example',

        mode            = 'coherent', 
        volume_attn     = 'Thorp',
        
        rx_range        = x,                                                   # m
        rx_depth        = z,                                                   # m
        
        top_boundary    = 'vacuum',
        top_interface   = np.column_stack((top_range,top_interface)),          # m
        
        ssp_range       = ssp_range,                                           # m
        ssp_depth       = ssp_depth,                                           # m
        ssp             = ssp,                                                 # m/s
        ssp_interp      = 'c-linear',
        
        tx_freq         = tx_freq,                                             # Hz
        tx_depth        = tx_depth,                                            # m
        tx_beam         = np.column_stack((tx_angle,tx_level)),                # degree, dB
        tx_nbeams       = 0,                                                   # 0 = automatic
        tx_minAngle     = -180,                                                # deg                         
        tx_maxAngle     = 180,                                                 # deg
        
        bot_boundary    = 'acousto-elastic',
        bot_interface   = np.column_stack((bot_range,bot_interface)),          # m
        bot_roughness   = 0.2,                                                 # m (rms)

        # Acousto-elastic bottom boundary required settings
        # typical value for rock
        attn_unit       = 'dB/wavelength',
        bot_density     = 2.7,                                                 # g/cm3 
        bot_PwaveSpeed  = 6000,                                                # m/s 
        bot_SwaveSpeed  = 3500,                                                # m/s 
        bot_PwaveAttn   = 0.02,                                                # dB/wavelength 
        bot_SwaveAttn   = 0.02,                                                # dB/wavelength 
                
        )
    
    ########################
    ### Compute and plot ###
    ########################
    
    BELLHOP = pm.BELLHOP(env)
    
    tl      = BELLHOP.compute_tranmission_loss(debug=True)
    fig, ax = BELLHOP.plot_transmission_loss()
    
    