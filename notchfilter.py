import numpy as np
def notchfilter(f0,fs,att=0.9995):
    
    # Define the angle of f0 in z-plot
    theta = 2*np.pi*f0/fs
    
    # Get coefficients
    b = [1,-2*np.cos(theta),1]
    a = [1,-att*2*np.cos(theta),att*att]

    return b,a    # Use these coefficients in scipy.signal.filtfilt()
