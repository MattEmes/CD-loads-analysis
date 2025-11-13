# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:09:36 2024

@author: memes
"""

def calculate_spectrum(channel, fs):
    ''' 
    calculates spectrum and smoothed spectrum
    use:
         X, Y, y2, bins1, smooth1 = calculate_spectrum(Balloon.w_E, fs=fs_Balloon)
         plt.loglog(X,Y,label='PSD')
         plt.loglog(bins1,smooth1,'-',marker = '.',label='PSD smoothed')
    '''     
    
    fs = float(fs)
    
    # Define signal
    fftsig = channel.interpolate(limit=2).dropna()
    
    import numpy as np
    import scipy.signal as sp
    import matplotlib.pyplot as plt

    
    # Detrend
    fftsig = sp.signal.detrend(fftsig)
    
    N = len(fftsig) 
    nyq = fs/2
    
    
    # frequency axis
    X = fftfreq(N, 1/fs)
    X = X[1:int(N/2)]
    
    # FFT
    Y = fft(fftsig)
    
    # PSD
    Y = 2 * (abs(Y[1:int(N/2)])  / N)**2 /(X[2] - X[1])
  
    # 5/3 line    
    y2 = X**(-5/3.) / 1e3
    
    # Smmothing ochanneler logarithmic aequidistant bins
    start_freq = X[2] # 0.01         # Smoothing starts at 0.1 Hz
    total_bins = 50                  # Time series is divided in N bins 
    
    start_log = np.log10(start_freq)
    stop_log  = np.log10(nyq)
    bins = np.logspace(start_log,stop_log, num = total_bins, endpoint = True)   # define bin boundaries
    idx  = np.digitize(X,bins)  # sort X-values into bins
    bins     = (bins[1:] + bins[:-1]) / 2   # center of bins, right edge of bins would be bins[1:total_bins]   
    smooth        = [np.average(Y[idx==k]) for k in range(total_bins)]                   # average Y-values for each bin                                                # remove 1st point - it's a NaN
    smooth        = smooth[1:total_bins]                                                      # remove 1st point - it's a NaN
    
    return X, Y, y2, bins, smooth