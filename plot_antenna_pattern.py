from mayavi import mlab
import numpy as np
from math import isclose

# normalize x
def normalize(x):
    x_max = np.max(x)
    x_min = np.min(x)
    
    if isclose(x_max, x_min):
        return np.ones(x.shape)
    else:
        return (x-x_min)

# plot 3d radiation pattern
def plot_antenna_pattern(gain_db, theta, phi):
    zoom = 3
    gain_lower = np.max(gain_db)-40
    
    gain_db = np.maximum(gain_db, gain_lower)
    
    
    r = np.array([np.sin(theta) * np.cos(phi),
                    np.sin(theta) *np.sin(phi),
                    np.cos(theta)])
    
    # Normalize the minimum gain value to 0
    gain_db_normed = normalize(gain_db)#gain_db - np.min(gain_db)
    

    r = r * gain_db_normed

    mlab.figure(size=(700, 830))
    mlab.mesh(r[0], r[1], r[2], scalars=gain_db, colormap="jet")
    mlab.view(azimuth=45, elevation=45, distance=np.max(np.abs(r))*zoom)
    mlab.scalarbar(orientation='vertical')
    mlab.show()
