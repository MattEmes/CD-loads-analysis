import os
import pandas as pd
from nptdms import TdmsFile
import zipfile
import matplotlib.pyplot as plt
import sys
import glob
from itertools import product
import pickle
import time
#import date
from datetime import datetime
import math

sys.path.append("C:/Users/memes/CD Analysis")


from Functions_general import *
from Functions_loads_CD import *



#%% Read data

inflow = pd.read_pickle('Inflow_1min_2024-03-13_to_2025-03-13.pkl')
mast = pd.read_pickle('mast_1min_2024-09-14_to_2025-03-13.pkl')
loads = pd.read_pickle('Loads_fastdata_1min_2024-03-11_to_2024-12-12.pkl')

# Remove duplicate timestamps, keeping the first occurrence
#loads = loads.reset_index()
#loads_no_duplicates = loads.drop_duplicates(subset=['LabVIEW Timestamp'])
#loads_no_duplicates = loads_no_duplicates.set_index('LabVIEW Timestamp')

#t = read_tdms_file_into_dataframe('Y:\Wind-data/Restricted/Projects/NSO/CrescentDunes-Loads/SlowData/2024-05-17/CrescentDunes_2024_05_17_13_38_18_1Hz.tdms')
#t = read_tdms_file_into_dataframe('Y:\Wind-data/Restricted/Projects/NSO/CrescentDunes-Loads/FastData/2024-09-26/CrescentDunes_2024_09_26_20_34_45_20Hz.tdms')
#t = read_tdms_file_into_dataframe('Y:\Wind-data/Restricted/Projects/NSO/CrescentDunes-Loads/FastData/2024-10-07/CrescentDunes_2024_10_07_23_56_57_20Hz.tdms')

#w = pd.read_pickle('Y:\Wind-data/Restricted/Projects/NSO/CrescentDunes_processed_met_tower_data_preliminary/Wake_Masts_1min_2024-12-04_0h_to_2024-12-05_00h.pkl')

#H1 = pd.read_pickle(f'SCADA_H1_1min_{H1.index[0].date()}_to_{H1.index[-1].date()}.pkl')
#H2 = pd.read_pickle(f'SCADA_H2_1min_{H2.index[0].date()}_to_{H2.index[-1].date()}.pkl')
#H3 = pd.read_pickle(f'SCADA_H3_1min_{H3.index[0].date()}_to_{H3.index[-1].date()}.pkl')

loads_inflow = pd.merge(loads, inflow, left_index=True, right_index=True, how="inner")
loads_inflow = loads_inflow[~loads_inflow.index.duplicated(keep='first')]

inflow_loads = loads.join(inflow, how='inner')  # You can use 'inner' if you only want matching timestamps
inflow_loads = inflow_loads[~inflow_loads.index.duplicated(keep='first')]

mast_loads = loads.join(mast, how='inner')  # You can use 'inner' if you only want matching timestamps
mast_loads = mast_loads[~mast_loads.index.duplicated(keep='first')]
                  
# Winds less than 2 m/s
inflow_lowwind_2ms_loads = inflow_loads[abs(inflow_loads['wspd_Mid'])<2]
inflow_lowwind_3ms_loads = inflow_loads[abs(inflow_loads['wspd_Mid'])<3]
inflow_lowwind_4ms_loads = inflow_loads[abs(inflow_loads['wspd_Mid'])<4]

H1 = pd.read_pickle('SCADA_H1_1min_2024-03-14_to_2025-01-10.pkl')
H2 = pd.read_pickle('SCADA_H2_1min_2024-03-14_to_2025-01-10.pkl')
H3 = pd.read_pickle('SCADA_H3_1min_2024-03-14_to_2025-01-10.pkl')

H1 = H1.tz_localize(None)
H2 = H2.tz_localize(None)
H3 = H3.tz_localize(None)

H1_elevation = 90-H1.AngElData
H1_azimuth = H1.AngAzData
H2_elevation = 90-H2.AngElData
H2_azimuth = H2.AngAzData
H3_elevation = 90-H3.AngElData
H3_azimuth = H3.AngAzData

H1_state = H1.State
H2_state = H2.State
H3_state = H3.State

H1_elevation.rename(columns={'mean': 'H1_elevation'}, inplace=True)
H1_azimuth.rename(columns={'mean': 'H1_azimuth'}, inplace=True)
H2_elevation.rename(columns={'mean': 'H2_elevation'}, inplace=True)
H2_azimuth.rename(columns={'mean': 'H2_azimuth'}, inplace=True)
H3_elevation.rename(columns={'mean': 'H3_elevation'}, inplace=True)
H3_azimuth.rename(columns={'mean': 'H3_azimuth'}, inplace=True)

H1_state.rename(columns={'last': 'H1_state'}, inplace=True)
H2_state.rename(columns={'last': 'H2_state'}, inplace=True)
H3_state.rename(columns={'first': 'H3_state'}, inplace=True)

H1_elevation_azimuth_state_inflow_loads = inflow_loads.join([H1_elevation, H1_azimuth, H1_state], how='inner')
H1_elevation_azimuth_state_inflow_loads = H1_elevation_azimuth_state_inflow_loads[~H1_elevation_azimuth_state_inflow_loads.index.duplicated(keep='last')]     
H2_elevation_azimuth_state_inflow_loads = inflow_loads.join([H2_elevation, H2_azimuth, H2_state], how='inner')
H2_elevation_azimuth_state_inflow_loads = H2_elevation_azimuth_state_inflow_loads[~H2_elevation_azimuth_state_inflow_loads.index.duplicated(keep='last')]
H3_elevation_azimuth_state_inflow_loads = inflow_loads.join([H3_elevation, H3_azimuth, H3_state], how='inner')
H3_elevation_azimuth_state_inflow_loads = H3_elevation_azimuth_state_inflow_loads[~H3_elevation_azimuth_state_inflow_loads.index.duplicated(keep='last')]

H1_elevation_azimuth_state_inflow_loads["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads.H3_Elevation_Right)/2


H1_elevation_azimuth_state_inflow_lowwind_2ms_loads = H1_elevation_azimuth_state_inflow_loads[abs(H1_elevation_azimuth_state_inflow_loads['wspd_Mid'])<2]
H2_elevation_azimuth_state_inflow_lowwind_2ms_loads = H2_elevation_azimuth_state_inflow_loads[abs(H2_elevation_azimuth_state_inflow_loads['wspd_Mid'])<2]
H3_elevation_azimuth_state_inflow_lowwind_2ms_loads = H3_elevation_azimuth_state_inflow_loads[abs(H3_elevation_azimuth_state_inflow_loads['wspd_Mid'])<2]

H1_elevation_azimuth_state_mast_loads = mast_loads.join([H1_elevation, H1_azimuth, H1_state], how='inner')
H1_elevation_azimuth_state_mast_loads = H1_elevation_azimuth_state_mast_loads[~H1_elevation_azimuth_state_mast_loads.index.duplicated(keep='last')]      
H2_elevation_azimuth_state_mast_loads = mast_loads.join([H2_elevation, H2_azimuth, H2_state], how='inner')
H2_elevation_azimuth_state_mast_loads = H2_elevation_azimuth_state_mast_loads[~H2_elevation_azimuth_state_mast_loads.index.duplicated(keep='last')]
H3_elevation_azimuth_state_mast_loads = mast_loads.join([H3_elevation, H3_azimuth, H3_state], how='inner')
H3_elevation_azimuth_state_mast_loads = H3_elevation_azimuth_state_mast_loads[~H3_elevation_azimuth_state_mast_loads.index.duplicated(keep='last')]

#H1_elevation_azimuth_state_mast_lowwind_2ms_loads = H1_elevation_azimuth_state_mast_loads[abs(H1_elevation_azimuth_state_mast_loads['U_ax_Mid'])<2]
#H2_elevation_azimuth_state_mast_lowwind_2ms_loads = H2_elevation_azimuth_state_mast_loads[abs(H2_elevation_azimuth_state_mast_loads['U_ax_Mid'])<2]
#H3_elevation_azimuth_state_mast_lowwind_2ms_loads = H3_elevation_azimuth_state_mast_loads[abs(H3_elevation_azimuth_state_mast_loads['U_ax_Mid'])<2]

#H1_elevation_inflow_loads = inflow_loads.join(H1_elevation, how='inner')  # You can use 'inner' if you only want matching timestamps
#H1_azimuth_inflow_loads = inflow_loads.join(H1_azimuth, how='inner')  # You can use 'inner' if you only want matching timestamps
#H2_elevation_inflow_loads = inflow_loads.join(H2_elevation, how='inner')  # You can use 'inner' if you only want matching timestamps
#H2_azimuth_inflow_loads = inflow_loads.join(H2_azimuth, how='inner')  # You can use 'inner' if you only want matching timestamps
#H3_elevation_inflow_loads = inflow_loads.join(H3_elevation, how='inner')  # You can use 'inner' if you only want matching timestamps
#H3_azimuth_inflow_loads = inflow_loads.join(H3_azimuth, how='inner')  # You can use 'inner' if you only want matching timestamps

#H1_elevation_inflow_lowwind_2ms_loads = H1_elevation_inflow_loads[abs(H1_elevation_inflow_loads['U_ax_Mid'])<2]
#H1_azimuth_inflow_lowwind_2ms_loads = H1_azimuth_inflow_loads[abs(H1_azimuth_inflow_loads['U_ax_Mid'])<2]
#H2_elevation_inflow_lowwind_2ms_loads = H2_elevation_inflow_loads[abs(H2_elevation_inflow_loads['U_ax_Mid'])<2]
#H2_azimuth_inflow_lowwind_2ms_loads = H2_azimuth_inflow_loads[abs(H2_azimuth_inflow_loads['U_ax_Mid'])<2]
#H3_elevation_inflow_lowwind_2ms_loads = H3_elevation_inflow_loads[abs(H3_elevation_inflow_loads['U_ax_Mid'])<2]
#H3_azimuth_inflow_lowwind_2ms_loads = H3_azimuth_inflow_loads[abs(H3_azimuth_inflow_loads['U_ax_Mid'])<2]

#H1_elevation_inflow_lowwind_3ms_loads = H1_elevation_inflow_loads[abs(H1_elevation_inflow_loads['U_ax_Mid'])<3]
#H1_azimuth_inflow_lowwind_3ms_loads = H1_azimuth_inflow_loads[abs(H1_azimuth_inflow_loads['U_ax_Mid'])<3]
#H2_elevation_inflow_lowwind_3ms_loads = H2_elevation_inflow_loads[abs(H2_elevation_inflow_loads['U_ax_Mid'])<3]
#H2_azimuth_inflow_lowwind_3ms_loads = H2_azimuth_inflow_loads[abs(H2_azimuth_inflow_loads['U_ax_Mid'])<3]
#H3_elevation_inflow_lowwind_3ms_loads = H3_elevation_inflow_loads[abs(H3_elevation_inflow_loads['U_ax_Mid'])<3]
#H3_azimuth_inflow_lowwind_3ms_loads = H3_azimuth_inflow_loads[abs(H3_azimuth_inflow_loads['U_ax_Mid'])<3]



#%% Only consider load periods after H3 online (5 October 2024)

index_loads_start = pd.Timestamp(2024,10,5,0,8)
index_loads_end = pd.Timestamp(2024,12,12,1,38)

H1_elevation_azimuth_state_inflow_loads_corr = H1_elevation_azimuth_state_inflow_loads[index_loads_start:index_loads_end]
#H1_elevation_azimuth_state_mast_loads_corr = H1_elevation_azimuth_state_mast_loads[index_loads_start:index_loads_end]
H2_elevation_azimuth_state_inflow_loads_corr = H2_elevation_azimuth_state_inflow_loads[index_loads_start:index_loads_end]
H2_elevation_azimuth_state_mast_loads_corr = H2_elevation_azimuth_state_mast_loads[index_loads_start:index_loads_end]
H3_elevation_azimuth_state_inflow_loads_corr = H3_elevation_azimuth_state_inflow_loads[index_loads_start:index_loads_end]
H3_elevation_azimuth_state_mast_loads_corr = H3_elevation_azimuth_state_mast_loads[index_loads_start:index_loads_end]

H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads[index_loads_start:index_loads_end]
H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads[index_loads_start:index_loads_end]
H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads[index_loads_start:index_loads_end]

H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right)/2




#%% Pedestal axial strain gage low wind offsets

H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Axial)<0.0005]
H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Axial)>0.0005]
H1_Pedestal_Axial_elevation_offset_mean = H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Axial.mean()

H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Axial)<0.0001]
H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Axial)>0.0001]
H2_Pedestal_Axial_elevation_offset_mean = H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Axial.mean()

H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Axial)<0.00002]
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Axial)>0.00002]
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>0.5]
H3_Pedestal_Axial_elevation_offset_mean = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Axial.mean()
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Pedestal_Axial'], 1)

bins = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Axial'].mean()
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

plt.rc('font', size=12)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Axial,marker='.')
plt.scatter(H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation,H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Axial,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H1 pedestal axial")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Axial,marker='.')
plt.scatter(H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Axial,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H2 pedestal axial")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Axial,marker='.')
plt.scatter(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Axial,marker='.')
plt.scatter(elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal axial")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")
    

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Axial,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H1 pedestal axial")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Axial,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H2 pedestal axial")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Axial,marker='.')
#plt.scatter(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Axial,marker='.')
#plt.scatter(elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'green')     
plt.plot(elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal axial")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    

bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Pedestal_Axial'].mean()
slope_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Pedestal_Axial'].mean()
slope_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Pedestal_Axial'].mean()
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Axial,marker='.')
plt.scatter(Ts_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)      
plt.title("H1 pedestal axial")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Axial,marker='.')
plt.scatter(Ts_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)      
plt.title("H2 pedestal axial") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Axial,marker='.')
plt.scatter(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 pedestal axial")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")


# Dependence on elevation angle and temp (H3 pedestal axial)
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80 = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean>80]
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80 = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean<80)&(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean>0.5)]
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0 = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean>0.5]
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0 = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean<0.5]

# Operating (elevation_05_80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['binned'] = pd.cut(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['Temp'].mean()
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['H3_Pedestal_Axial'].mean()
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, 1)

# Operating (elevationg80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['binned'] = pd.cut(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['Temp'].mean()
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['H3_Pedestal_Axial'].mean()
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, 1)

# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['binned'] = pd.cut(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['Temp'].mean()
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['H3_Pedestal_Axial'].mean()
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, 1)

# Stow (elevation0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['binned'] = pd.cut(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['Temp'].mean()
H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['H3_Pedestal_Axial'].mean()
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, 1)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.Ts_Mid,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Axial,marker='.')
plt.scatter(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.Ts_Mid,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.H3_Pedestal_Axial,marker='.')
plt.scatter(H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.Ts_Mid,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.H3_Pedestal_Axial,marker='.')
#plt.scatter(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,marker='o')
#plt.plot(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend,'black',label='oper (elev > 80)')
plt.scatter(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,marker='o')
plt.plot(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend,'black',label='oper (0.5<elev<80)')
plt.scatter(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,Ts_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 pedestal axial")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


# H3 pedestal axial time series operation low wind days 25 October 2024

# Stow period from 3-7am LT (10-14UTC)

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,10,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,25,14,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Pedestal_Axial, 1)

bins = [-1.5, -1, -0.5, 0]
labels = ['-1.5-1','-1-0.5','-0.5-0']

H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Axial'].mean()
slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Pedestal_Axial,marker='.')
plt.plot(H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(-0.00001, 0)     
plt.title("H3 pedestal axial (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()



H1_Mirror_Displacement_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_avg = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top.mean()
H2_Mirror_Displacement_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_avg = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top.mean()
H3_Mirror_Displacement_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_avg = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top.mean()

H1_Mirror_Displacement_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_avg = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom.mean()
H2_Mirror_Displacement_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_avg = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom.mean()
H3_Mirror_Displacement_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_avg = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom.mean()

H1_elevation_azimuth_state_inflow_loads["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads.H3_Elevation_Right)/2



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top,marker='.')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'],H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top,marker='.')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top,marker='.')

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom,marker='.')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'],H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom,marker='.')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom,marker='.')



#%% Pedestal torque strain gage low wind offsets

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Torque)<0.00005]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Torque)>0.00005]
H1_Pedestal_Torque_elevation_offset_mean = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Torque.mean()

H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Torque)<0.0000005]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Torque)>0.0000005]
H2_Pedestal_Torque_elevation_offset_mean = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Torque.mean()

H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Torque)<0.00005]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Torque)>0.00005]
H3_Pedestal_Torque_elevation_offset_mean = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Torque.mean()


# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,5,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,5,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right)/2


H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Torque)<0.00001]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Torque)>0.00001]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>0.5)&(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<80)]
#H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>0.5]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<0.5]
H1_Pedestal_Torque_elevation_offset_mean = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Torque.mean()

bins = [5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
labels = ['5-10','10-15','15-20','20-25','25-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Torque)<0.00001]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Torque)>0.00001]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5)&(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<80)]
#H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<0.5]
H2_Pedestal_Torque_elevation_offset_mean = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Torque.mean()

bins = [5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
labels = ['5-10','10-15','15-20','20-25','25-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80']

H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Pedestal_Torque'].mean()
slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Torque)<0.00005]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Torque)>0.00005]
#H3_Pedestal_Torque_elevation_offset_mean = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Torque.mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>50)&(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<60)]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>0.5]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<0.5]
H3_Pedestal_Torque_elevation_offset_mean = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Torque.mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Pedestal_Torque'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Torque'].mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_Pedestal_Torque,marker='.')
#plt.scatter(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Torque,marker='.')
#plt.scatter(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H1 pedestal torque")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Torque,marker='.')
#plt.scatter(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Torque,marker='.')
#plt.scatter(elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H2 pedestal torque")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Torque,marker='.')
#plt.scatter(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Torque,marker='.')
#plt.scatter(elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal torque")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Torque,marker='.')
#plt.scatter(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Torque,marker='.')
#plt.scatter(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H1 pedestal torque")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Torque,marker='.')
plt.plot(elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H2 pedestal torque")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Torque,marker='.')
#plt.scatter(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Torque,marker='.')
plt.scatter(elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'red')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal torque")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")






# Operating (elevationg0)
bins_Ts = [0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Pedestal_Torque'].mean()
slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Torque'].mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


# Stow (elevation0)
bins_Ts = [-5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H2_Pedestal_Torque'].mean()
slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H3_Pedestal_Torque'].mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Torque,marker='.')
plt.scatter(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H1 pedestal torque")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Torque,marker='.')
plt.scatter(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H2 pedestal torque") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Torque,marker='.')
plt.scatter(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper (elev > 0.5)')
plt.scatter(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 pedestal torque")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()





#%% Pedestal torque strain gage low wind offsets

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Torque)<0.00005]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Torque)>0.00005]
#H1_Pedestal_Torque_elevation_offset_mean = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Torque.mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>50)&(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<60)]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>0.5]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<0.5]
H1_Pedestal_Torque_elevation_offset_mean = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Torque.mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_elevation'], H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Pedestal_Torque'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

# Dependence on elevation angle and temp (H1 Pedestal torque)
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>80]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<80)&(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5)]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5]
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<0.5]

# Operating (elevation_05_80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['Temp'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, 1)

# Operating (elevationg80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['Temp'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, 1)

# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['Temp'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, 1)

# Stow (elevation0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['Temp'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, 1)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.Ts_Mid,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Torque,marker='.')
plt.scatter(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.Ts_Mid,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.H1_Pedestal_Torque,marker='.')
plt.scatter(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.Ts_Mid,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.H1_Pedestal_Torque,marker='.')
plt.scatter(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend,'black',label='oper (elev > 80)')
plt.scatter(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend,'black',label='oper (0.5<elev<80)')
plt.scatter(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H1 Pedestal torque")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


# H1 Pedestal torque time series operation low wind days 25 October 2024

# Stow period from 3-7am LT (10-14UTC)

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,10,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,25,14,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Pedestal_Torque, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Pedestal_Torque,marker='.')
plt.plot(H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H1 Pedestal torque (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()



#%% H3 Pedestal torque time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']


H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Torque'].mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Pedestal_Torque'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Pedestal_Torque, 1)
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Pedestal_Torque, 1)

slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)



H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>0]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Pedestal_Torque'].mean()
slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>65]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Pedestal_Torque'].mean()

H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Pedestal_Torque, 1)
slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Pedestal_Torque, 1)


plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right)/2


H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Torque)<0.00001]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Torque)>0.00001]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5)&(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<80)]
#H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5]
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<0.5]
H2_Pedestal_Torque_elevation_offset_mean = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Torque.mean()

bins = [5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
labels = ['5-10','10-15','15-20','20-25','25-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80']

H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Pedestal_Torque'].mean()
slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Torque)<0.00005]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Torque)>0.00005]
#H3_Pedestal_Torque_elevation_offset_mean = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Torque.mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>50)&(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<60)]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>0.5]
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<0.5]
H3_Pedestal_Torque_elevation_offset_mean = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Torque.mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Pedestal_Torque'], 1)



bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Torque'].mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)




# Operating (elevationg0)
bins_Ts = [0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Pedestal_Torque'].mean()
slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Torque'].mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


# Stow (elevation0)
bins_Ts = [-5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H1_Pedestal_Torque'].mean()
slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H2_Pedestal_Torque'].mean()
slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H3_Pedestal_Torque'].mean()
slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Torque,marker='.')
plt.scatter(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H1 Pedestal torque")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Torque,marker='.')
plt.scatter(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H2 Pedestal torque") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Torque,marker='.')
plt.scatter(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper (elev > 0.5)')
plt.scatter(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 Pedestal torque")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()





    

#%% Torque tube left strain gage low wind offsets

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Torque_Tube_Left)<0.00005]
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Torque_Tube_Left)>0.00005]
#H1_Torque_Tube_Left_elevation_offset_mean = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Torque_Tube_Left.mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>50)&(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<60)]
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>0.5]
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<0.5]
H1_Torque_Tube_Left_elevation_offset_mean = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Torque_Tube_Left.mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_elevation'], H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Torque_Tube_Left'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Torque_Tube_Left'].mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

