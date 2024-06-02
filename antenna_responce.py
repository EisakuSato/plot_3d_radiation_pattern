import numpy as np

def tr38901(theta, phi):
    assert(theta.shape==phi.shape)
    G0=20
    theta_3db=30
    phi_3db = 30
    
    # 垂直方向のゲイン計算
    G_theta = - np.minimum(12 * ((theta - np.pi/2) / np.deg2rad(theta_3db))**2, G0)
    G_phi = - np.minimum(12 * (phi / np.deg2rad(phi_3db))**2, G0)
    
    
    # 全体のゲイン計算
    G_total = -np.minimum(-(G_theta+G_phi), G0)
    
    return G_total

def omni(theta, phi):
    assert(theta.shape==phi.shape)
    return np.zeros(np.shape(theta))