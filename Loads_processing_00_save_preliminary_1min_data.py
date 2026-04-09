import os
import pandas as pd
from nptdms import TdmsFile
import zipfile
import matplotlib.pyplot as plt
import sys
import glob
from itertools import product

sys.path.append("C:/Users/memes/CD Analysis")


from Functions_general import *
from Functions_loads_CD import *



years   = [2024,2025] # 
months  = np.arange(1,12) 
days    = np.arange(1,31)   # [14,15]   # 



#%% Read inflow data


# Read Sonic data

read_sonics = 1
if read_sonics == 1:
    
    path = 'Y:\Wind-data/Restricted/Projects/NSO/CrescentDunes_processed_met_tower_data_preliminary/'  # 'CD_processed_data_preliminary/'    #  
    
    
    
    inflow_files = []
    mast_files = []
    
    for year in years:
        year = str(year)
    
        for month in months:
            
            if year == '2024' and month<3: # no data before March 2024
                continue
            
            month = f'{month:02d}'
        
            for day in days:
                day = f'{day:02d}'
                  
                print (year, month, day) 
                
                inflow_files += sorted(glob.glob(f"{path}Inflow_Mast_1min_{year}-{month}-{day}_*.pkl"))
                mast_files += sorted(glob.glob(f"{path}Wake_Masts_1min_{year}-{month}-{day}_*.pkl"))
    
    
    inflow = pd.concat([pd.read_pickle(file) for file in inflow_files]).sort_index()
    inflow = inflow.sort_index()
    inflow.to_pickle('C:/Users/memes/CD Analysis/Inflow_1min_{inflow.index[0].date()}_to_{inflow.index[-1].date()}.pkl')

    mast = pd.concat([pd.read_pickle(file) for file in mast_files]).sort_index()
    mast = mast.sort_index()    
    mast.to_pickle('C:/Users/memes/CD Analysis/mast_1min_{mast.index[0].date()}_to_{mast.index[-1].date()}.pkl')




#%% Read loads data

read_loads = 1
if read_loads == 1:
    
    path = 'Y:\Wind-data/Restricted/Projects/NSO/CrescentDunes-Loads/FastData/'  # 'CD_processed_data_preliminary/'    #
    
    
    loads_files = []
    
    for year in years:
        year = str(year)
    
        for month in months:
            
            if year == '2024' and month<11: # no data before March 2024
                continue
            
            month = f'{month:02d}'
        
            for day in days:
                
                if year == '2024' and day<21: # no data before March 2024
                    continue
                
                day = f'{day:02d}'
                  
                print (year, month, day) 
                
                loads_files += sorted(glob.glob(f"{path}{year}-{month}-{day}/CrescentDunes_*_20Hz.tdms"))
    
    # Read all loads files and resample
    loads = read_multiple_tdms_file_into_dataframe(loads_files, resample_freq = "1min")   #
    
    # Do the initial postprocessing
    loads = loads_initial_postprocess(loads)
    
    # Save the resampled file
    loads.to_pickle(f'Loads_fastdata_1min_{loads.index[0].date()}_to_{loads.index[-1].date()}.pkl')
    
    

    # loads["H1_Wind_Speed"].plot()
    # inflow.wspd_Mid.plot()




#%% Read SCADA data and combine in one file


H1, H2, H3 = read_SCADA_file(paths = ['C:/Users/memes/CD Analysis/SCADA/EMS1/','C:/Users/memes/CD Analysis/SCADA/EMS2/'], 
                             filename_search_strings = [ "Report_*"])  #"Report_14_MAR_2024*.csv",


H1.to_pickle(f'SCADA_H1_1min_{H1.index[0].date()}_to_{H1.index[-1].date()}.pkl')
H2.to_pickle(f'SCADA_H2_1min_{H2.index[0].date()}_to_{H2.index[-1].date()}.pkl')
H3.to_pickle(f'SCADA_H3_1min_{H3.index[0].date()}_to_{H3.index[-1].date()}.pkl')


#%% Read SCADA data for one file (EMS1)


H1, H2, H3 = read_SCADA_file(paths = ['C:/Users/memes/CD Analysis/SCADA/EMS1/'], 
                             filename_search_strings = [ "Report_14_NOV_2024_23_00_07_PDT.csv"])  #"Report_14_MAR_2024*.csv",


H1.to_pickle(f'SCADA_EMS1_H1_1min_{H1.index[0].date()}_to_{H1.index[-1].date()}.pkl')
H2.to_pickle(f'SCADA_EMS1_H2_1min_{H2.index[0].date()}_to_{H2.index[-1].date()}.pkl')
H3.to_pickle(f'SCADA_EMS1_H3_1min_{H3.index[0].date()}_to_{H3.index[-1].date()}.pkl')



#%% Read SCADA data for one file (EMS2)


H1, H2, H3 = read_SCADA_file(paths = ['C:/Users/memes/CD Analysis/SCADA/EMS2/'], 
                             filename_search_strings = [ "Report_14_NOV_2024_23_00_06_PDT.csv"])  #"Report_14_MAR_2024*.csv",


H1.to_pickle(f'SCADA_EMS2_H1_1min_{H1.index[0].date()}_to_{H1.index[-1].date()}.pkl')
H2.to_pickle(f'SCADA_EMS2_H2_1min_{H2.index[0].date()}_to_{H2.index[-1].date()}.pkl')
H3.to_pickle(f'SCADA_EMS2_H3_1min_{H3.index[0].date()}_to_{H3.index[-1].date()}.pkl')



