# Dependence on elevation angle and temp (H1 torque tube left)
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>80]
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<80)&(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5)]
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5]
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<0.5]

# Operating (elevation_05_80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['binned'] = pd.cut(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['Temp'].mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['H1_Torque_Tube_Left'].mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, 1)

# Operating (elevationg80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25']

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['binned'] = pd.cut(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['Temp'].mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['H1_Torque_Tube_Left'].mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, 1)

# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['binned'] = pd.cut(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['Temp'].mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['H1_Torque_Tube_Left'].mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, 1)

# Stow (elevation0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['binned'] = pd.cut(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['Temp'].mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['H1_Torque_Tube_Left'].mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, 1)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.Ts_Mid,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Torque_Tube_Left,marker='.')
plt.scatter(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.Ts_Mid,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.H1_Torque_Tube_Left,marker='.')
plt.scatter(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.Ts_Mid,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.H1_Torque_Tube_Left,marker='.')
plt.scatter(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,marker='o')
plt.plot(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend,'black',label='oper (elev > 80)')
plt.scatter(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,marker='o')
plt.plot(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend,'black',label='oper (0.5<elev<80)')
plt.scatter(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,marker='o')
plt.plot(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H1 torque tube left")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


# H1 torque tube left time series operation low wind days 25 October 2024

# Stow period from 3-7am LT (10-14UTC)

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,10,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,25,14,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Torque_Tube_Left, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Torque_Tube_Left'].mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Torque_Tube_Left,marker='.')
plt.plot(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H1 torque tube left (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()



#%% H3 torque tube left time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']


H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Torque_Tube_Left'].mean()
slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Torque_Tube_Left'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Torque_Tube_Left, 1)
slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Torque_Tube_Left, 1)

slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)



H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>0]
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Torque_Tube_Left'].mean()
slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>65]
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Torque_Tube_Left'].mean()

H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Torque_Tube_Left, 1)
slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Torque_Tube_Left, 1)


plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right)/2


H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>5]
H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>5]
H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>5]

H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>5]
H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>5]
H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>5]

slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp, H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top, 1)
slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp, H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top, 1)
slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp, H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top, 1)

slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp, H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom, 1)
slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp, H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom, 1)
slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp, H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom, 1)

plt.figure()
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"])

plt.figure()
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"])



plt.figure()
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top,label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top,label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top,label='H3')
plt.title("Mirror displacement top (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("D (mm)")
plt.legend()

plt.figure()
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom,label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom,label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom,label='H3')
plt.title("Mirror displacement bottom (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("D (mm)")
plt.legend()

plt.figure()
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top,label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top,label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top,label='H3')
plt.plot(H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp+intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'red')
plt.plot(H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp+intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'purple')
plt.plot(H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp+intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black')
plt.title("Mirror displacement top operation (25 Oct 2024)")   
plt.xlabel("Temp ($^\circ C$)")
plt.ylabel("D (mm)")
plt.legend()

plt.figure()
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom,label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom,label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom,label='H3')
plt.plot(H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp+intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'red')
plt.plot(H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp+intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'purple')
plt.plot(H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp+intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black')
plt.title("Mirror displacement bottom operation (25 Oct 2024)")   
plt.xlabel("Temp ($^\circ C$)")
plt.ylabel("D (mm)")
plt.legend()


# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,5,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,5,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right)/2

H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean<5]
H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean<5]
H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean<5]

H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean<5]
H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean<5]
H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean<5]

slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend, intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend = np.polyfit(H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp, H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H1_Mirror_Displacement_Top, 1)
slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend, intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend = np.polyfit(H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp, H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H2_Mirror_Displacement_Top, 1)
slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend, intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend = np.polyfit(H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp, H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H3_Mirror_Displacement_Top, 1)

slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend, intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend = np.polyfit(H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp, H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H1_Mirror_Displacement_Bottom, 1)
slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend, intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend = np.polyfit(H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp, H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H2_Mirror_Displacement_Bottom, 1)
slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend, intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend = np.polyfit(H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp, H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H3_Mirror_Displacement_Bottom, 1)


plt.figure()
plt.scatter(H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H1_Mirror_Displacement_Top,label='H1')
plt.scatter(H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H2_Mirror_Displacement_Top,label='H2')
plt.scatter(H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H3_Mirror_Displacement_Top,label='H3')
plt.plot(H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp+intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend,'red')
plt.plot(H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp+intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend,'purple')
plt.plot(H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp+intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend,'black')
plt.title("Mirror displacement top stow (25 Oct 2024)")   
plt.xlabel("Temp ($^\circ C$)")
plt.ylabel("D (mm)")
plt.legend()

plt.figure()
plt.scatter(H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H1_Mirror_Displacement_Bottom,label='H1')
plt.scatter(H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H2_Mirror_Displacement_Bottom,label='H2')
plt.scatter(H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.H3_Mirror_Displacement_Bottom,label='H3')
plt.plot(H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp+intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend,'red')
plt.plot(H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp+intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend,'purple')
plt.plot(H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp,slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025.Temp+intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend,'black')
plt.title("Mirror displacement bottom stow (25 Oct 2024)")   
plt.xlabel("Temp ($^\circ C$)")
plt.ylabel("D (mm)")
plt.legend()


H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Torque_Tube_Left)<0.00001]
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Torque_Tube_Left)>0.00001]
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5)&(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<80)]
#H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5]
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<0.5]
H2_Torque_Tube_Left_elevation_offset_mean = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Torque_Tube_Left.mean()

bins = [5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
labels = ['5-10','10-15','15-20','20-25','25-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80']

H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Elevation_mean'].mean()
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Torque_Tube_Left'].mean()
slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Torque_Tube_Left)<0.00005]
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Torque_Tube_Left)>0.00005]
#H3_Torque_Tube_Left_elevation_offset_mean = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Torque_Tube_Left.mean()
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>50)&(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<60)]
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>0.5]
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<0.5]
H3_Torque_Tube_Left_elevation_offset_mean = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Torque_Tube_Left.mean()
slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Torque_Tube_Left'], 1)



bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Torque_Tube_Left'].mean()
slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)




# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Torque_Tube_Left'].mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Torque_Tube_Left'].mean()
slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Torque_Tube_Left'].mean()
slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


# Stow (elevation0)
bins_Ts = [-5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H1_Torque_Tube_Left'].mean()
slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H2_Torque_Tube_Left'].mean()
slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H3_Torque_Tube_Left'].mean()
slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Torque_Tube_Left,marker='.')
plt.scatter(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H1 torque tube left")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Torque_Tube_Left,marker='.')
plt.scatter(Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H2 torque tube left") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Torque_Tube_Left,marker='.')
plt.scatter(Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper (elev > 0.5)')
plt.scatter(Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 torque tube left")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


#%%

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_Torque_Tube_Left,marker='.')
plt.scatter(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H1 torque tube left")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Torque_Tube_Left,marker='.')
plt.scatter(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation,H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation*slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H2 torque tube left")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Torque_Tube_Left,marker='.')
plt.scatter(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 torque tube left")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Torque_Tube_Left,marker='.')
#plt.scatter(H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H1 torque tube left")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Torque_Tube_Left,marker='.')
plt.plot(elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean*slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean*slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H2 torque tube left")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Torque_Tube_Left,marker='.')
#plt.scatter(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'red')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 torque tube left")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")


#%% Time series operation vs wind speed and elevation angles

import datetime

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr.index,H1_elevation_azimuth_state_inflow_loads_corr.H1_elevation,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr.index,H2_elevation_azimuth_state_inflow_loads_corr.H2_elevation,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr.index,H3_elevation_azimuth_state_inflow_loads_corr.H3_elevation,marker='.',label='H3')
plt.ylim(-10, 90)  
plt.yticks([0,15,30,45,60,75,90])
plt.title("Elevation angles SCADA H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,0,0), datetime.datetime(2024,11,3,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 
ax2 = ax1.twinx()
ax2.plot(H1_elevation_azimuth_state_inflow_loads_corr.index,H1_elevation_azimuth_state_inflow_loads_corr.U_ax_Mid, color='red')
ax2.set_ylabel('Inflow 5.5m wind speed (m/s)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(-10, 30)    
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,0,0), datetime.datetime(2024,11,3,0,0)])
plt.tight_layout()

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr.index,H1_elevation_azimuth_state_inflow_loads_corr.H1_Elevation_mean,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr.index,H2_elevation_azimuth_state_inflow_loads_corr.H2_Elevation_mean,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr.index,H3_elevation_azimuth_state_inflow_loads_corr.H3_Elevation_mean,marker='.',label='H3')
plt.ylim(-10, 90)  
plt.yticks([0,15,30,45,60,75,90])
plt.title("Elevation angles meas H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,0,0), datetime.datetime(2024,11,3,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 
ax2 = ax1.twinx()
ax2.plot(H1_elevation_azimuth_state_inflow_loads_corr.index,H1_elevation_azimuth_state_inflow_loads_corr.U_ax_Mid, color='red')
ax2.set_ylabel('Inflow 5.5m wind speed (m/s)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(-10, 30)    
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,0,0), datetime.datetime(2024,11,3,0,0)])
plt.tight_layout()



#%% Variation in offset on different low-wind days

index_lowwind_oper2_corr_start = pd.Timestamp(2024,10,26,12,0)
index_lowwind_oper2_corr_end = pd.Timestamp(2024,10,27,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper2_corr_start:index_lowwind_oper2_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper2_corr_start:index_lowwind_oper2_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper2_corr_start:index_lowwind_oper2_corr_end]

#H1_Torque_Tube_Left_elevation_azimuth_state_inflow_operation_20241026 = H1_Torque_Tube_Left_elevation_azimuth_state_inflow[index_lowwind_oper2_corr_start:index_lowwind_oper2_corr_end]
#H2_Torque_Tube_Left_elevation_azimuth_state_inflow_operation_20241026 = H2_Torque_Tube_Left_elevation_azimuth_state_inflow[index_lowwind_oper2_corr_start:index_lowwind_oper2_corr_end]
#H3_Torque_Tube_Left_elevation_azimuth_state_inflow_operation_20241026 = H3_Torque_Tube_Left_elevation_azimuth_state_inflow[index_lowwind_oper2_corr_start:index_lowwind_oper2_corr_end]


import datetime

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_elevation,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_elevation,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_elevation,marker='.',label='H3')
plt.ylim(-10, 90)  
plt.yticks([0,15,30,45,60,75,90])
plt.title("Elevation angles SCADA H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 


fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,-1*H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left,marker='.',label='H1 left')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,-1*H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left,marker='.',label='H2 left')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,-1*H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left,marker='.',label='H3 left')
plt.ylim(-10, 90)
plt.yticks([0,15,30,45,60,75,90])  
plt.title("Elevation angles meas H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle left ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 


fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,marker='.',label='H3')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.Temp,marker='.',color='red',label='temp')
plt.ylim(-10, 90)
plt.yticks([0,15,30,45,60,75,90])  
plt.title("Elevation angles meas H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle (left+right)/2 ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 

fig = plt.figure()
ax1 = fig.add_subplot(111)
#plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left,marker='.',label='H1 left')
#plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left,marker='.',label='H2 left')
#plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left,marker='.',label='H3 left')
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,-1*H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right,marker='.',label='H1 right')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,-1*H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right,marker='.',label='H2 right')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,-1*H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right,marker='.',label='H3 right')
#plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_elevation,marker='.',color='#1f77b4',label='H1 right',alpha=0.5)
#plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_elevation,marker='.',color='#ff7f0e',label='H2 right',alpha=0.5)
#plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_elevation,marker='.',color='#2ca02c',label='H3 right',alpha=0.5)
plt.ylim(-10, 90)
plt.yticks([0,15,30,45,60,75,90])  
plt.title("Elevation angles meas H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle right ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,-1*H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H1_elevation,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,-1*H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H2_elevation,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,-1*H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_elevation,marker='.',label='H3')
plt.ylim(-10, 90)  
plt.yticks([0,15,30,45,60,75,90])
plt.title("Elevation angles SCADA H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,26,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 


fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,-1*H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H1_Elevation_Left,marker='.',label='H1 left')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,-1*H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H2_Elevation_Left,marker='.',label='H2 left')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,-1*H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Elevation_Left,marker='.',label='H3 left')
plt.ylim(-10, 90)
plt.yticks([0,15,30,45,60,75,90])  
plt.title("Elevation angles meas H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle left ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,26,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 

fig = plt.figure()
ax1 = fig.add_subplot(111)
#plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H1_Elevation_Left,marker='.',label='H1 left')
#plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H2_Elevation_Left,marker='.',label='H2 left')
#plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Elevation_Left,marker='.',label='H3 left')
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H1_elevation,marker='.',label='H1 right')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H2_elevation,marker='.',label='H2 right')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_elevation,marker='.',label='H3 right')
#plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H1_elevation,marker='.',color='#1f77b4',label='H1 right',alpha=0.5)
#plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H2_elevation,marker='.',color='#ff7f0e',label='H2 right',alpha=0.5)
#plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_elevation,marker='.',color='#2ca02c',label='H3 right',alpha=0.5)
plt.ylim(-10, 90)
plt.yticks([0,15,30,45,60,75,90])  
plt.title("Elevation angles meas H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.xlabel("Elevation angle right ($^\circ$)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,26,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 


fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Torque_Tube_Left,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Torque_Tube_Left,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Torque_Tube_Left,marker='.',label='H3')
plt.ylim(-0.0003, 0.0003)  
plt.title("Torque tube left H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.ylabel("Low wind offset (V/V)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 
ax2 = ax1.twinx()
ax2.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.U_ax_Mid, color='red')
ax2.set_ylabel('Inflow 5.5m wind speed (m/s)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(-10, 30)    
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H1_Torque_Tube_Left,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H2_Torque_Tube_Left,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Torque_Tube_Left,marker='.',label='H3')
plt.ylim(-0.0003, 0.0003)  
plt.title("Torque tube left H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.ylabel("Low wind offset (V/V)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,26,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 
ax2 = ax1.twinx()
ax2.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.U_ax_Mid, color='red')
ax2.set_ylabel('Inflow 5.5m wind speed (m/s)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(-10, 30)    
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,26,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()


fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Pedestal_Bend_1,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Pedestal_Bend_1,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Pedestal_Bend_1,marker='.',label='H3')
plt.ylim(-0.0003, 0.0003)  
plt.title("Pedestal bending 1 H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.ylabel("Low wind offset (V/V)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 
ax2 = ax1.twinx()
ax2.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.U_ax_Mid, color='red')
ax2.set_ylabel('Inflow 5.5m wind speed (m/s)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(-10, 30)    
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,25,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()

fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H1_Pedestal_Bend_1,marker='.',label='H1')
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H2_Pedestal_Bend_1,marker='.',label='H2')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Pedestal_Bend_1,marker='.',label='H3')
plt.ylim(-0.0003, 0.0003)  
plt.title("Pedestal bending 1 H1 H2 H3")    
plt.xlabel("Date Time UTC")
plt.ylabel("Low wind offset (V/V)")
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,26,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()
plt.legend(loc='lower right',fontsize=10) 
ax2 = ax1.twinx()
ax2.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.index,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.U_ax_Mid, color='red')
ax2.set_ylabel('Inflow 5.5m wind speed (m/s)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.set_ylim(-10, 30)    
fig.autofmt_xdate()
ax1.set_xlim([datetime.datetime(2024,10,26,12,0), datetime.datetime(2024,10,27,0,0)])
plt.tight_layout()




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_elevation,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Torque_Tube_Left,marker='.')
#plt.scatter(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 torque tube left (25 Oct 2024)")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Torque_Tube_Left,marker='.')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Torque_Tube_Left[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)],marker='.')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean[pd.Timestamp(2024,10,25,22,52):pd.Timestamp(2024,10,26,0,0)],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Torque_Tube_Left[pd.Timestamp(2024,10,25,22,52):pd.Timestamp(2024,10,26,0,0)],marker='.')
plt.scatter(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg,marker='o')     
#plt.scatter(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0, 0.0003)      
plt.title("H3 torque tube left (25 Oct 2024)")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_elevation,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Torque_Tube_Left,marker='.')
#plt.scatter(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 torque tube left (26 Oct 2024)")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Torque_Tube_Left,marker='.')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Elevation_mean[pd.Timestamp(2024,10,26,12,0):pd.Timestamp(2024,10,26,14,17)],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Torque_Tube_Left[pd.Timestamp(2024,10,26,12,0):pd.Timestamp(2024,10,26,14,17)],marker='.')
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Elevation_mean[pd.Timestamp(2024,10,26,22,47):pd.Timestamp(2024,10,27,0,0)],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241026.H3_Torque_Tube_Left[pd.Timestamp(2024,10,26,22,47):pd.Timestamp(2024,10,27,0,0)],marker='.')
plt.scatter(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg,marker='o')     
#plt.scatter(H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Torque_Tube_Left,marker='.')
#plt.scatter(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
plt.xlim(60, 90)     
plt.xticks([60,65,70,75,80,85,90])
plt.ylim(0, 0.0003)    
plt.title("H3 torque tube left (26 Oct 2024)")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")



#%% Torque tube right strain gage low wind offsets

H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Torque_Tube_Right)<0.0001]
H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Torque_Tube_Right)>0.0001]
H1_Torque_Tube_Right_elevation_offset_mean = H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Torque_Tube_Right.mean()

H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Torque_Tube_Right)<0.0001]
H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Torque_Tube_Right)>0.0001]
H2_Torque_Tube_Right_elevation_offset_mean = H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Torque_Tube_Right.mean()

H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Torque_Tube_Right)<0.0001]
H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Torque_Tube_Right)>0.0001]
H3_Torque_Tube_Right_elevation_offset_mean = H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Torque_Tube_Right.mean()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Torque_Tube_Right,marker='.')
plt.scatter(H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation,H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Torque_Tube_Right,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H1 torque tube right")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Torque_Tube_Right,marker='.')
plt.scatter(H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Torque_Tube_Right,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.03, 0.03)    
plt.title("H2 torque tube right")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Torque_Tube_Right,marker='.')
plt.scatter(H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation,H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Torque_Tube_Right,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H3 torque tube right")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")
    

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Torque_Tube_Right,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H1 torque tube right")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Torque_Tube_Right,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H2 torque tube right")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left),H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Torque_Tube_Right,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H3 torque tube right")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    

bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Torque_Tube_Right'].mean()
slope_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Torque_Tube_Right'].mean()
slope_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Torque_Tube_Right'].mean()
slope_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Torque_Tube_Right,marker='.')
plt.scatter(Ts_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)       
plt.title("H1 torque tube right")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Torque_Tube_Right,marker='.')
plt.scatter(Ts_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)       
plt.title("H2 torque tube right") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Torque_Tube_Right,marker='.')
plt.scatter(Ts_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Torque_Tube_Right_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)     
plt.title("H3 torque tube right")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")




# H1 H2 H3 Pedestal bending 1 time series operation low wind days 25 October 2024

# Stow period from 3-7am LT (10-14UTC)

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,10,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,25,14,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Pedestal_Bend_1, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Pedestal_Bend_1,marker='.')
plt.plot(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H1 Pedestal bending 1 (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Pedestal_Bend_1, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Pedestal_Bend_1'].mean()
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Pedestal_Bend_1'].mean()
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'],H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Pedestal_Bend_1,marker='.')
plt.plot(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H2 Pedestal bending 1 (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Pedestal_Bend_1, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Pedestal_Bend_1,marker='.')
plt.plot(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H3 Pedestal bending 1 (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()




#%% H1 and H3 pedestal bending 1 time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]


bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>0]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>65]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H1_Pedestal_Bend_1'].mean()

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Elevation_mean, H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Pedestal_Bend_1, 1)
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Elevation_mean, H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Pedestal_Bend_1, 1)

slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Pedestal_Bend_1'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Pedestal_Bend_1, 1)
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Pedestal_Bend_1, 1)

slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)





    
#%% Pedestal bending 1 strain gage low wind offsets

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1)<0.00005]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1)>0.00005]
#H1_Pedestal_Bend_1_elevation_offset_mean = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_1.mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation>0.5]
H1_Pedestal_Bend_1_elevation_offset_mean = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_1.mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_elevation'], H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Pedestal_Bend_1'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1)<0.0005]
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1)>0.0005]
H2_Pedestal_Bend_1_elevation_offset_mean = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_1.mean()

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1)<0.00005]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1)>0.00005]
#H3_Pedestal_Bend_1_elevation_offset_mean = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_1.mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation>0.5]
H3_Pedestal_Bend_1_elevation_offset_mean = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_1.mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Pedestal_Bend_1'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_Pedestal_Bend_1,marker='.')
plt.scatter(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_1,marker='.')
plt.scatter(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H1 pedestal bending 1")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1,marker='.')
plt.scatter(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_1,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H2 pedestal bending 1")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1,marker='.')
plt.scatter(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_1,marker='.')
plt.scatter(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal bending 1")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1,marker='.')
#plt.scatter(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_1,marker='.')
#plt.scatter(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Elevation_mean,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Elevation_mean*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Elevation_mean,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Elevation_mean*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H1 pedestal bending 1")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H2 pedestal bending 1")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left),H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1,marker='.')
#plt.scatter(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_1,marker='.')
#plt.scatter(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal bending 1")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    

bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Pedestal_Bend_1'].mean()
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_1,marker='.')
plt.scatter(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H1 pedestal bending 1")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_1,marker='.')
plt.scatter(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)       
plt.title("H2 pedestal bending 1") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_1,marker='.')
plt.scatter(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 pedestal bending 1")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")


#%% Pedestal bending 1 strain gage low wind offsets


H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1)<0.00005]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1)>0.00005]
#H1_Pedestal_Bend_1_elevation_offset_mean = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_1.mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation>0.5]
H1_Pedestal_Bend_1_elevation_offset_mean = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_1.mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_elevation'], H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Pedestal_Bend_1'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1)<0.0005]
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1)>0.0005]
H2_Pedestal_Bend_1_elevation_offset_mean = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_1.mean()

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1)<0.00005]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1)>0.00005]
#H3_Pedestal_Bend_1_elevation_offset_mean = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_1.mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation>0.5]
H3_Pedestal_Bend_1_elevation_offset_mean = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_1.mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Pedestal_Bend_1'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1)<0.00005]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1)>0.00005]
#H1_Pedestal_Bend_1_elevation_offset_mean = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_1.mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>50)&(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<60)]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>0.5]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<0.5]
H1_Pedestal_Bend_1_elevation_offset_mean = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_1.mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_elevation'], H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Pedestal_Bend_1'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

