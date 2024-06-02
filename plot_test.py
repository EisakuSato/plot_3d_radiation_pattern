from plot_antenna_pattern import plot_antenna_pattern
from antenna_responce import tr38901, omni
import numpy as np
import sionna as sn
from gen_array_gain import sum_gain_single_pannel

theta_1d = np.linspace(0,   np.pi,  180) 
phi_1d   = np.linspace(-np.pi, np.pi, 360)
theta_2d, phi_2d = np.meshgrid(theta_1d, phi_1d)


# omni
gain = omni(theta_2d, phi_2d)
plot_antenna_pattern(gain, theta_2d, phi_2d)

# directional
gain = tr38901(theta_2d, phi_2d)
plot_antenna_pattern(gain, theta_2d, phi_2d)


# array antenna using sionna
nh = 8
nv = 8
elem_space = 0.5
antenna_element_pattern = "38.901"
carrier_freq = 30e9
pol = 'single'
pol_type = 'V'


array = sn.channel.tr38901.AntennaArray(vertical_spacing=elem_space,
                                        horizontal_spacing=elem_space,
                                        antenna_pattern=antenna_element_pattern,
                                        carrier_frequency=carrier_freq, 
                                        num_rows=nv,
                                        num_cols=nh,
                                        polarization=pol,
                                        polarization_type=pol_type)


    
gain= sum_gain_single_pannel(array, theta_2d, phi_2d, carrier_freq)
plot_antenna_pattern(gain, theta_2d, phi_2d)