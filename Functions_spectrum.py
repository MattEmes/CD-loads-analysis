# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:09:04 2024

@author: memes
"""

def spectrum(data, freq, channels, time_series=0):
    '''
    use:
    spectrum(data_spectrum,fs,['u_E', 'v_E', 'w_E'])
    '''
    
    import numpy as np
    import scipy as sp
    import scipy.signal as sp
    import matplotlib.pyplot as plt

    from matplotlib import pyplot as plt 
    from scipy.fft import fftfreq

    
    freq = float(freq)
    if data.index.dtype == 'datetime64[ns]':
        start = data.index[0].strftime("%Y-%m-%d %H:%M:%S")
        end   = data.index[-1].strftime("%H:%M:%S")
    else:
        try:
            start = data.GPStime.iloc[0].strftime("%Y-%m-%d %H:%M:%S")
            end   = data.GPStime.iloc[-1].strftime("%H:%M:%S") 
        except:
            start = 'start'
            end = 'end'
            
            
    if time_series==1:
        fig, (ax1, ax) = plt.subplots(1, 2, figsize=(15,7))
    else:
        fig, ax = plt.subplots(figsize=(8,6))
        
    
    i=0
    for v in channels: 
        i = i+1
        
        # Define signal
        fftsig = data[v].interpolate(limit=2).dropna()
        
        if time_series==1:
            times = fftsig.index
            #fig1, ax1 = plt.subplots()
            #ax1.plot(times,fftsig.values, label ='original')
        
        # Detrend
        fftsig = sp.signal.detrend(fftsig)
        
        if time_series==1:
            ax1.plot(times,fftsig, label =v+' detrend', lw=1, alpha=0.5)
            ax1.grid(True)
            ax1.set_xlabel("Time (s)")
            #ax1.set_ylabel("Wind speed "+v+' m/s', fontsize='x-large')
            ax1.legend(loc='best')  
            ax1.set_title('Time series')
            fig.autofmt_xdate()
        
        N = len(fftsig) 
        nyq = freq/2
        
        # frequency axis
        X = np.fft.fftfreq(N, 1/freq)
        X = X[1:int(N/2)]
        
        # FFT
        Y = fft(fftsig)
        
        # PSD
        Y = 2 * (abs(Y[1:int(N/2)])  / N)**2 /(X[2] - X[1])
  
        # 5/3 line    
        y2 = X**(-5/3.) / 1e3
        
        # Smothing over logarithmic aequidistant bins
        start_freq = X[2] # 0.01         # Smoothing starts at 0.1 Hz
        total_bins = 50                  # Time series is divided in N bins 
        
        start_log = np.log10(start_freq)
        stop_log  = np.log10(nyq)
        bins = np.logspace(start_log,stop_log, num = total_bins, endpoint = True)   # define bin boundaries
        idx  = np.digitize(X,bins)  # sort X-values into bins
        bins     = (bins[1:] + bins[:-1]) / 2   # center of bins, right edge of bins would be  bins[0:total_bins-1]       
        smooth        = [np.average(Y[idx==k]) for k in range(total_bins)]                   # average Y-values for each bin                                                # remove 1st point - it's a NaN
        smooth        = smooth[1:total_bins]                                                      # remove 1st point - it's a NaN

        if v == channels[0]: 
            #fig, ax = plt.subplots(figsize=(10,7))
            ax.grid(True) 
            ax.loglog(X,y2, label ='$f^{-5/3}$', color = 'black')
            ax.set_xlabel("Frequency f (Hz)", fontsize='large')
            ax.set_ylabel("Power spectral density ($\sigma^2 Hz^{-1})$", fontsize='large')
            plt.tight_layout()
            ax2 = ax.twiny()
            plt.xscale('log')
            mn, mx = ax.get_xlim()
            ax2.set_xlim(1/mn/60, 1/mx/60)
            ax2.xaxis.set_major_formatter(FormatStrFormatter('%g'))
            plt.xlabel('Time (min)', fontsize='large')
        first, = ax.loglog(X,Y, linewidth=0.5,label='$PSD$ '+v,alpha=0.3)
        ax.loglog(bins,smooth,'--',marker = '.',label='smooth $PSD$ '+v,color = first.get_color(), zorder=10)
        ax.legend(loc='best', fontsize='large')  
        ax.set_title('Power spectrum {} to {}'.format(start, end), fontsize='large')
 
    #ax.set_ylim(10**-9, 10**-1)
    plt.tight_layout()  
    return fig
  
  

  