# Dependence on elevation angle and temp (H1 Pedestal bending 1)
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>80]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<80)&(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5)]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5]
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<0.5]

# Operating (elevation_05_80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, 1)

# Operating (elevationg80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, 1)

# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, 1)

# Stow (elevation0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, 1)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.Ts_Mid,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1,marker='.')
plt.scatter(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.Ts_Mid,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.H1_Pedestal_Bend_1,marker='.')
plt.scatter(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.Ts_Mid,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.H1_Pedestal_Bend_1,marker='.')
plt.scatter(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend,'black',label='oper (elev > 80)')
plt.scatter(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend,'black',label='oper (0.5<elev<80)')
plt.scatter(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H1 Pedestal bending 1")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()



#%% H3 Pedestal bending 1 time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']


H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Pedestal_Bend_1'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Pedestal_Bend_1, 1)
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Pedestal_Bend_1, 1)

slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)



H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>0]
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Pedestal_Bend_1'].mean()
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>65]
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Pedestal_Bend_1'].mean()

H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Pedestal_Bend_1, 1)
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Pedestal_Bend_1, 1)


plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right)/2


H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1)<0.00001]
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1)>0.00001]
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5)&(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<80)]
#H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5]
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<0.5]
H2_Pedestal_Bend_1_elevation_offset_mean = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_1.mean()

bins = [5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
labels = ['5-10','10-15','15-20','20-25','25-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80']

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Pedestal_Bend_1'].mean()
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1)<0.00005]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1)>0.00005]
#H3_Pedestal_Bend_1_elevation_offset_mean = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_1.mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>50)&(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<60)]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>0.5]
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<0.5]
H3_Pedestal_Bend_1_elevation_offset_mean = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_1.mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Pedestal_Bend_1'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_Pedestal_Bend_1,marker='.')
plt.scatter(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_1,marker='.')
plt.scatter(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H1 pedestal bending 1")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1,marker='.')
plt.scatter(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_1,marker='.')
plt.scatter(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H2 pedestal bending 1")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1,marker='.')
plt.scatter(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_1,marker='.')
plt.scatter(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal bending 1")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_1,marker='.')
#plt.scatter(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_1,marker='.')
#plt.scatter(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H1 pedestal bending 1")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_1,marker='.')
plt.plot(elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H2 pedestal bending 1")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_1,marker='.')
#plt.scatter(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_1,marker='.')
#plt.scatter(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'red')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal bending 1")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")





# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Pedestal_Bend_1'].mean()
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


# Stow (elevation0)
bins_Ts = [-5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H1_Pedestal_Bend_1'].mean()
slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H2_Pedestal_Bend_1'].mean()
slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H3_Pedestal_Bend_1'].mean()
slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_1,marker='.')
plt.scatter(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H1 Pedestal bending 1")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_1,marker='.')
plt.scatter(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)       
plt.title("H2 Pedestal bending 1") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_1,marker='.')
plt.scatter(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper (elev > 0.5)')
plt.scatter(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 Pedestal bending 1")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


#%% H1 and H3 pedestal bending 2 time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]


bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>0]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Bend_2'].mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>65]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H1_Pedestal_Bend_2'].mean()

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Elevation_mean, H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Pedestal_Bend_2, 1)
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Elevation_mean, H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Pedestal_Bend_2, 1)

slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Pedestal_Bend_2'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Pedestal_Bend_2, 1)
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Pedestal_Bend_2, 1)

slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)


#%% Pedestal bending 2 strain gage low wind offsets




H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_2)<0.00005]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_2)>0.00005]
#H1_Pedestal_Bend_2_elevation_offset_mean = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_2.mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>50)&(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<60)]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>0.5]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<0.5]
H1_Pedestal_Bend_2_elevation_offset_mean = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_2.mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_elevation'], H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Pedestal_Bend_2'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

# Dependence on elevation angle and temp (H1 Pedestal bending 2)
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>80]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<80)&(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5)]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<0.5]

# Operating (elevation_05_80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, 1)

# Operating (elevationg80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, 1)

# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, 1)

# Stow (elevation0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, 1)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.Ts_Mid,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_2,marker='.')
plt.scatter(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.Ts_Mid,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.H1_Pedestal_Bend_2,marker='.')
plt.scatter(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.Ts_Mid,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.H1_Pedestal_Bend_2,marker='.')
plt.scatter(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend,'black',label='oper (elev > 80)')
plt.scatter(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend,'black',label='oper (0.5<elev<80)')
plt.scatter(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H1 Pedestal bending 2")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


# H1 H2 H3 Pedestal bending 2 time series operation low wind days 25 October 2024

# Stow period from 3-7am LT (10-14UTC)

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,10,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,25,14,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Pedestal_Bend_2, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Pedestal_Bend_2,marker='.')
plt.plot(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H1 Pedestal bending 2 (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Pedestal_Bend_2, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Pedestal_Bend_2'].mean()
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Pedestal_Bend_2'].mean()
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'],H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Pedestal_Bend_2,marker='.')
plt.plot(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H2 Pedestal bending 2 (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Pedestal_Bend_2, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Bend_2'].mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Bend_2'].mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Pedestal_Bend_2,marker='.')
plt.plot(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H3 Pedestal bending 2 (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


#%% H3 Pedestal bending 2 time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']


H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Pedestal_Bend_2'].mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Pedestal_Bend_2'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Pedestal_Bend_2, 1)
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Pedestal_Bend_2, 1)

slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)



H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>0]
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Pedestal_Bend_2'].mean()
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>65]
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Pedestal_Bend_2'].mean()

H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Pedestal_Bend_2, 1)
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Pedestal_Bend_2, 1)


plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right)/2


H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_2)<0.00001]
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_2)>0.00001]
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5)&(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<80)]
#H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5]
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<0.5]
H2_Pedestal_Bend_2_elevation_offset_mean = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_2.mean()

bins = [5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
labels = ['5-10','10-15','15-20','20-25','25-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80']

H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Elevation_mean'].mean()
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Pedestal_Bend_2'].mean()
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_2)<0.00005]
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_2)>0.00005]
#H3_Pedestal_Bend_2_elevation_offset_mean = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_2.mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>50)&(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<60)]
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>0.5]
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<0.5]
H3_Pedestal_Bend_2_elevation_offset_mean = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_2.mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Pedestal_Bend_2'], 1)



bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Bend_2'].mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_Pedestal_Bend_2,marker='.')
plt.scatter(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_2,marker='.')
plt.scatter(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.001, 0)    
plt.title("H1 pedestal bending 2")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_2,marker='.')
plt.scatter(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_2,marker='.')
plt.scatter(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H2 pedestal bending 2")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_2,marker='.')
plt.scatter(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_2,marker='.')
plt.scatter(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal bending 2")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_2,marker='.')
#plt.scatter(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Pedestal_Bend_2,marker='.')
#plt.scatter(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.001, 0)    
plt.title("H1 pedestal bending 2")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_2,marker='.')
plt.plot(elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H2 pedestal bending 2")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_2,marker='.')
#plt.scatter(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Pedestal_Bend_2,marker='.')
#plt.scatter(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'red')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal bending 2")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")






# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Pedestal_Bend_2'].mean()
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Pedestal_Bend_2'].mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


# Stow (elevation0)
bins_Ts = [-5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H2_Pedestal_Bend_2'].mean()
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H3_Pedestal_Bend_2'].mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_2,marker='.')
plt.scatter(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.001, 0)       
plt.title("H1 Pedestal bending 2")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_2,marker='.')
plt.scatter(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)       
plt.title("H2 Pedestal bending 2") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_2,marker='.')
plt.scatter(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper (elev > 0.5)')
plt.scatter(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 Pedestal bending 2")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


#%% H1 and H3 Support frame bending top time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]


bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>0]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>65]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Elevation_mean, H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Support_Frame_Bending_Top, 1)
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Elevation_mean, H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Support_Frame_Bending_Top, 1)

slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Support_Frame_Bending_Top, 1)
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Support_Frame_Bending_Top, 1)

slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)


#%% Support frame bending top strain gage low wind offsets

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Top)<0.00005]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Top)>0.00005]
#H1_Support_Frame_Bending_Top_elevation_offset_mean = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Top.mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>50)&(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<60)]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>0.5]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<0.5]
H1_Support_Frame_Bending_Top_elevation_offset_mean = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Support_Frame_Bending_Top.mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_elevation'], H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Support_Frame_Bending_Top'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

# Dependence on elevation angle and temp (H1 Support frame bending top)
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>80]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<80)&(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5)]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<0.5]

# Operating (elevation_05_80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, 1)

# Operating (elevationg80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, 1)

# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, 1)

# Stow (elevation0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, 1)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.Ts_Mid,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Top,marker='.')
plt.scatter(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.Ts_Mid,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.H1_Support_Frame_Bending_Top,marker='.')
plt.scatter(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.Ts_Mid,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.H1_Support_Frame_Bending_Top,marker='.')
plt.scatter(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend,'black',label='oper (elev > 80)')
plt.scatter(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend,'black',label='oper (0.5<elev<80)')
plt.scatter(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H1 Support frame bending top")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


# H1 H2 H3 Support frame bending top time series operation low wind days 25 October 2024

# Stow period from 3-7am LT (10-14UTC)

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,10,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,25,14,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Support_Frame_Bending_Top, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Support_Frame_Bending_Top,marker='.')
plt.plot(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H1 Support frame bending top (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Support_Frame_Bending_Top, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Support_Frame_Bending_Top'].mean()
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Support_Frame_Bending_Top'].mean()
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'],H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Support_Frame_Bending_Top,marker='.')
plt.plot(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H2 Support frame bending top (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Support_Frame_Bending_Top, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Support_Frame_Bending_Top,marker='.')
plt.plot(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H3 Support frame bending top (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


#%% H3 Support frame bending top time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']


H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Support_Frame_Bending_Top, 1)
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Support_Frame_Bending_Top, 1)

slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)



H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>0]
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Support_Frame_Bending_Top'].mean()
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>65]
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Support_Frame_Bending_Top'].mean()

H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Support_Frame_Bending_Top, 1)
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Support_Frame_Bending_Top, 1)


plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right)/2


H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Top)<0.00001]
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Top)>0.00001]
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5)&(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<80)]
#H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5]
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<0.5]
H2_Support_Frame_Bending_Top_elevation_offset_mean = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Top.mean()

bins = [5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
labels = ['5-10','10-15','15-20','20-25','25-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80']

H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Support_Frame_Bending_Top'].mean()
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Top)<0.00005]
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Top)>0.00005]
#H3_Support_Frame_Bending_Top_elevation_offset_mean = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Top.mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>50)&(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<60)]
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>0.5]
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<0.5]
H3_Support_Frame_Bending_Top_elevation_offset_mean = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Support_Frame_Bending_Top.mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Support_Frame_Bending_Top'], 1)



bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_Support_Frame_Bending_Top,marker='.')
plt.scatter(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Support_Frame_Bending_Top,marker='.')
#plt.scatter(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0005, 0)    
plt.title("H1 support frame bending top")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Top,marker='.')
plt.scatter(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Top,marker='.')
#plt.scatter(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0, 0.0003)    
plt.title("H2 support frame bending top")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Top,marker='.')
plt.scatter(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Support_Frame_Bending_Top,marker='.')
#plt.scatter(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0.0006, 0.0008)    
plt.title("H3 support frame bending top")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Top,marker='.')
#plt.scatter(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Support_Frame_Bending_Top,marker='.')
#plt.scatter(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0005, 0)    
plt.title("H1 support frame bending top")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Top,marker='.')
plt.plot(elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0, 0.0003)    
plt.title("H2 support frame bending top")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Top,marker='.')
#plt.scatter(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Support_Frame_Bending_Top,marker='.')
#plt.scatter(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'red')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0.0006, 0.0008)    
plt.title("H3 support frame bending top")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")






# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Support_Frame_Bending_Top'].mean()
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


# Stow (elevation0)
bins_Ts = [-5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H2_Support_Frame_Bending_Top'].mean()
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Top,marker='.')
plt.scatter(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0005, 0)       
plt.title("H1 Support frame bending top")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Top,marker='.')
plt.scatter(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(0, 0.0003)       
plt.title("H2 Support frame bending top") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Top,marker='.')
plt.scatter(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper (elev > 0.5)')
plt.scatter(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(0.0006, 0.0008)     
plt.title("H3 Support frame bending top")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


#%% H1 and H3 Support frame bending bottom time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]


bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>0]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean>65]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Elevation_mean, H1_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H1_Support_Frame_Bending_Bottom, 1)
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Elevation_mean, H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H1_Support_Frame_Bending_Bottom, 1)

slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Support_Frame_Bending_Bottom, 1)
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Support_Frame_Bending_Bottom, 1)

slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)


#%% Support frame bending bottom strain gage low wind offsets

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Bottom)<0.00005]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Bottom)>0.00005]
#H1_Support_Frame_Bending_Bottom_elevation_offset_mean = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Bottom.mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>50)&(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<60)]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean>0.5]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Elevation_mean<0.5]
H1_Support_Frame_Bending_Bottom_elevation_offset_mean = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Support_Frame_Bending_Bottom.mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_elevation'], H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Support_Frame_Bending_Bottom'], 1)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Elevation_mean'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

# Dependence on elevation angle and temp (H1 Support frame bending bottom)
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>80]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<80)&(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5)]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean>0.5]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0 = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_mean<0.5]

# Operating (elevation_05_80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg, 1)

# Operating (elevationg80)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg, 1)

# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_binned_avg, 1)

# Stow (elevation0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg, 1)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.Ts_Mid,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.Ts_Mid,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0.H1_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.Ts_Mid,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80.H1_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg,Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg80_Ts_binned_avg_trend,'black',label='oper (elev > 80)')
plt.scatter(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend,'black',label='oper (0.5<elev<80)')
plt.scatter(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg,Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H1 Support frame bending bottom")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()


# H1 H2 H3 Support frame bending bottom time series operation low wind days 25 October 2024

# Stow period from 3-7am LT (10-14UTC)

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,10,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,25,14,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Support_Frame_Bending_Bottom, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Elevation_mean'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H1_Elevation_mean'],H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Support_Frame_Bending_Bottom,marker='.')
plt.plot(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H1 Support frame bending bottom (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Support_Frame_Bending_Bottom, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Support_Frame_Bending_Bottom'].mean()
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Support_Frame_Bending_Bottom'].mean()
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'],H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Support_Frame_Bending_Bottom,marker='.')
plt.plot(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H2 Support frame bending bottom (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend = np.polyfit(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Support_Frame_Bending_Bottom, 1)

bins = [-0.5, 0]
labels = ['-0.5-0']

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'],H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Support_Frame_Bending_Bottom,marker='.')
plt.plot(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend,'black',label='stow')
#plt.scatter(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,marker='o')
#plt.plot(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend,'red',label='stow')
plt.xlim(-2, 1)
plt.xticks([-2,-1,0,1])     
plt.ylim(0.0001, 0.0002)     
plt.title("H3 Support frame bending bottom (25 Oct 2024)")   
plt.xlabel("Elevation angle meas ($^\circ$)")
plt.ylabel("V/V")
plt.legend()


#%% H3 Support frame bending bottom time series operation low wind days 25 October 2024

# Operating period from 1430-2230UTC

index_lowwind_oper_corr_start = pd.Timestamp(2024,10,25,12,0)
index_lowwind_oper_corr_end = pd.Timestamp(2024,10,26,0,0)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H1_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr[index_lowwind_oper_corr_start:index_lowwind_oper_corr_end]

bins = [5, 20, 35, 50, 60, 65, 70, 75, 80, 85]
labels = ['5-20','20-35','35-50','50-60','60-65','65-70','70-75','75-80','80-85']


H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>0]
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)

#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean>65]
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()

H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Support_Frame_Bending_Bottom, 1)
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean, H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Support_Frame_Bending_Bottom, 1)

slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)
intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave = 0.5*(intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend)



H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>0]
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['binned'] = pd.cut(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.groupby('binned')['H2_Support_Frame_Bending_Bottom'].mean()
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg_trend = np.polyfit(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_binned_avg, 1)


#Fit to 65-80 deg

bins = [65,67.5,70,72.5,75,77.5,80]
labels = ['65-67.5','67.5-70','70-72.5','72.5-75','75-77.5','77.5-80']

H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean>65]
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['binned'] = pd.cut(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_65_80_20241025.groupby('binned')['H2_Support_Frame_Bending_Bottom'].mean()

H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,12,0):pd.Timestamp(2024,10,25,14,23)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_track_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,14,23):pd.Timestamp(2024,10,25,22,47)]
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025 = H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025[pd.Timestamp(2024,10,25,22,47):pd.Timestamp(2024,10,26,0,0)]

slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Support_Frame_Bending_Bottom, 1)
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend = np.polyfit(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean, H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Support_Frame_Bending_Bottom, 1)


plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_mean)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Top)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Top)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Top)

plt.figure()
plt.plot(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Mirror_Displacement_Bottom)
plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Mirror_Displacement_Bottom)
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Mirror_Displacement_Bottom)

H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H1_Elevation_mean"] = -1*(H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Left+H1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H1_Elevation_Right)/2
H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H2_Elevation_mean"] = -1*(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Left+H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_Right)/2
H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025["H3_Elevation_mean"] = -1*(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Left+H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_Right)/2


H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Bottom)<0.00001]
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Bottom)>0.00001]
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5)&(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<80)]
#H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean>0.5]
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Elevation_mean<0.5]
H2_Support_Frame_Bending_Bottom_elevation_offset_mean = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Bottom.mean()

bins = [5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
labels = ['5-10','10-15','15-20','20-25','25-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80']

H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H2_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Elevation_mean'].mean()
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Support_Frame_Bending_Bottom'].mean()
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Bottom)<0.00005]
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Bottom)>0.00005]
#H3_Support_Frame_Bending_Bottom_elevation_offset_mean = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Bottom.mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg80 = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>50)&(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<60)]
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0 = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean>0.5]
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0 = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros[H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Elevation_mean<0.5]
H3_Support_Frame_Bending_Bottom_elevation_offset_mean = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Support_Frame_Bending_Bottom.mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend = np.polyfit(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_elevation'], H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Support_Frame_Bending_Bottom'], 1)



bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
labels = ['5-10','10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65-70','70-75','75-80','80-85']

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['H3_Elevation_mean'], bins=bins, labels=labels, right=False)
elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Elevation_mean'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend = np.polyfit(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads.H1_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0, 0.0002)    
plt.title("H1 support frame bending bottom")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H2_elevation*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0, 0.0003)    
plt.title("H2 support frame bending bottom")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_trend,'red')     
plt.plot(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'black')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0)    
plt.title("H3 support frame bending bottom")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Bottom,marker='.')
#plt.scatter(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_elevation,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H1_Support_Frame_Bending_Bottom,marker='.')
#plt.scatter(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0, 0.0002)    
plt.title("H1 support frame bending bottom")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Bottom,marker='.')
plt.plot(elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H2_Elevation_mean*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'black')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H2_Elevation_mean*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean,H2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H2_Elevation_mean*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(0, 0.0003)    
plt.title("H2 support frame bending bottom")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Bottom,marker='.')
#plt.scatter(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_elevation,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.H3_Support_Frame_Bending_Bottom,marker='.')
#plt.scatter(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
#plt.plot(elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,elevation_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend,'red')     
plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025.H3_Elevation_mean*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_operation_20241025_trend,'red')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025.H3_Elevation_mean*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_stow_20241025_trend,'purple')     
#plt.plot(H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean,H3_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025.H3_Elevation_mean*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave,'brown')     
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0)    
plt.title("H3 support frame bending bottom")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")





# Operating (elevationg0)
bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H2_Support_Frame_Bending_Bottom'].mean()
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['Temp'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg, 1)


# Stow (elevation0)
bins_Ts = [-5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H2_Support_Frame_Bending_Bottom'].mean()
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['Temp'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend = np.polyfit(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg, 1)




plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(0, 0.0002)       
plt.title("H1 Support frame bending bottom")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper')
plt.scatter(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(0, 0.0003)       
plt.title("H2 Support frame bending bottom") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,marker='o')
plt.plot(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg,Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend,'black',label='oper (elev > 0.5)')
plt.scatter(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,marker='o',color='red')
plt.plot(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg,Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_binned_avg*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend,'lime',label='stow (elev < 0.5)')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0)     
plt.title("H3 Support frame bending bottom")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")
plt.legend()









#%% Pedestal bending 2 strain gage low wind offsets

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_2)<0.0001]
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_2)>0.0001]
H1_Pedestal_Bend_2_elevation_offset_mean = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_2.mean()

H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_2)<0.0001]
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_2)>0.0001]
H2_Pedestal_Bend_2_elevation_offset_mean = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_2.mean()

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_2)<0.0001]
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_2)>0.0001]
H3_Pedestal_Bend_2_elevation_offset_mean = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_2.mean()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_2,marker='.')
plt.scatter(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H1 pedestal bending 2")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_2,marker='.')
plt.scatter(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H2 pedestal bending 2")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_2,marker='.')
plt.scatter(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal bending 2")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")
    

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Pedestal_Bend_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H1 pedestal bending 2")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Pedestal_Bend_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H2 pedestal bending 2")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left),H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Pedestal_Bend_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 pedestal bending 2")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")
    

bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Pedestal_Bend_2'].mean()
slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Pedestal_Bend_2'].mean()
slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Pedestal_Bend_2'].mean()
slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Pedestal_Bend_2,marker='.')
plt.scatter(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)       
plt.title("H1 pedestal bending 2")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Pedestal_Bend_2,marker='.')
plt.scatter(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.003, 0.003)       
plt.title("H2 pedestal bending 2") 
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Pedestal_Bend_2,marker='.')
plt.scatter(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0.0003)     
plt.title("H3 pedestal bending 2")   
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")


#%% Support frame bending top strain gage low wind offsets

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Top)<0.00005]
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Top)>0.00005]
H1_Support_Frame_Bending_Top_elevation_offset_mean = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Top.mean()

H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Top)<0.0001]
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Top)>0.0001]
H2_Support_Frame_Bending_Top_elevation_offset_mean = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Top.mean()

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Top)<0.00005]
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Top)>0.00005]
H3_Support_Frame_Bending_Top_elevation_offset_mean = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Top.mean()

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Top,marker='.')
plt.scatter(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Top,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0006, 0.0006)    
plt.title("H1 support frame bending top")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Top,marker='.')
plt.scatter(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Top,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0004, 0.0004)    
plt.title("H2 support frame bending top")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Top,marker='.')
plt.scatter(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Top,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H3 support frame bending top")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Top,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0006, 0.0006)    
plt.title("H1 support frame bending top")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Top,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0004, 0.0004)    
plt.title("H2 support frame bending top")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left),H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Top,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.003, 0.003)    
plt.title("H3 support frame bending top")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")



bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Support_Frame_Bending_Top'].mean()
slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Support_Frame_Bending_Top'].mean()
slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Support_Frame_Bending_Top'].mean()
slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Top,marker='.')
plt.scatter(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0005, 0)    
plt.title("H1 support frame bending top")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Top,marker='.')
plt.scatter(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(0, 0.0003)      
plt.title("H2 support frame bending top")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Top,marker='.')
plt.scatter(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(0, 0.001)    
plt.title("H3 support frame bending top")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")


#%% Support frame bending bottom strain gage low wind offsets

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Bottom)<0.00005]
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Bottom)>0.00005]
H1_Support_Frame_Bending_Bottom_elevation_offset_mean = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Bottom.mean()

H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Bottom)<0.0001]
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Bottom)>0.0001]
H2_Support_Frame_Bending_Bottom_elevation_offset_mean = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Bottom.mean()

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Bottom)<0.00005]
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Bottom)>0.00005]
H3_Support_Frame_Bending_Bottom_elevation_offset_mean = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Bottom.mean()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Bottom,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0006, 0.0006)    
plt.title("H1 support frame bending bottom")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Bottom,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0004, 0.0004)    
plt.title("H2 support frame bending bottom")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Bottom,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 support frame bending bottom")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("V/V")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Support_Frame_Bending_Bottom,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0006, 0.0006)    
plt.title("H1 support frame bending bottom")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Support_Frame_Bending_Bottom,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0004, 0.0004)    
plt.title("H2 support frame bending bottom")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left),H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Support_Frame_Bending_Bottom,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-0.0003, 0.0003)    
plt.title("H3 support frame bending bottom")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("V/V")



bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Support_Frame_Bending_Bottom'].mean()
slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Support_Frame_Bending_Bottom'].mean()
slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Support_Frame_Bending_Bottom'].mean()
slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)     
plt.xticks([-20,-10,0,10,20,30])
plt.ylim(0,0.0002)    
plt.title("H1 support frame bending bottom")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(0, 0.0004)      
plt.title("H2 support frame bending bottom")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Support_Frame_Bending_Bottom,marker='.')
plt.scatter(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
plt.plot(Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-0.0003, 0)    
plt.title("H3 support frame bending bottom")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("V/V")




#%% Differential pressure 1 low wind offsets

H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_1)<1]
H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_1)>1000]
H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_1)>1)&(abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_1)<1000)]
H1_Differential_Pressure_1_elevation_offset_mean = H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_1.mean()

H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_1)<1]
H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_1)>1000]
H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_1)>1)&(abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_1)<1000)]
H2_Differential_Pressure_1_elevation_offset_mean = H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_1.mean()

H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_1)<1]
H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_1)>1000]
H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_1)>1)&(abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_1)<1000)]
H3_Differential_Pressure_1_elevation_offset_mean = H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_1.mean()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_1,marker='.')
plt.scatter(H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation,H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_1,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H1 differential pressure 1")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_1,marker='.')
plt.scatter(H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_1,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H2 differential pressure 1")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_1,marker='.')
plt.scatter(H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation,H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_1,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)       
plt.title("H3 differential pressure 1")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_1,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H1 differential pressure 1")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_1,marker='.')
plt.xlim(-10, 90)   
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)  
plt.title("H2 differential pressure 1")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left),H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_1,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)  
plt.title("H3 differential pressure 1")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")



bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Differential_Pressure_1'].mean()
slope_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Differential_Pressure_1'].mean()
slope_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Differential_Pressure_1'].mean()
slope_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_1,marker='.')
#plt.scatter(Ts_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)     
plt.xticks([-20,-10,0,10,20,30])
plt.ylim(-40, 40)     
plt.title("H1 differential pressure 1")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_1,marker='.')
#plt.scatter(Ts_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-40, 40)      
plt.title("H2 differential pressure 1")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_1,marker='.')
#plt.scatter(Ts_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Differential_Pressure_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-40, 40)     
plt.title("H3 differential pressure 1")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")


#%% Differential pressure 2 low wind offsets

H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_2)<1]
H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_2)>1000]
H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_2)>1)&(abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_2)<1000)]
H1_Differential_Pressure_2_elevation_offset_mean = H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_2.mean()

H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_2)<1]
H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_2)>1000]
H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_2)>1)&(abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_2)<1000)]
H2_Differential_Pressure_2_elevation_offset_mean = H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_2.mean()

H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_2)<1]
H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_2)>1000]
H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_2)>1)&(abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_2)<1000)]
H3_Differential_Pressure_2_elevation_offset_mean = H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_2.mean()



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_2,marker='.')
plt.scatter(H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation,H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H1 differential pressure 2")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_2,marker='.')
plt.scatter(H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H2 differential pressure 2")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_2,marker='.')
plt.scatter(H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation,H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)       
plt.title("H3 differential pressure 2")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H1 differential pressure 2")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_2,marker='.')
plt.xlim(-10, 90)   
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)  
plt.title("H2 differential pressure 2")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left),H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_2,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)  
plt.title("H3 differential pressure 2")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")



bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Differential_Pressure_2'].mean()
slope_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Differential_Pressure_2'].mean()
slope_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Differential_Pressure_2'].mean()
slope_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_2,marker='.')
#plt.scatter(Ts_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)     
plt.xticks([-20,-10,0,10,20,30])
plt.ylim(-40, 40)     
plt.title("H1 differential pressure 2")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_2,marker='.')
#plt.scatter(Ts_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-40, 40)      
plt.title("H2 differential pressure 2")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_2,marker='.')
#plt.scatter(Ts_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Differential_Pressure_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-40, 40)     
plt.title("H3 differential pressure 2")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")


#%% Differential pressure 3 low wind offsets

H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_3)<1]
H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_3)>1000]
H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_3)>1)&(abs(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_3)<1000)]
H1_Differential_Pressure_3_elevation_offset_mean = H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_3.mean()

H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_3)<1]
H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_3)>1000]
H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_3)>1)&(abs(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_3)<1000)]
H2_Differential_Pressure_3_elevation_offset_mean = H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_3.mean()

H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_zeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_3)<1]
H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_high = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_3)>1000]
H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros = H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr[(abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_3)>1)&(abs(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_3)<1000)]
H3_Differential_Pressure_3_elevation_offset_mean = H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_3.mean()



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_elevation,H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_3,marker='.')
plt.scatter(H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_elevation,H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_3,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H1 differential pressure 3")    
plt.xlabel("H1 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_elevation,H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_3,marker='.')
plt.scatter(H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_elevation,H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_3,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H2 differential pressure 3")    
plt.xlabel("H2 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_elevation,H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_3,marker='.')
plt.scatter(H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_elevation,H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_3,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)       
plt.title("H3 differential pressure 3")    
plt.xlabel("H3 elevation SCADA ($^\circ$)")
plt.ylabel("DP (Pa)")


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Right+H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Elevation_Left),H1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H1_Differential_Pressure_3,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)    
plt.title("H1 differential pressure 3")    
plt.xlabel("H1 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Right+H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Elevation_Left),H2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H2_Differential_Pressure_3,marker='.')
plt.xlim(-10, 90)   
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)  
plt.title("H2 differential pressure 3")    
plt.xlabel("H2 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(-0.5*(H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Right+H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Elevation_Left),H3_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr.H3_Differential_Pressure_3,marker='.')
plt.xlim(-10, 90)     
plt.xticks([0,15,30,45,60,75,90])
plt.ylim(-40, 40)  
plt.title("H3 differential pressure 3")    
plt.xlabel("H3 elevation meas ($^\circ$)")
plt.ylabel("DP (Pa)")



bins_Ts = [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]
labels_Ts = ['-15-10','-10-5','-5-0','0-5','5-10','10-15','15-20','20-25','25-30']

H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H1_Differential_Pressure_3'].mean()
slope_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H2_Differential_Pressure_3'].mean()
slope_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)

H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['binned'] = pd.cut(H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros['Temp'], bins=bins_Ts, labels=labels_Ts, right=False)
Ts_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['Temp'].mean()
H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg = H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.groupby('binned')['H3_Differential_Pressure_3'].mean()
slope_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend, intercept_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend = np.polyfit(Ts_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg, 1)



plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H1_Differential_Pressure_3,marker='.')
#plt.scatter(Ts_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H1_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)     
plt.xticks([-20,-10,0,10,20,30])
plt.ylim(-4000, 40)     
plt.title("H1 differential pressure 3")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H2_Differential_Pressure_3,marker='.')
#plt.scatter(Ts_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H2_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-40, 40)      
plt.title("H2 differential pressure 3")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.Ts_Mid,H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros.H3_Differential_Pressure_3,marker='.')
#plt.scatter(Ts_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,marker='o')
#plt.plot(Ts_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg,Ts_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_binned_avg*slope_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend+intercept_H3_Differential_Pressure_3_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_Ts_binned_avg_trend,'black')
plt.xlim(-20, 30)
plt.xticks([-20,-10,0,10,20,30])     
plt.ylim(-40, 40)     
plt.title("H3 differential pressure 3")    
plt.xlabel("Temp 2.65m ($^\circ$C)")
plt.ylabel("DP (Pa)")



#%% Fit sine function to accelerometer offsets (using measured elevation angles)

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the sine function
def sine_function(x, amplitude, frequency, phase, offset):
    return amplitude * np.sin(frequency * x + phase) + offset

x_fit = np.linspace(5, 85, 100)
x_fit_radians = np.radians(x_fit)

H1_Support_Frame_Accel_1_X_fit = sine_function(x_fit_radians, -1, 0.3*math.pi, -0.053+math.pi/2, -0.1)
H1_Support_Frame_Accel_1_Y_fit = sine_function(x_fit_radians, 1, 0.4*math.pi, -0.053, 0.05)
H1_Support_Frame_Accel_2_X_fit = sine_function(x_fit_radians, -1, 0.33*math.pi, -0.053+math.pi/2, 0)
H1_Support_Frame_Accel_2_Y_fit = sine_function(x_fit_radians, 1, 0.35*math.pi, -0.053, 0)
H1_Support_Frame_Accel_3_X_fit = sine_function(x_fit_radians, -1, 0.32*math.pi, -0.053+math.pi/2, 0)
H1_Support_Frame_Accel_3_Y_fit = sine_function(x_fit_radians, 1, 0.3*math.pi, -0.053, 0)
H1_Support_Frame_Accel_4_X_fit = sine_function(x_fit_radians, -1, 0.33*math.pi, -0.053+math.pi/2, 0.05)
H1_Support_Frame_Accel_4_Y_fit = sine_function(x_fit_radians, 1, 0.28*math.pi, 0, 0)

H2_Support_Frame_Accel_1_X_fit = sine_function(x_fit_radians, -1, 0.33*math.pi, -0.053+math.pi/2, 0)
H2_Support_Frame_Accel_1_Y_fit = sine_function(x_fit_radians, 1, 0.35*math.pi, -0.053, 0)
H2_Support_Frame_Accel_2_X_fit = sine_function(x_fit_radians, -1, 0.32*math.pi, -0.053+math.pi/2, 0)
H2_Support_Frame_Accel_2_Y_fit = sine_function(x_fit_radians, 1, 0.35*math.pi, -0.053, 0)
H2_Support_Frame_Accel_3_X_fit = sine_function(x_fit_radians, -1, 0.32*math.pi, -0.053+math.pi/2, 0)
H2_Support_Frame_Accel_3_Y_fit = sine_function(x_fit_radians, 1, 0.32*math.pi, -0.053, 0)
H2_Support_Frame_Accel_4_X_fit = sine_function(x_fit_radians, -1, 0.31*math.pi, math.pi/2, 0.05)
H2_Support_Frame_Accel_4_Y_fit = sine_function(x_fit_radians, 1, 0.33*math.pi, -0.053, 0)

H3_Support_Frame_Accel_1_X_fit = sine_function(x_fit_radians, -1, 0.32*math.pi, -0.053+math.pi/2, 0)
H3_Support_Frame_Accel_1_Y_fit = sine_function(x_fit_radians, 1, 0.32*math.pi, -0.053, 0)
H3_Support_Frame_Accel_2_X_fit = sine_function(x_fit_radians, -1, 0.34*math.pi, -0.053+math.pi/2, 0)
H3_Support_Frame_Accel_2_Y_fit = sine_function(x_fit_radians, 1, 0.34*math.pi, -0.053, 0)
H3_Support_Frame_Accel_3_X_fit = sine_function(x_fit_radians, -1, 0.32*math.pi, -0.053+math.pi/2, 0)
H3_Support_Frame_Accel_3_Y_fit = sine_function(x_fit_radians, 1, 0.32*math.pi, -0.053, 0)
H3_Support_Frame_Accel_4_X_fit = sine_function(x_fit_radians, -1, 0.32*math.pi, math.pi/2, 0)
H3_Support_Frame_Accel_4_Y_fit = sine_function(x_fit_radians, 1, 0.29*math.pi, -0.053, 0)

#%% Mean and peak-peak load coefficients (loads + inflow 28 October 2024)

loads_20Hz_20241028 = pd.read_pickle('Loads_fastdata_20Hz_2024-10-28_to_2024-10-29.pkl')
inflow_20Hz_20241028 = pd.read_pickle('Inflow_20Hz_2024-10-28_to_2024-10-29.pkl')
mast_20Hz_20241028 = pd.read_pickle('mast_20Hz_2024-10-28_to_2024-10-29.pkl')

axial_slope = 82075.28 # kN/V/V
torque_tube_slopeT = 191171 # kNm/V/V	 
pedestal_bending_slopeM = 205961.1	 # kNm/V/V	 
pedestal_torque_slopeT =	213386.9 # kNm/V/V
support_frame_bending_slopeM = 395.6838	#kNm/V/V

loads_20Hz_20241028['H1_Elevation_mean'] = -0.5*(loads_20Hz_20241028['H1_Elevation_Left '] + loads_20Hz_20241028['H1_Elevation_Right '])
loads_20Hz_20241028['H2_Elevation_mean'] = -0.5*(loads_20Hz_20241028['H2_Elevation_Left '] + loads_20Hz_20241028['H2_Elevation_Right '])
loads_20Hz_20241028['H3_Elevation_mean'] = -0.5*(loads_20Hz_20241028['H3_Elevation_Left '] + loads_20Hz_20241028['H3_Elevation_Right '])

loads_inflow_20Hz_20241028 = pd.merge(loads_20Hz_20241028, inflow_20Hz_20241028, left_index=True, right_index=True, how="inner")
loads_mast_20Hz_20241028 = pd.merge(loads_20Hz_20241028, mast_20Hz_20241028, left_index=True, right_index=True, how="inner")
#loads = pd.merge(loads, H1[['State', 'AngAzData', 'AngElData']], left_index=True, right_index=True, suffixes=('', '_H1'))
    
