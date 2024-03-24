import arlpy.uwapm as pm
import numpy as np

if __name__ == '__main__':

    ####################
    ### Results grid ###
    ####################
    
    x = np.linspace(-7500, 15000, 1080)
    z = np.linspace(-15, 3100,  720)
                    
    ###############
    ### Surface ###
    ###############
    
    surfaceWaveHeight = 3 # m
    surfaceWaveLength = 7 # m
    top_range         = np.array([-13000, 1000, 5000, 10000])
    top_interface     = surfaceWaveHeight*np.sin(2*np.pi/surfaceWaveLength*top_range)
    
    #############
    ### Bathy ###
    #############
    
    bot_range     = np.array([-10000, -500, 5000, 7000, 10000])
    bot_interface = np.array([2000, 1000, 3000, 2000, 1500])
    
    ###################################
    ### Sound speed in water column ###
    ###################################
    
    ssp_range = np.array([-5000, 0, 5000])
    ssp_depth = np.array([100, 500, 1000, 2500])
    ssp       = np.array([[1200,  1600, 1600],
                          [1200,  1600, 1600],
                          [1600,  1200, 1200], 
                          [1600,  1600, 1600]])
    """
    ssp_range = np.array([0])
    ssp_depth = np.array([500, 1000, 2000, 2500])
    ssp       = np.array([[1500], 
                         [1200], 
                         [1532],
                         [1400]])
    """
    ####################
    ### Source specs ###
    ####################
    
    tx_freq  = 50
    tx_depth = 250
    tx_angle = np.linspace(-180, 180 , 10)
    tx_level = 10*np.sin(2*np.pi*4*tx_angle/360)  
 

    #######################
    ### Bottom settings ###
    #######################
    
    bot_xrange = np.array([-1000, 0, 10000])
    bot_xdepth = np.array([np.min(bot_interface), 2700])
    
    bot_attenuation = np.array([
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
                
        pad_inputData   = True, 
        name            = 'Example',

        # BELLHOP mode and attn
        mode            = 'coherent', 
        volume_attn     = 'Thorp',
        
        # ALL: Receiver positoins
        rx_range        = x,                                                   # m
        rx_depth        = z,                                                   # m
        
        # OALIB: Top boundary condition
        top_boundary    = 'vacuum',
        
        # ALL: Top interface
        top_interface   = np.column_stack((top_range,top_interface)),          # m
        
        # ALL: Sound speed profiles
        ssp_range       = ssp_range,                                           # m
        ssp_depth       = ssp_depth,                                           # m
        ssp             = ssp,                                                 # m/s
        ssp_interp      = 'c-linear',
        
        # ALL: Source freq and depth
        tx_freq         = tx_freq,                                             # Hz
        tx_depth        = tx_depth,                                            # m
        
        # BELLHOP: Source directivity
        tx_beam         = np.column_stack((tx_angle,tx_level)),                # degree, dB
        tx_nbeams       = 0,                                                   # 0 = automatic
        tx_minAngle     = -180,                                                # deg                         
        tx_maxAngle     = 180,                                                 # deg

        # ALL: Bottom interface
        bot_interface   = np.column_stack((bot_range,bot_interface)),          # m
                                                        
        # OALIB: Bottom boundary 
        bot_boundary    = 'acousto-elastic',
        bot_roughness   = 0.2,                                                 # m (rms)

        # OALIB: Acousto-elastic bottom boundary 
        attn_unit       = 'dB/wavelength',
        bot_PwaveSpeed  = 6000,                                                # m/s 
        bot_SwaveSpeed  = 3500,                                                # m/s 
        bot_PwaveAttn   = 0.02,                                                # dB/wavelength 
        bot_SwaveAttn   = 0.02,                                                # dB/wavelength 
            
        # RAM: Bottom settings   
        bot_range       = bot_xrange,
        bot_depth       = bot_xdepth,
        bot_ssp         = bot_ssp,
        bot_density     = bot_density,
        bot_attn        = bot_attenuation,
        )
    
    ########################
    ### Compute and plot ###
    ########################
    
    BELLHOP = pm.BELLHOP(env, cp=True)
    RAM     = pm.RAM(env, cp=True)
    RAM.plot_bot_density()
    RAM.plot_bot_attn()
    RAM.plot_ssp()
  
    RAM.compute_transmission_loss()
    RAM.plot_transmission_loss()
    RAM.plot_ssp(vmin=1000, vmax=2000)
    
    BELLHOP.compute_transmission_loss()
    BELLHOP.plot_transmission_loss()
    BELLHOP.plot_ssp(vmin=1000, vmax=2000)
    
    env['rx_range'] = 10000
    env['rx_depth'] = 1000
    env = pm.make_env2d(**env)
    BELLHOP.set_env(env, cp=True)

    BELLHOP.compute_impulse_respsonse(fs=24000, nArrivals=10)
    BELLHOP.plot_impulse_response() 
    
    BELLHOP.compute_arrivals()
    BELLHOP.plot_arrivals()  

    BELLHOP.compute_rays()
    BELLHOP.plot_rays(number=8)   

    BELLHOP.compute_eigen_rays()
    BELLHOP.plot_eigen_rays(number=8)     
