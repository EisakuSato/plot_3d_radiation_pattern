import numpy as np
c = 299792458.0

def polar2cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return np.stack([x,y,z])


def sum_gain_single_pannel(array, theta_rad, phi_rad, fc):
    l = c/fc
    
    vec = polar2cartesian(1,theta_rad, phi_rad) #radius is 1
    vec = vec.reshape([1,3,np.shape(theta_rad)[0],np.shape(theta_rad)[1]])
    
    pos = array.ant_pos.numpy()
    pos = pos.reshape([array.num_ant,3,1,1])
    
    
    inn_prod = np.sum( pos * vec, axis=1)

    AF = np.sum( np.exp(2*np.pi*1j*inn_prod/l), axis=0)
    AF_db = 20*np.log10(np.abs(AF))
    return AF_db