loads_inflow_20Hz_20241028['H1_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241028['H1_Elevation_Left '] + loads_inflow_20Hz_20241028['H1_Elevation_Right '])
loads_inflow_20Hz_20241028['H2_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241028['H2_Elevation_Left '] + loads_inflow_20Hz_20241028['H2_Elevation_Right '])
loads_inflow_20Hz_20241028['H3_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241028['H3_Elevation_Left '] + loads_inflow_20Hz_20241028['H3_Elevation_Right '])

loads_inflow_20Hz_20241028['H1_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241028['H1_Elevation_Left ']-loads_inflow_20Hz_20241028['H1_Elevation_Right '])>2,loads_inflow_20Hz_20241028['H1_Elevation_Right '],loads_inflow_20Hz_20241028['H1_Elevation_mean'])
loads_inflow_20Hz_20241028['H2_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241028['H2_Elevation_Left ']-loads_inflow_20Hz_20241028['H2_Elevation_Right '])>2,loads_inflow_20Hz_20241028['H2_Elevation_Right '],loads_inflow_20Hz_20241028['H2_Elevation_mean'])
loads_inflow_20Hz_20241028['H3_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241028['H3_Elevation_Left ']-loads_inflow_20Hz_20241028['H3_Elevation_Right '])>2,loads_inflow_20Hz_20241028['H3_Elevation_Left '],loads_inflow_20Hz_20241028['H3_Elevation_mean'])

loads_inflow_20Hz_20241028['H1_Displacement_Top_temp_stow_offset'] = slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241028.Temp+intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241028['H2_Displacement_Top_temp_stow_offset'] = slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241028['H3_Displacement_Top_temp_stow_offset'] = slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241028['H1_Displacement_Top'] = loads_inflow_20Hz_20241028['H1_Mirror_Displacement_Top']-loads_inflow_20Hz_20241028['H1_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241028['H2_Displacement_Top'] = loads_inflow_20Hz_20241028['H2_Mirror_Displacement_Top']-loads_inflow_20Hz_20241028['H2_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241028['H3_Displacement_Top'] = loads_inflow_20Hz_20241028['H3_Mirror_Displacement_Top']-loads_inflow_20Hz_20241028['H3_Displacement_Top_temp_stow_offset']

loads_inflow_20Hz_20241028['H1_Displacement_Bottom_temp_stow_offset'] = slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241028.Temp+intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241028['H2_Displacement_Bottom_temp_stow_offset'] = slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241028['H3_Displacement_Bottom_temp_stow_offset'] = slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241028['H1_Displacement_Bottom'] = loads_inflow_20Hz_20241028['H1_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241028['H1_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241028['H2_Displacement_Bottom'] = loads_inflow_20Hz_20241028['H2_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241028['H2_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241028['H3_Displacement_Bottom'] = loads_inflow_20Hz_20241028['H3_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241028['H3_Displacement_Bottom_temp_stow_offset']

loads_inflow_20Hz_20241028["H1_F_Lift"] = (loads_inflow_20Hz_20241028['H1_Pedestal_Axial '] - H1_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241028["H2_F_Lift"] = (loads_inflow_20Hz_20241028['H2_Pedestal_Axial '] - H2_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_oper_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241028.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_stow_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*loads_inflow_20Hz_20241028.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Axial_temp_stow_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Axial_temp_oper_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_temp_stow_offset'] = 0.5*(loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_stow_offset']+loads_inflow_20Hz_20241028['H3_Pedestal_Axial_temp_stow_offset'])
loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_oper_offset']+loads_inflow_20Hz_20241028['H3_Pedestal_Axial_temp_oper_offset'])
loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_temp_stow_offset'])
loads_inflow_20Hz_20241028["H3_F_Lift"] = (loads_inflow_20Hz_20241028['H3_Pedestal_Axial '] - loads_inflow_20Hz_20241028['H3_Pedestal_Axial_elevation_temp_offset_average']) * axial_slope 

loads_inflow_20Hz_20241028["H1_CF_Lift"] = loads_inflow_20Hz_20241028.H1_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241028["H2_CF_Lift"] = loads_inflow_20Hz_20241028.H2_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241028["H3_CF_Lift"] = loads_inflow_20Hz_20241028.H3_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23)

loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_elevation_offset'] = slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241028.H1_Elevation_mean+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_temp_stow_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_temp_oper_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H1_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241028["H1_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241028.H1_Torque_Tube_Left - loads_inflow_20Hz_20241028.H1_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_elevation_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_temp_stow_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_temp_oper_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H2_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241028["H2_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241028.H2_Torque_Tube_Left - loads_inflow_20Hz_20241028.H2_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_elevation_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241028.H3_Elevation_mean+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_temp_stow_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_temp_oper_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H3_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241028["H3_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241028.H3_Torque_Tube_Left - loads_inflow_20Hz_20241028.H3_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241028["H1_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241028["H1_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241028["H2_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241028["H2_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241028["H3_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241028["H3_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241028['H1_Pedestal_Torque_elevation_offset'] = slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241028.H1_Elevation_mean+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Torque_temp_stow_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Torque_temp_oper_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H1_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241028['H1_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241028['H1_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H1_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H1_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241028["H1_Pedestal_Torque"] = (loads_inflow_20Hz_20241028.H1_Pedestal_Torque - loads_inflow_20Hz_20241028.H1_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241028['H2_Pedestal_Torque_elevation_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Torque_temp_stow_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Torque_temp_oper_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H2_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241028['H2_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241028['H2_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H2_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H2_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241028["H2_Pedestal_Torque"] = (loads_inflow_20Hz_20241028.H2_Pedestal_Torque - loads_inflow_20Hz_20241028.H2_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241028['H3_Pedestal_Torque_elevation_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241028.H3_Elevation_mean+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241028['H3_Pedestal_Torque_temp_stow_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Torque_temp_oper_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H3_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241028['H3_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241028['H3_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H3_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H3_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241028["H3_Pedestal_Torque"] = (loads_inflow_20Hz_20241028.H3_Pedestal_Torque - loads_inflow_20Hz_20241028.H3_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241028["H1_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241028["H1_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241028["H2_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241028["H2_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241028["H3_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241028["H3_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_elevation_offset'] = slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241028.H1_Elevation_mean+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_temp_stow_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_temp_oper_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H1_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241028["H1_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241028.H1_Pedestal_Bend_1 - loads_inflow_20Hz_20241028.H1_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_elevation_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_temp_stow_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_temp_oper_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H2_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241028["H2_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241028.H2_Pedestal_Bend_1 - loads_inflow_20Hz_20241028.H2_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_elevation_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241028.H3_Elevation_mean+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_temp_stow_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_temp_oper_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H3_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241028["H3_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241028.H3_Pedestal_Bend_1 - loads_inflow_20Hz_20241028.H3_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241028["H1_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241028["H1_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241028["H2_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241028["H2_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241028["H3_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241028["H3_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_elevation_offset'] = slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241028.H1_Elevation_mean+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_temp_stow_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_temp_oper_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241028["H1_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241028['H1_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241028.H1_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_elevation_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_temp_stow_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_temp_oper_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241028["H2_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241028['H2_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241028.H2_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_elevation_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241028.H3_Elevation_mean+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_temp_stow_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_temp_oper_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241028["H3_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241028['H3_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241028.H3_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241028["H1_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241028["H1_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241028["H2_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241028["H2_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241028["H3_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241028["H3_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_elevation_offset'] = slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241028.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241028["H1_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241028.H1_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_elevation_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241028["H2_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241028.H2_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_elevation_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241028.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241028["H3_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241028.H3_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241028.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241028["H1_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241028['H1_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241028.H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241028["H2_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241028['H2_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241028.H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241028.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241028.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241028['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241028["H3_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241028['H3_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241028.H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241028["H1_DP1"] = loads_inflow_20Hz_20241028['H1_Differential_Pressure_1'] - H1_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241028["H1_DP2"] = loads_inflow_20Hz_20241028['H1_Differential_Pressure_2'] - H1_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241028["H1_DP3"] = loads_inflow_20Hz_20241028['H1_Differential_Pressure_3'] - H1_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241028["H2_DP1"] = loads_inflow_20Hz_20241028['H2_Differential_Pressure_1'] - H2_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241028["H2_DP2"] = loads_inflow_20Hz_20241028['H2_Differential_Pressure_2'] - H2_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241028["H2_DP3"] = loads_inflow_20Hz_20241028['H2_Differential_Pressure_3'] - H2_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241028["H3_DP1"] = loads_inflow_20Hz_20241028['H3_Differential_Pressure_1'] - H3_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241028["H3_DP2"] = loads_inflow_20Hz_20241028['H3_Differential_Pressure_2'] - H3_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241028["H3_DP3"] = loads_inflow_20Hz_20241028['H3_Differential_Pressure_3'] - H3_Differential_Pressure_3_elevation_offset_mean

A3 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 3) 
A2 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 2) 
A1 = 10.3*(11.23/5)*2  # heliostat width x 2 facet heights (differential pressure 1) 

x1 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 1) 
x2 = (11.23/5)*0.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 2) 
x3 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 3) 

loads_inflow_20Hz_names = loads_inflow_20Hz_20241028.columns

loads_inflow_20Hz_20241028["H1_DP_F_Normal"] = (loads_inflow_20Hz_20241028.H1_DP1*A1)+(loads_inflow_20Hz_20241028.H1_DP2*A2)+(loads_inflow_20Hz_20241028.H1_DP3*A3)
loads_inflow_20Hz_20241028["H1_DP_F_Drag"] = loads_inflow_20Hz_20241028.H1_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean))
loads_inflow_20Hz_20241028["H1_DP_F_Lift"] = loads_inflow_20Hz_20241028.H1_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean))
loads_inflow_20Hz_20241028["H1_DP_M_Hy"] = (loads_inflow_20Hz_20241028.H1_DP1*A1*x1)+(loads_inflow_20Hz_20241028.H1_DP2*A2*x2)-(loads_inflow_20Hz_20241028.H1_DP3*A3*x3)

loads_inflow_20Hz_20241028["H2_DP_F_Normal"] = (loads_inflow_20Hz_20241028.H2_DP1*A1)+(loads_inflow_20Hz_20241028.H2_DP2*A2)+(loads_inflow_20Hz_20241028.H2_DP3*A3)
loads_inflow_20Hz_20241028["H2_DP_F_Drag"] = loads_inflow_20Hz_20241028.H2_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean))
loads_inflow_20Hz_20241028["H2_DP_F_Lift"] = loads_inflow_20Hz_20241028.H2_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean))
loads_inflow_20Hz_20241028["H2_DP_M_Hy"] = (loads_inflow_20Hz_20241028.H2_DP1*A1*x1)+(loads_inflow_20Hz_20241028.H2_DP2*A2*x2)-(loads_inflow_20Hz_20241028.H2_DP3*A3*x3)

loads_inflow_20Hz_20241028["H3_DP_F_Normal"] = (loads_inflow_20Hz_20241028.H3_DP1*A1)+(loads_inflow_20Hz_20241028.H3_DP2*A2)+(loads_inflow_20Hz_20241028.H3_DP3*A3)
loads_inflow_20Hz_20241028["H3_DP_F_Drag"] = loads_inflow_20Hz_20241028.H3_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean))
loads_inflow_20Hz_20241028["H3_DP_F_Lift"] = loads_inflow_20Hz_20241028.H3_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean))
loads_inflow_20Hz_20241028["H3_DP_M_Hy"] = (loads_inflow_20Hz_20241028.H3_DP1*A1*x1)+(loads_inflow_20Hz_20241028.H3_DP2*A2*x2)-(loads_inflow_20Hz_20241028.H3_DP3*A3*x3)

loads_inflow_20Hz_20241028["H1_DP_CF_Lift"] = loads_inflow_20Hz_20241028.H1_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241028["H2_DP_CF_Lift"] = loads_inflow_20Hz_20241028.H2_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241028["H3_DP_CF_Lift"] = loads_inflow_20Hz_20241028.H3_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23)

loads_inflow_20Hz_20241028["H1_DP_CMHy"] = loads_inflow_20Hz_20241028.H1_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241028["H2_DP_CMHy"] = loads_inflow_20Hz_20241028.H2_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241028["H3_DP_CMHy"] = loads_inflow_20Hz_20241028.H3_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241028.p, loads_inflow_20Hz_20241028.RH, loads_inflow_20Hz_20241028.Temp)*loads_inflow_20Hz_20241028.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean), -1, 0.3*math.pi, -0.053+math.pi/2, -0.1)
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0.05)
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean), 1, 0.4*math.pi, -0.053, 0.05)
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean), 1, 0.3*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H1_Elevation_mean), 1, 0.28*math.pi, 0, 0)
loads_inflow_20Hz_20241028["H1_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H1_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean), -1, 0.31*math.pi, math.pi/2, 0.05)
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H2_Elevation_mean), 1, 0.33*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H2_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H2_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean), -1, 0.34*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean), -1, 0.32*math.pi, math.pi/2, 0)
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean), 1, 0.34*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241028.H3_Elevation_mean), 1, 0.29*math.pi, -0.053, 0)
loads_inflow_20Hz_20241028["H3_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241028.H3_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241028[["H1_Elevation_mean","H2_Elevation_mean","H3_Elevation_mean","H1_F_Lift","H2_F_Lift","H3_F_Lift","H1_Torque_Tube_Torque_Left","H2_Torque_Tube_Torque_Left","H3_Torque_Tube_Torque_Left","H1_Pedestal_Torque","H2_Pedestal_Torque","H3_Pedestal_Torque","H1_Pedestal_Bend_1","H2_Pedestal_Bend_1","H3_Pedestal_Bend_1","H1_Pedestal_Bend_2","H2_Pedestal_Bend_2","H3_Pedestal_Bend_2","H1_Support_Frame_Bending_Top","H2_Support_Frame_Bending_Top","H3_Support_Frame_Bending_Top","H1_DP1","H1_DP2","H1_DP3","H2_DP1","H2_DP2","H2_DP3","H3_DP1","H3_DP2","H3_DP3","H1_Mirror_Displacement_Top","H2_Mirror_Displacement_Top","H3_Mirror_Displacement_Top","H1_Mirror_Displacement_Bottom","H2_Mirror_Displacement_Bottom","H3_Mirror_Displacement_Bottom","H1_Support_Frame_Accel_1_X_processed","H1_Support_Frame_Accel_2_X_processed","H1_Support_Frame_Accel_3_X_processed","H1_Support_Frame_Accel_4_X_processed","H1_Support_Frame_Accel_1_Y_processed","H1_Support_Frame_Accel_2_Y_processed","H1_Support_Frame_Accel_3_Y_processed","H1_Support_Frame_Accel_4_Y_processed","H2_Support_Frame_Accel_1_X_processed","H2_Support_Frame_Accel_2_X_processed","H2_Support_Frame_Accel_3_X_processed","H2_Support_Frame_Accel_4_X_processed","H2_Support_Frame_Accel_1_Y_processed","H2_Support_Frame_Accel_2_Y_processed","H2_Support_Frame_Accel_3_Y_processed","H2_Support_Frame_Accel_4_Y_processed","H3_Support_Frame_Accel_1_X_processed","H3_Support_Frame_Accel_2_X_processed","H3_Support_Frame_Accel_3_X_processed","H3_Support_Frame_Accel_4_X_processed","H3_Support_Frame_Accel_1_Y_processed","H3_Support_Frame_Accel_2_Y_processed","H3_Support_Frame_Accel_3_Y_processed","H3_Support_Frame_Accel_4_Y_processed"]].to_parquet("Loads_20Hz_2024-10-28_00h_to_2024-10-29_00h.parquet")

pacific_tz = pytz.timezone('America/Los_Angeles')

# Assuming 'index' of DataFrames is already in UTC
loads_inflow_20Hz_20241028.index = loads_inflow_20Hz_20241028.index.tz_localize('UTC').tz_convert(pacific_tz)

loads_mast_20Hz_20241028.index = loads_mast_20Hz_20241028.index.tz_localize('UTC').tz_convert(pacific_tz)

#%% Mean and peak-peak load coefficients (loads + inflow 15 November 2024)

loads_20Hz_20241115 = pd.read_pickle('Loads_fastdata_20Hz_2024-11-15_to_2024-11-16.pkl')
inflow_20Hz_20241115 = pd.read_pickle('Inflow_20Hz_2024-11-15_to_2024-11-16.pkl')
mast_20Hz_20241115 = pd.read_pickle('mast_20Hz_2024-11-15_to_2024-11-16.pkl')

axial_slope = 82075.28 # kN/V/V
torque_tube_slopeT = 191171 # kNm/V/V	 
pedestal_bending_slopeM = 205961.1	 # kNm/V/V	 
pedestal_torque_slopeT =	213386.9 # kNm/V/V
support_frame_bending_slopeM = 395.6838	#kNm/V/V

loads_20Hz_20241115['H1_Elevation_mean'] = -0.5*(loads_20Hz_20241115['H1_Elevation_Left '] + loads_20Hz_20241115['H1_Elevation_Right '])
loads_20Hz_20241115['H2_Elevation_mean'] = -0.5*(loads_20Hz_20241115['H2_Elevation_Left '] + loads_20Hz_20241115['H2_Elevation_Right '])
loads_20Hz_20241115['H3_Elevation_mean'] = -0.5*(loads_20Hz_20241115['H3_Elevation_Left '] + loads_20Hz_20241115['H3_Elevation_Right '])

loads_inflow_20Hz_20241115 = pd.merge(loads_20Hz_20241115, inflow_20Hz_20241115, left_index=True, right_index=True, how="inner")
loads_mast_20Hz_20241115 = pd.merge(loads_20Hz_20241115, mast_20Hz_20241115, left_index=True, right_index=True, how="inner")
#loads = pd.merge(loads, H1[['State', 'AngAzData', 'AngElData']], left_index=True, right_index=True, suffixes=('', '_H1'))
    
loads_inflow_20Hz_20241115['H1_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241115['H1_Elevation_Left '] + loads_inflow_20Hz_20241115['H1_Elevation_Right '])
loads_inflow_20Hz_20241115['H2_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241115['H2_Elevation_Left '] + loads_inflow_20Hz_20241115['H2_Elevation_Right '])
loads_inflow_20Hz_20241115['H3_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241115['H3_Elevation_Left '] + loads_inflow_20Hz_20241115['H3_Elevation_Right '])

loads_inflow_20Hz_20241115['H1_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241115['H1_Elevation_Left ']-loads_inflow_20Hz_20241115['H1_Elevation_Right '])>2,loads_inflow_20Hz_20241115['H1_Elevation_Right '],loads_inflow_20Hz_20241115['H1_Elevation_mean'])
loads_inflow_20Hz_20241115['H2_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241115['H2_Elevation_Left ']-loads_inflow_20Hz_20241115['H2_Elevation_Right '])>2,loads_inflow_20Hz_20241115['H2_Elevation_Right '],loads_inflow_20Hz_20241115['H2_Elevation_mean'])
loads_inflow_20Hz_20241115['H3_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241115['H3_Elevation_Left ']-loads_inflow_20Hz_20241115['H3_Elevation_Right '])>2,loads_inflow_20Hz_20241115['H3_Elevation_Left '],loads_inflow_20Hz_20241115['H3_Elevation_mean'])

loads_inflow_20Hz_20241115['H1_Displacement_Top_temp_stow_offset'] = slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241115.Temp+intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241115['H2_Displacement_Top_temp_stow_offset'] = slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241115['H3_Displacement_Top_temp_stow_offset'] = slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241115['H1_Displacement_Top'] = loads_inflow_20Hz_20241115['H1_Mirror_Displacement_Top']-loads_inflow_20Hz_20241115['H1_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241115['H2_Displacement_Top'] = loads_inflow_20Hz_20241115['H2_Mirror_Displacement_Top']-loads_inflow_20Hz_20241115['H2_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241115['H3_Displacement_Top'] = loads_inflow_20Hz_20241115['H3_Mirror_Displacement_Top']-loads_inflow_20Hz_20241115['H3_Displacement_Top_temp_stow_offset']

loads_inflow_20Hz_20241115['H1_Displacement_Bottom_temp_stow_offset'] = slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241115.Temp+intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241115['H2_Displacement_Bottom_temp_stow_offset'] = slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241115['H3_Displacement_Bottom_temp_stow_offset'] = slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241115['H1_Displacement_Bottom'] = loads_inflow_20Hz_20241115['H1_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241115['H1_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241115['H2_Displacement_Bottom'] = loads_inflow_20Hz_20241115['H2_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241115['H2_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241115['H3_Displacement_Bottom'] = loads_inflow_20Hz_20241115['H3_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241115['H3_Displacement_Bottom_temp_stow_offset']

loads_inflow_20Hz_20241115["H1_F_Lift"] = (loads_inflow_20Hz_20241115['H1_Pedestal_Axial '] - H1_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241115["H2_F_Lift"] = (loads_inflow_20Hz_20241115['H2_Pedestal_Axial '] - H2_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_oper_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241115.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_stow_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*loads_inflow_20Hz_20241115.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Axial_temp_stow_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Axial_temp_oper_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_temp_stow_offset'] = 0.5*(loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_stow_offset']+loads_inflow_20Hz_20241115['H3_Pedestal_Axial_temp_stow_offset'])
loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_oper_offset']+loads_inflow_20Hz_20241115['H3_Pedestal_Axial_temp_oper_offset'])
loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_temp_stow_offset'])
loads_inflow_20Hz_20241115["H3_F_Lift"] = (loads_inflow_20Hz_20241115['H3_Pedestal_Axial '] - loads_inflow_20Hz_20241115['H3_Pedestal_Axial_elevation_temp_offset_average']) * axial_slope 

loads_inflow_20Hz_20241115["H1_CF_Lift"] = loads_inflow_20Hz_20241115.H1_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241115["H2_CF_Lift"] = loads_inflow_20Hz_20241115.H2_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241115["H3_CF_Lift"] = loads_inflow_20Hz_20241115.H3_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23)

loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_elevation_offset'] = slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241115.H1_Elevation_mean+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_temp_stow_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_temp_oper_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H1_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241115["H1_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241115.H1_Torque_Tube_Left - loads_inflow_20Hz_20241115.H1_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_elevation_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_temp_stow_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_temp_oper_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H2_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241115["H2_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241115.H2_Torque_Tube_Left - loads_inflow_20Hz_20241115.H2_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_elevation_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241115.H3_Elevation_mean+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_temp_stow_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_temp_oper_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H3_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241115["H3_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241115.H3_Torque_Tube_Left - loads_inflow_20Hz_20241115.H3_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241115["H1_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241115["H1_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241115["H2_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241115["H2_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241115["H3_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241115["H3_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241115['H1_Pedestal_Torque_elevation_offset'] = slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241115.H1_Elevation_mean+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Torque_temp_stow_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Torque_temp_oper_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H1_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241115['H1_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241115['H1_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H1_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H1_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241115["H1_Pedestal_Torque"] = (loads_inflow_20Hz_20241115.H1_Pedestal_Torque - loads_inflow_20Hz_20241115.H1_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241115['H2_Pedestal_Torque_elevation_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Torque_temp_stow_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Torque_temp_oper_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H2_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241115['H2_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241115['H2_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H2_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H2_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241115["H2_Pedestal_Torque"] = (loads_inflow_20Hz_20241115.H2_Pedestal_Torque - loads_inflow_20Hz_20241115.H2_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241115['H3_Pedestal_Torque_elevation_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241115.H3_Elevation_mean+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241115['H3_Pedestal_Torque_temp_stow_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Torque_temp_oper_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H3_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241115['H3_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241115['H3_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H3_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H3_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241115["H3_Pedestal_Torque"] = (loads_inflow_20Hz_20241115.H3_Pedestal_Torque - loads_inflow_20Hz_20241115.H3_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241115["H1_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241115["H1_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241115["H2_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241115["H2_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241115["H3_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241115["H3_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_elevation_offset'] = slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241115.H1_Elevation_mean+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_temp_stow_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_temp_oper_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H1_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241115["H1_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241115.H1_Pedestal_Bend_1 - loads_inflow_20Hz_20241115.H1_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_elevation_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_temp_stow_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_temp_oper_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H2_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241115["H2_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241115.H2_Pedestal_Bend_1 - loads_inflow_20Hz_20241115.H2_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_elevation_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241115.H3_Elevation_mean+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_temp_stow_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_temp_oper_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H3_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241115["H3_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241115.H3_Pedestal_Bend_1 - loads_inflow_20Hz_20241115.H3_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241115["H1_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241115["H1_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241115["H2_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241115["H2_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241115["H3_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241115["H3_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_elevation_offset'] = slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241115.H1_Elevation_mean+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_temp_stow_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_temp_oper_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241115["H1_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241115['H1_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241115.H1_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_elevation_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_temp_stow_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_temp_oper_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241115["H2_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241115['H2_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241115.H2_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_elevation_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241115.H3_Elevation_mean+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_temp_stow_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_temp_oper_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241115["H3_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241115['H3_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241115.H3_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241115["H1_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241115["H1_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241115["H2_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241115["H2_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241115["H3_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241115["H3_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_elevation_offset'] = slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241115.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241115["H1_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241115.H1_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_elevation_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241115["H2_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241115.H2_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_elevation_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241115.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241115["H3_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241115.H3_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241115.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241115["H1_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241115['H1_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241115.H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241115["H2_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241115['H2_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241115.H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241115.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241115.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241115['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241115["H3_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241115['H3_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241115.H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241115["H1_DP1"] = loads_inflow_20Hz_20241115['H1_Differential_Pressure_1'] - H1_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241115["H1_DP2"] = loads_inflow_20Hz_20241115['H1_Differential_Pressure_2'] - H1_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241115["H1_DP3"] = loads_inflow_20Hz_20241115['H1_Differential_Pressure_3'] - H1_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241115["H2_DP1"] = loads_inflow_20Hz_20241115['H2_Differential_Pressure_1'] - H2_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241115["H2_DP2"] = loads_inflow_20Hz_20241115['H2_Differential_Pressure_2'] - H2_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241115["H2_DP3"] = loads_inflow_20Hz_20241115['H2_Differential_Pressure_3'] - H2_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241115["H3_DP1"] = loads_inflow_20Hz_20241115['H3_Differential_Pressure_1'] - H3_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241115["H3_DP2"] = loads_inflow_20Hz_20241115['H3_Differential_Pressure_2'] - H3_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241115["H3_DP3"] = loads_inflow_20Hz_20241115['H3_Differential_Pressure_3'] - H3_Differential_Pressure_3_elevation_offset_mean

A3 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 3) 
A2 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 2) 
A1 = 10.3*(11.23/5)*2  # heliostat width x 2 facet heights (differential pressure 1) 

x1 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 1) 
x2 = (11.23/5)*0.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 2) 
x3 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 3) 

loads_inflow_20Hz_names = loads_inflow_20Hz_20241115.columns

loads_inflow_20Hz_20241115["H1_DP_F_Normal"] = (loads_inflow_20Hz_20241115.H1_DP1*A1)+(loads_inflow_20Hz_20241115.H1_DP2*A2)+(loads_inflow_20Hz_20241115.H1_DP3*A3)
loads_inflow_20Hz_20241115["H1_DP_F_Drag"] = loads_inflow_20Hz_20241115.H1_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean))
loads_inflow_20Hz_20241115["H1_DP_F_Lift"] = loads_inflow_20Hz_20241115.H1_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean))
loads_inflow_20Hz_20241115["H1_DP_M_Hy"] = (loads_inflow_20Hz_20241115.H1_DP1*A1*x1)+(loads_inflow_20Hz_20241115.H1_DP2*A2*x2)-(loads_inflow_20Hz_20241115.H1_DP3*A3*x3)

loads_inflow_20Hz_20241115["H2_DP_F_Normal"] = (loads_inflow_20Hz_20241115.H2_DP1*A1)+(loads_inflow_20Hz_20241115.H2_DP2*A2)+(loads_inflow_20Hz_20241115.H2_DP3*A3)
loads_inflow_20Hz_20241115["H2_DP_F_Drag"] = loads_inflow_20Hz_20241115.H2_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean))
loads_inflow_20Hz_20241115["H2_DP_F_Lift"] = loads_inflow_20Hz_20241115.H2_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean))
loads_inflow_20Hz_20241115["H2_DP_M_Hy"] = (loads_inflow_20Hz_20241115.H2_DP1*A1*x1)+(loads_inflow_20Hz_20241115.H2_DP2*A2*x2)-(loads_inflow_20Hz_20241115.H2_DP3*A3*x3)

loads_inflow_20Hz_20241115["H3_DP_F_Normal"] = (loads_inflow_20Hz_20241115.H3_DP1*A1)+(loads_inflow_20Hz_20241115.H3_DP2*A2)+(loads_inflow_20Hz_20241115.H3_DP3*A3)
loads_inflow_20Hz_20241115["H3_DP_F_Drag"] = loads_inflow_20Hz_20241115.H3_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean))
loads_inflow_20Hz_20241115["H3_DP_F_Lift"] = loads_inflow_20Hz_20241115.H3_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean))
loads_inflow_20Hz_20241115["H3_DP_M_Hy"] = (loads_inflow_20Hz_20241115.H3_DP1*A1*x1)+(loads_inflow_20Hz_20241115.H3_DP2*A2*x2)-(loads_inflow_20Hz_20241115.H3_DP3*A3*x3)

loads_inflow_20Hz_20241115["H1_DP_CF_Lift"] = loads_inflow_20Hz_20241115.H1_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241115["H2_DP_CF_Lift"] = loads_inflow_20Hz_20241115.H2_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241115["H3_DP_CF_Lift"] = loads_inflow_20Hz_20241115.H3_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23)

loads_inflow_20Hz_20241115["H1_DP_CMHy"] = loads_inflow_20Hz_20241115.H1_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241115["H2_DP_CMHy"] = loads_inflow_20Hz_20241115.H2_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241115["H3_DP_CMHy"] = loads_inflow_20Hz_20241115.H3_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241115.p, loads_inflow_20Hz_20241115.RH, loads_inflow_20Hz_20241115.Temp)*loads_inflow_20Hz_20241115.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean), -1, 0.3*math.pi, -0.053+math.pi/2, -0.1)
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0.05)
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean), 1, 0.4*math.pi, -0.053, 0.05)
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean), 1, 0.3*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H1_Elevation_mean), 1, 0.28*math.pi, 0, 0)
loads_inflow_20Hz_20241115["H1_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H1_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean), -1, 0.31*math.pi, math.pi/2, 0.05)
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H2_Elevation_mean), 1, 0.33*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H2_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H2_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean), -1, 0.34*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean), -1, 0.32*math.pi, math.pi/2, 0)
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean), 1, 0.34*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241115.H3_Elevation_mean), 1, 0.29*math.pi, -0.053, 0)
loads_inflow_20Hz_20241115["H3_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241115.H3_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241115[["H1_Elevation_mean","H2_Elevation_mean","H3_Elevation_mean","H1_F_Lift","H2_F_Lift","H3_F_Lift","H1_Torque_Tube_Torque_Left","H2_Torque_Tube_Torque_Left","H3_Torque_Tube_Torque_Left","H1_Pedestal_Torque","H2_Pedestal_Torque","H3_Pedestal_Torque","H1_Pedestal_Bend_1","H2_Pedestal_Bend_1","H3_Pedestal_Bend_1","H1_Pedestal_Bend_2","H2_Pedestal_Bend_2","H3_Pedestal_Bend_2","H1_Support_Frame_Bending_Top","H2_Support_Frame_Bending_Top","H3_Support_Frame_Bending_Top","H1_DP1","H1_DP2","H1_DP3","H2_DP1","H2_DP2","H2_DP3","H3_DP1","H3_DP2","H3_DP3","H1_Mirror_Displacement_Top","H2_Mirror_Displacement_Top","H3_Mirror_Displacement_Top","H1_Mirror_Displacement_Bottom","H2_Mirror_Displacement_Bottom","H3_Mirror_Displacement_Bottom","H1_Support_Frame_Accel_1_X_processed","H1_Support_Frame_Accel_2_X_processed","H1_Support_Frame_Accel_3_X_processed","H1_Support_Frame_Accel_4_X_processed","H1_Support_Frame_Accel_1_Y_processed","H1_Support_Frame_Accel_2_Y_processed","H1_Support_Frame_Accel_3_Y_processed","H1_Support_Frame_Accel_4_Y_processed","H2_Support_Frame_Accel_1_X_processed","H2_Support_Frame_Accel_2_X_processed","H2_Support_Frame_Accel_3_X_processed","H2_Support_Frame_Accel_4_X_processed","H2_Support_Frame_Accel_1_Y_processed","H2_Support_Frame_Accel_2_Y_processed","H2_Support_Frame_Accel_3_Y_processed","H2_Support_Frame_Accel_4_Y_processed","H3_Support_Frame_Accel_1_X_processed","H3_Support_Frame_Accel_2_X_processed","H3_Support_Frame_Accel_3_X_processed","H3_Support_Frame_Accel_4_X_processed","H3_Support_Frame_Accel_1_Y_processed","H3_Support_Frame_Accel_2_Y_processed","H3_Support_Frame_Accel_3_Y_processed","H3_Support_Frame_Accel_4_Y_processed"]].to_parquet("Loads_20Hz_2024-11-15_00h_to_2024-11-16_00h.parquet")

# Convert time zone to local
pacific_tz = pytz.timezone('America/Los_Angeles')

# Assuming 'index' of DataFrames is already in UTC
loads_inflow_20Hz_20241115.index = loads_inflow_20Hz_20241115.index.tz_localize('UTC').tz_convert(pacific_tz)

loads_mast_20Hz_20241115.index = loads_mast_20Hz_20241115.index.tz_localize('UTC').tz_convert(pacific_tz)

#%% Mean and peak-peak load coefficients (loads + inflow 18 November 2024)

loads_20Hz_20241118 = pd.read_pickle('Loads_fastdata_20Hz_2024-11-18_to_2024-11-19.pkl')
inflow_20Hz_20241118 = pd.read_pickle('Inflow_20Hz_2024-11-18_to_2024-11-19.pkl')
mast_20Hz_20241118 = pd.read_pickle('mast_20Hz_2024-11-18_to_2024-11-19.pkl')

axial_slope = 82075.28 # kN/V/V
torque_tube_slopeT = 191171 # kNm/V/V	 
pedestal_bending_slopeM = 205961.1	 # kNm/V/V	 
pedestal_torque_slopeT =	213386.9 # kNm/V/V
support_frame_bending_slopeM = 395.6838	#kNm/V/V

loads_20Hz_20241118['H1_Elevation_mean'] = -0.5*(loads_20Hz_20241118['H1_Elevation_Left '] + loads_20Hz_20241118['H1_Elevation_Right '])
loads_20Hz_20241118['H2_Elevation_mean'] = -0.5*(loads_20Hz_20241118['H2_Elevation_Left '] + loads_20Hz_20241118['H2_Elevation_Right '])
loads_20Hz_20241118['H3_Elevation_mean'] = -0.5*(loads_20Hz_20241118['H3_Elevation_Left '] + loads_20Hz_20241118['H3_Elevation_Right '])

loads_inflow_20Hz_20241118 = pd.merge(loads_20Hz_20241118, inflow_20Hz_20241118, left_index=True, right_index=True, how="inner")
loads_mast_20Hz_20241118 = pd.merge(loads_20Hz_20241118, mast_20Hz_20241118, left_index=True, right_index=True, how="inner")
#loads = pd.merge(loads, H1[['State', 'AngAzData', 'AngElData']], left_index=True, right_index=True, suffixes=('', '_H1'))
    
loads_inflow_20Hz_20241118['H1_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241118['H1_Elevation_Left '] + loads_inflow_20Hz_20241118['H1_Elevation_Right '])
loads_inflow_20Hz_20241118['H2_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241118['H2_Elevation_Left '] + loads_inflow_20Hz_20241118['H2_Elevation_Right '])
loads_inflow_20Hz_20241118['H3_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241118['H3_Elevation_Left '] + loads_inflow_20Hz_20241118['H3_Elevation_Right '])

loads_inflow_20Hz_20241118['H1_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241118['H1_Elevation_Left ']-loads_inflow_20Hz_20241118['H1_Elevation_Right '])>2,loads_inflow_20Hz_20241118['H1_Elevation_Right '],loads_inflow_20Hz_20241118['H1_Elevation_mean'])
loads_inflow_20Hz_20241118['H2_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241118['H2_Elevation_Left ']-loads_inflow_20Hz_20241118['H2_Elevation_Right '])>2,loads_inflow_20Hz_20241118['H2_Elevation_Right '],loads_inflow_20Hz_20241118['H2_Elevation_mean'])
loads_inflow_20Hz_20241118['H3_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241118['H3_Elevation_Left ']-loads_inflow_20Hz_20241118['H3_Elevation_Right '])>2,loads_inflow_20Hz_20241118['H3_Elevation_Left '],loads_inflow_20Hz_20241118['H3_Elevation_mean'])

loads_inflow_20Hz_20241118['H1_Displacement_Top_temp_stow_offset'] = slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241118.Temp+intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241118['H2_Displacement_Top_temp_stow_offset'] = slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241118['H3_Displacement_Top_temp_stow_offset'] = slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241118['H1_Displacement_Top'] = loads_inflow_20Hz_20241118['H1_Mirror_Displacement_Top']-loads_inflow_20Hz_20241118['H1_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241118['H2_Displacement_Top'] = loads_inflow_20Hz_20241118['H2_Mirror_Displacement_Top']-loads_inflow_20Hz_20241118['H2_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241118['H3_Displacement_Top'] = loads_inflow_20Hz_20241118['H3_Mirror_Displacement_Top']-loads_inflow_20Hz_20241118['H3_Displacement_Top_temp_stow_offset']

loads_inflow_20Hz_20241118['H1_Displacement_Bottom_temp_stow_offset'] = slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241118.Temp+intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241118['H2_Displacement_Bottom_temp_stow_offset'] = slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241118['H3_Displacement_Bottom_temp_stow_offset'] = slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241118['H1_Displacement_Bottom'] = loads_inflow_20Hz_20241118['H1_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241118['H1_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241118['H2_Displacement_Bottom'] = loads_inflow_20Hz_20241118['H2_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241118['H2_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241118['H3_Displacement_Bottom'] = loads_inflow_20Hz_20241118['H3_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241118['H3_Displacement_Bottom_temp_stow_offset']

loads_inflow_20Hz_20241118["H1_F_Lift"] = (loads_inflow_20Hz_20241118['H1_Pedestal_Axial '] - H1_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241118["H2_F_Lift"] = (loads_inflow_20Hz_20241118['H2_Pedestal_Axial '] - H2_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_oper_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241118.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_stow_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*loads_inflow_20Hz_20241118.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Axial_temp_stow_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Axial_temp_oper_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_temp_stow_offset'] = 0.5*(loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_stow_offset']+loads_inflow_20Hz_20241118['H3_Pedestal_Axial_temp_stow_offset'])
loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_oper_offset']+loads_inflow_20Hz_20241118['H3_Pedestal_Axial_temp_oper_offset'])
loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_temp_stow_offset'])
loads_inflow_20Hz_20241118["H3_F_Lift"] = (loads_inflow_20Hz_20241118['H3_Pedestal_Axial '] - loads_inflow_20Hz_20241118['H3_Pedestal_Axial_elevation_temp_offset_average']) * axial_slope 

loads_inflow_20Hz_20241118["H1_CF_Lift"] = loads_inflow_20Hz_20241118.H1_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241118["H2_CF_Lift"] = loads_inflow_20Hz_20241118.H2_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241118["H3_CF_Lift"] = loads_inflow_20Hz_20241118.H3_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23)

loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_elevation_offset'] = slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241118.H1_Elevation_mean+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_temp_stow_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_temp_oper_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H1_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241118["H1_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241118.H1_Torque_Tube_Left - loads_inflow_20Hz_20241118.H1_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_elevation_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_temp_stow_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_temp_oper_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H2_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241118["H2_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241118.H2_Torque_Tube_Left - loads_inflow_20Hz_20241118.H2_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_elevation_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241118.H3_Elevation_mean+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_temp_stow_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_temp_oper_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H3_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241118["H3_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241118.H3_Torque_Tube_Left - loads_inflow_20Hz_20241118.H3_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241118["H1_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241118["H1_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241118["H2_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241118["H2_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241118["H3_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241118["H3_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241118['H1_Pedestal_Torque_elevation_offset'] = slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241118.H1_Elevation_mean+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Torque_temp_stow_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Torque_temp_oper_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H1_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241118['H1_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241118['H1_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H1_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H1_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241118["H1_Pedestal_Torque"] = (loads_inflow_20Hz_20241118.H1_Pedestal_Torque - loads_inflow_20Hz_20241118.H1_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241118['H2_Pedestal_Torque_elevation_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Torque_temp_stow_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Torque_temp_oper_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H2_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241118['H2_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241118['H2_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H2_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H2_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241118["H2_Pedestal_Torque"] = (loads_inflow_20Hz_20241118.H2_Pedestal_Torque - loads_inflow_20Hz_20241118.H2_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241118['H3_Pedestal_Torque_elevation_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241118.H3_Elevation_mean+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241118['H3_Pedestal_Torque_temp_stow_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Torque_temp_oper_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H3_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241118['H3_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241118['H3_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H3_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H3_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241118["H3_Pedestal_Torque"] = (loads_inflow_20Hz_20241118.H3_Pedestal_Torque - loads_inflow_20Hz_20241118.H3_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241118["H1_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241118["H1_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241118["H2_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241118["H2_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241118["H3_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241118["H3_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_elevation_offset'] = slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241118.H1_Elevation_mean+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_temp_stow_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_temp_oper_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H1_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241118["H1_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241118.H1_Pedestal_Bend_1 - loads_inflow_20Hz_20241118.H1_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_elevation_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_temp_stow_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_temp_oper_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H2_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241118["H2_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241118.H2_Pedestal_Bend_1 - loads_inflow_20Hz_20241118.H2_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_elevation_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241118.H3_Elevation_mean+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_temp_stow_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_temp_oper_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H3_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241118["H3_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241118.H3_Pedestal_Bend_1 - loads_inflow_20Hz_20241118.H3_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241118["H1_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241118["H1_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241118["H2_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241118["H2_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241118["H3_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241118["H3_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_elevation_offset'] = slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241118.H1_Elevation_mean+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_temp_stow_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_temp_oper_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241118["H1_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241118['H1_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241118.H1_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_elevation_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_temp_stow_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_temp_oper_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241118["H2_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241118['H2_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241118.H2_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_elevation_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241118.H3_Elevation_mean+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_temp_stow_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_temp_oper_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241118["H3_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241118['H3_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241118.H3_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241118["H1_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241118["H1_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241118["H2_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241118["H2_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241118["H3_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241118["H3_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_elevation_offset'] = slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241118.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241118["H1_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241118.H1_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_elevation_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241118["H2_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241118.H2_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_elevation_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241118.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241118["H3_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241118.H3_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241118.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241118["H1_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241118['H1_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241118.H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241118["H2_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241118['H2_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241118.H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241118.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241118.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241118['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241118["H3_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241118['H3_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241118.H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241118["H1_DP1"] = loads_inflow_20Hz_20241118['H1_Differential_Pressure_1'] - H1_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241118["H1_DP2"] = loads_inflow_20Hz_20241118['H1_Differential_Pressure_2'] - H1_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241118["H1_DP3"] = loads_inflow_20Hz_20241118['H1_Differential_Pressure_3'] - H1_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241118["H2_DP1"] = loads_inflow_20Hz_20241118['H2_Differential_Pressure_1'] - H2_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241118["H2_DP2"] = loads_inflow_20Hz_20241118['H2_Differential_Pressure_2'] - H2_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241118["H2_DP3"] = loads_inflow_20Hz_20241118['H2_Differential_Pressure_3'] - H2_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241118["H3_DP1"] = loads_inflow_20Hz_20241118['H3_Differential_Pressure_1'] - H3_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241118["H3_DP2"] = loads_inflow_20Hz_20241118['H3_Differential_Pressure_2'] - H3_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241118["H3_DP3"] = loads_inflow_20Hz_20241118['H3_Differential_Pressure_3'] - H3_Differential_Pressure_3_elevation_offset_mean

A3 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 3) 
A2 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 2) 
A1 = 10.3*(11.23/5)*2  # heliostat width x 2 facet heights (differential pressure 1) 

x1 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 1) 
x2 = (11.23/5)*0.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 2) 
x3 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 3) 

loads_inflow_20Hz_names = loads_inflow_20Hz_20241118.columns

loads_inflow_20Hz_20241118["H1_DP_F_Normal"] = (loads_inflow_20Hz_20241118.H1_DP1*A1)+(loads_inflow_20Hz_20241118.H1_DP2*A2)+(loads_inflow_20Hz_20241118.H1_DP3*A3)
loads_inflow_20Hz_20241118["H1_DP_F_Drag"] = loads_inflow_20Hz_20241118.H1_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean))
loads_inflow_20Hz_20241118["H1_DP_F_Lift"] = loads_inflow_20Hz_20241118.H1_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean))
loads_inflow_20Hz_20241118["H1_DP_M_Hy"] = (loads_inflow_20Hz_20241118.H1_DP1*A1*x1)+(loads_inflow_20Hz_20241118.H1_DP2*A2*x2)-(loads_inflow_20Hz_20241118.H1_DP3*A3*x3)

loads_inflow_20Hz_20241118["H2_DP_F_Normal"] = (loads_inflow_20Hz_20241118.H2_DP1*A1)+(loads_inflow_20Hz_20241118.H2_DP2*A2)+(loads_inflow_20Hz_20241118.H2_DP3*A3)
loads_inflow_20Hz_20241118["H2_DP_F_Drag"] = loads_inflow_20Hz_20241118.H2_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean))
loads_inflow_20Hz_20241118["H2_DP_F_Lift"] = loads_inflow_20Hz_20241118.H2_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean))
loads_inflow_20Hz_20241118["H2_DP_M_Hy"] = (loads_inflow_20Hz_20241118.H2_DP1*A1*x1)+(loads_inflow_20Hz_20241118.H2_DP2*A2*x2)-(loads_inflow_20Hz_20241118.H2_DP3*A3*x3)

loads_inflow_20Hz_20241118["H3_DP_F_Normal"] = (loads_inflow_20Hz_20241118.H3_DP1*A1)+(loads_inflow_20Hz_20241118.H3_DP2*A2)+(loads_inflow_20Hz_20241118.H3_DP3*A3)
loads_inflow_20Hz_20241118["H3_DP_F_Drag"] = loads_inflow_20Hz_20241118.H3_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean))
loads_inflow_20Hz_20241118["H3_DP_F_Lift"] = loads_inflow_20Hz_20241118.H3_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean))
loads_inflow_20Hz_20241118["H3_DP_M_Hy"] = (loads_inflow_20Hz_20241118.H3_DP1*A1*x1)+(loads_inflow_20Hz_20241118.H3_DP2*A2*x2)-(loads_inflow_20Hz_20241118.H3_DP3*A3*x3)

loads_inflow_20Hz_20241118["H1_DP_CF_Lift"] = loads_inflow_20Hz_20241118.H1_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241118["H2_DP_CF_Lift"] = loads_inflow_20Hz_20241118.H2_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241118["H3_DP_CF_Lift"] = loads_inflow_20Hz_20241118.H3_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23)

loads_inflow_20Hz_20241118["H1_DP_CMHy"] = loads_inflow_20Hz_20241118.H1_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241118["H2_DP_CMHy"] = loads_inflow_20Hz_20241118.H2_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241118["H3_DP_CMHy"] = loads_inflow_20Hz_20241118.H3_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241118.p, loads_inflow_20Hz_20241118.RH, loads_inflow_20Hz_20241118.Temp)*loads_inflow_20Hz_20241118.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean), -1, 0.3*math.pi, -0.053+math.pi/2, -0.1)
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0.05)
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean), 1, 0.4*math.pi, -0.053, 0.05)
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean), 1, 0.3*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H1_Elevation_mean), 1, 0.28*math.pi, 0, 0)
loads_inflow_20Hz_20241118["H1_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H1_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean), -1, 0.31*math.pi, math.pi/2, 0.05)
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H2_Elevation_mean), 1, 0.33*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H2_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H2_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean), -1, 0.34*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean), -1, 0.32*math.pi, math.pi/2, 0)
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean), 1, 0.34*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241118.H3_Elevation_mean), 1, 0.29*math.pi, -0.053, 0)
loads_inflow_20Hz_20241118["H3_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241118.H3_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241118[["H1_Elevation_mean","H2_Elevation_mean","H3_Elevation_mean","H1_F_Lift","H2_F_Lift","H3_F_Lift","H1_Torque_Tube_Torque_Left","H2_Torque_Tube_Torque_Left","H3_Torque_Tube_Torque_Left","H1_Pedestal_Torque","H2_Pedestal_Torque","H3_Pedestal_Torque","H1_Pedestal_Bend_1","H2_Pedestal_Bend_1","H3_Pedestal_Bend_1","H1_Pedestal_Bend_2","H2_Pedestal_Bend_2","H3_Pedestal_Bend_2","H1_Support_Frame_Bending_Top","H2_Support_Frame_Bending_Top","H3_Support_Frame_Bending_Top","H1_DP1","H1_DP2","H1_DP3","H2_DP1","H2_DP2","H2_DP3","H3_DP1","H3_DP2","H3_DP3","H1_Mirror_Displacement_Top","H2_Mirror_Displacement_Top","H3_Mirror_Displacement_Top","H1_Mirror_Displacement_Bottom","H2_Mirror_Displacement_Bottom","H3_Mirror_Displacement_Bottom","H1_Support_Frame_Accel_1_X_processed","H1_Support_Frame_Accel_2_X_processed","H1_Support_Frame_Accel_3_X_processed","H1_Support_Frame_Accel_4_X_processed","H1_Support_Frame_Accel_1_Y_processed","H1_Support_Frame_Accel_2_Y_processed","H1_Support_Frame_Accel_3_Y_processed","H1_Support_Frame_Accel_4_Y_processed","H2_Support_Frame_Accel_1_X_processed","H2_Support_Frame_Accel_2_X_processed","H2_Support_Frame_Accel_3_X_processed","H2_Support_Frame_Accel_4_X_processed","H2_Support_Frame_Accel_1_Y_processed","H2_Support_Frame_Accel_2_Y_processed","H2_Support_Frame_Accel_3_Y_processed","H2_Support_Frame_Accel_4_Y_processed","H3_Support_Frame_Accel_1_X_processed","H3_Support_Frame_Accel_2_X_processed","H3_Support_Frame_Accel_3_X_processed","H3_Support_Frame_Accel_4_X_processed","H3_Support_Frame_Accel_1_Y_processed","H3_Support_Frame_Accel_2_Y_processed","H3_Support_Frame_Accel_3_Y_processed","H3_Support_Frame_Accel_4_Y_processed"]].to_parquet("Loads_20Hz_2024-11-18_00h_to_2024-11-19_00h.parquet")

# Convert time zone to local
pacific_tz = pytz.timezone('America/Los_Angeles')

# Assuming 'index' of DataFrames is already in UTC
loads_inflow_20Hz_20241118.index = loads_inflow_20Hz_20241118.index.tz_localize('UTC').tz_convert(pacific_tz)

loads_mast_20Hz_20241118.index = loads_mast_20Hz_20241118.index.tz_localize('UTC').tz_convert(pacific_tz)

#%% Mean and peak-peak load coefficients (loads + inflow 20 November 2024)

loads_20Hz_20241120 = pd.read_pickle('Loads_fastdata_20Hz_2024-11-20_to_2024-11-21.pkl')
inflow_20Hz_20241120 = pd.read_pickle('Inflow_20Hz_2024-11-20_to_2024-11-21.pkl')
mast_20Hz_20241120 = pd.read_pickle('mast_20Hz_2024-11-20_to_2024-11-21.pkl')

axial_slope = 82075.28 # kN/V/V
torque_tube_slopeT = 191171 # kNm/V/V	 
pedestal_bending_slopeM = 205961.1	 # kNm/V/V	 
pedestal_torque_slopeT =	213386.9 # kNm/V/V
support_frame_bending_slopeM = 395.6838	#kNm/V/V

loads_20Hz_20241120['H1_Elevation_mean'] = -0.5*(loads_20Hz_20241120['H1_Elevation_Left '] + loads_20Hz_20241120['H1_Elevation_Right '])
loads_20Hz_20241120['H2_Elevation_mean'] = -0.5*(loads_20Hz_20241120['H2_Elevation_Left '] + loads_20Hz_20241120['H2_Elevation_Right '])
loads_20Hz_20241120['H3_Elevation_mean'] = -0.5*(loads_20Hz_20241120['H3_Elevation_Left '] + loads_20Hz_20241120['H3_Elevation_Right '])

loads_inflow_20Hz_20241120 = pd.merge(loads_20Hz_20241120, inflow_20Hz_20241120, left_index=True, right_index=True, how="inner")
loads_mast_20Hz_20241120 = pd.merge(loads_20Hz_20241120, mast_20Hz_20241120, left_index=True, right_index=True, how="inner")
#loads = pd.merge(loads, H1[['State', 'AngAzData', 'AngElData']], left_index=True, right_index=True, suffixes=('', '_H1'))
    
loads_inflow_20Hz_20241120['H1_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241120['H1_Elevation_Left '] + loads_inflow_20Hz_20241120['H1_Elevation_Right '])
loads_inflow_20Hz_20241120['H2_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241120['H2_Elevation_Left '] + loads_inflow_20Hz_20241120['H2_Elevation_Right '])
loads_inflow_20Hz_20241120['H3_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241120['H3_Elevation_Left '] + loads_inflow_20Hz_20241120['H3_Elevation_Right '])

loads_inflow_20Hz_20241120['H1_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241120['H1_Elevation_Left ']-loads_inflow_20Hz_20241120['H1_Elevation_Right '])>2,loads_inflow_20Hz_20241120['H1_Elevation_Right '],loads_inflow_20Hz_20241120['H1_Elevation_mean'])
loads_inflow_20Hz_20241120['H2_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241120['H2_Elevation_Left ']-loads_inflow_20Hz_20241120['H2_Elevation_Right '])>2,loads_inflow_20Hz_20241120['H2_Elevation_Right '],loads_inflow_20Hz_20241120['H2_Elevation_mean'])
loads_inflow_20Hz_20241120['H3_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241120['H3_Elevation_Left ']-loads_inflow_20Hz_20241120['H3_Elevation_Right '])>2,loads_inflow_20Hz_20241120['H3_Elevation_Left '],loads_inflow_20Hz_20241120['H3_Elevation_mean'])

loads_inflow_20Hz_20241120['H1_Displacement_Top_temp_stow_offset'] = slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241120.Temp+intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241120['H2_Displacement_Top_temp_stow_offset'] = slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241120['H3_Displacement_Top_temp_stow_offset'] = slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241120['H1_Displacement_Top'] = loads_inflow_20Hz_20241120['H1_Mirror_Displacement_Top']-loads_inflow_20Hz_20241120['H1_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241120['H2_Displacement_Top'] = loads_inflow_20Hz_20241120['H2_Mirror_Displacement_Top']-loads_inflow_20Hz_20241120['H2_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241120['H3_Displacement_Top'] = loads_inflow_20Hz_20241120['H3_Mirror_Displacement_Top']-loads_inflow_20Hz_20241120['H3_Displacement_Top_temp_stow_offset']

loads_inflow_20Hz_20241120['H1_Displacement_Bottom_temp_stow_offset'] = slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241120.Temp+intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241120['H2_Displacement_Bottom_temp_stow_offset'] = slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241120['H3_Displacement_Bottom_temp_stow_offset'] = slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241120['H1_Displacement_Bottom'] = loads_inflow_20Hz_20241120['H1_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241120['H1_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241120['H2_Displacement_Bottom'] = loads_inflow_20Hz_20241120['H2_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241120['H2_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241120['H3_Displacement_Bottom'] = loads_inflow_20Hz_20241120['H3_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241120['H3_Displacement_Bottom_temp_stow_offset']

loads_inflow_20Hz_20241120["H1_F_Lift"] = (loads_inflow_20Hz_20241120['H1_Pedestal_Axial '] - H1_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241120["H2_F_Lift"] = (loads_inflow_20Hz_20241120['H2_Pedestal_Axial '] - H2_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_oper_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241120.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_stow_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*loads_inflow_20Hz_20241120.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Axial_temp_stow_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Axial_temp_oper_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_temp_stow_offset'] = 0.5*(loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_stow_offset']+loads_inflow_20Hz_20241120['H3_Pedestal_Axial_temp_stow_offset'])
loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_oper_offset']+loads_inflow_20Hz_20241120['H3_Pedestal_Axial_temp_oper_offset'])
loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_temp_stow_offset'])
loads_inflow_20Hz_20241120["H3_F_Lift"] = (loads_inflow_20Hz_20241120['H3_Pedestal_Axial '] - loads_inflow_20Hz_20241120['H3_Pedestal_Axial_elevation_temp_offset_average']) * axial_slope 

loads_inflow_20Hz_20241120["H1_CF_Lift"] = loads_inflow_20Hz_20241120.H1_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23)
loads_inflow_20Hz_20241120["H2_CF_Lift"] = loads_inflow_20Hz_20241120.H2_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23)
loads_inflow_20Hz_20241120["H3_CF_Lift"] = loads_inflow_20Hz_20241120.H3_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23)

loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_elevation_offset'] = slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241120.H1_Elevation_mean+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_temp_stow_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_temp_oper_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H1_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241120["H1_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241120.H1_Torque_Tube_Left - loads_inflow_20Hz_20241120.H1_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_elevation_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_temp_stow_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_temp_oper_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H2_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241120["H2_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241120.H2_Torque_Tube_Left - loads_inflow_20Hz_20241120.H2_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_elevation_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241120.H3_Elevation_mean+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_temp_stow_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_temp_oper_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H3_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241120["H3_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241120.H3_Torque_Tube_Left - loads_inflow_20Hz_20241120.H3_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241120["H1_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241120["H1_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241120["H2_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241120["H2_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241120["H3_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241120["H3_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241120['H1_Pedestal_Torque_elevation_offset'] = slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241120.H1_Elevation_mean+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Torque_temp_stow_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Torque_temp_oper_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H1_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241120['H1_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241120['H1_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H1_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H1_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241120["H1_Pedestal_Torque"] = (loads_inflow_20Hz_20241120.H1_Pedestal_Torque - loads_inflow_20Hz_20241120.H1_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241120['H2_Pedestal_Torque_elevation_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Torque_temp_stow_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Torque_temp_oper_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H2_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241120['H2_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241120['H2_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H2_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H2_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241120["H2_Pedestal_Torque"] = (loads_inflow_20Hz_20241120.H2_Pedestal_Torque - loads_inflow_20Hz_20241120.H2_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241120['H3_Pedestal_Torque_elevation_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241120.H3_Elevation_mean+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241120['H3_Pedestal_Torque_temp_stow_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Torque_temp_oper_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H3_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241120['H3_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241120['H3_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H3_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H3_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241120["H3_Pedestal_Torque"] = (loads_inflow_20Hz_20241120.H3_Pedestal_Torque - loads_inflow_20Hz_20241120.H3_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241120["H1_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241120["H1_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241120["H2_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241120["H2_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241120["H3_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241120["H3_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_elevation_offset'] = slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241120.H1_Elevation_mean+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_temp_stow_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_temp_oper_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H1_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241120["H1_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241120.H1_Pedestal_Bend_1 - loads_inflow_20Hz_20241120.H1_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_elevation_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_temp_stow_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_temp_oper_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H2_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241120["H2_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241120.H2_Pedestal_Bend_1 - loads_inflow_20Hz_20241120.H2_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_elevation_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241120.H3_Elevation_mean+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_temp_stow_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_temp_oper_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H3_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241120["H3_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241120.H3_Pedestal_Bend_1 - loads_inflow_20Hz_20241120.H3_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241120["H1_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241120["H1_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241120["H2_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241120["H2_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241120["H3_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241120["H3_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_elevation_offset'] = slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241120.H1_Elevation_mean+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_temp_stow_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_temp_oper_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241120["H1_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241120['H1_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241120.H1_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_elevation_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_temp_stow_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_temp_oper_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241120["H2_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241120['H2_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241120.H2_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_elevation_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241120.H3_Elevation_mean+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_temp_stow_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_temp_oper_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241120["H3_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241120['H3_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241120.H3_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241120["H1_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241120["H1_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241120["H2_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241120["H2_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241120["H3_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241120["H3_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_elevation_offset'] = slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241120.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241120["H1_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241120.H1_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_elevation_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241120["H2_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241120.H2_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_elevation_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241120.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241120["H3_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241120.H3_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241120.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241120["H1_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241120['H1_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241120.H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241120["H2_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241120['H2_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241120.H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241120.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241120.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241120['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241120["H3_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241120['H3_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241120.H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241120["H1_DP1"] = loads_inflow_20Hz_20241120['H1_Differential_Pressure_1'] - H1_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241120["H1_DP2"] = loads_inflow_20Hz_20241120['H1_Differential_Pressure_2'] - H1_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241120["H1_DP3"] = loads_inflow_20Hz_20241120['H1_Differential_Pressure_3'] - H1_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241120["H2_DP1"] = loads_inflow_20Hz_20241120['H2_Differential_Pressure_1'] - H2_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241120["H2_DP2"] = loads_inflow_20Hz_20241120['H2_Differential_Pressure_2'] - H2_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241120["H2_DP3"] = loads_inflow_20Hz_20241120['H2_Differential_Pressure_3'] - H2_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241120["H3_DP1"] = loads_inflow_20Hz_20241120['H3_Differential_Pressure_1'] - H3_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241120["H3_DP2"] = loads_inflow_20Hz_20241120['H3_Differential_Pressure_2'] - H3_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241120["H3_DP3"] = loads_inflow_20Hz_20241120['H3_Differential_Pressure_3'] - H3_Differential_Pressure_3_elevation_offset_mean

A3 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 3) 
A2 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 2) 
A1 = 10.3*(11.23/5)*2  # heliostat width x 2 facet heights (differential pressure 1) 

x1 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 1) 
x2 = (11.23/5)*0.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 2) 
x3 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 3) 

loads_inflow_20Hz_names = loads_inflow_20Hz_20241120.columns

loads_inflow_20Hz_20241120["H1_DP_F_Normal"] = (loads_inflow_20Hz_20241120.H1_DP1*A1)+(loads_inflow_20Hz_20241120.H1_DP2*A2)+(loads_inflow_20Hz_20241120.H1_DP3*A3)
loads_inflow_20Hz_20241120["H1_DP_F_Drag"] = loads_inflow_20Hz_20241120.H1_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean))
loads_inflow_20Hz_20241120["H1_DP_F_Lift"] = loads_inflow_20Hz_20241120.H1_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean))
loads_inflow_20Hz_20241120["H1_DP_M_Hy"] = (loads_inflow_20Hz_20241120.H1_DP1*A1*x1)+(loads_inflow_20Hz_20241120.H1_DP2*A2*x2)-(loads_inflow_20Hz_20241120.H1_DP3*A3*x3)

loads_inflow_20Hz_20241120["H2_DP_F_Normal"] = (loads_inflow_20Hz_20241120.H2_DP1*A1)+(loads_inflow_20Hz_20241120.H2_DP2*A2)+(loads_inflow_20Hz_20241120.H2_DP3*A3)
loads_inflow_20Hz_20241120["H2_DP_F_Drag"] = loads_inflow_20Hz_20241120.H2_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean))
loads_inflow_20Hz_20241120["H2_DP_F_Lift"] = loads_inflow_20Hz_20241120.H2_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean))
loads_inflow_20Hz_20241120["H2_DP_M_Hy"] = (loads_inflow_20Hz_20241120.H2_DP1*A1*x1)+(loads_inflow_20Hz_20241120.H2_DP2*A2*x2)-(loads_inflow_20Hz_20241120.H2_DP3*A3*x3)

loads_inflow_20Hz_20241120["H3_DP_F_Normal"] = (loads_inflow_20Hz_20241120.H3_DP1*A1)+(loads_inflow_20Hz_20241120.H3_DP2*A2)+(loads_inflow_20Hz_20241120.H3_DP3*A3)
loads_inflow_20Hz_20241120["H3_DP_F_Drag"] = loads_inflow_20Hz_20241120.H3_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean))
loads_inflow_20Hz_20241120["H3_DP_F_Lift"] = loads_inflow_20Hz_20241120.H3_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean))
loads_inflow_20Hz_20241120["H3_DP_M_Hy"] = (loads_inflow_20Hz_20241120.H3_DP1*A1*x1)+(loads_inflow_20Hz_20241120.H3_DP2*A2*x2)-(loads_inflow_20Hz_20241120.H3_DP3*A3*x3)

loads_inflow_20Hz_20241120["H1_DP_CF_Lift"] = loads_inflow_20Hz_20241120.H1_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23)
loads_inflow_20Hz_20241120["H2_DP_CF_Lift"] = loads_inflow_20Hz_20241120.H2_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23)
loads_inflow_20Hz_20241120["H3_DP_CF_Lift"] = loads_inflow_20Hz_20241120.H3_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23)

loads_inflow_20Hz_20241120["H1_DP_CMHy"] = loads_inflow_20Hz_20241120.H1_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241120["H2_DP_CMHy"] = loads_inflow_20Hz_20241120.H2_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241120["H3_DP_CMHy"] = loads_inflow_20Hz_20241120.H3_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241120.p, loads_inflow_20Hz_20241120.RH, loads_inflow_20Hz_20241120.Temp)*loads_inflow_20Hz_20241120.wspd_Top**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean), -1, 0.3*math.pi, -0.053+math.pi/2, -0.1)
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0.05)
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean), 1, 0.4*math.pi, -0.053, 0.05)
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean), 1, 0.3*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H1_Elevation_mean), 1, 0.28*math.pi, 0, 0)
loads_inflow_20Hz_20241120["H1_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H1_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean), -1, 0.31*math.pi, math.pi/2, 0.05)
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H2_Elevation_mean), 1, 0.33*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H2_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H2_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean), -1, 0.34*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean), -1, 0.32*math.pi, math.pi/2, 0)
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean), 1, 0.34*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241120.H3_Elevation_mean), 1, 0.29*math.pi, -0.053, 0)
loads_inflow_20Hz_20241120["H3_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241120.H3_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241120[["H1_Elevation_mean","H2_Elevation_mean","H3_Elevation_mean","H1_F_Lift","H2_F_Lift","H3_F_Lift","H1_Torque_Tube_Torque_Left","H2_Torque_Tube_Torque_Left","H3_Torque_Tube_Torque_Left","H1_Pedestal_Torque","H2_Pedestal_Torque","H3_Pedestal_Torque","H1_Pedestal_Bend_1","H2_Pedestal_Bend_1","H3_Pedestal_Bend_1","H1_Pedestal_Bend_2","H2_Pedestal_Bend_2","H3_Pedestal_Bend_2","H1_Support_Frame_Bending_Top","H2_Support_Frame_Bending_Top","H3_Support_Frame_Bending_Top","H1_DP1","H1_DP2","H1_DP3","H2_DP1","H2_DP2","H2_DP3","H3_DP1","H3_DP2","H3_DP3","H1_Mirror_Displacement_Top","H2_Mirror_Displacement_Top","H3_Mirror_Displacement_Top","H1_Mirror_Displacement_Bottom","H2_Mirror_Displacement_Bottom","H3_Mirror_Displacement_Bottom","H1_Support_Frame_Accel_1_X_processed","H1_Support_Frame_Accel_2_X_processed","H1_Support_Frame_Accel_3_X_processed","H1_Support_Frame_Accel_4_X_processed","H1_Support_Frame_Accel_1_Y_processed","H1_Support_Frame_Accel_2_Y_processed","H1_Support_Frame_Accel_3_Y_processed","H1_Support_Frame_Accel_4_Y_processed","H2_Support_Frame_Accel_1_X_processed","H2_Support_Frame_Accel_2_X_processed","H2_Support_Frame_Accel_3_X_processed","H2_Support_Frame_Accel_4_X_processed","H2_Support_Frame_Accel_1_Y_processed","H2_Support_Frame_Accel_2_Y_processed","H2_Support_Frame_Accel_3_Y_processed","H2_Support_Frame_Accel_4_Y_processed","H3_Support_Frame_Accel_1_X_processed","H3_Support_Frame_Accel_2_X_processed","H3_Support_Frame_Accel_3_X_processed","H3_Support_Frame_Accel_4_X_processed","H3_Support_Frame_Accel_1_Y_processed","H3_Support_Frame_Accel_2_Y_processed","H3_Support_Frame_Accel_3_Y_processed","H3_Support_Frame_Accel_4_Y_processed"]].to_parquet("Loads_20Hz_2024-11-20_00h_to_2024-11-21_00h.parquet")

# Convert time zone to local
pacific_tz = pytz.timezone('America/Los_Angeles')

# Assuming 'index' of DataFrames is already in UTC
loads_inflow_20Hz_20241120.index = loads_inflow_20Hz_20241120.index.tz_localize('UTC').tz_convert(pacific_tz)

loads_mast_20Hz_20241120.index = loads_mast_20Hz_20241120.index.tz_localize('UTC').tz_convert(pacific_tz)


#%% Mean and peak-peak load coefficients (loads + inflow 21 November 2024)

loads_20Hz_20241121 = pd.read_pickle('Loads_fastdata_20Hz_2024-11-21_to_2024-11-22.pkl')
inflow_20Hz_20241121 = pd.read_pickle('Inflow_20Hz_2024-11-21_to_2024-11-22.pkl')
mast_20Hz_20241121 = pd.read_pickle('mast_20Hz_2024-11-21_to_2024-11-22.pkl')

axial_slope = 82075.28 # kN/V/V
torque_tube_slopeT = 191171 # kNm/V/V	 
pedestal_bending_slopeM = 205961.1	 # kNm/V/V	 
pedestal_torque_slopeT =	213386.9 # kNm/V/V
support_frame_bending_slopeM = 395.6838	#kNm/V/V

loads_20Hz_20241121['H1_Elevation_mean'] = -0.5*(loads_20Hz_20241121['H1_Elevation_Left '] + loads_20Hz_20241121['H1_Elevation_Right '])
loads_20Hz_20241121['H2_Elevation_mean'] = -0.5*(loads_20Hz_20241121['H2_Elevation_Left '] + loads_20Hz_20241121['H2_Elevation_Right '])
loads_20Hz_20241121['H3_Elevation_mean'] = -0.5*(loads_20Hz_20241121['H3_Elevation_Left '] + loads_20Hz_20241121['H3_Elevation_Right '])

loads_inflow_20Hz_20241121 = pd.merge(loads_20Hz_20241121, inflow_20Hz_20241121, left_index=True, right_index=True, how="inner")
loads_mast_20Hz_20241121 = pd.merge(loads_20Hz_20241121, mast_20Hz_20241121, left_index=True, right_index=True, how="inner")
#loads = pd.merge(loads, H1[['State', 'AngAzData', 'AngElData']], left_index=True, right_index=True, suffixes=('', '_H1'))
    
loads_inflow_20Hz_20241121['H1_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241121['H1_Elevation_Left '] + loads_inflow_20Hz_20241121['H1_Elevation_Right '])
loads_inflow_20Hz_20241121['H2_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241121['H2_Elevation_Left '] + loads_inflow_20Hz_20241121['H2_Elevation_Right '])
loads_inflow_20Hz_20241121['H3_Elevation_mean'] = -0.5*(loads_inflow_20Hz_20241121['H3_Elevation_Left '] + loads_inflow_20Hz_20241121['H3_Elevation_Right '])

loads_inflow_20Hz_20241121['H1_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241121['H1_Elevation_Left ']-loads_inflow_20Hz_20241121['H1_Elevation_Right '])>2,loads_inflow_20Hz_20241121['H1_Elevation_Right '],loads_inflow_20Hz_20241121['H1_Elevation_mean'])
loads_inflow_20Hz_20241121['H2_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241121['H2_Elevation_Left ']-loads_inflow_20Hz_20241121['H2_Elevation_Right '])>2,loads_inflow_20Hz_20241121['H2_Elevation_Right '],loads_inflow_20Hz_20241121['H2_Elevation_mean'])
loads_inflow_20Hz_20241121['H3_Elevation_mean'] = np.where(abs(loads_inflow_20Hz_20241121['H3_Elevation_Left ']-loads_inflow_20Hz_20241121['H3_Elevation_Right '])>2,loads_inflow_20Hz_20241121['H3_Elevation_Left '],loads_inflow_20Hz_20241121['H3_Elevation_mean'])

loads_inflow_20Hz_20241121['H1_Displacement_Top_temp_stow_offset'] = slope_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241121.Temp+intercept_H1_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241121['H2_Displacement_Top_temp_stow_offset'] = slope_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241121['H3_Displacement_Top_temp_stow_offset'] = slope_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Mirror_Displacement_Top_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241121['H1_Displacement_Top'] = loads_inflow_20Hz_20241121['H1_Mirror_Displacement_Top']-loads_inflow_20Hz_20241121['H1_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241121['H2_Displacement_Top'] = loads_inflow_20Hz_20241121['H2_Mirror_Displacement_Top']-loads_inflow_20Hz_20241121['H2_Displacement_Top_temp_stow_offset']
loads_inflow_20Hz_20241121['H3_Displacement_Top'] = loads_inflow_20Hz_20241121['H3_Mirror_Displacement_Top']-loads_inflow_20Hz_20241121['H3_Displacement_Top_temp_stow_offset']

loads_inflow_20Hz_20241121['H1_Displacement_Bottom_temp_stow_offset'] = slope_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241121.Temp+intercept_H1_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241121['H2_Displacement_Bottom_temp_stow_offset'] = slope_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241121['H3_Displacement_Bottom_temp_stow_offset'] = slope_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Mirror_Displacement_Bottom_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_stow_5deg_20241025_trend
loads_inflow_20Hz_20241121['H1_Displacement_Bottom'] = loads_inflow_20Hz_20241121['H1_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241121['H1_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241121['H2_Displacement_Bottom'] = loads_inflow_20Hz_20241121['H2_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241121['H2_Displacement_Bottom_temp_stow_offset']
loads_inflow_20Hz_20241121['H3_Displacement_Bottom'] = loads_inflow_20Hz_20241121['H3_Mirror_Displacement_Bottom']-loads_inflow_20Hz_20241121['H3_Displacement_Bottom_temp_stow_offset']

loads_inflow_20Hz_20241121["H1_F_Lift"] = (loads_inflow_20Hz_20241121['H1_Pedestal_Axial '] - H1_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241121["H2_F_Lift"] = (loads_inflow_20Hz_20241121['H2_Pedestal_Axial '] - H2_Pedestal_Axial_elevation_offset_mean) * axial_slope 
loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_oper_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241121.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_stow_offset'] = slope_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend*loads_inflow_20Hz_20241121.H3_Elevation_mean+intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Axial_temp_stow_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Axial_temp_oper_offset'] = intercept_H3_Pedestal_Axial_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation_05_80_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_temp_stow_offset'] = 0.5*(loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_stow_offset']+loads_inflow_20Hz_20241121['H3_Pedestal_Axial_temp_stow_offset'])
loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_oper_offset']+loads_inflow_20Hz_20241121['H3_Pedestal_Axial_temp_oper_offset'])
loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_temp_stow_offset'])
loads_inflow_20Hz_20241121["H3_F_Lift"] = (loads_inflow_20Hz_20241121['H3_Pedestal_Axial '] - loads_inflow_20Hz_20241121['H3_Pedestal_Axial_elevation_temp_offset_average']) * axial_slope 

loads_inflow_20Hz_20241121["H1_CF_Lift"] = loads_inflow_20Hz_20241121.H1_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241121["H2_CF_Lift"] = loads_inflow_20Hz_20241121.H2_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241121["H3_CF_Lift"] = loads_inflow_20Hz_20241121.H3_F_Lift*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23)

loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_elevation_offset'] = slope_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241121.H1_Elevation_mean+intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_temp_stow_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_temp_oper_offset'] = intercept_H1_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H1_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241121["H1_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241121.H1_Torque_Tube_Left - loads_inflow_20Hz_20241121.H1_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_elevation_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_temp_stow_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_temp_oper_offset'] = slope_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H2_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241121["H2_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241121.H2_Torque_Tube_Left - loads_inflow_20Hz_20241121.H2_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_elevation_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241121.H3_Elevation_mean+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_temp_stow_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_temp_oper_offset'] = slope_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Torque_Tube_Left_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_elevation_offset']+loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_temp_oper_offset'])
loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H3_Torque_Tube_Left_temp_stow_offset'])
loads_inflow_20Hz_20241121["H3_Torque_Tube_Torque_Left"] = (loads_inflow_20Hz_20241121.H3_Torque_Tube_Left - loads_inflow_20Hz_20241121.H3_Torque_Tube_Left_elevation_temp_offset_average) * torque_tube_slopeT

loads_inflow_20Hz_20241121["H1_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241121["H1_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241121["H2_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241121["H2_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241121["H3_Torque_Tube_Torque_Left_coefficient"] = loads_inflow_20Hz_20241121["H3_Torque_Tube_Torque_Left"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241121['H1_Pedestal_Torque_elevation_offset'] = slope_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241121.H1_Elevation_mean+intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Torque_temp_stow_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Torque_temp_oper_offset'] = intercept_H1_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H1_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241121['H1_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241121['H1_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H1_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H1_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241121["H1_Pedestal_Torque"] = (loads_inflow_20Hz_20241121.H1_Pedestal_Torque - loads_inflow_20Hz_20241121.H1_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241121['H2_Pedestal_Torque_elevation_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Torque_temp_stow_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Torque_temp_oper_offset'] = slope_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H2_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241121['H2_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241121['H2_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H2_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H2_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241121["H2_Pedestal_Torque"] = (loads_inflow_20Hz_20241121.H2_Pedestal_Torque - loads_inflow_20Hz_20241121.H2_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241121['H3_Pedestal_Torque_elevation_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241121.H3_Elevation_mean+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241121['H3_Pedestal_Torque_temp_stow_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Torque_temp_oper_offset'] = slope_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Pedestal_Torque_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Torque_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H3_Pedestal_Torque_elevation_offset']+loads_inflow_20Hz_20241121['H3_Pedestal_Torque_temp_oper_offset'])
loads_inflow_20Hz_20241121['H3_Pedestal_Torque_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H3_Pedestal_Torque_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H3_Pedestal_Torque_temp_stow_offset'])
loads_inflow_20Hz_20241121["H3_Pedestal_Torque"] = (loads_inflow_20Hz_20241121.H3_Pedestal_Torque - loads_inflow_20Hz_20241121.H3_Pedestal_Torque_elevation_temp_offset_average) * pedestal_torque_slopeT

loads_inflow_20Hz_20241121["H1_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241121["H1_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241121["H2_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241121["H2_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241121["H3_Pedestal_Torque_coefficient"] = loads_inflow_20Hz_20241121["H3_Pedestal_Torque"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_elevation_offset'] = slope_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241121.H1_Elevation_mean+intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_temp_stow_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_temp_oper_offset'] = intercept_H1_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H1_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241121["H1_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241121.H1_Pedestal_Bend_1 - loads_inflow_20Hz_20241121.H1_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_elevation_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_temp_stow_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_temp_oper_offset'] = slope_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H2_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241121["H2_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241121.H2_Pedestal_Bend_1 - loads_inflow_20Hz_20241121.H2_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_elevation_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241121.H3_Elevation_mean+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_temp_stow_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_temp_oper_offset'] = slope_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Pedestal_Bend_1_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_elevation_offset']+loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_temp_oper_offset'])
loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H3_Pedestal_Bend_1_temp_stow_offset'])
loads_inflow_20Hz_20241121["H3_Pedestal_Bend_1"] = (loads_inflow_20Hz_20241121.H3_Pedestal_Bend_1 - loads_inflow_20Hz_20241121.H3_Pedestal_Bend_1_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241121["H1_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241121["H1_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241121["H2_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241121["H2_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241121["H3_Pedestal_Bend_1_coefficient"] = loads_inflow_20Hz_20241121["H3_Pedestal_Bend_1"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_elevation_offset'] = slope_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241121.H1_Elevation_mean+intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_temp_stow_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_temp_oper_offset'] = intercept_H1_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241121["H1_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241121['H1_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241121.H1_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_elevation_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_temp_stow_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_temp_oper_offset'] = slope_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241121["H2_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241121['H2_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241121.H2_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_elevation_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241121.H3_Elevation_mean+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_temp_stow_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_temp_oper_offset'] = slope_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Pedestal_Bend_2_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_elevation_offset']+loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_temp_oper_offset'])
loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2_temp_stow_offset'])
loads_inflow_20Hz_20241121["H3_Pedestal_Bend_2"] = (loads_inflow_20Hz_20241121['H3_Pedestal_Bend_2 '] - loads_inflow_20Hz_20241121.H3_Pedestal_Bend_2_elevation_temp_offset_average) * pedestal_bending_slopeM

loads_inflow_20Hz_20241121["H1_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241121["H1_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241121["H2_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241121["H2_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*5.5)
loads_inflow_20Hz_20241121["H3_Pedestal_Bend_2_coefficient"] = loads_inflow_20Hz_20241121["H3_Pedestal_Bend_2"]*1000/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*5.5)

loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_elevation_offset'] = slope_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241121.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241121["H1_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241121.H1_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_elevation_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241121["H2_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241121.H2_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_elevation_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241121.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Support_Frame_Bending_Top_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_elevation_offset']+loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_temp_oper_offset'])
loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top_temp_stow_offset'])
loads_inflow_20Hz_20241121["H3_Support_Frame_Bending_Top"] = (loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Top'] - loads_inflow_20Hz_20241121.H3_Support_Frame_Bending_Top_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend*loads_inflow_20Hz_20241121.H1_Elevation_mean+intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_temp_stow_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_temp_oper_offset'] = intercept_H1_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_loads_corr_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H1_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241121["H1_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241121['H1_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241121.H1_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H2_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H2_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241121["H2_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241121['H2_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241121.H2_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_elevation_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave*loads_inflow_20Hz_20241121.H3_Elevation_mean+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_loads_corr_lowwind_operation_20241025_trend_ave
loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_temp_stow_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevation0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_temp_oper_offset'] = slope_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend*loads_inflow_20Hz_20241121.Temp+intercept_H3_Support_Frame_Bending_Bottom_elevation_azimuth_state_inflow_lowwind_2ms_nonzeros_elevationg0_Ts_binned_avg_trend
loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'] = 0.5*(loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_elevation_offset']+loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_temp_oper_offset'])
loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average'] = np.where(abs(loads_inflow_20Hz_20241121['H3_Elevation_mean'])>1.26,loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_elevation_temp_oper_offset'],loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom_temp_stow_offset'])
loads_inflow_20Hz_20241121["H3_Support_Frame_Bending_Bottom"] = (loads_inflow_20Hz_20241121['H3_Support_Frame_Bending_Bottom'] - loads_inflow_20Hz_20241121.H3_Support_Frame_Bending_Bottom_elevation_temp_offset_average) * support_frame_bending_slopeM

loads_inflow_20Hz_20241121["H1_DP1"] = loads_inflow_20Hz_20241121['H1_Differential_Pressure_1'] - H1_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241121["H1_DP2"] = loads_inflow_20Hz_20241121['H1_Differential_Pressure_2'] - H1_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241121["H1_DP3"] = loads_inflow_20Hz_20241121['H1_Differential_Pressure_3'] - H1_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241121["H2_DP1"] = loads_inflow_20Hz_20241121['H2_Differential_Pressure_1'] - H2_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241121["H2_DP2"] = loads_inflow_20Hz_20241121['H2_Differential_Pressure_2'] - H2_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241121["H2_DP3"] = loads_inflow_20Hz_20241121['H2_Differential_Pressure_3'] - H2_Differential_Pressure_3_elevation_offset_mean

loads_inflow_20Hz_20241121["H3_DP1"] = loads_inflow_20Hz_20241121['H3_Differential_Pressure_1'] - H3_Differential_Pressure_1_elevation_offset_mean
loads_inflow_20Hz_20241121["H3_DP2"] = loads_inflow_20Hz_20241121['H3_Differential_Pressure_2'] - H3_Differential_Pressure_2_elevation_offset_mean
loads_inflow_20Hz_20241121["H3_DP3"] = loads_inflow_20Hz_20241121['H3_Differential_Pressure_3'] - H3_Differential_Pressure_3_elevation_offset_mean

A3 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 3) 
A2 = 10.3*(11.23/5)*1.5  # heliostat width x 1.5 facet heights (differential pressure 2) 
A1 = 10.3*(11.23/5)*2  # heliostat width x 2 facet heights (differential pressure 1) 

x1 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 1) 
x2 = (11.23/5)*0.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 2) 
x3 = (11.23/5)*1.5  # heliostat height x 1.5 facet heights (vertical distance from central horizontal axis of surface to differential pressure 3) 

loads_inflow_20Hz_names = loads_inflow_20Hz_20241121.columns

loads_inflow_20Hz_20241121["H1_DP_F_Normal"] = (loads_inflow_20Hz_20241121.H1_DP1*A1)+(loads_inflow_20Hz_20241121.H1_DP2*A2)+(loads_inflow_20Hz_20241121.H1_DP3*A3)
loads_inflow_20Hz_20241121["H1_DP_F_Drag"] = loads_inflow_20Hz_20241121.H1_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean))
loads_inflow_20Hz_20241121["H1_DP_F_Lift"] = loads_inflow_20Hz_20241121.H1_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean))
loads_inflow_20Hz_20241121["H1_DP_M_Hy"] = (loads_inflow_20Hz_20241121.H1_DP1*A1*x1)+(loads_inflow_20Hz_20241121.H1_DP2*A2*x2)-(loads_inflow_20Hz_20241121.H1_DP3*A3*x3)

loads_inflow_20Hz_20241121["H2_DP_F_Normal"] = (loads_inflow_20Hz_20241121.H2_DP1*A1)+(loads_inflow_20Hz_20241121.H2_DP2*A2)+(loads_inflow_20Hz_20241121.H2_DP3*A3)
loads_inflow_20Hz_20241121["H2_DP_F_Drag"] = loads_inflow_20Hz_20241121.H2_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean))
loads_inflow_20Hz_20241121["H2_DP_F_Lift"] = loads_inflow_20Hz_20241121.H2_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean))
loads_inflow_20Hz_20241121["H2_DP_M_Hy"] = (loads_inflow_20Hz_20241121.H2_DP1*A1*x1)+(loads_inflow_20Hz_20241121.H2_DP2*A2*x2)-(loads_inflow_20Hz_20241121.H2_DP3*A3*x3)

loads_inflow_20Hz_20241121["H3_DP_F_Normal"] = (loads_inflow_20Hz_20241121.H3_DP1*A1)+(loads_inflow_20Hz_20241121.H3_DP2*A2)+(loads_inflow_20Hz_20241121.H3_DP3*A3)
loads_inflow_20Hz_20241121["H3_DP_F_Drag"] = loads_inflow_20Hz_20241121.H3_DP_F_Normal*np.sin(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean))
loads_inflow_20Hz_20241121["H3_DP_F_Lift"] = loads_inflow_20Hz_20241121.H3_DP_F_Normal*np.cos(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean))
loads_inflow_20Hz_20241121["H3_DP_M_Hy"] = (loads_inflow_20Hz_20241121.H3_DP1*A1*x1)+(loads_inflow_20Hz_20241121.H3_DP2*A2*x2)-(loads_inflow_20Hz_20241121.H3_DP3*A3*x3)

loads_inflow_20Hz_20241121["H1_DP_CF_Lift"] = loads_inflow_20Hz_20241121.H1_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241121["H2_DP_CF_Lift"] = loads_inflow_20Hz_20241121.H2_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23)
loads_inflow_20Hz_20241121["H3_DP_CF_Lift"] = loads_inflow_20Hz_20241121.H3_DP_F_Lift/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23)

loads_inflow_20Hz_20241121["H1_DP_CMHy"] = loads_inflow_20Hz_20241121.H1_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241121["H2_DP_CMHy"] = loads_inflow_20Hz_20241121.H2_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)
loads_inflow_20Hz_20241121["H3_DP_CMHy"] = loads_inflow_20Hz_20241121.H3_DP_M_Hy/(0.5*rho(loads_inflow_20Hz_20241121.p, loads_inflow_20Hz_20241121.RH, loads_inflow_20Hz_20241121.Temp)*loads_inflow_20Hz_20241121.wspd_Mid**2*10.3*11.23*11.23)

loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean), -1, 0.3*math.pi, -0.053+math.pi/2, -0.1)
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0.05)
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean), 1, 0.4*math.pi, -0.053, 0.05)
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean), 1, 0.3*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H1_Elevation_mean), 1, 0.28*math.pi, 0, 0)
loads_inflow_20Hz_20241121["H1_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H1_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean), -1, 0.33*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean), -1, 0.31*math.pi, math.pi/2, 0.05)
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean), 1, 0.35*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H2_Elevation_mean), 1, 0.33*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H2_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H2_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_1_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_1_X_processed"] = loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_X_offset
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_2_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean), -1, 0.34*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_2_X_processed"] = loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_2_X_offset
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_3_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean), -1, 0.32*math.pi, -0.053+math.pi/2, 0)
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_3_X_processed"] = loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_3_X_offset
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_4_X_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean), -1, 0.32*math.pi, math.pi/2, 0)
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_4_X_processed"] = loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_X - loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_4_X_offset

loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_1_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_1_Y_processed"] = loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_Y_offset
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_2_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean), 1, 0.34*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_2_Y_processed"] = loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_2_Y_offset
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_3_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean), 1, 0.32*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_3_Y_processed"] = loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_3_Y_offset
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_4_Y_offset"] = sine_function(np.radians(loads_inflow_20Hz_20241121.H3_Elevation_mean), 1, 0.29*math.pi, -0.053, 0)
loads_inflow_20Hz_20241121["H3_Support_Frame_Accel_4_Y_processed"] = loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_1_Y - loads_inflow_20Hz_20241121.H3_Support_Frame_Accel_4_Y_offset

loads_inflow_20Hz_20241121[["H1_Elevation_mean","H2_Elevation_mean","H3_Elevation_mean","H1_F_Lift","H2_F_Lift","H3_F_Lift","H1_Torque_Tube_Torque_Left","H2_Torque_Tube_Torque_Left","H3_Torque_Tube_Torque_Left","H1_Pedestal_Torque","H2_Pedestal_Torque","H3_Pedestal_Torque","H1_Pedestal_Bend_1","H2_Pedestal_Bend_1","H3_Pedestal_Bend_1","H1_Pedestal_Bend_2","H2_Pedestal_Bend_2","H3_Pedestal_Bend_2","H1_Support_Frame_Bending_Top","H2_Support_Frame_Bending_Top","H3_Support_Frame_Bending_Top","H1_DP1","H1_DP2","H1_DP3","H2_DP1","H2_DP2","H2_DP3","H3_DP1","H3_DP2","H3_DP3","H1_Mirror_Displacement_Top","H2_Mirror_Displacement_Top","H3_Mirror_Displacement_Top","H1_Mirror_Displacement_Bottom","H2_Mirror_Displacement_Bottom","H3_Mirror_Displacement_Bottom","H1_Support_Frame_Accel_1_X_processed","H1_Support_Frame_Accel_2_X_processed","H1_Support_Frame_Accel_3_X_processed","H1_Support_Frame_Accel_4_X_processed","H1_Support_Frame_Accel_1_Y_processed","H1_Support_Frame_Accel_2_Y_processed","H1_Support_Frame_Accel_3_Y_processed","H1_Support_Frame_Accel_4_Y_processed","H2_Support_Frame_Accel_1_X_processed","H2_Support_Frame_Accel_2_X_processed","H2_Support_Frame_Accel_3_X_processed","H2_Support_Frame_Accel_4_X_processed","H2_Support_Frame_Accel_1_Y_processed","H2_Support_Frame_Accel_2_Y_processed","H2_Support_Frame_Accel_3_Y_processed","H2_Support_Frame_Accel_4_Y_processed","H3_Support_Frame_Accel_1_X_processed","H3_Support_Frame_Accel_2_X_processed","H3_Support_Frame_Accel_3_X_processed","H3_Support_Frame_Accel_4_X_processed","H3_Support_Frame_Accel_1_Y_processed","H3_Support_Frame_Accel_2_Y_processed","H3_Support_Frame_Accel_3_Y_processed","H3_Support_Frame_Accel_4_Y_processed"]].to_parquet("Loads_20Hz_2024-11-21_00h_to_2024-11-22_00h.parquet")

# Convert time zone to local
pacific_tz = pytz.timezone('America/Los_Angeles')

# Assuming 'index' of DataFrames is already in UTC
loads_inflow_20Hz_20241121.index = loads_inflow_20Hz_20241121.index.tz_localize('UTC').tz_convert(pacific_tz)

loads_mast_20Hz_20241121.index = loads_mast_20Hz_20241121.index.tz_localize('UTC').tz_convert(pacific_tz)



