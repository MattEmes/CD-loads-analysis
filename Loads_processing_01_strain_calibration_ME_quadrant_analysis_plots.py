# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 10:45:51 2025

@author: memes
"""
from Functions_masts_CD import *
from Functions_loads_CD import *
from Functions_general import *
from Functions_calc_spectrum import *  
from Functions_spectrum import *


#%% Plot time series of load coefficients

import datetime

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H1_CF_Lift,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H2_CF_Lift,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H3_CF_Lift,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241028.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241028.index[0],color='black',linestyle='-.',linewidth=1.25)
#plt.xlabel("Time (October 28, 2024)")
plt.ylabel("CFz")
plt.ylim(-3, 3)    
plt.yticks([-3,-1.5,0,1.5,3])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,10,28,16,0), datetime.datetime(2024,10,28,22,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()
#plt.legend(loc='upper right',fontsize=10)

ax1 = fig.add_subplot(212)
#ax1.axvspan(pd.Timestamp(2024,10,28,18,20).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,18,57).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H1_Torque_Tube_Torque_Left_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H2_Torque_Tube_Torque_Left_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H3_Torque_Tube_Torque_Left_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241028.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241028.index[0],color='black',linestyle='-.',linewidth=1.25)
plt.ylim(-0.5, 0.5)    
#plt.title("Differential pressure 1")    
#plt.xlabel("Local time (November 18, 2024)")
plt.xlabel("Local time (October 28, 2024)")
plt.ylabel("CMHy")
plt.yticks([-0.5,-0.25,0,0.25,0.5])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,10,28,16,0), datetime.datetime(2024,10,28,22,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()

fig = plt.figure()
ax1 = fig.add_subplot(211)
#ax1.axvspan(pd.Timestamp(2024,10,28,18,20).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,18,57).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H1_Pedestal_Torque_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H2_Pedestal_Torque_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H3_Pedestal_Torque_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241028.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241028.index[0],color='black',linestyle='-.',linewidth=1.25)
plt.ylim(-0.5, 0.5)    
#plt.title("Differential pressure 1")    
#plt.xlabel("Local time (October 28, 2024)")
plt.ylabel("CMz")
plt.yticks([-0.5,-0.25,0,0.25,0.5])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,10,28,16,0), datetime.datetime(2024,10,28,22,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()
#plt.legend(loc='upper right',fontsize=10)

ax1 = fig.add_subplot(212)
#ax1.axvspan(pd.Timestamp(2024,10,28,18,20).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,18,57).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H1_Pedestal_Bend_2_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H2_Pedestal_Bend_2_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241028.index,loads_inflow_20Hz_20241028.H3_Pedestal_Bend_2_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241028.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241028.index[0],color='black',linestyle='-.',linewidth=1.25)  
#plt.title("Differential pressure 1")    
plt.xlabel("Local time (October 28, 2024)")
plt.ylabel("CMy")
plt.ylim(-1, 3)    
plt.yticks([-1,0,1,2,3])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,10,28,16,0), datetime.datetime(2024,10,28,22,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()


fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H1_CF_Lift,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H2_CF_Lift,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H3_CF_Lift,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241118.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241118.index[0],color='black',linestyle='-.',linewidth=1.25)
#plt.xlabel("Time (October 28, 2024)")
plt.ylabel("CFz")
plt.ylim(-3, 3)    
plt.yticks([-3,-1.5,0,1.5,3])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,18,14,0), datetime.datetime(2024,11,18,20,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()
#plt.legend(loc='upper right',fontsize=10)

ax1 = fig.add_subplot(212)
#ax1.axvspan(pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,11,18,17,00).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H1_Torque_Tube_Torque_Left_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H2_Torque_Tube_Torque_Left_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H3_Torque_Tube_Torque_Left_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241118.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241118.index[0],color='black',linestyle='-.',linewidth=1.25)
plt.ylim(-0.5, 0.5)    
#plt.title("Differential pressure 1")    
#plt.xlabel("Local time (November 18, 2024)")
plt.xlabel("Local time (November 18, 2024)")
plt.ylabel("CMHy")
plt.yticks([-0.5,-0.25,0,0.25,0.5])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,18,14,0), datetime.datetime(2024,11,18,20,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()

fig = plt.figure()
ax1 = fig.add_subplot(211)
#ax1.axvspan(pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,11,18,17,00).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H1_Pedestal_Torque_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H2_Pedestal_Torque_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H3_Pedestal_Torque_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241118.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241118.index[0],color='black',linestyle='-.',linewidth=1.25)
plt.ylim(-0.5, 0.5)    
#plt.title("Differential pressure 1")    
#plt.xlabel("Local time (October 28, 2024)")
plt.ylabel("CMz")
plt.yticks([-0.5,-0.25,0,0.25,0.5])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,18,14,0), datetime.datetime(2024,11,18,20,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()
#plt.legend(loc='upper right',fontsize=10)

ax1 = fig.add_subplot(212)
#ax1.axvspan(pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,11,18,17,00).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H1_Pedestal_Bend_2_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H2_Pedestal_Bend_2_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241118.index,loads_inflow_20Hz_20241118.H3_Pedestal_Bend_2_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241118.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241118.index[0],color='black',linestyle='-.',linewidth=1.25)  
#plt.title("Differential pressure 1")    
plt.xlabel("Local time (November 18, 2024)")
plt.ylabel("CMy")
plt.ylim(-1, 3)    
plt.yticks([-1,0,1,2,3])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,18,14,0), datetime.datetime(2024,11,18,20,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()


fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H1_CF_Lift,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H2_CF_Lift,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H3_CF_Lift,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241120.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241120.index[0],color='black',linestyle='-.',linewidth=1.25)
#plt.xlabel("Time (October 28, 2024)")
plt.ylabel("CFz")
plt.ylim(-3, 3)    
plt.yticks([-3,-1.5,0,1.5,3])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,20,14,0), datetime.datetime(2024,11,20,21,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()
#plt.legend(loc='upper right',fontsize=10)

ax1 = fig.add_subplot(212)
#ax1.axvspan(pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,11,18,17,00).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H1_Torque_Tube_Torque_Left_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H2_Torque_Tube_Torque_Left_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H3_Torque_Tube_Torque_Left_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241120.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241120.index[0],color='black',linestyle='-.',linewidth=1.25)
plt.ylim(-0.5, 0.5)    
#plt.title("Differential pressure 1")    
#plt.xlabel("Local time (November 18, 2024)")
plt.xlabel("Local time (November 20, 2024)")
plt.ylabel("CMHy")
plt.yticks([-0.5,-0.25,0,0.25,0.5])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,20,14,0), datetime.datetime(2024,11,20,21,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()

fig = plt.figure()
ax1 = fig.add_subplot(211)
#ax1.axvspan(pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,11,18,17,00).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H1_Pedestal_Torque_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H2_Pedestal_Torque_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H3_Pedestal_Torque_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241120.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241120.index[0],color='black',linestyle='-.',linewidth=1.25)
plt.ylim(-0.5, 0.5)    
#plt.title("Differential pressure 1")    
#plt.xlabel("Local time (October 28, 2024)")
plt.ylabel("CMz")
plt.yticks([-0.5,-0.25,0,0.25,0.5])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,20,14,0), datetime.datetime(2024,11,20,21,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()
#plt.legend(loc='upper right',fontsize=10)

ax1 = fig.add_subplot(212)
#ax1.axvspan(pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,11,18,17,00).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H1_Pedestal_Bend_2_coefficient,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H2_Pedestal_Bend_2_coefficient,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H3_Pedestal_Bend_2_coefficient,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241120.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241120.index[0],color='black',linestyle='-.',linewidth=1.25)  
#plt.title("Differential pressure 1")    
plt.xlabel("Local time (November 20, 2024)")
plt.ylabel("CMy")
plt.ylim(-1, 3)    
plt.yticks([-1,0,1,2,3])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,20,14,0), datetime.datetime(2024,11,20,21,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.axvspan(pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz),color='purple',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,11,18,17,00).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz),color='red',alpha=0.2)
#ax1.axvspan(pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz),pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz),color='maroon',alpha=0.2)
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H1_Elevation_mean,marker='.',color='#1f77b4',edgecolor='none',alpha=0.3,s=1,label='H1')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H2_Elevation_mean,marker='.',color='#ff7f0e',edgecolor='none',alpha=0.3,s=1,label='H2')
plt.scatter(loads_inflow_20Hz_20241120.index,loads_inflow_20Hz_20241120.H3_Elevation_mean,marker='.',color='#2ca02c',edgecolor='none',alpha=0.3,s=1,label='H3')
#plt.axvline(x=H3_stowed_times_20241120.index[0],color='black',linestyle='--',linewidth=1.25)
#plt.axvline(x=H1_stowed_times_20241120.index[0],color='black',linestyle='-.',linewidth=1.25)  
#plt.title("Differential pressure 1")    
plt.xlabel("Local time (November 20, 2024)")
plt.ylabel("Elevation angle")
#plt.ylim(-1, 3)    
#plt.yticks([-1,0,1,2,3])
#fig.autofmt_xdate()
plt.xlim([datetime.datetime(2024,11,20,14,0), datetime.datetime(2024,11,20,21,0)])
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=pacific_tz))
plt.tight_layout()



#%% Break into periods

loads_inflow_20Hz_20241028_1820_1850_operation = loads_inflow_20Hz_20241028[pd.Timestamp(2024,10,28,18,20).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz)]
loads_inflow_20Hz_20241028_1857_1927_stowH3 = loads_inflow_20Hz_20241028[pd.Timestamp(2024,10,28,18,57).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz)]
loads_inflow_20Hz_20241028_2030_2100_stow = loads_inflow_20Hz_20241028[pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz)]

loads_inflow_20Hz_20241115_2045_2115_operation = loads_inflow_20Hz_20241115[pd.Timestamp(2024,11,15,20,45).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,15,21,15).tz_localize('UTC').tz_convert(pacific_tz)]
loads_inflow_20Hz_20241115_1800_1830_stowH1H2 = loads_inflow_20Hz_20241115[pd.Timestamp(2024,11,15,18,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,15,18,30).tz_localize('UTC').tz_convert(pacific_tz)]
loads_inflow_20Hz_20241115_2130_2200_stow = loads_inflow_20Hz_20241115[pd.Timestamp(2024,11,15,21,30).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,15,22,0).tz_localize('UTC').tz_convert(pacific_tz)]

loads_inflow_20Hz_20241118_1640_1700_operation = loads_inflow_20Hz_20241118[pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,18,17,0).tz_localize('UTC').tz_convert(pacific_tz)]
loads_inflow_20Hz_20241118_1700_1720_stowH1H2 = loads_inflow_20Hz_20241118[pd.Timestamp(2024,11,18,17,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,18,17,20).tz_localize('UTC').tz_convert(pacific_tz)]
loads_inflow_20Hz_20241118_1840_1900_stow = loads_inflow_20Hz_20241118[pd.Timestamp(2024,11,18,18,40).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,18,19,0).tz_localize('UTC').tz_convert(pacific_tz)]

loads_inflow_20Hz_20241120_1600_1630_operation = loads_inflow_20Hz_20241120[pd.Timestamp(2024,11,20,16,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,20,16,30).tz_localize('UTC').tz_convert(pacific_tz)]
loads_inflow_20Hz_20241120_1800_1830_stow = loads_inflow_20Hz_20241120[pd.Timestamp(2024,11,20,18,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,20,18,30).tz_localize('UTC').tz_convert(pacific_tz)]

loads_inflow_20Hz_20241121_0000_0030_stow1 = loads_inflow_20Hz_20241121[pd.Timestamp(2024,11,21,0,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,21,0,30).tz_localize('UTC').tz_convert(pacific_tz)]
loads_inflow_20Hz_20241121_0300_0330_stow2 = loads_inflow_20Hz_20241121[pd.Timestamp(2024,11,21,3,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,21,3,30).tz_localize('UTC').tz_convert(pacific_tz)]


loads_mast_20Hz_20241028_1820_1850_operation = loads_mast_20Hz_20241028[pd.Timestamp(2024,10,28,18,20).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,10,28,18,50).tz_localize('UTC').tz_convert(pacific_tz)]
loads_mast_20Hz_20241028_1857_1927_stowH3 = loads_mast_20Hz_20241028[pd.Timestamp(2024,10,28,18,57).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,10,28,19,27).tz_localize('UTC').tz_convert(pacific_tz)]
loads_mast_20Hz_20241028_2030_2100_stow = loads_mast_20Hz_20241028[pd.Timestamp(2024,10,28,20,30).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,10,28,21,0).tz_localize('UTC').tz_convert(pacific_tz)]

loads_mast_20Hz_20241115_2045_2115_operation = loads_mast_20Hz_20241115[pd.Timestamp(2024,11,15,20,45).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,15,21,15).tz_localize('UTC').tz_convert(pacific_tz)]
loads_mast_20Hz_20241115_1800_1830_stowH1H2 = loads_mast_20Hz_20241115[pd.Timestamp(2024,11,15,18,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,15,18,30).tz_localize('UTC').tz_convert(pacific_tz)]
loads_mast_20Hz_20241115_2130_2200_stow = loads_mast_20Hz_20241115[pd.Timestamp(2024,11,15,21,30).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,15,22,0).tz_localize('UTC').tz_convert(pacific_tz)]

loads_mast_20Hz_20241118_1640_1700_operation = loads_mast_20Hz_20241118[pd.Timestamp(2024,11,18,16,40).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,18,17,0).tz_localize('UTC').tz_convert(pacific_tz)]
loads_mast_20Hz_20241118_1700_1720_stowH1H2 = loads_mast_20Hz_20241118[pd.Timestamp(2024,11,18,17,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,18,17,20).tz_localize('UTC').tz_convert(pacific_tz)]
loads_mast_20Hz_20241118_1840_1900_stow = loads_mast_20Hz_20241118[pd.Timestamp(2024,11,18,18,40).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,18,19,0).tz_localize('UTC').tz_convert(pacific_tz)]

loads_mast_20Hz_20241120_1600_1630_operation = loads_mast_20Hz_20241120[pd.Timestamp(2024,11,20,16,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,20,16,30).tz_localize('UTC').tz_convert(pacific_tz)]
loads_mast_20Hz_20241120_1800_1830_stow = loads_mast_20Hz_20241120[pd.Timestamp(2024,11,20,18,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,20,18,30).tz_localize('UTC').tz_convert(pacific_tz)]

loads_mast_20Hz_20241121_0000_0030_stow1 = loads_mast_20Hz_20241121[pd.Timestamp(2024,11,21,0,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,21,0,30).tz_localize('UTC').tz_convert(pacific_tz)]
loads_mast_20Hz_20241121_0300_0330_stow2 = loads_mast_20Hz_20241121[pd.Timestamp(2024,11,21,3,0).tz_localize('UTC').tz_convert(pacific_tz):pd.Timestamp(2024,11,21,3,30).tz_localize('UTC').tz_convert(pacific_tz)]


#%% Masts wind speeds and turbulence parameters (stow)

H1_wspd_20241028_2030_2100_stow_z1 = loads_inflow_20Hz_20241028_2030_2100_stow.wspd_Low.mean()
H2_wspd_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m1_wspd_Low.mean()
H3_wspd_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m3_wspd_Low.mean()

H1_wdir_20241028_2030_2100_stow_z1 = loads_inflow_20Hz_20241028_2030_2100_stow.wdir_Low.mean()
H2_wdir_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m1_wdir_Low.mean()
H3_wdir_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m3_wdir_Low.mean()

H1_wspd_20241115_2130_2200_stow_z1 = loads_inflow_20Hz_20241115_2130_2200_stow.wspd_Low.mean()
H2_wspd_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m1_wspd_Low.mean()
H3_wspd_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m3_wspd_Low.mean()

H1_wdir_20241115_2130_2200_stow_z1 = loads_inflow_20Hz_20241115_2130_2200_stow.wdir_Low.mean()
H2_wdir_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m1_wdir_Low.mean()
H3_wdir_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m3_wdir_Low.mean()

H1_wspd_20241118_1840_1900_stow_z1 = loads_inflow_20Hz_20241118_1840_1900_stow.wspd_Low.mean()
H2_wspd_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m1_wspd_Low.mean()
H3_wspd_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m3_wspd_Low.mean()

H1_wdir_20241118_1840_1900_stow_z1 = loads_inflow_20Hz_20241118_1840_1900_stow.wdir_Low.mean()
H2_wdir_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m1_wdir_Low.mean()
H3_wdir_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m3_wdir_Low.mean()

H1_wspd_20241120_1800_1830_stow_z1 = loads_inflow_20Hz_20241120_1800_1830_stow.wspd_Low.mean()
H2_wspd_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m1_wspd_Low.mean()
H3_wspd_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m3_wspd_Low.mean()

H1_wdir_20241120_1800_1830_stow_z1 = loads_inflow_20Hz_20241120_1800_1830_stow.wdir_Low.mean()
H2_wdir_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m1_wdir_Low.mean()
H3_wdir_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m3_wdir_Low.mean()

H1_wspd_20241121_0000_0030_stow1_z1 = loads_inflow_20Hz_20241121_0000_0030_stow1.wspd_Low.mean()
H2_wspd_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_wspd_Low.mean()
H3_wspd_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_wspd_Low.mean()

H1_wdir_20241121_0000_0030_stow1_z1 = loads_inflow_20Hz_20241121_0000_0030_stow1.wdir_Low.mean()
H2_wdir_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_wdir_Low.mean()
H3_wdir_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_wdir_Low.mean()

H1_wspd_20241121_0300_0330_stow2_z1 = loads_inflow_20Hz_20241121_0300_0330_stow2.wspd_Low.mean()
H2_wspd_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_wspd_Low.mean()
H3_wspd_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_wspd_Low.mean()

H1_wdir_20241121_0300_0330_stow2_z1 = loads_inflow_20Hz_20241121_0300_0330_stow2.wdir_Low.mean()
H2_wdir_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_wdir_Low.mean()
H3_wdir_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_wdir_Low.mean()


H1_Iu_20241028_2030_2100_stow_z1 = loads_inflow_20Hz_20241028_2030_2100_stow.TI_Low.mean()
H2_Iu_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m1_TI_Low.mean()
H3_Iu_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m3_TI_Low.mean()

H1_Iw_20241028_2030_2100_stow_z1 = loads_inflow_20Hz_20241028_2030_2100_stow.TI_w_Low.mean()
H2_Iw_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m1_TI_w_Low.mean()
H3_Iw_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m3_TI_w_Low.mean()

H1_Iu_20241115_2130_2200_stow_z1 = loads_inflow_20Hz_20241115_2130_2200_stow.TI_Low.mean()
H2_Iu_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m1_TI_Low.mean()
H3_Iu_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m3_TI_Low.mean()

H1_Iw_20241115_2130_2200_stow_z1 = loads_inflow_20Hz_20241115_2130_2200_stow.TI_w_Low.mean()
H2_Iw_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m1_TI_w_Low.mean()
H3_Iw_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m3_TI_w_Low.mean()

H1_Iu_20241118_1840_1900_stow_z1 = loads_inflow_20Hz_20241118_1840_1900_stow.TI_Low.mean()
H2_Iu_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m1_TI_Low.mean()
H3_Iu_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m3_TI_Low.mean()

H1_Iw_20241118_1840_1900_stow_z1 = loads_inflow_20Hz_20241118_1840_1900_stow.TI_w_Low.mean()
H2_Iw_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m1_TI_w_Low.mean()
H3_Iw_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m3_TI_w_Low.mean()

H1_Iu_20241120_1800_1830_stow_z1 = loads_inflow_20Hz_20241120_1800_1830_stow.TI_Low.mean()
H2_Iu_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m1_TI_Low.mean()
H3_Iu_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m3_TI_Low.mean()

H1_Iw_20241120_1800_1830_stow_z1 = loads_inflow_20Hz_20241120_1800_1830_stow.TI_w_Low.mean()
H2_Iw_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m1_TI_w_Low.mean()
H3_Iw_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m3_TI_w_Low.mean()

H1_Iu_20241121_0000_0030_stow1_z1 = loads_inflow_20Hz_20241121_0000_0030_stow1.TI_Low.mean()
H2_Iu_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_TI_Low.mean()
H3_Iu_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_TI_Low.mean()

H1_Iw_20241121_0000_0030_stow1_z1 = loads_inflow_20Hz_20241121_0000_0030_stow1.TI_w_Low.mean()
H2_Iw_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_TI_w_Low.mean()
H3_Iw_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_TI_w_Low.mean()

H1_Iu_20241121_0300_0330_stow2_z1 = loads_inflow_20Hz_20241121_0300_0330_stow2.TI_Low.mean()
H2_Iu_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_TI_Low.mean()
H3_Iu_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_TI_Low.mean()

H1_Iw_20241121_0300_0330_stow2_z1 = loads_inflow_20Hz_20241121_0300_0330_stow2.TI_w_Low.mean()
H2_Iw_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_TI_w_Low.mean()
H3_Iw_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_TI_w_Low.mean()


H1_wspd_20241028_2030_2100_stow_z2 = loads_inflow_20Hz_20241028_2030_2100_stow.wspd_Mid.mean()
H2_wspd_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m1_wspd_Mid.mean()
H3_wspd_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m3_wspd_Mid.mean()

H1_wdir_20241028_2030_2100_stow_z2 = loads_inflow_20Hz_20241028_2030_2100_stow.wdir_Mid.mean()
H2_wdir_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m1_wdir_Mid.mean()
H3_wdir_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m3_wdir_Mid.mean()

H1_wspd_20241115_2130_2200_stow_z2 = loads_inflow_20Hz_20241115_2130_2200_stow.wspd_Mid.mean()
H2_wspd_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m1_wspd_Mid.mean()
H3_wspd_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m3_wspd_Mid.mean()

H1_wdir_20241115_2130_2200_stow_z2 = loads_inflow_20Hz_20241115_2130_2200_stow.wdir_Mid.mean()
H2_wdir_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m1_wdir_Mid.mean()
H3_wdir_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m3_wdir_Mid.mean()

H1_wspd_20241118_1840_1900_stow_z2 = loads_inflow_20Hz_20241118_1840_1900_stow.wspd_Mid.mean()
H2_wspd_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m1_wspd_Mid.mean()
H3_wspd_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m3_wspd_Mid.mean()

H1_wdir_20241118_1840_1900_stow_z2 = loads_inflow_20Hz_20241118_1840_1900_stow.wdir_Mid.mean()
H2_wdir_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m1_wdir_Mid.mean()
H3_wdir_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m3_wdir_Mid.mean()

H1_wspd_20241120_1800_1830_stow_z2 = loads_inflow_20Hz_20241120_1800_1830_stow.wspd_Mid.mean()
H2_wspd_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m1_wspd_Mid.mean()
H3_wspd_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m3_wspd_Mid.mean()

H1_wdir_20241120_1800_1830_stow_z2 = loads_inflow_20Hz_20241120_1800_1830_stow.wdir_Mid.mean()
H2_wdir_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m1_wdir_Mid.mean()
H3_wdir_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m3_wdir_Mid.mean()

H1_wspd_20241121_0000_0030_stow1_z2 = loads_inflow_20Hz_20241121_0000_0030_stow1.wspd_Mid.mean()
H2_wspd_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_wspd_Mid.mean()
H3_wspd_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_wspd_Mid.mean()

H1_wdir_20241121_0000_0030_stow1_z2 = loads_inflow_20Hz_20241121_0000_0030_stow1.wdir_Mid.mean()
H2_wdir_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_wdir_Mid.mean()
H3_wdir_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_wdir_Mid.mean()

H1_wspd_20241121_0300_0330_stow2_z2 = loads_inflow_20Hz_20241121_0300_0330_stow2.wspd_Mid.mean()
H2_wspd_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_wspd_Mid.mean()
H3_wspd_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_wspd_Mid.mean()

H1_wdir_20241121_0300_0330_stow2_z2 = loads_inflow_20Hz_20241121_0300_0330_stow2.wdir_Mid.mean()
H2_wdir_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_wdir_Mid.mean()
H3_wdir_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_wdir_Mid.mean()


H1_Iu_20241028_2030_2100_stow_z2 = loads_inflow_20Hz_20241028_2030_2100_stow.TI_Mid.mean()
H2_Iu_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m1_TI_Mid.mean()
H3_Iu_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m3_TI_Mid.mean()

H1_Iw_20241028_2030_2100_stow_z2 = loads_inflow_20Hz_20241028_2030_2100_stow.TI_w_Mid.mean()
H2_Iw_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m1_TI_w_Mid.mean()
H3_Iw_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m3_TI_w_Mid.mean()

H1_Iu_20241115_2130_2200_stow_z2 = loads_inflow_20Hz_20241115_2130_2200_stow.TI_Mid.mean()
H2_Iu_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m1_TI_Mid.mean()
H3_Iu_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m3_TI_Mid.mean()

H1_Iw_20241115_2130_2200_stow_z2 = loads_inflow_20Hz_20241115_2130_2200_stow.TI_w_Mid.mean()
H2_Iw_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m1_TI_w_Mid.mean()
H3_Iw_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m3_TI_w_Mid.mean()

H1_Iu_20241118_1840_1900_stow_z2 = loads_inflow_20Hz_20241118_1840_1900_stow.TI_Mid.mean()
H2_Iu_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m1_TI_Mid.mean()
H3_Iu_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m3_TI_Mid.mean()

H1_Iw_20241118_1840_1900_stow_z2 = loads_inflow_20Hz_20241118_1840_1900_stow.TI_w_Mid.mean()
H2_Iw_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m1_TI_w_Mid.mean()
H3_Iw_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m3_TI_w_Mid.mean()

H1_Iu_20241120_1800_1830_stow_z2 = loads_inflow_20Hz_20241120_1800_1830_stow.TI_Mid.mean()
H2_Iu_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m1_TI_Mid.mean()
H3_Iu_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m3_TI_Mid.mean()

H1_Iw_20241120_1800_1830_stow_z2 = loads_inflow_20Hz_20241120_1800_1830_stow.TI_w_Mid.mean()
H2_Iw_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m1_TI_w_Mid.mean()
H3_Iw_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m3_TI_w_Mid.mean()

H1_Iu_20241121_0000_0030_stow1_z2 = loads_inflow_20Hz_20241121_0000_0030_stow1.TI_Mid.mean()
H2_Iu_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_TI_Mid.mean()
H3_Iu_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_TI_Mid.mean()

H1_Iw_20241121_0000_0030_stow1_z2 = loads_inflow_20Hz_20241121_0000_0030_stow1.TI_w_Mid.mean()
H2_Iw_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_TI_w_Mid.mean()
H3_Iw_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_TI_w_Mid.mean()

H1_Iu_20241121_0300_0330_stow2_z2 = loads_inflow_20Hz_20241121_0300_0330_stow2.TI_Mid.mean()
H2_Iu_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_TI_Mid.mean()
H3_Iu_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_TI_Mid.mean()

H1_Iw_20241121_0300_0330_stow2_z2 = loads_inflow_20Hz_20241121_0300_0330_stow2.TI_w_Mid.mean()
H2_Iw_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_TI_w_Mid.mean()
H3_Iw_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_TI_w_Mid.mean()


H1_wspd_20241028_2030_2100_stow_z3 = loads_inflow_20Hz_20241028_2030_2100_stow.wspd_Top.mean()
H2_wspd_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m1_wspd_Top.mean()
H3_wspd_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m3_wspd_Top.mean()

H1_wdir_20241028_2030_2100_stow_z3 = loads_inflow_20Hz_20241028_2030_2100_stow.wdir_Top.mean()
H2_wdir_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m1_wdir_Top.mean()
H3_wdir_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m3_wdir_Top.mean()

H1_wspd_20241115_2130_2200_stow_z3 = loads_inflow_20Hz_20241115_2130_2200_stow.wspd_Top.mean()
H2_wspd_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m1_wspd_Top.mean()
H3_wspd_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m3_wspd_Top.mean()

H1_wdir_20241115_2130_2200_stow_z3 = loads_inflow_20Hz_20241115_2130_2200_stow.wdir_Top.mean()
H2_wdir_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m1_wdir_Top.mean()
H3_wdir_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m3_wdir_Top.mean()

H1_wspd_20241118_1840_1900_stow_z3 = loads_inflow_20Hz_20241118_1840_1900_stow.wspd_Top.mean()
H2_wspd_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m1_wspd_Top.mean()
H3_wspd_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m3_wspd_Top.mean()

H1_wdir_20241118_1840_1900_stow_z3 = loads_inflow_20Hz_20241118_1840_1900_stow.wdir_Top.mean()
H2_wdir_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m1_wdir_Top.mean()
H3_wdir_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m3_wdir_Top.mean()

H1_wspd_20241120_1800_1830_stow_z3 = loads_inflow_20Hz_20241120_1800_1830_stow.wspd_Top.mean()
H2_wspd_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m1_wspd_Top.mean()
H3_wspd_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m3_wspd_Top.mean()

H1_wdir_20241120_1800_1830_stow_z3 = loads_inflow_20Hz_20241120_1800_1830_stow.wdir_Top.mean()
H2_wdir_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m1_wdir_Top.mean()
H3_wdir_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m3_wdir_Top.mean()

H1_wspd_20241121_0000_0030_stow1_z3 = loads_inflow_20Hz_20241121_0000_0030_stow1.wspd_Top.mean()
H2_wspd_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_wspd_Top.mean()
H3_wspd_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_wspd_Top.mean()

H1_wdir_20241121_0000_0030_stow1_z3 = loads_inflow_20Hz_20241121_0000_0030_stow1.wdir_Top.mean()
H2_wdir_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_wdir_Top.mean()
H3_wdir_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_wdir_Top.mean()

H1_wspd_20241121_0300_0330_stow2_z3 = loads_inflow_20Hz_20241121_0300_0330_stow2.wspd_Top.mean()
H2_wspd_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_wspd_Top.mean()
H3_wspd_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_wspd_Top.mean()

H1_wdir_20241121_0300_0330_stow2_z3 = loads_inflow_20Hz_20241121_0300_0330_stow2.wdir_Top.mean()
H2_wdir_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_wdir_Top.mean()
H3_wdir_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_wdir_Top.mean()


H1_Iu_20241028_2030_2100_stow_z3 = loads_inflow_20Hz_20241028_2030_2100_stow.TI_Top.mean()
H2_Iu_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m1_TI_Top.mean()
H3_Iu_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m3_TI_Top.mean()

H1_Iw_20241028_2030_2100_stow_z3 = loads_inflow_20Hz_20241028_2030_2100_stow.TI_w_Top.mean()
H2_Iw_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m1_TI_w_Top.mean()
H3_Iw_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m3_TI_w_Top.mean()

H1_Iu_20241115_2130_2200_stow_z3 = loads_inflow_20Hz_20241115_2130_2200_stow.TI_Top.mean()
H2_Iu_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m1_TI_Top.mean()
H3_Iu_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m3_TI_Top.mean()

H1_Iw_20241115_2130_2200_stow_z3 = loads_inflow_20Hz_20241115_2130_2200_stow.TI_w_Top.mean()
H2_Iw_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m1_TI_w_Top.mean()
H3_Iw_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m3_TI_w_Top.mean()

H1_Iu_20241118_1840_1900_stow_z3 = loads_inflow_20Hz_20241118_1840_1900_stow.TI_Top.mean()
H2_Iu_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m1_TI_Top.mean()
H3_Iu_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m3_TI_Top.mean()

H1_Iw_20241118_1840_1900_stow_z3 = loads_inflow_20Hz_20241118_1840_1900_stow.TI_w_Top.mean()
H2_Iw_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m1_TI_w_Top.mean()
H3_Iw_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m3_TI_w_Top.mean()

H1_Iu_20241120_1800_1830_stow_z3 = loads_inflow_20Hz_20241120_1800_1830_stow.TI_Top.mean()
H2_Iu_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m1_TI_Top.mean()
H3_Iu_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m3_TI_Top.mean()

H1_Iw_20241120_1800_1830_stow_z3 = loads_inflow_20Hz_20241120_1800_1830_stow.TI_w_Top.mean()
H2_Iw_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m1_TI_w_Top.mean()
H3_Iw_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m3_TI_w_Top.mean()

H1_Iu_20241121_0000_0030_stow1_z3 = loads_inflow_20Hz_20241121_0000_0030_stow1.TI_Top.mean()
H2_Iu_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_TI_Top.mean()
H3_Iu_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_TI_Top.mean()

H1_Iw_20241121_0000_0030_stow1_z3 = loads_inflow_20Hz_20241121_0000_0030_stow1.TI_w_Top.mean()
H2_Iw_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_TI_w_Top.mean()
H3_Iw_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_TI_w_Top.mean()

H1_Iu_20241121_0300_0330_stow2_z3 = loads_inflow_20Hz_20241121_0300_0330_stow2.TI_Top.mean()
H2_Iu_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_TI_Top.mean()
H3_Iu_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_TI_Top.mean()

H1_Iw_20241121_0300_0330_stow2_z3 = loads_inflow_20Hz_20241121_0300_0330_stow2.TI_w_Top.mean()
H2_Iw_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_TI_w_Top.mean()
H3_Iw_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_TI_w_Top.mean()


H1_U_ax_20241028_2030_2100_stow_z1 = loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.mean()
H2_U_ax_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.mean()
H3_U_ax_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.mean()

H1_W_ax_20241028_2030_2100_stow_z1 = loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.mean()
H2_W_ax_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.mean()
H3_W_ax_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.mean()

H1_U_ax_20241115_2130_2200_stow_z1 = loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.mean()
H2_U_ax_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.mean()
H3_U_ax_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.mean()

H1_W_ax_20241115_2130_2200_stow_z1 = loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.mean()
H2_W_ax_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.mean()
H3_W_ax_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.mean()

H1_U_ax_20241118_1840_1900_stow_z1 = loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.mean()
H2_U_ax_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.mean()
H3_U_ax_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.mean()

H1_W_ax_20241118_1840_1900_stow_z1 = loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.mean()
H2_W_ax_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.mean()
H3_W_ax_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.mean()

H1_U_ax_20241120_1800_1830_stow_z1 = loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.mean()
H2_U_ax_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.mean()
H3_U_ax_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.mean()

H1_W_ax_20241120_1800_1830_stow_z1 = loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.mean()
H2_W_ax_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.mean()
H3_W_ax_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.mean()

H1_U_ax_20241121_0000_0030_stow1_z1 = loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.mean()
H2_U_ax_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.mean()
H3_U_ax_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.mean()

H1_W_ax_20241121_0000_0030_stow1_z1 = loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.mean()
H2_W_ax_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.mean()
H3_W_ax_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.mean()

H1_U_ax_20241121_0300_0330_stow2_z1 = loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.mean()
H2_U_ax_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.mean()
H3_U_ax_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.mean()

H1_W_ax_20241121_0300_0330_stow2_z1 = loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.mean()
H2_W_ax_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.mean()
H3_W_ax_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.mean()


H1_U_ax_20241028_2030_2100_stow_z2 = loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.mean()
H2_U_ax_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.mean()
H3_U_ax_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.mean()

H1_W_ax_20241028_2030_2100_stow_z2 = loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.mean()
H2_W_ax_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.mean()
H3_W_ax_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.mean()

H1_U_ax_20241115_2130_2200_stow_z2 = loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.mean()
H2_U_ax_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.mean()
H3_U_ax_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.mean()

H1_W_ax_20241115_2130_2200_stow_z2 = loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.mean()
H2_W_ax_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.mean()
H3_W_ax_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.mean()

H1_U_ax_20241118_1840_1900_stow_z2 = loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.mean()
H2_U_ax_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.mean()
H3_U_ax_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.mean()

H1_W_ax_20241118_1840_1900_stow_z2 = loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.mean()
H2_W_ax_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.mean()
H3_W_ax_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.mean()

H1_U_ax_20241120_1800_1830_stow_z2 = loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.mean()
H2_U_ax_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.mean()
H3_U_ax_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.mean()

H1_W_ax_20241120_1800_1830_stow_z2 = loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.mean()
H2_W_ax_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.mean()
H3_W_ax_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.mean()

H1_U_ax_20241121_0000_0030_stow1_z2 = loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.mean()
H2_U_ax_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.mean()
H3_U_ax_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.mean()

H1_W_ax_20241121_0000_0030_stow1_z2 = loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.mean()
H2_W_ax_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.mean()
H3_W_ax_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.mean()

H1_U_ax_20241121_0300_0330_stow2_z2 = loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.mean()
H2_U_ax_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.mean()
H3_U_ax_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.mean()

H1_W_ax_20241121_0300_0330_stow2_z2 = loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.mean()
H2_W_ax_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.mean()
H3_W_ax_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.mean()



H1_U_ax_20241028_2030_2100_stow_z3 = loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.mean()
H2_U_ax_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.mean()
H3_U_ax_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.mean()

H1_W_ax_20241028_2030_2100_stow_z3 = loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.mean()
H2_W_ax_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.mean()
H3_W_ax_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.mean()

H1_U_ax_20241115_2130_2200_stow_z3 = loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.mean()
H2_U_ax_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.mean()
H3_U_ax_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.mean()

H1_W_ax_20241115_2130_2200_stow_z3 = loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.mean()
H2_W_ax_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.mean()
H3_W_ax_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.mean()

H1_U_ax_20241118_1840_1900_stow_z3 = loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.mean()
H2_U_ax_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.mean()
H3_U_ax_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.mean()

H1_W_ax_20241118_1840_1900_stow_z3 = loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.mean()
H2_W_ax_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.mean()
H3_W_ax_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.mean()

H1_U_ax_20241120_1800_1830_stow_z3 = loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.mean()
H2_U_ax_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.mean()
H3_U_ax_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.mean()

H1_W_ax_20241120_1800_1830_stow_z3 = loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.mean()
H2_W_ax_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.mean()
H3_W_ax_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.mean()

H1_U_ax_20241121_0000_0030_stow1_z3 = loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.mean()
H2_U_ax_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.mean()
H3_U_ax_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.mean()

H1_W_ax_20241121_0000_0030_stow1_z3 = loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.mean()
H2_W_ax_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.mean()
H3_W_ax_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.mean()

H1_U_ax_20241121_0300_0330_stow2_z3 = loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.mean()
H2_U_ax_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.mean()
H3_U_ax_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.mean()

H1_W_ax_20241121_0300_0330_stow2_z3 = loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.mean()
H2_W_ax_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.mean()
H3_W_ax_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.mean()



H1_Ts_20241028_2030_2100_stow_z1 = loads_inflow_20Hz_20241028_2030_2100_stow.Ts_Low.mean()
H2_Ts_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m1_Ts_Low.mean()
H3_Ts_20241028_2030_2100_stow_z1 = loads_mast_20Hz_20241028_2030_2100_stow.m3_Ts_Low.mean()

H1_Ts_20241115_2130_2200_stow_z1 = loads_inflow_20Hz_20241115_2130_2200_stow.Ts_Low.mean()
H2_Ts_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m1_Ts_Low.mean()
H3_Ts_20241115_2130_2200_stow_z1 = loads_mast_20Hz_20241115_2130_2200_stow.m3_Ts_Low.mean()

H1_Ts_20241118_1840_1900_stow_z1 = loads_inflow_20Hz_20241118_1840_1900_stow.Ts_Low.mean()
H2_Ts_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m1_Ts_Low.mean()
H3_Ts_20241118_1840_1900_stow_z1 = loads_mast_20Hz_20241118_1840_1900_stow.m3_Ts_Low.mean()

H1_Ts_20241120_1800_1830_stow_z1 = loads_inflow_20Hz_20241120_1800_1830_stow.Ts_Low.mean()
H2_Ts_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m1_Ts_Low.mean()
H3_Ts_20241120_1800_1830_stow_z1 = loads_mast_20Hz_20241120_1800_1830_stow.m3_Ts_Low.mean()

H1_Ts_20241121_0000_0030_stow1_z1 = loads_inflow_20Hz_20241121_0000_0030_stow1.Ts_Low.mean()
H2_Ts_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_Ts_Low.mean()
H3_Ts_20241121_0000_0030_stow1_z1 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_Ts_Low.mean()

H1_Ts_20241121_0300_0330_stow2_z1 = loads_inflow_20Hz_20241121_0300_0330_stow2.Ts_Low.mean()
H2_Ts_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_Ts_Low.mean()
H3_Ts_20241121_0300_0330_stow2_z1 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_Ts_Low.mean()

H1_Ts_20241028_2030_2100_stow_z2 = loads_inflow_20Hz_20241028_2030_2100_stow.Ts_Mid.mean()
H2_Ts_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m1_Ts_Mid.mean()
H3_Ts_20241028_2030_2100_stow_z2 = loads_mast_20Hz_20241028_2030_2100_stow.m3_Ts_Mid.mean()

H1_Ts_20241115_2130_2200_stow_z2 = loads_inflow_20Hz_20241115_2130_2200_stow.Ts_Mid.mean()
H2_Ts_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m1_Ts_Mid.mean()
H3_Ts_20241115_2130_2200_stow_z2 = loads_mast_20Hz_20241115_2130_2200_stow.m3_Ts_Mid.mean()

H1_Ts_20241118_1840_1900_stow_z2 = loads_inflow_20Hz_20241118_1840_1900_stow.Ts_Mid.mean()
H2_Ts_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m1_Ts_Mid.mean()
H3_Ts_20241118_1840_1900_stow_z2 = loads_mast_20Hz_20241118_1840_1900_stow.m3_Ts_Mid.mean()

H1_Ts_20241120_1800_1830_stow_z2 = loads_inflow_20Hz_20241120_1800_1830_stow.Ts_Mid.mean()
H2_Ts_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m1_Ts_Mid.mean()
H3_Ts_20241120_1800_1830_stow_z2 = loads_mast_20Hz_20241120_1800_1830_stow.m3_Ts_Mid.mean()

H1_Ts_20241121_0000_0030_stow1_z2 = loads_inflow_20Hz_20241121_0000_0030_stow1.Ts_Mid.mean()
H2_Ts_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_Ts_Mid.mean()
H3_Ts_20241121_0000_0030_stow1_z2 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_Ts_Mid.mean()

H1_Ts_20241121_0300_0330_stow2_z2 = loads_inflow_20Hz_20241121_0300_0330_stow2.Ts_Mid.mean()
H2_Ts_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_Ts_Mid.mean()
H3_Ts_20241121_0300_0330_stow2_z2 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_Ts_Mid.mean()

H1_Ts_20241028_2030_2100_stow_z3 = loads_inflow_20Hz_20241028_2030_2100_stow.Ts_Top.mean()
H2_Ts_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m1_Ts_Top.mean()
H3_Ts_20241028_2030_2100_stow_z3 = loads_mast_20Hz_20241028_2030_2100_stow.m3_Ts_Top.mean()

H1_Ts_20241115_2130_2200_stow_z3 = loads_inflow_20Hz_20241115_2130_2200_stow.Ts_Top.mean()
H2_Ts_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m1_Ts_Top.mean()
H3_Ts_20241115_2130_2200_stow_z3 = loads_mast_20Hz_20241115_2130_2200_stow.m3_Ts_Top.mean()

H1_Ts_20241118_1840_1900_stow_z3 = loads_inflow_20Hz_20241118_1840_1900_stow.Ts_Top.mean()
H2_Ts_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m1_Ts_Top.mean()
H3_Ts_20241118_1840_1900_stow_z3 = loads_mast_20Hz_20241118_1840_1900_stow.m3_Ts_Top.mean()

H1_Ts_20241120_1800_1830_stow_z3 = loads_inflow_20Hz_20241120_1800_1830_stow.Ts_Top.mean()
H2_Ts_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m1_Ts_Top.mean()
H3_Ts_20241120_1800_1830_stow_z3 = loads_mast_20Hz_20241120_1800_1830_stow.m3_Ts_Top.mean()

H1_Ts_20241121_0000_0030_stow1_z3 = loads_inflow_20Hz_20241121_0000_0030_stow1.Ts_Top.mean()
H2_Ts_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m1_Ts_Top.mean()
H3_Ts_20241121_0000_0030_stow1_z3 = loads_mast_20Hz_20241121_0000_0030_stow1.m3_Ts_Top.mean()

H1_Ts_20241121_0300_0330_stow2_z3 = loads_inflow_20Hz_20241121_0300_0330_stow2.Ts_Top.mean()
H2_Ts_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m1_Ts_Top.mean()
H3_Ts_20241121_0300_0330_stow2_z3 = loads_mast_20Hz_20241121_0300_0330_stow2.m3_Ts_Top.mean()




H1_wspd_20241115_2045_2115_operation_z1 = loads_inflow_20Hz_20241115_2045_2115_operation.wspd_Low.mean()
H2_wspd_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m1_wspd_Low.mean()
H3_wspd_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m3_wspd_Low.mean()

H1_wdir_20241115_2045_2115_operation_z1 = loads_inflow_20Hz_20241115_2045_2115_operation.wdir_Low.mean()
H2_wdir_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m1_wdir_Low.mean()
H3_wdir_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m3_wdir_Low.mean()

H1_Iu_20241115_2045_2115_operation_z1 = loads_inflow_20Hz_20241115_2045_2115_operation.TI_Low.mean()
H2_Iu_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m1_TI_Low.mean()
H3_Iu_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m3_TI_Low.mean()

H1_Iw_20241115_2045_2115_operation_z1 = loads_inflow_20Hz_20241115_2045_2115_operation.TI_w_Low.mean()
H2_Iw_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m1_TI_w_Low.mean()
H3_Iw_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m3_TI_w_Low.mean()

H1_wspd_20241115_2045_2115_operation_z2 = loads_inflow_20Hz_20241115_2045_2115_operation.wspd_Mid.mean()
H2_wspd_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m1_wspd_Mid.mean()
H3_wspd_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m3_wspd_Mid.mean()

H1_wdir_20241115_2045_2115_operation_z2 = loads_inflow_20Hz_20241115_2045_2115_operation.wdir_Mid.mean()
H2_wdir_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m1_wdir_Mid.mean()
H3_wdir_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m3_wdir_Mid.mean()

H1_Iu_20241115_2045_2115_operation_z2 = loads_inflow_20Hz_20241115_2045_2115_operation.TI_Mid.mean()
H2_Iu_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m1_TI_Mid.mean()
H3_Iu_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m3_TI_Mid.mean()

H1_Iw_20241115_2045_2115_operation_z2 = loads_inflow_20Hz_20241115_2045_2115_operation.TI_w_Mid.mean()
H2_Iw_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m1_TI_w_Mid.mean()
H3_Iw_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m3_TI_w_Mid.mean()

H1_wspd_20241115_2045_2115_operation_z3 = loads_inflow_20Hz_20241115_2045_2115_operation.wspd_Top.mean()
H2_wspd_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m1_wspd_Top.mean()
H3_wspd_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m3_wspd_Top.mean()

H1_wdir_20241115_2045_2115_operation_z3 = loads_inflow_20Hz_20241115_2045_2115_operation.wdir_Top.mean()
H2_wdir_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m1_wdir_Top.mean()
H3_wdir_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m3_wdir_Top.mean()

H1_Iu_20241115_2045_2115_operation_z3 = loads_inflow_20Hz_20241115_2045_2115_operation.TI_Top.mean()
H2_Iu_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m1_TI_Top.mean()
H3_Iu_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m3_TI_Top.mean()

H1_Iw_20241115_2045_2115_operation_z3 = loads_inflow_20Hz_20241115_2045_2115_operation.TI_w_Top.mean()
H2_Iw_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m1_TI_w_Top.mean()
H3_Iw_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m3_TI_w_Top.mean()

H1_U_ax_20241115_2045_2115_operation_z1 = loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.mean()
H2_U_ax_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.mean()
H3_U_ax_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.mean()

H1_W_ax_20241115_2045_2115_operation_z1 = loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.mean()
H2_W_ax_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.mean()
H3_W_ax_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.mean()

H1_U_ax_20241115_2045_2115_operation_z2 = loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.mean()
H2_U_ax_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.mean()
H3_U_ax_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.mean()

H1_W_ax_20241115_2045_2115_operation_z2 = loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.mean()
H2_W_ax_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.mean()
H3_W_ax_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.mean()

H1_U_ax_20241115_2045_2115_operation_z3 = loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.mean()
H2_U_ax_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.mean()
H3_U_ax_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.mean()

H1_W_ax_20241115_2045_2115_operation_z3 = loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.mean()
H2_W_ax_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.mean()
H3_W_ax_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.mean()

H1_Ts_20241115_2045_2115_operation_z1 = loads_inflow_20Hz_20241115_2045_2115_operation.Ts_Low.mean()
H2_Ts_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m1_Ts_Low.mean()
H3_Ts_20241115_2045_2115_operation_z1 = loads_mast_20Hz_20241115_2045_2115_operation.m3_Ts_Low.mean()

H1_Ts_20241115_2045_2115_operation_z2 = loads_inflow_20Hz_20241115_2045_2115_operation.Ts_Mid.mean()
H2_Ts_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m1_Ts_Mid.mean()
H3_Ts_20241115_2045_2115_operation_z2 = loads_mast_20Hz_20241115_2045_2115_operation.m3_Ts_Mid.mean()

H1_Ts_20241115_2045_2115_operation_z3 = loads_inflow_20Hz_20241115_2045_2115_operation.Ts_Top.mean()
H2_Ts_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m1_Ts_Top.mean()
H3_Ts_20241115_2045_2115_operation_z3 = loads_mast_20Hz_20241115_2045_2115_operation.m3_Ts_Top.mean()




#%% PSD analysis

heights = [2.75,5.5,11] 
fs = 20

# Spectra
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from numpy import hanning
import math

overlap = 0
nblock = len(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_inflow_20Hz_20241028_2030_2100_stow_z1, Pxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = welch(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = fu_loads_inflow_20Hz_20241028_2030_2100_stow_z1*heights[0]/H1_U_ax_20241028_2030_2100_stow_z1
nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = (fu_loads_inflow_20Hz_20241028_2030_2100_stow_z1*Pxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1)/loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.std()**2

fu_loads_inflow_20Hz_20241028_2030_2100_stow_z2, Pxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = welch(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = fu_loads_inflow_20Hz_20241028_2030_2100_stow_z2*heights[1]/H1_U_ax_20241028_2030_2100_stow_z2
nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = (fu_loads_inflow_20Hz_20241028_2030_2100_stow_z2*Pxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2)/loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.std()**2
 
fu_loads_inflow_20Hz_20241028_2030_2100_stow_z3, Pxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = welch(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = fu_loads_inflow_20Hz_20241028_2030_2100_stow_z3*heights[2]/H1_U_ax_20241028_2030_2100_stow_z3
nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = (fu_loads_inflow_20Hz_20241028_2030_2100_stow_z3*Pxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3)/loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.std()**2              
    
fw_loads_inflow_20Hz_20241028_2030_2100_stow_z1, Pxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = welch(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = fw_loads_inflow_20Hz_20241028_2030_2100_stow_z1*heights[0]/H1_W_ax_20241028_2030_2100_stow_z1
nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = (fw_loads_inflow_20Hz_20241028_2030_2100_stow_z1*Pxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1)/loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.std()**2

fw_loads_inflow_20Hz_20241028_2030_2100_stow_z2, Pxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = welch(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = fw_loads_inflow_20Hz_20241028_2030_2100_stow_z2*heights[1]/H1_W_ax_20241028_2030_2100_stow_z2
nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = (fw_loads_inflow_20Hz_20241028_2030_2100_stow_z2*Pxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2)/loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.std()**2
 
fw_loads_inflow_20Hz_20241028_2030_2100_stow_z3, Pxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = welch(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = fw_loads_inflow_20Hz_20241028_2030_2100_stow_z3*heights[2]/H1_W_ax_20241028_2030_2100_stow_z3
nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = (fw_loads_inflow_20Hz_20241028_2030_2100_stow_z3*Pxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3)/loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = list(np.where([abs(nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1[index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z1[0][0]:len(nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1)]
nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z1,200)
nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = [nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1[0:index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z1[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z1]

index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = list(np.where([abs(nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2[index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z2[0][0]:len(nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2)]
nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z2,200)
nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = [nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2[0:index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z2[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z2]

index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = list(np.where([abs(nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3[index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z3[0][0]:len(nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3)]
nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z3,200)
nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = [nPxxfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3[0:index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z3[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z3]

index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = list(np.where([abs(nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1[index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z1[0][0]:len(nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1)]
nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z1,200)
nPxxfw_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z1 = [nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1[0:index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z1[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z1]

index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = list(np.where([abs(nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2[index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z2[0][0]:len(nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2)]
nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z2,200)
nPxxfw_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z2 = [nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2[0:index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z2[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z2]

index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = list(np.where([abs(nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3[index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z3[0][0]:len(nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3)]
nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z3,200)
nPxxfw_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z3 = [nPxxfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3[0:index_highfreq_loads_inflow_20Hz_20241028_2030_2100_stow_z3[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241028_2030_2100_stow_z3]


plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z1[0:len(nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z2[0:len(nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241028_2030_2100_stow_z3[0:len(nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('inflow')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z1[0:len(nPxxfw_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z2[0:len(nPxxfw_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241028_2030_2100_stow_z3[0:len(nPxxfw_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241028_2030_2100_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('inflow')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()


#%% Extract data by height

U_corr_inflow_20241028_2030_2100_stow_z1 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low)
U_corr_inflow_20241028_2030_2100_stow_z2 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid)
U_corr_inflow_20241028_2030_2100_stow_z3 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top)

V_corr_inflow_20241028_2030_2100_stow_z1 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.V_ax_Low)
V_corr_inflow_20241028_2030_2100_stow_z2 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.V_ax_Mid)
V_corr_inflow_20241028_2030_2100_stow_z3 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.V_ax_Top)

W_corr_inflow_20241028_2030_2100_stow_z1 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low)
W_corr_inflow_20241028_2030_2100_stow_z2 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid)
W_corr_inflow_20241028_2030_2100_stow_z3 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top)

Ts_corr_inflow_20241028_2030_2100_stow_z1 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.Ts_Low)
Ts_corr_inflow_20241028_2030_2100_stow_z2 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.Ts_Mid)
Ts_corr_inflow_20241028_2030_2100_stow_z3 = pd.Series(loads_inflow_20Hz_20241028_2030_2100_stow.Ts_Top)

# Detrend
U_corr_inflow_20241028_2030_2100_stow_z1[U_corr_inflow_20241028_2030_2100_stow_z1.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241028_2030_2100_stow_z1.dropna()) 
U_corr_inflow_20241028_2030_2100_stow_z2[U_corr_inflow_20241028_2030_2100_stow_z2.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241028_2030_2100_stow_z2.dropna()) 
U_corr_inflow_20241028_2030_2100_stow_z3[U_corr_inflow_20241028_2030_2100_stow_z3.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241028_2030_2100_stow_z3.dropna()) 

V_corr_inflow_20241028_2030_2100_stow_z1[V_corr_inflow_20241028_2030_2100_stow_z1.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241028_2030_2100_stow_z1.dropna()) 
V_corr_inflow_20241028_2030_2100_stow_z2[V_corr_inflow_20241028_2030_2100_stow_z2.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241028_2030_2100_stow_z2.dropna()) 
V_corr_inflow_20241028_2030_2100_stow_z3[V_corr_inflow_20241028_2030_2100_stow_z3.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241028_2030_2100_stow_z3.dropna()) 

W_corr_inflow_20241028_2030_2100_stow_z1[W_corr_inflow_20241028_2030_2100_stow_z1.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241028_2030_2100_stow_z1.dropna()) 
W_corr_inflow_20241028_2030_2100_stow_z2[W_corr_inflow_20241028_2030_2100_stow_z2.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241028_2030_2100_stow_z2.dropna()) 
W_corr_inflow_20241028_2030_2100_stow_z3[W_corr_inflow_20241028_2030_2100_stow_z3.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241028_2030_2100_stow_z3.dropna()) 

Ts_corr_inflow_20241028_2030_2100_stow_z1[Ts_corr_inflow_20241028_2030_2100_stow_z1.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241028_2030_2100_stow_z1.dropna()) 
Ts_corr_inflow_20241028_2030_2100_stow_z2[Ts_corr_inflow_20241028_2030_2100_stow_z2.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241028_2030_2100_stow_z2.dropna()) 
Ts_corr_inflow_20241028_2030_2100_stow_z3[Ts_corr_inflow_20241028_2030_2100_stow_z3.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241028_2030_2100_stow_z3.dropna()) 

# Reynolds stresses and length scales (south2)

inflow_uv_z1_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z1*V_corr_inflow_20241028_2030_2100_stow_z1).mean()-(U_corr_inflow_20241028_2030_2100_stow_z1.mean()*V_corr_inflow_20241028_2030_2100_stow_z1.mean());
inflow_vw_z1_20241028_2030_2100_stow = (V_corr_inflow_20241028_2030_2100_stow_z1*W_corr_inflow_20241028_2030_2100_stow_z1).mean()-(V_corr_inflow_20241028_2030_2100_stow_z1.mean()*W_corr_inflow_20241028_2030_2100_stow_z1.mean());
inflow_uw_z1_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z1*W_corr_inflow_20241028_2030_2100_stow_z1).mean()-(U_corr_inflow_20241028_2030_2100_stow_z1.mean()*W_corr_inflow_20241028_2030_2100_stow_z1.mean());
inflow_wT_z1_20241028_2030_2100_stow = (W_corr_inflow_20241028_2030_2100_stow_z1*Ts_corr_inflow_20241028_2030_2100_stow_z1).mean()-(W_corr_inflow_20241028_2030_2100_stow_z1.mean()*Ts_corr_inflow_20241028_2030_2100_stow_z1.mean());

inflow_uv_z2_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z2*V_corr_inflow_20241028_2030_2100_stow_z2).mean()-(U_corr_inflow_20241028_2030_2100_stow_z2.mean()*V_corr_inflow_20241028_2030_2100_stow_z2.mean());
inflow_vw_z2_20241028_2030_2100_stow = (V_corr_inflow_20241028_2030_2100_stow_z2*W_corr_inflow_20241028_2030_2100_stow_z2).mean()-(V_corr_inflow_20241028_2030_2100_stow_z2.mean()*W_corr_inflow_20241028_2030_2100_stow_z2.mean());
inflow_uw_z2_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z2*W_corr_inflow_20241028_2030_2100_stow_z2).mean()-(U_corr_inflow_20241028_2030_2100_stow_z2.mean()*W_corr_inflow_20241028_2030_2100_stow_z2.mean());
inflow_wT_z2_20241028_2030_2100_stow = (W_corr_inflow_20241028_2030_2100_stow_z2*Ts_corr_inflow_20241028_2030_2100_stow_z2).mean()-(W_corr_inflow_20241028_2030_2100_stow_z2.mean()*Ts_corr_inflow_20241028_2030_2100_stow_z2.mean());

inflow_uv_z3_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z3*V_corr_inflow_20241028_2030_2100_stow_z3).mean()-(U_corr_inflow_20241028_2030_2100_stow_z3.mean()*V_corr_inflow_20241028_2030_2100_stow_z3.mean());
inflow_vw_z3_20241028_2030_2100_stow = (V_corr_inflow_20241028_2030_2100_stow_z3*W_corr_inflow_20241028_2030_2100_stow_z3).mean()-(V_corr_inflow_20241028_2030_2100_stow_z3.mean()*W_corr_inflow_20241028_2030_2100_stow_z3.mean());
inflow_uw_z3_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z3*W_corr_inflow_20241028_2030_2100_stow_z3).mean()-(U_corr_inflow_20241028_2030_2100_stow_z3.mean()*W_corr_inflow_20241028_2030_2100_stow_z3.mean());
inflow_wT_z3_20241028_2030_2100_stow = (W_corr_inflow_20241028_2030_2100_stow_z3*Ts_corr_inflow_20241028_2030_2100_stow_z3).mean()-(W_corr_inflow_20241028_2030_2100_stow_z3.mean()*Ts_corr_inflow_20241028_2030_2100_stow_z3.mean());

utau_z1_20241028_2030_2100_stow = (inflow_uw_z1_20241028_2030_2100_stow**2+inflow_vw_z1_20241028_2030_2100_stow**2)**(1/4) 
utau_z2_20241028_2030_2100_stow = (inflow_uw_z2_20241028_2030_2100_stow**2+inflow_vw_z2_20241028_2030_2100_stow**2)**(1/4) 
utau_z3_20241028_2030_2100_stow = (inflow_uw_z3_20241028_2030_2100_stow**2+inflow_vw_z3_20241028_2030_2100_stow**2)**(1/4) 

L_z1_20241028_2030_2100_stow = -1*(utau_z1_20241028_2030_2100_stow**3)/(0.4*(9.81/H1_Ts_20241028_2030_2100_stow_z1)*inflow_wT_z1_20241028_2030_2100_stow)
L_z2_20241028_2030_2100_stow = -1*(utau_z2_20241028_2030_2100_stow**3)/(0.4*(9.81/H1_Ts_20241028_2030_2100_stow_z2)*inflow_wT_z2_20241028_2030_2100_stow)
L_z3_20241028_2030_2100_stow = -1*(utau_z3_20241028_2030_2100_stow**3)/(0.4*(9.81/H1_Ts_20241028_2030_2100_stow_z3)*inflow_wT_z3_20241028_2030_2100_stow)

zL_z1_20241028_2030_2100_stow = heights[0]/L_z1_20241028_2030_2100_stow
zL_z2_20241028_2030_2100_stow = heights[1]/L_z2_20241028_2030_2100_stow
zL_z3_20241028_2030_2100_stow = heights[2]/L_z3_20241028_2030_2100_stow

inflow_uprimewprime_z1_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z1*W_corr_inflow_20241028_2030_2100_stow_z1);
inflow_uprimewprime_z2_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z2*W_corr_inflow_20241028_2030_2100_stow_z2);
inflow_uprimewprime_z3_20241028_2030_2100_stow = (U_corr_inflow_20241028_2030_2100_stow_z3*W_corr_inflow_20241028_2030_2100_stow_z3);


#%% LS exponential fit method

autocorr_inflow_20241028_2030_2100_stow = np.correlate(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241028_2030_2100_stow_z1)
Lux_20241028_2030_2100_stow_z1 = Lux_20241028_2030_2100_stow_z1[Lux_20241028_2030_2100_stow_z1>0]

autocorr_inflow_20241028_2030_2100_stow = np.correlate(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241028_2030_2100_stow_z2)
Lux_20241028_2030_2100_stow_z2 = Lux_20241028_2030_2100_stow_z2[Lux_20241028_2030_2100_stow_z2>0]

autocorr_inflow_20241028_2030_2100_stow = np.correlate(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241028_2030_2100_stow.U_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241028_2030_2100_stow_z3)
Lux_20241028_2030_2100_stow_z3 = Lux_20241028_2030_2100_stow_z3[Lux_20241028_2030_2100_stow_z3>0]

autocorr_inflow_20241028_2030_2100_stow = np.correlate(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241028_2030_2100_stow_z1)
Lwx_20241028_2030_2100_stow_z1 = Lwx_20241028_2030_2100_stow_z1[Lwx_20241028_2030_2100_stow_z1>0]

autocorr_inflow_20241028_2030_2100_stow = np.correlate(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241028_2030_2100_stow_z2)
Lwx_20241028_2030_2100_stow_z2 = Lwx_20241028_2030_2100_stow_z2[Lwx_20241028_2030_2100_stow_z2>0]

autocorr_inflow_20241028_2030_2100_stow = np.correlate(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241028_2030_2100_stow.W_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241028_2030_2100_stow_z3)
Lwx_20241028_2030_2100_stow_z3 = Lwx_20241028_2030_2100_stow_z3[Lwx_20241028_2030_2100_stow_z3>0]

Lux_profile_inflow_20241028_2030_2100_stow = pd.Series([Lux_20241028_2030_2100_stow_z1,Lux_20241028_2030_2100_stow_z2,Lux_20241028_2030_2100_stow_z3])
Lwx_profile_inflow_20241028_2030_2100_stow = pd.Series([Lwx_20241028_2030_2100_stow_z1,Lwx_20241028_2030_2100_stow_z2,Lwx_20241028_2030_2100_stow_z3])
 


#%% Mast 1

overlap = 0
nblock = len(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast1_20Hz_20241028_2030_2100_stow_z1, Pxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1 = fu_loads_mast1_20Hz_20241028_2030_2100_stow_z1*heights[0]/H2_U_ax_20241028_2030_2100_stow_z1
nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1 = (fu_loads_mast1_20Hz_20241028_2030_2100_stow_z1*Pxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1)/loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.std()**2

fu_loads_mast1_20Hz_20241028_2030_2100_stow_z2, Pxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2 = fu_loads_mast1_20Hz_20241028_2030_2100_stow_z2*heights[1]/H2_U_ax_20241028_2030_2100_stow_z2
nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2 = (fu_loads_mast1_20Hz_20241028_2030_2100_stow_z2*Pxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2)/loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.std()**2
 
fu_loads_mast1_20Hz_20241028_2030_2100_stow_z3, Pxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3 = fu_loads_mast1_20Hz_20241028_2030_2100_stow_z3*heights[2]/H2_U_ax_20241028_2030_2100_stow_z3
nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3 = (fu_loads_mast1_20Hz_20241028_2030_2100_stow_z3*Pxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3)/loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.std()**2              
    
fw_loads_mast1_20Hz_20241028_2030_2100_stow_z1, Pxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1 = fw_loads_mast1_20Hz_20241028_2030_2100_stow_z1*heights[0]/H2_W_ax_20241028_2030_2100_stow_z1
nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1 = (fw_loads_mast1_20Hz_20241028_2030_2100_stow_z1*Pxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1)/loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.std()**2

fw_loads_mast1_20Hz_20241028_2030_2100_stow_z2, Pxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2 = fw_loads_mast1_20Hz_20241028_2030_2100_stow_z2*heights[1]/H2_W_ax_20241028_2030_2100_stow_z2
nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2 = (fw_loads_mast1_20Hz_20241028_2030_2100_stow_z2*Pxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2)/loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.std()**2
 
fw_loads_mast1_20Hz_20241028_2030_2100_stow_z3, Pxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3 = fw_loads_mast1_20Hz_20241028_2030_2100_stow_z3*heights[2]/H2_W_ax_20241028_2030_2100_stow_z3
nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3 = (fw_loads_mast1_20Hz_20241028_2030_2100_stow_z3*Pxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3)/loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.std()**2              



#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1 = list(np.where([abs(nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1 = nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1[0][0]:len(nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1 = [nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2 = list(np.where([abs(nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2 = nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2[0][0]:len(nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2 = [nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3 = list(np.where([abs(nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3 = nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3[0][0]:len(nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3 = [nPxxfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1 = list(np.where([abs(nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1 = nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1[0][0]:len(nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1 = [nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2 = list(np.where([abs(nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2 = nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2[0][0]:len(nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2 = [nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3 = list(np.where([abs(nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3 = nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3[0][0]:len(nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3 = [nPxxfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241028_2030_2100_stow_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast1')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241028_2030_2100_stow_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast1')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()



#%% LS exponential fit method

autocorr_mast1_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241028_2030_2100_stow_z1)
Lux_mast1_20241028_2030_2100_stow_z1 = Lux_20241028_2030_2100_stow_z1[Lux_20241028_2030_2100_stow_z1>0]

autocorr_mast1_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241028_2030_2100_stow_z2)
Lux_mast1_20241028_2030_2100_stow_z2 = Lux_20241028_2030_2100_stow_z2[Lux_20241028_2030_2100_stow_z2>0]

autocorr_mast1_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m1_U_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241028_2030_2100_stow_z3)
Lux_mast1_20241028_2030_2100_stow_z3 = Lux_20241028_2030_2100_stow_z3[Lux_20241028_2030_2100_stow_z3>0]

autocorr_mast1_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241028_2030_2100_stow_z1)
Lwx_mast1_20241028_2030_2100_stow_z1 = Lwx_20241028_2030_2100_stow_z1[Lwx_20241028_2030_2100_stow_z1>0]

autocorr_mast1_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241028_2030_2100_stow_z2)
Lwx_mast1_20241028_2030_2100_stow_z2 = Lwx_20241028_2030_2100_stow_z2[Lwx_20241028_2030_2100_stow_z2>0]

autocorr_mast1_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m1_W_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241028_2030_2100_stow_z3)
Lwx_mast1_20241028_2030_2100_stow_z3 = Lwx_20241028_2030_2100_stow_z3[Lwx_20241028_2030_2100_stow_z3>0]

Lux_profile_mast1_20241028_2030_2100_stow = pd.Series([Lux_mast1_20241028_2030_2100_stow_z1,Lux_mast1_20241028_2030_2100_stow_z2,Lux_mast1_20241028_2030_2100_stow_z3])
Lwx_profile_mast1_20241028_2030_2100_stow = pd.Series([Lwx_mast1_20241028_2030_2100_stow_z1,Lwx_mast1_20241028_2030_2100_stow_z2,Lwx_mast1_20241028_2030_2100_stow_z3])
 


#%% Mast 3

overlap = 0
nblock = len(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast3_20Hz_20241028_2030_2100_stow_z1, Pxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1 = fu_loads_mast3_20Hz_20241028_2030_2100_stow_z1*heights[0]/H3_U_ax_20241028_2030_2100_stow_z1
nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1 = (fu_loads_mast3_20Hz_20241028_2030_2100_stow_z1*Pxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1)/loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.std()**2

fu_loads_mast3_20Hz_20241028_2030_2100_stow_z2, Pxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2 = fu_loads_mast3_20Hz_20241028_2030_2100_stow_z2*heights[1]/H3_U_ax_20241028_2030_2100_stow_z2
nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2 = (fu_loads_mast3_20Hz_20241028_2030_2100_stow_z2*Pxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2)/loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.std()**2
 
fu_loads_mast3_20Hz_20241028_2030_2100_stow_z3, Pxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3 = fu_loads_mast3_20Hz_20241028_2030_2100_stow_z3*heights[2]/H3_U_ax_20241028_2030_2100_stow_z3
nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3 = (fu_loads_mast3_20Hz_20241028_2030_2100_stow_z3*Pxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3)/loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.std()**2              
    
fw_loads_mast3_20Hz_20241028_2030_2100_stow_z1, Pxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1 = fw_loads_mast3_20Hz_20241028_2030_2100_stow_z1*heights[0]/H3_W_ax_20241028_2030_2100_stow_z1
nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1 = (fw_loads_mast3_20Hz_20241028_2030_2100_stow_z1*Pxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1)/loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.std()**2

fw_loads_mast3_20Hz_20241028_2030_2100_stow_z2, Pxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2 = fw_loads_mast3_20Hz_20241028_2030_2100_stow_z2*heights[1]/H3_W_ax_20241028_2030_2100_stow_z2
nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2 = (fw_loads_mast3_20Hz_20241028_2030_2100_stow_z2*Pxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2)/loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.std()**2
 
fw_loads_mast3_20Hz_20241028_2030_2100_stow_z3, Pxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3 = welch(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3 = fw_loads_mast3_20Hz_20241028_2030_2100_stow_z3*heights[2]/H3_W_ax_20241028_2030_2100_stow_z3
nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3 = (fw_loads_mast3_20Hz_20241028_2030_2100_stow_z3*Pxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3)/loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1 = list(np.where([abs(nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1 = nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1[0][0]:len(nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1 = [nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2 = list(np.where([abs(nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2 = nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2[0][0]:len(nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2 = [nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3 = list(np.where([abs(nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3 = nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3[0][0]:len(nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3 = [nPxxfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1 = list(np.where([abs(nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1 = nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1[0][0]:len(nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1 = [nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z1]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2 = list(np.where([abs(nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2 = nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2[0][0]:len(nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2 = [nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z2]

index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3 = list(np.where([abs(nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3 = nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3[index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3[0][0]:len(nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3 = [nPxxfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3[0:index_highfreq_loads_mast_20Hz_20241028_2030_2100_stow_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241028_2030_2100_stow_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241028_2030_2100_stow_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast3')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241028_2030_2100_stow_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241028_2030_2100_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast3')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()





#%% LS exponential fit method

autocorr_mast3_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241028_2030_2100_stow_z1)
Lux_mast3_20241028_2030_2100_stow_z1 = Lux_20241028_2030_2100_stow_z1[Lux_20241028_2030_2100_stow_z1>0]

autocorr_mast3_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241028_2030_2100_stow_z2)
Lux_mast3_20241028_2030_2100_stow_z2 = Lux_20241028_2030_2100_stow_z2[Lux_20241028_2030_2100_stow_z2>0]

autocorr_mast3_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m3_U_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241028_2030_2100_stow)
Lux_20241028_2030_2100_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241028_2030_2100_stow_z3)
Lux_mast3_20241028_2030_2100_stow_z3 = Lux_20241028_2030_2100_stow_z3[Lux_20241028_2030_2100_stow_z3>0]

autocorr_mast3_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241028_2030_2100_stow_z1)
Lwx_mast3_20241028_2030_2100_stow_z1 = Lwx_20241028_2030_2100_stow_z1[Lwx_20241028_2030_2100_stow_z1>0]

autocorr_mast3_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241028_2030_2100_stow_z2)
Lwx_mast3_20241028_2030_2100_stow_z2 = Lwx_20241028_2030_2100_stow_z2[Lwx_20241028_2030_2100_stow_z2>0]

autocorr_mast3_20241028_2030_2100_stow = np.correlate(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241028_2030_2100_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241028_2030_2100_stow.m3_W_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241028_2030_2100_stow)
Lwx_20241028_2030_2100_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241028_2030_2100_stow_z3)
Lwx_mast3_20241028_2030_2100_stow_z3 = Lwx_20241028_2030_2100_stow_z3[Lwx_20241028_2030_2100_stow_z3>0]

Lux_profile_mast3_20241028_2030_2100_stow = pd.Series([Lux_mast3_20241028_2030_2100_stow_z1,Lux_mast3_20241028_2030_2100_stow_z2,Lux_mast3_20241028_2030_2100_stow_z3])
Lwx_profile_mast3_20241028_2030_2100_stow = pd.Series([Lwx_mast3_20241028_2030_2100_stow_z1,Lwx_mast3_20241028_2030_2100_stow_z2,Lwx_mast3_20241028_2030_2100_stow_z3])
 

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241028_2030_2100_stow, heights, label='Lux')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_u^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10000)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241028_2030_2100_stow, heights, label='Lwx')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_w^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wspd_20241028_2030_2100_stow_z1,H1_wspd_20241028_2030_2100_stow_z2,H1_wspd_20241028_2030_2100_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wspd_20241028_2030_2100_stow_z1,H2_wspd_20241028_2030_2100_stow_z2,H2_wspd_20241028_2030_2100_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wspd_20241028_2030_2100_stow_z1,H3_wspd_20241028_2030_2100_stow_z2,H3_wspd_20241028_2030_2100_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind speed (m/s)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,15)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wdir_20241028_2030_2100_stow_z1,H1_wdir_20241028_2030_2100_stow_z2,H1_wdir_20241028_2030_2100_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wdir_20241028_2030_2100_stow_z1,H2_wdir_20241028_2030_2100_stow_z2,H2_wdir_20241028_2030_2100_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wdir_20241028_2030_2100_stow_z1,H3_wdir_20241028_2030_2100_stow_z2,H3_wdir_20241028_2030_2100_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind direction (deg)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(300,360)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iu_20241028_2030_2100_stow_z1,H1_Iu_20241028_2030_2100_stow_z2,H1_Iu_20241028_2030_2100_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iu_20241028_2030_2100_stow_z1,H2_Iu_20241028_2030_2100_stow_z2,H2_Iu_20241028_2030_2100_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iu_20241028_2030_2100_stow_z1,H3_Iu_20241028_2030_2100_stow_z2,H3_Iu_20241028_2030_2100_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_u$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iw_20241028_2030_2100_stow_z1,H1_Iw_20241028_2030_2100_stow_z2,H1_Iw_20241028_2030_2100_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iw_20241028_2030_2100_stow_z1,H2_Iw_20241028_2030_2100_stow_z2,H2_Iw_20241028_2030_2100_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iw_20241028_2030_2100_stow_z1,H3_Iw_20241028_2030_2100_stow_z2,H3_Iw_20241028_2030_2100_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_w$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.2)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241028_2030_2100_stow/11.23, heights, s=8,label='inflow')            
plt.scatter(Lux_profile_mast1_20241028_2030_2100_stow/11.23, heights, s=8,label='mast1')            
plt.scatter(Lux_profile_mast3_20241028_2030_2100_stow/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_u^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,150)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241028_2030_2100_stow/11.23, heights, s=8,label='inflow')            
plt.scatter(Lwx_profile_mast1_20241028_2030_2100_stow/11.23, heights, s=8,label='mast1')            
plt.scatter(Lwx_profile_mast3_20241028_2030_2100_stow/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_w^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()





#%% PSD analysis

heights = [2.75,5.5,11] 
fs = 20

# Spectra
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from numpy import hanning
import math

overlap = 0
nblock = len(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_inflow_20Hz_20241115_2045_2115_operation_z1, Pxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = welch(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = fu_loads_inflow_20Hz_20241115_2045_2115_operation_z1*heights[0]/H1_U_ax_20241115_2045_2115_operation_z1
nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = (fu_loads_inflow_20Hz_20241115_2045_2115_operation_z1*Pxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1)/loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.std()**2

fu_loads_inflow_20Hz_20241115_2045_2115_operation_z2, Pxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = welch(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = fu_loads_inflow_20Hz_20241115_2045_2115_operation_z2*heights[1]/H1_U_ax_20241115_2045_2115_operation_z2
nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = (fu_loads_inflow_20Hz_20241115_2045_2115_operation_z2*Pxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2)/loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.std()**2
 
fu_loads_inflow_20Hz_20241115_2045_2115_operation_z3, Pxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = welch(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = fu_loads_inflow_20Hz_20241115_2045_2115_operation_z3*heights[2]/H1_U_ax_20241115_2045_2115_operation_z3
nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = (fu_loads_inflow_20Hz_20241115_2045_2115_operation_z3*Pxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3)/loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.std()**2              
    
fw_loads_inflow_20Hz_20241115_2045_2115_operation_z1, Pxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = welch(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = fw_loads_inflow_20Hz_20241115_2045_2115_operation_z1*heights[0]/H1_W_ax_20241115_2045_2115_operation_z1
nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = (fw_loads_inflow_20Hz_20241115_2045_2115_operation_z1*Pxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1)/loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.std()**2

fw_loads_inflow_20Hz_20241115_2045_2115_operation_z2, Pxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = welch(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = fw_loads_inflow_20Hz_20241115_2045_2115_operation_z2*heights[1]/H1_W_ax_20241115_2045_2115_operation_z2
nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = (fw_loads_inflow_20Hz_20241115_2045_2115_operation_z2*Pxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2)/loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.std()**2
 
fw_loads_inflow_20Hz_20241115_2045_2115_operation_z3, Pxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = welch(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = fw_loads_inflow_20Hz_20241115_2045_2115_operation_z3*heights[2]/H1_W_ax_20241115_2045_2115_operation_z3
nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = (fw_loads_inflow_20Hz_20241115_2045_2115_operation_z3*Pxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3)/loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = list(np.where([abs(nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1[index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z1[0][0]:len(nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1)]
nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z1,200)
nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = [nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1[0:index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z1[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z1]

index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = list(np.where([abs(nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2[index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z2[0][0]:len(nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2)]
nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z2,200)
nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = [nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2[0:index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z2[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z2]

index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = list(np.where([abs(nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3[index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z3[0][0]:len(nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3)]
nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z3,200)
nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = [nPxxfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3[0:index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z3[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z3]

index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = list(np.where([abs(nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1[index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z1[0][0]:len(nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1)]
nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z1,200)
nPxxfw_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z1 = [nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1[0:index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z1[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z1]

index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = list(np.where([abs(nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2[index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z2[0][0]:len(nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2)]
nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z2,200)
nPxxfw_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z2 = [nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2[0:index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z2[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z2]

index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = list(np.where([abs(nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3[index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z3[0][0]:len(nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3)]
nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z3,200)
nPxxfw_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z3 = [nPxxfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3[0:index_highfreq_loads_inflow_20Hz_20241115_2045_2115_operation_z3[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241115_2045_2115_operation_z3]


plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z1[0:len(nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z2[0:len(nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241115_2045_2115_operation_z3[0:len(nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('inflow')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z1[0:len(nPxxfw_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z2[0:len(nPxxfw_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241115_2045_2115_operation_z3[0:len(nPxxfw_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2045_2115_operation_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('inflow')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()


#%% Extract data by height

U_corr_inflow_20241115_2045_2115_operation_z1 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low)
U_corr_inflow_20241115_2045_2115_operation_z2 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid)
U_corr_inflow_20241115_2045_2115_operation_z3 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top)

V_corr_inflow_20241115_2045_2115_operation_z1 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.V_ax_Low)
V_corr_inflow_20241115_2045_2115_operation_z2 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.V_ax_Mid)
V_corr_inflow_20241115_2045_2115_operation_z3 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.V_ax_Top)

W_corr_inflow_20241115_2045_2115_operation_z1 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low)
W_corr_inflow_20241115_2045_2115_operation_z2 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid)
W_corr_inflow_20241115_2045_2115_operation_z3 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top)

Ts_corr_inflow_20241115_2045_2115_operation_z1 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.Ts_Low)
Ts_corr_inflow_20241115_2045_2115_operation_z2 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.Ts_Mid)
Ts_corr_inflow_20241115_2045_2115_operation_z3 = pd.Series(loads_inflow_20Hz_20241115_2045_2115_operation.Ts_Top)

# Detrend
U_corr_inflow_20241115_2045_2115_operation_z1[U_corr_inflow_20241115_2045_2115_operation_z1.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241115_2045_2115_operation_z1.dropna()) 
U_corr_inflow_20241115_2045_2115_operation_z2[U_corr_inflow_20241115_2045_2115_operation_z2.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241115_2045_2115_operation_z2.dropna()) 
U_corr_inflow_20241115_2045_2115_operation_z3[U_corr_inflow_20241115_2045_2115_operation_z3.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241115_2045_2115_operation_z3.dropna()) 

V_corr_inflow_20241115_2045_2115_operation_z1[V_corr_inflow_20241115_2045_2115_operation_z1.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241115_2045_2115_operation_z1.dropna()) 
V_corr_inflow_20241115_2045_2115_operation_z2[V_corr_inflow_20241115_2045_2115_operation_z2.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241115_2045_2115_operation_z2.dropna()) 
V_corr_inflow_20241115_2045_2115_operation_z3[V_corr_inflow_20241115_2045_2115_operation_z3.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241115_2045_2115_operation_z3.dropna()) 

W_corr_inflow_20241115_2045_2115_operation_z1[W_corr_inflow_20241115_2045_2115_operation_z1.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241115_2045_2115_operation_z1.dropna()) 
W_corr_inflow_20241115_2045_2115_operation_z2[W_corr_inflow_20241115_2045_2115_operation_z2.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241115_2045_2115_operation_z2.dropna()) 
W_corr_inflow_20241115_2045_2115_operation_z3[W_corr_inflow_20241115_2045_2115_operation_z3.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241115_2045_2115_operation_z3.dropna()) 

Ts_corr_inflow_20241115_2045_2115_operation_z1[Ts_corr_inflow_20241115_2045_2115_operation_z1.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241115_2045_2115_operation_z1.dropna()) 
Ts_corr_inflow_20241115_2045_2115_operation_z2[Ts_corr_inflow_20241115_2045_2115_operation_z2.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241115_2045_2115_operation_z2.dropna()) 
Ts_corr_inflow_20241115_2045_2115_operation_z3[Ts_corr_inflow_20241115_2045_2115_operation_z3.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241115_2045_2115_operation_z3.dropna()) 

# Reynolds stresses and length scales (south2)

inflow_uv_z1_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z1*V_corr_inflow_20241115_2045_2115_operation_z1).mean()-(U_corr_inflow_20241115_2045_2115_operation_z1.mean()*V_corr_inflow_20241115_2045_2115_operation_z1.mean());
inflow_vw_z1_20241115_2045_2115_operation = (V_corr_inflow_20241115_2045_2115_operation_z1*W_corr_inflow_20241115_2045_2115_operation_z1).mean()-(V_corr_inflow_20241115_2045_2115_operation_z1.mean()*W_corr_inflow_20241115_2045_2115_operation_z1.mean());
inflow_uw_z1_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z1*W_corr_inflow_20241115_2045_2115_operation_z1).mean()-(U_corr_inflow_20241115_2045_2115_operation_z1.mean()*W_corr_inflow_20241115_2045_2115_operation_z1.mean());
inflow_wT_z1_20241115_2045_2115_operation = (W_corr_inflow_20241115_2045_2115_operation_z1*Ts_corr_inflow_20241115_2045_2115_operation_z1).mean()-(W_corr_inflow_20241115_2045_2115_operation_z1.mean()*Ts_corr_inflow_20241115_2045_2115_operation_z1.mean());

inflow_uv_z2_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z2*V_corr_inflow_20241115_2045_2115_operation_z2).mean()-(U_corr_inflow_20241115_2045_2115_operation_z2.mean()*V_corr_inflow_20241115_2045_2115_operation_z2.mean());
inflow_vw_z2_20241115_2045_2115_operation = (V_corr_inflow_20241115_2045_2115_operation_z2*W_corr_inflow_20241115_2045_2115_operation_z2).mean()-(V_corr_inflow_20241115_2045_2115_operation_z2.mean()*W_corr_inflow_20241115_2045_2115_operation_z2.mean());
inflow_uw_z2_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z2*W_corr_inflow_20241115_2045_2115_operation_z2).mean()-(U_corr_inflow_20241115_2045_2115_operation_z2.mean()*W_corr_inflow_20241115_2045_2115_operation_z2.mean());
inflow_wT_z2_20241115_2045_2115_operation = (W_corr_inflow_20241115_2045_2115_operation_z2*Ts_corr_inflow_20241115_2045_2115_operation_z2).mean()-(W_corr_inflow_20241115_2045_2115_operation_z2.mean()*Ts_corr_inflow_20241115_2045_2115_operation_z2.mean());

inflow_uv_z3_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z3*V_corr_inflow_20241115_2045_2115_operation_z3).mean()-(U_corr_inflow_20241115_2045_2115_operation_z3.mean()*V_corr_inflow_20241115_2045_2115_operation_z3.mean());
inflow_vw_z3_20241115_2045_2115_operation = (V_corr_inflow_20241115_2045_2115_operation_z3*W_corr_inflow_20241115_2045_2115_operation_z3).mean()-(V_corr_inflow_20241115_2045_2115_operation_z3.mean()*W_corr_inflow_20241115_2045_2115_operation_z3.mean());
inflow_uw_z3_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z3*W_corr_inflow_20241115_2045_2115_operation_z3).mean()-(U_corr_inflow_20241115_2045_2115_operation_z3.mean()*W_corr_inflow_20241115_2045_2115_operation_z3.mean());
inflow_wT_z3_20241115_2045_2115_operation = (W_corr_inflow_20241115_2045_2115_operation_z3*Ts_corr_inflow_20241115_2045_2115_operation_z3).mean()-(W_corr_inflow_20241115_2045_2115_operation_z3.mean()*Ts_corr_inflow_20241115_2045_2115_operation_z3.mean());

utau_z1_20241115_2045_2115_operation = (inflow_uw_z1_20241115_2045_2115_operation**2+inflow_vw_z1_20241115_2045_2115_operation**2)**(1/4) 
utau_z2_20241115_2045_2115_operation = (inflow_uw_z2_20241115_2045_2115_operation**2+inflow_vw_z2_20241115_2045_2115_operation**2)**(1/4) 
utau_z3_20241115_2045_2115_operation = (inflow_uw_z3_20241115_2045_2115_operation**2+inflow_vw_z3_20241115_2045_2115_operation**2)**(1/4) 

L_z1_20241115_2045_2115_operation = -1*(utau_z1_20241115_2045_2115_operation**3)/(0.4*(9.81/H1_Ts_20241115_2045_2115_operation_z1)*inflow_wT_z1_20241115_2045_2115_operation)
L_z2_20241115_2045_2115_operation = -1*(utau_z2_20241115_2045_2115_operation**3)/(0.4*(9.81/H1_Ts_20241115_2045_2115_operation_z2)*inflow_wT_z2_20241115_2045_2115_operation)
L_z3_20241115_2045_2115_operation = -1*(utau_z3_20241115_2045_2115_operation**3)/(0.4*(9.81/H1_Ts_20241115_2045_2115_operation_z3)*inflow_wT_z3_20241115_2045_2115_operation)

zL_z1_20241115_2045_2115_operation = heights[0]/L_z1_20241115_2045_2115_operation
zL_z2_20241115_2045_2115_operation = heights[1]/L_z2_20241115_2045_2115_operation
zL_z3_20241115_2045_2115_operation = heights[2]/L_z3_20241115_2045_2115_operation

inflow_uprimewprime_z1_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z1*W_corr_inflow_20241115_2045_2115_operation_z1);
inflow_uprimewprime_z2_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z2*W_corr_inflow_20241115_2045_2115_operation_z2);
inflow_uprimewprime_z3_20241115_2045_2115_operation = (U_corr_inflow_20241115_2045_2115_operation_z3*W_corr_inflow_20241115_2045_2115_operation_z3);


#%% LS exponential fit method

autocorr_inflow_20241115_2045_2115_operation = np.correlate(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2045_2115_operation_z1)
Lux_20241115_2045_2115_operation_z1 = Lux_20241115_2045_2115_operation_z1[Lux_20241115_2045_2115_operation_z1>0]

autocorr_inflow_20241115_2045_2115_operation = np.correlate(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2045_2115_operation_z2)
Lux_20241115_2045_2115_operation_z2 = Lux_20241115_2045_2115_operation_z2[Lux_20241115_2045_2115_operation_z2>0]

autocorr_inflow_20241115_2045_2115_operation = np.correlate(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241115_2045_2115_operation.U_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2045_2115_operation_z3)
Lux_20241115_2045_2115_operation_z3 = Lux_20241115_2045_2115_operation_z3[Lux_20241115_2045_2115_operation_z3>0]

autocorr_inflow_20241115_2045_2115_operation = np.correlate(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2045_2115_operation_z1)
Lwx_20241115_2045_2115_operation_z1 = Lwx_20241115_2045_2115_operation_z1[Lwx_20241115_2045_2115_operation_z1>0]

autocorr_inflow_20241115_2045_2115_operation = np.correlate(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2045_2115_operation_z2)
Lwx_20241115_2045_2115_operation_z2 = Lwx_20241115_2045_2115_operation_z2[Lwx_20241115_2045_2115_operation_z2>0]

autocorr_inflow_20241115_2045_2115_operation = np.correlate(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna(), loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241115_2045_2115_operation.W_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2045_2115_operation_z3)
Lwx_20241115_2045_2115_operation_z3 = Lwx_20241115_2045_2115_operation_z3[Lwx_20241115_2045_2115_operation_z3>0]

Lux_profile_inflow_20241115_2045_2115_operation = pd.Series([Lux_20241115_2045_2115_operation_z1,Lux_20241115_2045_2115_operation_z2,Lux_20241115_2045_2115_operation_z3])
Lwx_profile_inflow_20241115_2045_2115_operation = pd.Series([Lwx_20241115_2045_2115_operation_z1,Lwx_20241115_2045_2115_operation_z2,Lwx_20241115_2045_2115_operation_z3])
 


#%% Mast 1

U_corr_mast1_20241115_2045_2115_operation_z1 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low)
U_corr_mast1_20241115_2045_2115_operation_z2 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid)
U_corr_mast1_20241115_2045_2115_operation_z3 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top)

V_corr_mast1_20241115_2045_2115_operation_z1 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_V_ax_Low)
V_corr_mast1_20241115_2045_2115_operation_z2 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_V_ax_Mid)
V_corr_mast1_20241115_2045_2115_operation_z3 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_V_ax_Top)

W_corr_mast1_20241115_2045_2115_operation_z1 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low)
W_corr_mast1_20241115_2045_2115_operation_z2 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid)
W_corr_mast1_20241115_2045_2115_operation_z3 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top)

mast1_uprimewprime_z1_20241115_2045_2115_operation = (U_corr_mast1_20241115_2045_2115_operation_z1*W_corr_mast1_20241115_2045_2115_operation_z1);
mast1_uprimewprime_z2_20241115_2045_2115_operation = (U_corr_mast1_20241115_2045_2115_operation_z2*W_corr_mast1_20241115_2045_2115_operation_z2);
mast1_uprimewprime_z3_20241115_2045_2115_operation = (U_corr_mast1_20241115_2045_2115_operation_z3*W_corr_mast1_20241115_2045_2115_operation_z3);


overlap = 0
nblock = len(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast1_20Hz_20241115_2045_2115_operation_z1, Pxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1 = fu_loads_mast1_20Hz_20241115_2045_2115_operation_z1*heights[0]/H2_U_ax_20241115_2045_2115_operation_z1
nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1 = (fu_loads_mast1_20Hz_20241115_2045_2115_operation_z1*Pxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1)/loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.std()**2

fu_loads_mast1_20Hz_20241115_2045_2115_operation_z2, Pxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2 = fu_loads_mast1_20Hz_20241115_2045_2115_operation_z2*heights[1]/H2_U_ax_20241115_2045_2115_operation_z2
nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2 = (fu_loads_mast1_20Hz_20241115_2045_2115_operation_z2*Pxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2)/loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.std()**2
 
fu_loads_mast1_20Hz_20241115_2045_2115_operation_z3, Pxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3 = fu_loads_mast1_20Hz_20241115_2045_2115_operation_z3*heights[2]/H2_U_ax_20241115_2045_2115_operation_z3
nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3 = (fu_loads_mast1_20Hz_20241115_2045_2115_operation_z3*Pxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3)/loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.std()**2              
    
fw_loads_mast1_20Hz_20241115_2045_2115_operation_z1, Pxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1 = fw_loads_mast1_20Hz_20241115_2045_2115_operation_z1*heights[0]/H2_W_ax_20241115_2045_2115_operation_z1
nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1 = (fw_loads_mast1_20Hz_20241115_2045_2115_operation_z1*Pxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1)/loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.std()**2

fw_loads_mast1_20Hz_20241115_2045_2115_operation_z2, Pxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2 = fw_loads_mast1_20Hz_20241115_2045_2115_operation_z2*heights[1]/H2_W_ax_20241115_2045_2115_operation_z2
nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2 = (fw_loads_mast1_20Hz_20241115_2045_2115_operation_z2*Pxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2)/loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.std()**2
 
fw_loads_mast1_20Hz_20241115_2045_2115_operation_z3, Pxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3 = fw_loads_mast1_20Hz_20241115_2045_2115_operation_z3*heights[2]/H2_W_ax_20241115_2045_2115_operation_z3
nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3 = (fw_loads_mast1_20Hz_20241115_2045_2115_operation_z3*Pxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3)/loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.std()**2              



#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1 = list(np.where([abs(nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1 = nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1[0][0]:len(nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1 = [nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2 = list(np.where([abs(nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2 = nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2[0][0]:len(nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2 = [nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3 = list(np.where([abs(nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3 = nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3[0][0]:len(nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3 = [nPxxfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1 = list(np.where([abs(nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1 = nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1[0][0]:len(nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1 = [nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2 = list(np.where([abs(nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2 = nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2[0][0]:len(nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2 = [nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3 = list(np.where([abs(nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3 = nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3[0][0]:len(nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3 = [nPxxfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241115_2045_2115_operation_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast1')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241115_2045_2115_operation_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast1')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()



#%% LS exponential fit method

autocorr_mast1_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2045_2115_operation_z1)
Lux_mast1_20241115_2045_2115_operation_z1 = Lux_20241115_2045_2115_operation_z1[Lux_20241115_2045_2115_operation_z1>0]

autocorr_mast1_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2045_2115_operation_z2)
Lux_mast1_20241115_2045_2115_operation_z2 = Lux_20241115_2045_2115_operation_z2[Lux_20241115_2045_2115_operation_z2>0]

autocorr_mast1_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m1_U_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2045_2115_operation_z3)
Lux_mast1_20241115_2045_2115_operation_z3 = Lux_20241115_2045_2115_operation_z3[Lux_20241115_2045_2115_operation_z3>0]

autocorr_mast1_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2045_2115_operation_z1)
Lwx_mast1_20241115_2045_2115_operation_z1 = Lwx_20241115_2045_2115_operation_z1[Lwx_20241115_2045_2115_operation_z1>0]

autocorr_mast1_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2045_2115_operation_z2)
Lwx_mast1_20241115_2045_2115_operation_z2 = Lwx_20241115_2045_2115_operation_z2[Lwx_20241115_2045_2115_operation_z2>0]

autocorr_mast1_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m1_W_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2045_2115_operation_z3)
Lwx_mast1_20241115_2045_2115_operation_z3 = Lwx_20241115_2045_2115_operation_z3[Lwx_20241115_2045_2115_operation_z3>0]

Lux_profile_mast1_20241115_2045_2115_operation = pd.Series([Lux_mast1_20241115_2045_2115_operation_z1,Lux_mast1_20241115_2045_2115_operation_z2,Lux_mast1_20241115_2045_2115_operation_z3])
Lwx_profile_mast1_20241115_2045_2115_operation = pd.Series([Lwx_mast1_20241115_2045_2115_operation_z1,Lwx_mast1_20241115_2045_2115_operation_z2,Lwx_mast1_20241115_2045_2115_operation_z3])
 


#%% Mast 3

U_corr_mast3_20241115_2045_2115_operation_z1 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low)
U_corr_mast3_20241115_2045_2115_operation_z2 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid)
U_corr_mast3_20241115_2045_2115_operation_z3 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top)

V_corr_mast3_20241115_2045_2115_operation_z1 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_V_ax_Low)
V_corr_mast3_20241115_2045_2115_operation_z2 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_V_ax_Mid)
V_corr_mast3_20241115_2045_2115_operation_z3 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_V_ax_Top)

W_corr_mast3_20241115_2045_2115_operation_z1 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low)
W_corr_mast3_20241115_2045_2115_operation_z2 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid)
W_corr_mast3_20241115_2045_2115_operation_z3 = pd.Series(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top)

mast3_uprimewprime_z1_20241115_2045_2115_operation = (U_corr_mast3_20241115_2045_2115_operation_z1*W_corr_mast3_20241115_2045_2115_operation_z1);
mast3_uprimewprime_z2_20241115_2045_2115_operation = (U_corr_mast3_20241115_2045_2115_operation_z2*W_corr_mast3_20241115_2045_2115_operation_z2);
mast3_uprimewprime_z3_20241115_2045_2115_operation = (U_corr_mast3_20241115_2045_2115_operation_z3*W_corr_mast3_20241115_2045_2115_operation_z3);


overlap = 0
nblock = len(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast3_20Hz_20241115_2045_2115_operation_z1, Pxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1 = fu_loads_mast3_20Hz_20241115_2045_2115_operation_z1*heights[0]/H3_U_ax_20241115_2045_2115_operation_z1
nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1 = (fu_loads_mast3_20Hz_20241115_2045_2115_operation_z1*Pxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1)/loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.std()**2

fu_loads_mast3_20Hz_20241115_2045_2115_operation_z2, Pxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2 = fu_loads_mast3_20Hz_20241115_2045_2115_operation_z2*heights[1]/H3_U_ax_20241115_2045_2115_operation_z2
nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2 = (fu_loads_mast3_20Hz_20241115_2045_2115_operation_z2*Pxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2)/loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.std()**2
 
fu_loads_mast3_20Hz_20241115_2045_2115_operation_z3, Pxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3 = fu_loads_mast3_20Hz_20241115_2045_2115_operation_z3*heights[2]/H3_U_ax_20241115_2045_2115_operation_z3
nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3 = (fu_loads_mast3_20Hz_20241115_2045_2115_operation_z3*Pxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3)/loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.std()**2              
    
fw_loads_mast3_20Hz_20241115_2045_2115_operation_z1, Pxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1 = fw_loads_mast3_20Hz_20241115_2045_2115_operation_z1*heights[0]/H3_W_ax_20241115_2045_2115_operation_z1
nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1 = (fw_loads_mast3_20Hz_20241115_2045_2115_operation_z1*Pxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1)/loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.std()**2

fw_loads_mast3_20Hz_20241115_2045_2115_operation_z2, Pxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2 = fw_loads_mast3_20Hz_20241115_2045_2115_operation_z2*heights[1]/H3_W_ax_20241115_2045_2115_operation_z2
nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2 = (fw_loads_mast3_20Hz_20241115_2045_2115_operation_z2*Pxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2)/loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.std()**2
 
fw_loads_mast3_20Hz_20241115_2045_2115_operation_z3, Pxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3 = welch(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3 = fw_loads_mast3_20Hz_20241115_2045_2115_operation_z3*heights[2]/H3_W_ax_20241115_2045_2115_operation_z3
nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3 = (fw_loads_mast3_20Hz_20241115_2045_2115_operation_z3*Pxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3)/loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1 = list(np.where([abs(nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1 = nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1[0][0]:len(nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1 = [nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2 = list(np.where([abs(nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2 = nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2[0][0]:len(nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2 = [nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3 = list(np.where([abs(nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3 = nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3[0][0]:len(nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3 = [nPxxfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1 = list(np.where([abs(nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1 = nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1[0][0]:len(nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1 = [nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z1]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2 = list(np.where([abs(nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2 = nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2[0][0]:len(nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2 = [nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z2]

index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3 = list(np.where([abs(nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3 = nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3[index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3[0][0]:len(nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3 = [nPxxfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3[0:index_highfreq_loads_mast_20Hz_20241115_2045_2115_operation_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2045_2115_operation_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241115_2045_2115_operation_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast3')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241115_2045_2115_operation_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2045_2115_operation_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast3')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()





#%% LS exponential fit method

autocorr_mast3_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2045_2115_operation_z1)
Lux_mast3_20241115_2045_2115_operation_z1 = Lux_20241115_2045_2115_operation_z1[Lux_20241115_2045_2115_operation_z1>0]

autocorr_mast3_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2045_2115_operation_z2)
Lux_mast3_20241115_2045_2115_operation_z2 = Lux_20241115_2045_2115_operation_z2[Lux_20241115_2045_2115_operation_z2>0]

autocorr_mast3_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m3_U_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241115_2045_2115_operation)
Lux_20241115_2045_2115_operation_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2045_2115_operation_z3)
Lux_mast3_20241115_2045_2115_operation_z3 = Lux_20241115_2045_2115_operation_z3[Lux_20241115_2045_2115_operation_z3>0]

autocorr_mast3_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2045_2115_operation_z1)
Lwx_mast3_20241115_2045_2115_operation_z1 = Lwx_20241115_2045_2115_operation_z1[Lwx_20241115_2045_2115_operation_z1>0]

autocorr_mast3_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2045_2115_operation_z2)
Lwx_mast3_20241115_2045_2115_operation_z2 = Lwx_20241115_2045_2115_operation_z2[Lwx_20241115_2045_2115_operation_z2>0]

autocorr_mast3_20241115_2045_2115_operation = np.correlate(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241115_2045_2115_operation /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241115_2045_2115_operation.m3_W_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241115_2045_2115_operation)
Lwx_20241115_2045_2115_operation_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2045_2115_operation_z3)
Lwx_mast3_20241115_2045_2115_operation_z3 = Lwx_20241115_2045_2115_operation_z3[Lwx_20241115_2045_2115_operation_z3>0]

Lux_profile_mast3_20241115_2045_2115_operation = pd.Series([Lux_mast3_20241115_2045_2115_operation_z1,Lux_mast3_20241115_2045_2115_operation_z2,Lux_mast3_20241115_2045_2115_operation_z3])
Lwx_profile_mast3_20241115_2045_2115_operation = pd.Series([Lwx_mast3_20241115_2045_2115_operation_z1,Lwx_mast3_20241115_2045_2115_operation_z2,Lwx_mast3_20241115_2045_2115_operation_z3])
 

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241115_2045_2115_operation, heights, label='Lux')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_u^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10000)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241115_2045_2115_operation, heights, label='Lwx')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_w^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wspd_20241115_2045_2115_operation_z1,H1_wspd_20241115_2045_2115_operation_z2,H1_wspd_20241115_2045_2115_operation_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wspd_20241115_2045_2115_operation_z1,H2_wspd_20241115_2045_2115_operation_z2,H2_wspd_20241115_2045_2115_operation_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wspd_20241115_2045_2115_operation_z1,H3_wspd_20241115_2045_2115_operation_z2,H3_wspd_20241115_2045_2115_operation_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind speed (m/s)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,15)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wdir_20241115_2045_2115_operation_z1,H1_wdir_20241115_2045_2115_operation_z2,H1_wdir_20241115_2045_2115_operation_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wdir_20241115_2045_2115_operation_z1,H2_wdir_20241115_2045_2115_operation_z2,H2_wdir_20241115_2045_2115_operation_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wdir_20241115_2045_2115_operation_z1,H3_wdir_20241115_2045_2115_operation_z2,H3_wdir_20241115_2045_2115_operation_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind direction (deg)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(250,350)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iu_20241115_2045_2115_operation_z1,H1_Iu_20241115_2045_2115_operation_z2,H1_Iu_20241115_2045_2115_operation_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iu_20241115_2045_2115_operation_z1,H2_Iu_20241115_2045_2115_operation_z2,H2_Iu_20241115_2045_2115_operation_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iu_20241115_2045_2115_operation_z1,H3_Iu_20241115_2045_2115_operation_z2,H3_Iu_20241115_2045_2115_operation_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_u$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.6)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iw_20241115_2045_2115_operation_z1,H1_Iw_20241115_2045_2115_operation_z2,H1_Iw_20241115_2045_2115_operation_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iw_20241115_2045_2115_operation_z1,H2_Iw_20241115_2045_2115_operation_z2,H2_Iw_20241115_2045_2115_operation_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iw_20241115_2045_2115_operation_z1,H3_Iw_20241115_2045_2115_operation_z2,H3_Iw_20241115_2045_2115_operation_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_w$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.6)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241115_2045_2115_operation/11.23, heights, s=8,label='inflow')            
plt.scatter(Lux_profile_mast1_20241115_2045_2115_operation/11.23, heights, s=8,label='mast1')            
plt.scatter(Lux_profile_mast3_20241115_2045_2115_operation/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_u^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,100)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241115_2045_2115_operation/11.23, heights, s=8,label='inflow')            
plt.scatter(Lwx_profile_mast1_20241115_2045_2115_operation/11.23, heights, s=8,label='mast1')            
plt.scatter(Lwx_profile_mast3_20241115_2045_2115_operation/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_w^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()





#%% PSD analysis

heights = [2.75,5.5,11] 
fs = 20

# Spectra
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from numpy import hanning
import math

overlap = 0
nblock = len(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_inflow_20Hz_20241115_2130_2200_stow_z1, Pxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = welch(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = fu_loads_inflow_20Hz_20241115_2130_2200_stow_z1*heights[0]/H1_U_ax_20241115_2130_2200_stow_z1
nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = (fu_loads_inflow_20Hz_20241115_2130_2200_stow_z1*Pxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1)/loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.std()**2

fu_loads_inflow_20Hz_20241115_2130_2200_stow_z2, Pxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = welch(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = fu_loads_inflow_20Hz_20241115_2130_2200_stow_z2*heights[1]/H1_U_ax_20241115_2130_2200_stow_z2
nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = (fu_loads_inflow_20Hz_20241115_2130_2200_stow_z2*Pxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2)/loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.std()**2
 
fu_loads_inflow_20Hz_20241115_2130_2200_stow_z3, Pxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = welch(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = fu_loads_inflow_20Hz_20241115_2130_2200_stow_z3*heights[2]/H1_U_ax_20241115_2130_2200_stow_z3
nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = (fu_loads_inflow_20Hz_20241115_2130_2200_stow_z3*Pxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3)/loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.std()**2              
    
fw_loads_inflow_20Hz_20241115_2130_2200_stow_z1, Pxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = welch(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = fw_loads_inflow_20Hz_20241115_2130_2200_stow_z1*heights[0]/H1_W_ax_20241115_2130_2200_stow_z1
nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = (fw_loads_inflow_20Hz_20241115_2130_2200_stow_z1*Pxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1)/loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.std()**2

fw_loads_inflow_20Hz_20241115_2130_2200_stow_z2, Pxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = welch(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = fw_loads_inflow_20Hz_20241115_2130_2200_stow_z2*heights[1]/H1_W_ax_20241115_2130_2200_stow_z2
nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = (fw_loads_inflow_20Hz_20241115_2130_2200_stow_z2*Pxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2)/loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.std()**2
 
fw_loads_inflow_20Hz_20241115_2130_2200_stow_z3, Pxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = welch(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = fw_loads_inflow_20Hz_20241115_2130_2200_stow_z3*heights[2]/H1_W_ax_20241115_2130_2200_stow_z3
nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = (fw_loads_inflow_20Hz_20241115_2130_2200_stow_z3*Pxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3)/loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = list(np.where([abs(nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1[index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z1[0][0]:len(nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1)]
nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z1,200)
nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = [nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1[0:index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z1[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z1]

index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = list(np.where([abs(nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2[index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z2[0][0]:len(nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2)]
nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z2,200)
nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = [nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2[0:index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z2[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z2]

index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = list(np.where([abs(nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3[index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z3[0][0]:len(nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3)]
nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z3,200)
nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = [nPxxfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3[0:index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z3[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z3]

index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = list(np.where([abs(nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1[index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z1[0][0]:len(nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1)]
nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z1,200)
nPxxfw_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z1 = [nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1[0:index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z1[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z1]

index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = list(np.where([abs(nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2[index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z2[0][0]:len(nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2)]
nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z2,200)
nPxxfw_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z2 = [nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2[0:index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z2[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z2]

index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = list(np.where([abs(nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3[index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z3[0][0]:len(nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3)]
nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z3,200)
nPxxfw_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z3 = [nPxxfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3[0:index_highfreq_loads_inflow_20Hz_20241115_2130_2200_stow_z3[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241115_2130_2200_stow_z3]


plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z1[0:len(nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z2[0:len(nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241115_2130_2200_stow_z3[0:len(nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('inflow')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z1[0:len(nPxxfw_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z2[0:len(nPxxfw_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241115_2130_2200_stow_z3[0:len(nPxxfw_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241115_2130_2200_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('inflow')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()


#%% Extract data by height

U_corr_inflow_20241115_2130_2200_stow_z1 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low)
U_corr_inflow_20241115_2130_2200_stow_z2 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid)
U_corr_inflow_20241115_2130_2200_stow_z3 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top)

V_corr_inflow_20241115_2130_2200_stow_z1 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.V_ax_Low)
V_corr_inflow_20241115_2130_2200_stow_z2 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.V_ax_Mid)
V_corr_inflow_20241115_2130_2200_stow_z3 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.V_ax_Top)

W_corr_inflow_20241115_2130_2200_stow_z1 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low)
W_corr_inflow_20241115_2130_2200_stow_z2 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid)
W_corr_inflow_20241115_2130_2200_stow_z3 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top)

Ts_corr_inflow_20241115_2130_2200_stow_z1 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.Ts_Low)
Ts_corr_inflow_20241115_2130_2200_stow_z2 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.Ts_Mid)
Ts_corr_inflow_20241115_2130_2200_stow_z3 = pd.Series(loads_inflow_20Hz_20241115_2130_2200_stow.Ts_Top)

# Detrend
U_corr_inflow_20241115_2130_2200_stow_z1[U_corr_inflow_20241115_2130_2200_stow_z1.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241115_2130_2200_stow_z1.dropna()) 
U_corr_inflow_20241115_2130_2200_stow_z2[U_corr_inflow_20241115_2130_2200_stow_z2.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241115_2130_2200_stow_z2.dropna()) 
U_corr_inflow_20241115_2130_2200_stow_z3[U_corr_inflow_20241115_2130_2200_stow_z3.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241115_2130_2200_stow_z3.dropna()) 

V_corr_inflow_20241115_2130_2200_stow_z1[V_corr_inflow_20241115_2130_2200_stow_z1.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241115_2130_2200_stow_z1.dropna()) 
V_corr_inflow_20241115_2130_2200_stow_z2[V_corr_inflow_20241115_2130_2200_stow_z2.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241115_2130_2200_stow_z2.dropna()) 
V_corr_inflow_20241115_2130_2200_stow_z3[V_corr_inflow_20241115_2130_2200_stow_z3.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241115_2130_2200_stow_z3.dropna()) 

W_corr_inflow_20241115_2130_2200_stow_z1[W_corr_inflow_20241115_2130_2200_stow_z1.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241115_2130_2200_stow_z1.dropna()) 
W_corr_inflow_20241115_2130_2200_stow_z2[W_corr_inflow_20241115_2130_2200_stow_z2.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241115_2130_2200_stow_z2.dropna()) 
W_corr_inflow_20241115_2130_2200_stow_z3[W_corr_inflow_20241115_2130_2200_stow_z3.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241115_2130_2200_stow_z3.dropna()) 

Ts_corr_inflow_20241115_2130_2200_stow_z1[Ts_corr_inflow_20241115_2130_2200_stow_z1.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241115_2130_2200_stow_z1.dropna()) 
Ts_corr_inflow_20241115_2130_2200_stow_z2[Ts_corr_inflow_20241115_2130_2200_stow_z2.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241115_2130_2200_stow_z2.dropna()) 
Ts_corr_inflow_20241115_2130_2200_stow_z3[Ts_corr_inflow_20241115_2130_2200_stow_z3.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241115_2130_2200_stow_z3.dropna()) 

# Reynolds stresses and length scales (south2)

inflow_uv_z1_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z1*V_corr_inflow_20241115_2130_2200_stow_z1).mean()-(U_corr_inflow_20241115_2130_2200_stow_z1.mean()*V_corr_inflow_20241115_2130_2200_stow_z1.mean());
inflow_vw_z1_20241115_2130_2200_stow = (V_corr_inflow_20241115_2130_2200_stow_z1*W_corr_inflow_20241115_2130_2200_stow_z1).mean()-(V_corr_inflow_20241115_2130_2200_stow_z1.mean()*W_corr_inflow_20241115_2130_2200_stow_z1.mean());
inflow_uw_z1_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z1*W_corr_inflow_20241115_2130_2200_stow_z1).mean()-(U_corr_inflow_20241115_2130_2200_stow_z1.mean()*W_corr_inflow_20241115_2130_2200_stow_z1.mean());
inflow_wT_z1_20241115_2130_2200_stow = (W_corr_inflow_20241115_2130_2200_stow_z1*Ts_corr_inflow_20241115_2130_2200_stow_z1).mean()-(W_corr_inflow_20241115_2130_2200_stow_z1.mean()*Ts_corr_inflow_20241115_2130_2200_stow_z1.mean());

inflow_uv_z2_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z2*V_corr_inflow_20241115_2130_2200_stow_z2).mean()-(U_corr_inflow_20241115_2130_2200_stow_z2.mean()*V_corr_inflow_20241115_2130_2200_stow_z2.mean());
inflow_vw_z2_20241115_2130_2200_stow = (V_corr_inflow_20241115_2130_2200_stow_z2*W_corr_inflow_20241115_2130_2200_stow_z2).mean()-(V_corr_inflow_20241115_2130_2200_stow_z2.mean()*W_corr_inflow_20241115_2130_2200_stow_z2.mean());
inflow_uw_z2_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z2*W_corr_inflow_20241115_2130_2200_stow_z2).mean()-(U_corr_inflow_20241115_2130_2200_stow_z2.mean()*W_corr_inflow_20241115_2130_2200_stow_z2.mean());
inflow_wT_z2_20241115_2130_2200_stow = (W_corr_inflow_20241115_2130_2200_stow_z2*Ts_corr_inflow_20241115_2130_2200_stow_z2).mean()-(W_corr_inflow_20241115_2130_2200_stow_z2.mean()*Ts_corr_inflow_20241115_2130_2200_stow_z2.mean());

inflow_uv_z3_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z3*V_corr_inflow_20241115_2130_2200_stow_z3).mean()-(U_corr_inflow_20241115_2130_2200_stow_z3.mean()*V_corr_inflow_20241115_2130_2200_stow_z3.mean());
inflow_vw_z3_20241115_2130_2200_stow = (V_corr_inflow_20241115_2130_2200_stow_z3*W_corr_inflow_20241115_2130_2200_stow_z3).mean()-(V_corr_inflow_20241115_2130_2200_stow_z3.mean()*W_corr_inflow_20241115_2130_2200_stow_z3.mean());
inflow_uw_z3_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z3*W_corr_inflow_20241115_2130_2200_stow_z3).mean()-(U_corr_inflow_20241115_2130_2200_stow_z3.mean()*W_corr_inflow_20241115_2130_2200_stow_z3.mean());
inflow_wT_z3_20241115_2130_2200_stow = (W_corr_inflow_20241115_2130_2200_stow_z3*Ts_corr_inflow_20241115_2130_2200_stow_z3).mean()-(W_corr_inflow_20241115_2130_2200_stow_z3.mean()*Ts_corr_inflow_20241115_2130_2200_stow_z3.mean());

utau_z1_20241115_2130_2200_stow = (inflow_uw_z1_20241115_2130_2200_stow**2+inflow_vw_z1_20241115_2130_2200_stow**2)**(1/4) 
utau_z2_20241115_2130_2200_stow = (inflow_uw_z2_20241115_2130_2200_stow**2+inflow_vw_z2_20241115_2130_2200_stow**2)**(1/4) 
utau_z3_20241115_2130_2200_stow = (inflow_uw_z3_20241115_2130_2200_stow**2+inflow_vw_z3_20241115_2130_2200_stow**2)**(1/4) 

L_z1_20241115_2130_2200_stow = -1*(utau_z1_20241115_2130_2200_stow**3)/(0.4*(9.81/H1_Ts_20241115_2130_2200_stow_z1)*inflow_wT_z1_20241115_2130_2200_stow)
L_z2_20241115_2130_2200_stow = -1*(utau_z2_20241115_2130_2200_stow**3)/(0.4*(9.81/H1_Ts_20241115_2130_2200_stow_z2)*inflow_wT_z2_20241115_2130_2200_stow)
L_z3_20241115_2130_2200_stow = -1*(utau_z3_20241115_2130_2200_stow**3)/(0.4*(9.81/H1_Ts_20241115_2130_2200_stow_z3)*inflow_wT_z3_20241115_2130_2200_stow)

zL_z1_20241115_2130_2200_stow = heights[0]/L_z1_20241115_2130_2200_stow
zL_z2_20241115_2130_2200_stow = heights[1]/L_z2_20241115_2130_2200_stow
zL_z3_20241115_2130_2200_stow = heights[2]/L_z3_20241115_2130_2200_stow

inflow_uprimewprime_z1_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z1*W_corr_inflow_20241115_2130_2200_stow_z1);
inflow_uprimewprime_z2_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z2*W_corr_inflow_20241115_2130_2200_stow_z2);
inflow_uprimewprime_z3_20241115_2130_2200_stow = (U_corr_inflow_20241115_2130_2200_stow_z3*W_corr_inflow_20241115_2130_2200_stow_z3);


#%% LS exponential fit method

autocorr_inflow_20241115_2130_2200_stow = np.correlate(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2130_2200_stow_z1)
Lux_20241115_2130_2200_stow_z1 = Lux_20241115_2130_2200_stow_z1[Lux_20241115_2130_2200_stow_z1>0]

autocorr_inflow_20241115_2130_2200_stow = np.correlate(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2130_2200_stow_z2)
Lux_20241115_2130_2200_stow_z2 = Lux_20241115_2130_2200_stow_z2[Lux_20241115_2130_2200_stow_z2>0]

autocorr_inflow_20241115_2130_2200_stow = np.correlate(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241115_2130_2200_stow.U_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2130_2200_stow_z3)
Lux_20241115_2130_2200_stow_z3 = Lux_20241115_2130_2200_stow_z3[Lux_20241115_2130_2200_stow_z3>0]

autocorr_inflow_20241115_2130_2200_stow = np.correlate(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2130_2200_stow_z1)
Lwx_20241115_2130_2200_stow_z1 = Lwx_20241115_2130_2200_stow_z1[Lwx_20241115_2130_2200_stow_z1>0]

autocorr_inflow_20241115_2130_2200_stow = np.correlate(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2130_2200_stow_z2)
Lwx_20241115_2130_2200_stow_z2 = Lwx_20241115_2130_2200_stow_z2[Lwx_20241115_2130_2200_stow_z2>0]

autocorr_inflow_20241115_2130_2200_stow = np.correlate(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241115_2130_2200_stow.W_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241115_2130_2200_stow_z3)
Lwx_20241115_2130_2200_stow_z3 = Lwx_20241115_2130_2200_stow_z3[Lwx_20241115_2130_2200_stow_z3>0]

Lux_profile_inflow_20241115_2130_2200_stow = pd.Series([Lux_20241115_2130_2200_stow_z1,Lux_20241115_2130_2200_stow_z2,Lux_20241115_2130_2200_stow_z3])
Lwx_profile_inflow_20241115_2130_2200_stow = pd.Series([Lwx_20241115_2130_2200_stow_z1,Lwx_20241115_2130_2200_stow_z2,Lwx_20241115_2130_2200_stow_z3])
 


#%% Mast 1

U_corr_mast1_20241115_2130_2200_stow_z1 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low)
U_corr_mast1_20241115_2130_2200_stow_z2 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid)
U_corr_mast1_20241115_2130_2200_stow_z3 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top)

V_corr_mast1_20241115_2130_2200_stow_z1 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_V_ax_Low)
V_corr_mast1_20241115_2130_2200_stow_z2 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_V_ax_Mid)
V_corr_mast1_20241115_2130_2200_stow_z3 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_V_ax_Top)

W_corr_mast1_20241115_2130_2200_stow_z1 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low)
W_corr_mast1_20241115_2130_2200_stow_z2 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid)
W_corr_mast1_20241115_2130_2200_stow_z3 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top)

mast1_uprimewprime_z1_20241115_2130_2200_stow = (U_corr_mast1_20241115_2130_2200_stow_z1*W_corr_mast1_20241115_2130_2200_stow_z1);
mast1_uprimewprime_z2_20241115_2130_2200_stow = (U_corr_mast1_20241115_2130_2200_stow_z2*W_corr_mast1_20241115_2130_2200_stow_z2);
mast1_uprimewprime_z3_20241115_2130_2200_stow = (U_corr_mast1_20241115_2130_2200_stow_z3*W_corr_mast1_20241115_2130_2200_stow_z3);


overlap = 0
nblock = len(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast1_20Hz_20241115_2130_2200_stow_z1, Pxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1 = fu_loads_mast1_20Hz_20241115_2130_2200_stow_z1*heights[0]/H2_U_ax_20241115_2130_2200_stow_z1
nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1 = (fu_loads_mast1_20Hz_20241115_2130_2200_stow_z1*Pxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1)/loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.std()**2

fu_loads_mast1_20Hz_20241115_2130_2200_stow_z2, Pxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2 = fu_loads_mast1_20Hz_20241115_2130_2200_stow_z2*heights[1]/H2_U_ax_20241115_2130_2200_stow_z2
nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2 = (fu_loads_mast1_20Hz_20241115_2130_2200_stow_z2*Pxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2)/loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.std()**2
 
fu_loads_mast1_20Hz_20241115_2130_2200_stow_z3, Pxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3 = fu_loads_mast1_20Hz_20241115_2130_2200_stow_z3*heights[2]/H2_U_ax_20241115_2130_2200_stow_z3
nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3 = (fu_loads_mast1_20Hz_20241115_2130_2200_stow_z3*Pxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3)/loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.std()**2              
    
fw_loads_mast1_20Hz_20241115_2130_2200_stow_z1, Pxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1 = fw_loads_mast1_20Hz_20241115_2130_2200_stow_z1*heights[0]/H2_W_ax_20241115_2130_2200_stow_z1
nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1 = (fw_loads_mast1_20Hz_20241115_2130_2200_stow_z1*Pxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1)/loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.std()**2

fw_loads_mast1_20Hz_20241115_2130_2200_stow_z2, Pxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2 = fw_loads_mast1_20Hz_20241115_2130_2200_stow_z2*heights[1]/H2_W_ax_20241115_2130_2200_stow_z2
nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2 = (fw_loads_mast1_20Hz_20241115_2130_2200_stow_z2*Pxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2)/loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.std()**2
 
fw_loads_mast1_20Hz_20241115_2130_2200_stow_z3, Pxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3 = fw_loads_mast1_20Hz_20241115_2130_2200_stow_z3*heights[2]/H2_W_ax_20241115_2130_2200_stow_z3
nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3 = (fw_loads_mast1_20Hz_20241115_2130_2200_stow_z3*Pxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3)/loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.std()**2              



#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1 = list(np.where([abs(nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1 = nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1[0][0]:len(nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1 = [nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2 = list(np.where([abs(nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2 = nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2[0][0]:len(nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2 = [nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3 = list(np.where([abs(nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3 = nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3[0][0]:len(nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3 = [nPxxfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1 = list(np.where([abs(nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1 = nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1[0][0]:len(nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1 = [nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2 = list(np.where([abs(nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2 = nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2[0][0]:len(nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2 = [nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3 = list(np.where([abs(nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3 = nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3[0][0]:len(nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3 = [nPxxfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241115_2130_2200_stow_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast1')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241115_2130_2200_stow_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast1')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()



#%% LS exponential fit method

autocorr_mast1_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2130_2200_stow_z1)
Lux_mast1_20241115_2130_2200_stow_z1 = Lux_20241115_2130_2200_stow_z1[Lux_20241115_2130_2200_stow_z1>0]

autocorr_mast1_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2130_2200_stow_z2)
Lux_mast1_20241115_2130_2200_stow_z2 = Lux_20241115_2130_2200_stow_z2[Lux_20241115_2130_2200_stow_z2>0]

autocorr_mast1_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m1_U_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2130_2200_stow_z3)
Lux_mast1_20241115_2130_2200_stow_z3 = Lux_20241115_2130_2200_stow_z3[Lux_20241115_2130_2200_stow_z3>0]

autocorr_mast1_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2130_2200_stow_z1)
Lwx_mast1_20241115_2130_2200_stow_z1 = Lwx_20241115_2130_2200_stow_z1[Lwx_20241115_2130_2200_stow_z1>0]

autocorr_mast1_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2130_2200_stow_z2)
Lwx_mast1_20241115_2130_2200_stow_z2 = Lwx_20241115_2130_2200_stow_z2[Lwx_20241115_2130_2200_stow_z2>0]

autocorr_mast1_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m1_W_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241115_2130_2200_stow_z3)
Lwx_mast1_20241115_2130_2200_stow_z3 = Lwx_20241115_2130_2200_stow_z3[Lwx_20241115_2130_2200_stow_z3>0]

Lux_profile_mast1_20241115_2130_2200_stow = pd.Series([Lux_mast1_20241115_2130_2200_stow_z1,Lux_mast1_20241115_2130_2200_stow_z2,Lux_mast1_20241115_2130_2200_stow_z3])
Lwx_profile_mast1_20241115_2130_2200_stow = pd.Series([Lwx_mast1_20241115_2130_2200_stow_z1,Lwx_mast1_20241115_2130_2200_stow_z2,Lwx_mast1_20241115_2130_2200_stow_z3])
 


#%% Mast 3

U_corr_mast3_20241115_2130_2200_stow_z1 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low)
U_corr_mast3_20241115_2130_2200_stow_z2 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid)
U_corr_mast3_20241115_2130_2200_stow_z3 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top)

V_corr_mast3_20241115_2130_2200_stow_z1 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_V_ax_Low)
V_corr_mast3_20241115_2130_2200_stow_z2 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_V_ax_Mid)
V_corr_mast3_20241115_2130_2200_stow_z3 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_V_ax_Top)

W_corr_mast3_20241115_2130_2200_stow_z1 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low)
W_corr_mast3_20241115_2130_2200_stow_z2 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid)
W_corr_mast3_20241115_2130_2200_stow_z3 = pd.Series(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top)

mast3_uprimewprime_z1_20241115_2130_2200_stow = (U_corr_mast3_20241115_2130_2200_stow_z1*W_corr_mast3_20241115_2130_2200_stow_z1);
mast3_uprimewprime_z2_20241115_2130_2200_stow = (U_corr_mast3_20241115_2130_2200_stow_z2*W_corr_mast3_20241115_2130_2200_stow_z2);
mast3_uprimewprime_z3_20241115_2130_2200_stow = (U_corr_mast3_20241115_2130_2200_stow_z3*W_corr_mast3_20241115_2130_2200_stow_z3);


overlap = 0
nblock = len(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast3_20Hz_20241115_2130_2200_stow_z1, Pxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1 = fu_loads_mast3_20Hz_20241115_2130_2200_stow_z1*heights[0]/H3_U_ax_20241115_2130_2200_stow_z1
nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1 = (fu_loads_mast3_20Hz_20241115_2130_2200_stow_z1*Pxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1)/loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.std()**2

fu_loads_mast3_20Hz_20241115_2130_2200_stow_z2, Pxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2 = fu_loads_mast3_20Hz_20241115_2130_2200_stow_z2*heights[1]/H3_U_ax_20241115_2130_2200_stow_z2
nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2 = (fu_loads_mast3_20Hz_20241115_2130_2200_stow_z2*Pxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2)/loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.std()**2
 
fu_loads_mast3_20Hz_20241115_2130_2200_stow_z3, Pxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3 = fu_loads_mast3_20Hz_20241115_2130_2200_stow_z3*heights[2]/H3_U_ax_20241115_2130_2200_stow_z3
nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3 = (fu_loads_mast3_20Hz_20241115_2130_2200_stow_z3*Pxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3)/loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.std()**2              
    
fw_loads_mast3_20Hz_20241115_2130_2200_stow_z1, Pxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1 = fw_loads_mast3_20Hz_20241115_2130_2200_stow_z1*heights[0]/H3_W_ax_20241115_2130_2200_stow_z1
nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1 = (fw_loads_mast3_20Hz_20241115_2130_2200_stow_z1*Pxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1)/loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.std()**2

fw_loads_mast3_20Hz_20241115_2130_2200_stow_z2, Pxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2 = fw_loads_mast3_20Hz_20241115_2130_2200_stow_z2*heights[1]/H3_W_ax_20241115_2130_2200_stow_z2
nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2 = (fw_loads_mast3_20Hz_20241115_2130_2200_stow_z2*Pxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2)/loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.std()**2
 
fw_loads_mast3_20Hz_20241115_2130_2200_stow_z3, Pxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3 = welch(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3 = fw_loads_mast3_20Hz_20241115_2130_2200_stow_z3*heights[2]/H3_W_ax_20241115_2130_2200_stow_z3
nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3 = (fw_loads_mast3_20Hz_20241115_2130_2200_stow_z3*Pxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3)/loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1 = list(np.where([abs(nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1 = nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1[0][0]:len(nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1 = [nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2 = list(np.where([abs(nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2 = nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2[0][0]:len(nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2 = [nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3 = list(np.where([abs(nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3 = nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3[0][0]:len(nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3 = [nPxxfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1 = list(np.where([abs(nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1 = nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1[0][0]:len(nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1 = [nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z1]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2 = list(np.where([abs(nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2 = nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2[0][0]:len(nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2 = [nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z2]

index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3 = list(np.where([abs(nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3 = nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3[index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3[0][0]:len(nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3 = [nPxxfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3[0:index_highfreq_loads_mast_20Hz_20241115_2130_2200_stow_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241115_2130_2200_stow_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241115_2130_2200_stow_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast3')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241115_2130_2200_stow_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241115_2130_2200_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast3')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()





#%% LS exponential fit method

autocorr_mast3_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2130_2200_stow_z1)
Lux_mast3_20241115_2130_2200_stow_z1 = Lux_20241115_2130_2200_stow_z1[Lux_20241115_2130_2200_stow_z1>0]

autocorr_mast3_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2130_2200_stow_z2)
Lux_mast3_20241115_2130_2200_stow_z2 = Lux_20241115_2130_2200_stow_z2[Lux_20241115_2130_2200_stow_z2>0]

autocorr_mast3_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m3_U_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241115_2130_2200_stow)
Lux_20241115_2130_2200_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2130_2200_stow_z3)
Lux_mast3_20241115_2130_2200_stow_z3 = Lux_20241115_2130_2200_stow_z3[Lux_20241115_2130_2200_stow_z3>0]

autocorr_mast3_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2130_2200_stow_z1)
Lwx_mast3_20241115_2130_2200_stow_z1 = Lwx_20241115_2130_2200_stow_z1[Lwx_20241115_2130_2200_stow_z1>0]

autocorr_mast3_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2130_2200_stow_z2)
Lwx_mast3_20241115_2130_2200_stow_z2 = Lwx_20241115_2130_2200_stow_z2[Lwx_20241115_2130_2200_stow_z2>0]

autocorr_mast3_20241115_2130_2200_stow = np.correlate(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241115_2130_2200_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241115_2130_2200_stow.m3_W_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241115_2130_2200_stow)
Lwx_20241115_2130_2200_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241115_2130_2200_stow_z3)
Lwx_mast3_20241115_2130_2200_stow_z3 = Lwx_20241115_2130_2200_stow_z3[Lwx_20241115_2130_2200_stow_z3>0]

Lux_profile_mast3_20241115_2130_2200_stow = pd.Series([Lux_mast3_20241115_2130_2200_stow_z1,Lux_mast3_20241115_2130_2200_stow_z2,Lux_mast3_20241115_2130_2200_stow_z3])
Lwx_profile_mast3_20241115_2130_2200_stow = pd.Series([Lwx_mast3_20241115_2130_2200_stow_z1,Lwx_mast3_20241115_2130_2200_stow_z2,Lwx_mast3_20241115_2130_2200_stow_z3])
 

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241115_2130_2200_stow, heights, label='Lux')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_u^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10000)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241115_2130_2200_stow, heights, label='Lwx')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_w^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wspd_20241115_2130_2200_stow_z1,H1_wspd_20241115_2130_2200_stow_z2,H1_wspd_20241115_2130_2200_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wspd_20241115_2130_2200_stow_z1,H2_wspd_20241115_2130_2200_stow_z2,H2_wspd_20241115_2130_2200_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wspd_20241115_2130_2200_stow_z1,H3_wspd_20241115_2130_2200_stow_z2,H3_wspd_20241115_2130_2200_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind speed (m/s)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,15)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wdir_20241115_2130_2200_stow_z1,H1_wdir_20241115_2130_2200_stow_z2,H1_wdir_20241115_2130_2200_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wdir_20241115_2130_2200_stow_z1,H2_wdir_20241115_2130_2200_stow_z2,H2_wdir_20241115_2130_2200_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wdir_20241115_2130_2200_stow_z1,H3_wdir_20241115_2130_2200_stow_z2,H3_wdir_20241115_2130_2200_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind direction (deg)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(300,360)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iu_20241115_2130_2200_stow_z1,H1_Iu_20241115_2130_2200_stow_z2,H1_Iu_20241115_2130_2200_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iu_20241115_2130_2200_stow_z1,H2_Iu_20241115_2130_2200_stow_z2,H2_Iu_20241115_2130_2200_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iu_20241115_2130_2200_stow_z1,H3_Iu_20241115_2130_2200_stow_z2,H3_Iu_20241115_2130_2200_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_u$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iw_20241115_2130_2200_stow_z1,H1_Iw_20241115_2130_2200_stow_z2,H1_Iw_20241115_2130_2200_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iw_20241115_2130_2200_stow_z1,H2_Iw_20241115_2130_2200_stow_z2,H2_Iw_20241115_2130_2200_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iw_20241115_2130_2200_stow_z1,H3_Iw_20241115_2130_2200_stow_z2,H3_Iw_20241115_2130_2200_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_w$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.2)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241115_2130_2200_stow/11.23, heights, s=8,label='inflow')            
plt.scatter(Lux_profile_mast1_20241115_2130_2200_stow/11.23, heights, s=8,label='mast1')            
plt.scatter(Lux_profile_mast3_20241115_2130_2200_stow/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_u^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,150)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241115_2130_2200_stow/11.23, heights, s=8,label='inflow')            
plt.scatter(Lwx_profile_mast1_20241115_2130_2200_stow/11.23, heights, s=8,label='mast1')            
plt.scatter(Lwx_profile_mast3_20241115_2130_2200_stow/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_w^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()




#%% Quadrant analysis (inflow Nov 15, 2024)


Q1_inflow_20241115_2045_2115_operation_z1 = Q2_inflow_20241115_2045_2115_operation_z1 = Q3_inflow_20241115_2045_2115_operation_z1 = Q4_inflow_20241115_2045_2115_operation_z1 = 0
ejections_inflow_20241115_2045_2115_operation_z1 = outward_interactions_inflow_20241115_2045_2115_operation_z1 = sweeps_inflow_20241115_2045_2115_operation_z1 = inward_interactions_inflow_20241115_2045_2115_operation_z1 = 0

for i in range(0,len(W_corr_inflow_20241115_2045_2115_operation_z1)):
    if (U_corr_inflow_20241115_2045_2115_operation_z1[i]>0)&(W_corr_inflow_20241115_2045_2115_operation_z1[i]>0):
        Q1_inflow_20241115_2045_2115_operation_z1 += 1
        if (inflow_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            ejections_inflow_20241115_2045_2115_operation_z1 += 1
        elif (inflow_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            outward_interactions_inflow_20241115_2045_2115_operation_z1 += 1            
    elif (U_corr_inflow_20241115_2045_2115_operation_z1[i]>0)&(W_corr_inflow_20241115_2045_2115_operation_z1[i]<0):
        Q2_inflow_20241115_2045_2115_operation_z1 += 1
        if (inflow_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            sweeps_inflow_20241115_2045_2115_operation_z1 += 1
        elif (inflow_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            inward_interactions_inflow_20241115_2045_2115_operation_z1 += 1 
    elif (U_corr_inflow_20241115_2045_2115_operation_z1[i]<0)&(W_corr_inflow_20241115_2045_2115_operation_z1[i]<0):
        Q3_inflow_20241115_2045_2115_operation_z1 += 1
        if (inflow_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            sweeps_inflow_20241115_2045_2115_operation_z1 += 1
        elif (inflow_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            inward_interactions_inflow_20241115_2045_2115_operation_z1 += 1 
    elif (U_corr_inflow_20241115_2045_2115_operation_z1[i]<0)&(W_corr_inflow_20241115_2045_2115_operation_z1[i]>0):
        Q2_inflow_20241115_2045_2115_operation_z1 += 1
        if (inflow_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            ejections_inflow_20241115_2045_2115_operation_z1 += 1
        elif (inflow_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            outward_interactions_inflow_20241115_2045_2115_operation_z1 += 1 


S1_inflow_20241115_2045_2115_operation_z1 = 100*Q1_inflow_20241115_2045_2115_operation_z1/(Q1_inflow_20241115_2045_2115_operation_z1+Q2_inflow_20241115_2045_2115_operation_z1+Q3_inflow_20241115_2045_2115_operation_z1+Q4_inflow_20241115_2045_2115_operation_z1)
S2_inflow_20241115_2045_2115_operation_z1 = 100*Q2_inflow_20241115_2045_2115_operation_z1/(Q1_inflow_20241115_2045_2115_operation_z1+Q2_inflow_20241115_2045_2115_operation_z1+Q3_inflow_20241115_2045_2115_operation_z1+Q4_inflow_20241115_2045_2115_operation_z1)
S3_inflow_20241115_2045_2115_operation_z1 = 100*Q3_inflow_20241115_2045_2115_operation_z1/(Q1_inflow_20241115_2045_2115_operation_z1+Q2_inflow_20241115_2045_2115_operation_z1+Q3_inflow_20241115_2045_2115_operation_z1+Q4_inflow_20241115_2045_2115_operation_z1)
S4_inflow_20241115_2045_2115_operation_z1 = 100*Q4_inflow_20241115_2045_2115_operation_z1/(Q1_inflow_20241115_2045_2115_operation_z1+Q2_inflow_20241115_2045_2115_operation_z1+Q3_inflow_20241115_2045_2115_operation_z1+Q4_inflow_20241115_2045_2115_operation_z1)

S_ejections_inflow_20241115_2045_2115_operation_z1 = 100*ejections_inflow_20241115_2045_2115_operation_z1/(Q1_inflow_20241115_2045_2115_operation_z1+Q2_inflow_20241115_2045_2115_operation_z1+Q3_inflow_20241115_2045_2115_operation_z1+Q4_inflow_20241115_2045_2115_operation_z1)
S_outward_interactions_inflow_20241115_2045_2115_operation_z1 = 100*outward_interactions_inflow_20241115_2045_2115_operation_z1/(Q1_inflow_20241115_2045_2115_operation_z1+Q2_inflow_20241115_2045_2115_operation_z1+Q3_inflow_20241115_2045_2115_operation_z1+Q4_inflow_20241115_2045_2115_operation_z1)
S_sweeps_inflow_20241115_2045_2115_operation_z1 = 100*sweeps_inflow_20241115_2045_2115_operation_z1/(Q1_inflow_20241115_2045_2115_operation_z1+Q2_inflow_20241115_2045_2115_operation_z1+Q3_inflow_20241115_2045_2115_operation_z1+Q4_inflow_20241115_2045_2115_operation_z1)
S_inward_interactions_inflow_20241115_2045_2115_operation_z1 = 100*inward_interactions_inflow_20241115_2045_2115_operation_z1/(Q1_inflow_20241115_2045_2115_operation_z1+Q2_inflow_20241115_2045_2115_operation_z1+Q3_inflow_20241115_2045_2115_operation_z1+Q4_inflow_20241115_2045_2115_operation_z1)


Q1_inflow_20241115_2045_2115_operation_z2 = Q2_inflow_20241115_2045_2115_operation_z2 = Q3_inflow_20241115_2045_2115_operation_z2 = Q4_inflow_20241115_2045_2115_operation_z2 = 0
ejections_inflow_20241115_2045_2115_operation_z2 = outward_interactions_inflow_20241115_2045_2115_operation_z2 = sweeps_inflow_20241115_2045_2115_operation_z2 = inward_interactions_inflow_20241115_2045_2115_operation_z2 = 0

for i in range(0,len(W_corr_inflow_20241115_2045_2115_operation_z2)):
    if (U_corr_inflow_20241115_2045_2115_operation_z2[i]>0)&(W_corr_inflow_20241115_2045_2115_operation_z2[i]>0):
        Q1_inflow_20241115_2045_2115_operation_z2 += 1
        if (inflow_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            ejections_inflow_20241115_2045_2115_operation_z2 += 1
        elif (inflow_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            outward_interactions_inflow_20241115_2045_2115_operation_z2 += 1            
    elif (U_corr_inflow_20241115_2045_2115_operation_z2[i]<0)&(W_corr_inflow_20241115_2045_2115_operation_z2[i]>0):
        Q2_inflow_20241115_2045_2115_operation_z2 += 1
        if (inflow_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            ejections_inflow_20241115_2045_2115_operation_z2 += 1
        elif (inflow_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            outward_interactions_inflow_20241115_2045_2115_operation_z2 += 1 
    elif (U_corr_inflow_20241115_2045_2115_operation_z2[i]<0)&(W_corr_inflow_20241115_2045_2115_operation_z2[i]<0):
        Q3_inflow_20241115_2045_2115_operation_z2 += 1
        if (inflow_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            sweeps_inflow_20241115_2045_2115_operation_z2 += 1
        elif (inflow_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            inward_interactions_inflow_20241115_2045_2115_operation_z2 += 1 
    elif (U_corr_inflow_20241115_2045_2115_operation_z2[i]>0)&(W_corr_inflow_20241115_2045_2115_operation_z2[i]<0):
        Q4_inflow_20241115_2045_2115_operation_z2 += 1
        if (inflow_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            sweeps_inflow_20241115_2045_2115_operation_z2 += 1
        elif (inflow_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            inward_interactions_inflow_20241115_2045_2115_operation_z2 += 1 

S1_inflow_20241115_2045_2115_operation_z2 = 100*Q1_inflow_20241115_2045_2115_operation_z2/(Q1_inflow_20241115_2045_2115_operation_z2+Q2_inflow_20241115_2045_2115_operation_z2+Q3_inflow_20241115_2045_2115_operation_z2+Q4_inflow_20241115_2045_2115_operation_z2)
S2_inflow_20241115_2045_2115_operation_z2 = 100*Q2_inflow_20241115_2045_2115_operation_z2/(Q1_inflow_20241115_2045_2115_operation_z2+Q2_inflow_20241115_2045_2115_operation_z2+Q3_inflow_20241115_2045_2115_operation_z2+Q4_inflow_20241115_2045_2115_operation_z2)
S3_inflow_20241115_2045_2115_operation_z2 = 100*Q3_inflow_20241115_2045_2115_operation_z2/(Q1_inflow_20241115_2045_2115_operation_z2+Q2_inflow_20241115_2045_2115_operation_z2+Q3_inflow_20241115_2045_2115_operation_z2+Q4_inflow_20241115_2045_2115_operation_z2)
S4_inflow_20241115_2045_2115_operation_z2 = 100*Q4_inflow_20241115_2045_2115_operation_z2/(Q1_inflow_20241115_2045_2115_operation_z2+Q2_inflow_20241115_2045_2115_operation_z2+Q3_inflow_20241115_2045_2115_operation_z2+Q4_inflow_20241115_2045_2115_operation_z2)

S_ejections_inflow_20241115_2045_2115_operation_z2 = 100*ejections_inflow_20241115_2045_2115_operation_z2/(Q1_inflow_20241115_2045_2115_operation_z2+Q2_inflow_20241115_2045_2115_operation_z2+Q3_inflow_20241115_2045_2115_operation_z2+Q4_inflow_20241115_2045_2115_operation_z2)
S_outward_interactions_inflow_20241115_2045_2115_operation_z2 = 100*outward_interactions_inflow_20241115_2045_2115_operation_z2/(Q1_inflow_20241115_2045_2115_operation_z2+Q2_inflow_20241115_2045_2115_operation_z2+Q3_inflow_20241115_2045_2115_operation_z2+Q4_inflow_20241115_2045_2115_operation_z2)
S_sweeps_inflow_20241115_2045_2115_operation_z2 = 100*sweeps_inflow_20241115_2045_2115_operation_z2/(Q1_inflow_20241115_2045_2115_operation_z2+Q2_inflow_20241115_2045_2115_operation_z2+Q3_inflow_20241115_2045_2115_operation_z2+Q4_inflow_20241115_2045_2115_operation_z2)
S_inward_interactions_inflow_20241115_2045_2115_operation_z2 = 100*inward_interactions_inflow_20241115_2045_2115_operation_z2/(Q1_inflow_20241115_2045_2115_operation_z2+Q2_inflow_20241115_2045_2115_operation_z2+Q3_inflow_20241115_2045_2115_operation_z2+Q4_inflow_20241115_2045_2115_operation_z2)


Q1_inflow_20241115_2045_2115_operation_z3 = Q2_inflow_20241115_2045_2115_operation_z3 = Q3_inflow_20241115_2045_2115_operation_z3 = Q4_inflow_20241115_2045_2115_operation_z3 = 0
ejections_inflow_20241115_2045_2115_operation_z3 = outward_interactions_inflow_20241115_2045_2115_operation_z3 = sweeps_inflow_20241115_2045_2115_operation_z3 = inward_interactions_inflow_20241115_2045_2115_operation_z3 = 0

for i in range(0,len(W_corr_inflow_20241115_2045_2115_operation_z3)):
    if (U_corr_inflow_20241115_2045_2115_operation_z3[i]>0)&(W_corr_inflow_20241115_2045_2115_operation_z3[i]>0):
        Q1_inflow_20241115_2045_2115_operation_z3 += 1
        if (inflow_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            ejections_inflow_20241115_2045_2115_operation_z3 += 1
        elif (inflow_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            outward_interactions_inflow_20241115_2045_2115_operation_z3 += 1            
    elif (U_corr_inflow_20241115_2045_2115_operation_z3[i]<0)&(W_corr_inflow_20241115_2045_2115_operation_z3[i]>0):
        Q2_inflow_20241115_2045_2115_operation_z3 += 1
        if (inflow_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            ejections_inflow_20241115_2045_2115_operation_z3 += 1
        elif (inflow_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            outward_interactions_inflow_20241115_2045_2115_operation_z3 += 1 
    elif (U_corr_inflow_20241115_2045_2115_operation_z3[i]<0)&(W_corr_inflow_20241115_2045_2115_operation_z3[i]<0):
        Q3_inflow_20241115_2045_2115_operation_z3 += 1
        if (inflow_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            sweeps_inflow_20241115_2045_2115_operation_z3 += 1
        elif (inflow_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            inward_interactions_inflow_20241115_2045_2115_operation_z3 += 1 
    elif (U_corr_inflow_20241115_2045_2115_operation_z3[i]>0)&(W_corr_inflow_20241115_2045_2115_operation_z3[i]<0):
        Q4_inflow_20241115_2045_2115_operation_z3 += 1
        if (inflow_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            sweeps_inflow_20241115_2045_2115_operation_z3 += 1
        elif (inflow_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            inward_interactions_inflow_20241115_2045_2115_operation_z3 += 1 

S1_inflow_20241115_2045_2115_operation_z3 = 100*Q1_inflow_20241115_2045_2115_operation_z3/(Q1_inflow_20241115_2045_2115_operation_z3+Q2_inflow_20241115_2045_2115_operation_z3+Q3_inflow_20241115_2045_2115_operation_z3+Q4_inflow_20241115_2045_2115_operation_z3)
S2_inflow_20241115_2045_2115_operation_z3 = 100*Q2_inflow_20241115_2045_2115_operation_z3/(Q1_inflow_20241115_2045_2115_operation_z3+Q2_inflow_20241115_2045_2115_operation_z3+Q3_inflow_20241115_2045_2115_operation_z3+Q4_inflow_20241115_2045_2115_operation_z3)
S3_inflow_20241115_2045_2115_operation_z3 = 100*Q3_inflow_20241115_2045_2115_operation_z3/(Q1_inflow_20241115_2045_2115_operation_z3+Q2_inflow_20241115_2045_2115_operation_z3+Q3_inflow_20241115_2045_2115_operation_z3+Q4_inflow_20241115_2045_2115_operation_z3)
S4_inflow_20241115_2045_2115_operation_z3 = 100*Q4_inflow_20241115_2045_2115_operation_z3/(Q1_inflow_20241115_2045_2115_operation_z3+Q2_inflow_20241115_2045_2115_operation_z3+Q3_inflow_20241115_2045_2115_operation_z3+Q4_inflow_20241115_2045_2115_operation_z3)

S_ejections_inflow_20241115_2045_2115_operation_z3 = 100*ejections_inflow_20241115_2045_2115_operation_z3/(Q1_inflow_20241115_2045_2115_operation_z3+Q2_inflow_20241115_2045_2115_operation_z3+Q3_inflow_20241115_2045_2115_operation_z3+Q4_inflow_20241115_2045_2115_operation_z3)
S_outward_interactions_inflow_20241115_2045_2115_operation_z3 = 100*outward_interactions_inflow_20241115_2045_2115_operation_z3/(Q1_inflow_20241115_2045_2115_operation_z3+Q2_inflow_20241115_2045_2115_operation_z3+Q3_inflow_20241115_2045_2115_operation_z3+Q4_inflow_20241115_2045_2115_operation_z3)
S_sweeps_inflow_20241115_2045_2115_operation_z3 = 100*sweeps_inflow_20241115_2045_2115_operation_z3/(Q1_inflow_20241115_2045_2115_operation_z3+Q2_inflow_20241115_2045_2115_operation_z3+Q3_inflow_20241115_2045_2115_operation_z3+Q4_inflow_20241115_2045_2115_operation_z3)
S_inward_interactions_inflow_20241115_2045_2115_operation_z3 = 100*inward_interactions_inflow_20241115_2045_2115_operation_z3/(Q1_inflow_20241115_2045_2115_operation_z3+Q2_inflow_20241115_2045_2115_operation_z3+Q3_inflow_20241115_2045_2115_operation_z3+Q4_inflow_20241115_2045_2115_operation_z3)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S1_inflow_20241115_2045_2115_operation_z1,S1_inflow_20241115_2045_2115_operation_z2,S1_inflow_20241115_2045_2115_operation_z3],heights,marker='o',s=20, label='u+w+ (Q1)')    
plt.scatter([S2_inflow_20241115_2045_2115_operation_z1,S2_inflow_20241115_2045_2115_operation_z2,S2_inflow_20241115_2045_2115_operation_z3],heights,marker='s',s=20, label='u-w+ (Q2)')    
plt.scatter([S3_inflow_20241115_2045_2115_operation_z1,S3_inflow_20241115_2045_2115_operation_z2,S3_inflow_20241115_2045_2115_operation_z3],heights,marker='d',s=20, label='u-w- (Q3)')    
plt.scatter([S4_inflow_20241115_2045_2115_operation_z1,S4_inflow_20241115_2045_2115_operation_z2,S4_inflow_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='u+w- (Q4)')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 55)
plt.xticks([0,10,20,30,40,50])  
plt.ylim(0, 12)
plt.title('Operation inflow (Nov 15, 2024)')    
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S_ejections_inflow_20241115_2045_2115_operation_z1,S_ejections_inflow_20241115_2045_2115_operation_z2,S_ejections_inflow_20241115_2045_2115_operation_z3],heights,marker='o',s=20, label='ejections')    
plt.scatter([S_outward_interactions_inflow_20241115_2045_2115_operation_z1,S_outward_interactions_inflow_20241115_2045_2115_operation_z2,S_outward_interactions_inflow_20241115_2045_2115_operation_z3],heights,marker='s',s=20, label='outward interactions')    
plt.scatter([S_sweeps_inflow_20241115_2045_2115_operation_z1,S_sweeps_inflow_20241115_2045_2115_operation_z2,S_sweeps_inflow_20241115_2045_2115_operation_z3],heights,marker='d',s=20, label='sweeps')    
plt.scatter([S_inward_interactions_inflow_20241115_2045_2115_operation_z1,S_inward_interactions_inflow_20241115_2045_2115_operation_z2,S_inward_interactions_inflow_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='inward interactions')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 100)
plt.ylim(0, 12)
plt.title('Operation inflow (Nov 15, 2024)')     
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


#%% Quadrant analysis (mast1 Nov 15, 2024)

Q1_mast1_20241115_2045_2115_operation_z1 = Q2_mast1_20241115_2045_2115_operation_z1 = Q3_mast1_20241115_2045_2115_operation_z1 = Q4_mast1_20241115_2045_2115_operation_z1 = 0
ejections_mast1_20241115_2045_2115_operation_z1 = outward_interactions_mast1_20241115_2045_2115_operation_z1 = sweeps_mast1_20241115_2045_2115_operation_z1 = inward_interactions_mast1_20241115_2045_2115_operation_z1 = 0

for i in range(0,len(W_corr_mast1_20241115_2045_2115_operation_z1)):
    if (U_corr_mast1_20241115_2045_2115_operation_z1[i]>0)&(W_corr_mast1_20241115_2045_2115_operation_z1[i]>0):
        Q1_mast1_20241115_2045_2115_operation_z1 += 1
        if (mast1_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            ejections_mast1_20241115_2045_2115_operation_z1 += 1
        elif (mast1_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            outward_interactions_mast1_20241115_2045_2115_operation_z1 += 1            
    elif (U_corr_mast1_20241115_2045_2115_operation_z1[i]>0)&(W_corr_mast1_20241115_2045_2115_operation_z1[i]<0):
        Q2_mast1_20241115_2045_2115_operation_z1 += 1
        if (mast1_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            sweeps_mast1_20241115_2045_2115_operation_z1 += 1
        elif (mast1_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            inward_interactions_mast1_20241115_2045_2115_operation_z1 += 1 
    elif (U_corr_mast1_20241115_2045_2115_operation_z1[i]<0)&(W_corr_mast1_20241115_2045_2115_operation_z1[i]<0):
        Q3_mast1_20241115_2045_2115_operation_z1 += 1
        if (mast1_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            sweeps_mast1_20241115_2045_2115_operation_z1 += 1
        elif (mast1_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            inward_interactions_mast1_20241115_2045_2115_operation_z1 += 1 
    elif (U_corr_mast1_20241115_2045_2115_operation_z1[i]<0)&(W_corr_mast1_20241115_2045_2115_operation_z1[i]>0):
        Q2_mast1_20241115_2045_2115_operation_z1 += 1
        if (mast1_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            ejections_mast1_20241115_2045_2115_operation_z1 += 1
        elif (mast1_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            outward_interactions_mast1_20241115_2045_2115_operation_z1 += 1 


S1_mast1_20241115_2045_2115_operation_z1 = 100*Q1_mast1_20241115_2045_2115_operation_z1/(Q1_mast1_20241115_2045_2115_operation_z1+Q2_mast1_20241115_2045_2115_operation_z1+Q3_mast1_20241115_2045_2115_operation_z1+Q4_mast1_20241115_2045_2115_operation_z1)
S2_mast1_20241115_2045_2115_operation_z1 = 100*Q2_mast1_20241115_2045_2115_operation_z1/(Q1_mast1_20241115_2045_2115_operation_z1+Q2_mast1_20241115_2045_2115_operation_z1+Q3_mast1_20241115_2045_2115_operation_z1+Q4_mast1_20241115_2045_2115_operation_z1)
S3_mast1_20241115_2045_2115_operation_z1 = 100*Q3_mast1_20241115_2045_2115_operation_z1/(Q1_mast1_20241115_2045_2115_operation_z1+Q2_mast1_20241115_2045_2115_operation_z1+Q3_mast1_20241115_2045_2115_operation_z1+Q4_mast1_20241115_2045_2115_operation_z1)
S4_mast1_20241115_2045_2115_operation_z1 = 100*Q4_mast1_20241115_2045_2115_operation_z1/(Q1_mast1_20241115_2045_2115_operation_z1+Q2_mast1_20241115_2045_2115_operation_z1+Q3_mast1_20241115_2045_2115_operation_z1+Q4_mast1_20241115_2045_2115_operation_z1)

S_ejections_mast1_20241115_2045_2115_operation_z1 = 100*ejections_mast1_20241115_2045_2115_operation_z1/(Q1_mast1_20241115_2045_2115_operation_z1+Q2_mast1_20241115_2045_2115_operation_z1+Q3_mast1_20241115_2045_2115_operation_z1+Q4_mast1_20241115_2045_2115_operation_z1)
S_outward_interactions_mast1_20241115_2045_2115_operation_z1 = 100*outward_interactions_mast1_20241115_2045_2115_operation_z1/(Q1_mast1_20241115_2045_2115_operation_z1+Q2_mast1_20241115_2045_2115_operation_z1+Q3_mast1_20241115_2045_2115_operation_z1+Q4_mast1_20241115_2045_2115_operation_z1)
S_sweeps_mast1_20241115_2045_2115_operation_z1 = 100*sweeps_mast1_20241115_2045_2115_operation_z1/(Q1_mast1_20241115_2045_2115_operation_z1+Q2_mast1_20241115_2045_2115_operation_z1+Q3_mast1_20241115_2045_2115_operation_z1+Q4_mast1_20241115_2045_2115_operation_z1)
S_inward_interactions_mast1_20241115_2045_2115_operation_z1 = 100*inward_interactions_mast1_20241115_2045_2115_operation_z1/(Q1_mast1_20241115_2045_2115_operation_z1+Q2_mast1_20241115_2045_2115_operation_z1+Q3_mast1_20241115_2045_2115_operation_z1+Q4_mast1_20241115_2045_2115_operation_z1)


Q1_mast1_20241115_2045_2115_operation_z2 = Q2_mast1_20241115_2045_2115_operation_z2 = Q3_mast1_20241115_2045_2115_operation_z2 = Q4_mast1_20241115_2045_2115_operation_z2 = 0
ejections_mast1_20241115_2045_2115_operation_z2 = outward_interactions_mast1_20241115_2045_2115_operation_z2 = sweeps_mast1_20241115_2045_2115_operation_z2 = inward_interactions_mast1_20241115_2045_2115_operation_z2 = 0

for i in range(0,len(W_corr_mast1_20241115_2045_2115_operation_z2)):
    if (U_corr_mast1_20241115_2045_2115_operation_z2[i]>0)&(W_corr_mast1_20241115_2045_2115_operation_z2[i]>0):
        Q1_mast1_20241115_2045_2115_operation_z2 += 1
        if (mast1_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            ejections_mast1_20241115_2045_2115_operation_z2 += 1
        elif (mast1_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            outward_interactions_mast1_20241115_2045_2115_operation_z2 += 1            
    elif (U_corr_mast1_20241115_2045_2115_operation_z2[i]<0)&(W_corr_mast1_20241115_2045_2115_operation_z2[i]>0):
        Q2_mast1_20241115_2045_2115_operation_z2 += 1
        if (mast1_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            ejections_mast1_20241115_2045_2115_operation_z2 += 1
        elif (mast1_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            outward_interactions_mast1_20241115_2045_2115_operation_z2 += 1 
    elif (U_corr_mast1_20241115_2045_2115_operation_z2[i]<0)&(W_corr_mast1_20241115_2045_2115_operation_z2[i]<0):
        Q3_mast1_20241115_2045_2115_operation_z2 += 1
        if (mast1_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            sweeps_mast1_20241115_2045_2115_operation_z2 += 1
        elif (mast1_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            inward_interactions_mast1_20241115_2045_2115_operation_z2 += 1 
    elif (U_corr_mast1_20241115_2045_2115_operation_z2[i]>0)&(W_corr_mast1_20241115_2045_2115_operation_z2[i]<0):
        Q4_mast1_20241115_2045_2115_operation_z2 += 1
        if (mast1_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            sweeps_mast1_20241115_2045_2115_operation_z2 += 1
        elif (mast1_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            inward_interactions_mast1_20241115_2045_2115_operation_z2 += 1 

S1_mast1_20241115_2045_2115_operation_z2 = 100*Q1_mast1_20241115_2045_2115_operation_z2/(Q1_mast1_20241115_2045_2115_operation_z2+Q2_mast1_20241115_2045_2115_operation_z2+Q3_mast1_20241115_2045_2115_operation_z2+Q4_mast1_20241115_2045_2115_operation_z2)
S2_mast1_20241115_2045_2115_operation_z2 = 100*Q2_mast1_20241115_2045_2115_operation_z2/(Q1_mast1_20241115_2045_2115_operation_z2+Q2_mast1_20241115_2045_2115_operation_z2+Q3_mast1_20241115_2045_2115_operation_z2+Q4_mast1_20241115_2045_2115_operation_z2)
S3_mast1_20241115_2045_2115_operation_z2 = 100*Q3_mast1_20241115_2045_2115_operation_z2/(Q1_mast1_20241115_2045_2115_operation_z2+Q2_mast1_20241115_2045_2115_operation_z2+Q3_mast1_20241115_2045_2115_operation_z2+Q4_mast1_20241115_2045_2115_operation_z2)
S4_mast1_20241115_2045_2115_operation_z2 = 100*Q4_mast1_20241115_2045_2115_operation_z2/(Q1_mast1_20241115_2045_2115_operation_z2+Q2_mast1_20241115_2045_2115_operation_z2+Q3_mast1_20241115_2045_2115_operation_z2+Q4_mast1_20241115_2045_2115_operation_z2)

S_ejections_mast1_20241115_2045_2115_operation_z2 = 100*ejections_mast1_20241115_2045_2115_operation_z2/(Q1_mast1_20241115_2045_2115_operation_z2+Q2_mast1_20241115_2045_2115_operation_z2+Q3_mast1_20241115_2045_2115_operation_z2+Q4_mast1_20241115_2045_2115_operation_z2)
S_outward_interactions_mast1_20241115_2045_2115_operation_z2 = 100*outward_interactions_mast1_20241115_2045_2115_operation_z2/(Q1_mast1_20241115_2045_2115_operation_z2+Q2_mast1_20241115_2045_2115_operation_z2+Q3_mast1_20241115_2045_2115_operation_z2+Q4_mast1_20241115_2045_2115_operation_z2)
S_sweeps_mast1_20241115_2045_2115_operation_z2 = 100*sweeps_mast1_20241115_2045_2115_operation_z2/(Q1_mast1_20241115_2045_2115_operation_z2+Q2_mast1_20241115_2045_2115_operation_z2+Q3_mast1_20241115_2045_2115_operation_z2+Q4_mast1_20241115_2045_2115_operation_z2)
S_inward_interactions_mast1_20241115_2045_2115_operation_z2 = 100*inward_interactions_mast1_20241115_2045_2115_operation_z2/(Q1_mast1_20241115_2045_2115_operation_z2+Q2_mast1_20241115_2045_2115_operation_z2+Q3_mast1_20241115_2045_2115_operation_z2+Q4_mast1_20241115_2045_2115_operation_z2)


Q1_mast1_20241115_2045_2115_operation_z3 = Q2_mast1_20241115_2045_2115_operation_z3 = Q3_mast1_20241115_2045_2115_operation_z3 = Q4_mast1_20241115_2045_2115_operation_z3 = 0
ejections_mast1_20241115_2045_2115_operation_z3 = outward_interactions_mast1_20241115_2045_2115_operation_z3 = sweeps_mast1_20241115_2045_2115_operation_z3 = inward_interactions_mast1_20241115_2045_2115_operation_z3 = 0

for i in range(0,len(W_corr_mast1_20241115_2045_2115_operation_z3)):
    if (U_corr_mast1_20241115_2045_2115_operation_z3[i]>0)&(W_corr_mast1_20241115_2045_2115_operation_z3[i]>0):
        Q1_mast1_20241115_2045_2115_operation_z3 += 1
        if (mast1_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            ejections_mast1_20241115_2045_2115_operation_z3 += 1
        elif (mast1_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            outward_interactions_mast1_20241115_2045_2115_operation_z3 += 1            
    elif (U_corr_mast1_20241115_2045_2115_operation_z3[i]<0)&(W_corr_mast1_20241115_2045_2115_operation_z3[i]>0):
        Q2_mast1_20241115_2045_2115_operation_z3 += 1
        if (mast1_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            ejections_mast1_20241115_2045_2115_operation_z3 += 1
        elif (mast1_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            outward_interactions_mast1_20241115_2045_2115_operation_z3 += 1 
    elif (U_corr_mast1_20241115_2045_2115_operation_z3[i]<0)&(W_corr_mast1_20241115_2045_2115_operation_z3[i]<0):
        Q3_mast1_20241115_2045_2115_operation_z3 += 1
        if (mast1_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            sweeps_mast1_20241115_2045_2115_operation_z3 += 1
        elif (mast1_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            inward_interactions_mast1_20241115_2045_2115_operation_z3 += 1 
    elif (U_corr_mast1_20241115_2045_2115_operation_z3[i]>0)&(W_corr_mast1_20241115_2045_2115_operation_z3[i]<0):
        Q4_mast1_20241115_2045_2115_operation_z3 += 1
        if (mast1_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            sweeps_mast1_20241115_2045_2115_operation_z3 += 1
        elif (mast1_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            inward_interactions_mast1_20241115_2045_2115_operation_z3 += 1 

S1_mast1_20241115_2045_2115_operation_z3 = 100*Q1_mast1_20241115_2045_2115_operation_z3/(Q1_mast1_20241115_2045_2115_operation_z3+Q2_mast1_20241115_2045_2115_operation_z3+Q3_mast1_20241115_2045_2115_operation_z3+Q4_mast1_20241115_2045_2115_operation_z3)
S2_mast1_20241115_2045_2115_operation_z3 = 100*Q2_mast1_20241115_2045_2115_operation_z3/(Q1_mast1_20241115_2045_2115_operation_z3+Q2_mast1_20241115_2045_2115_operation_z3+Q3_mast1_20241115_2045_2115_operation_z3+Q4_mast1_20241115_2045_2115_operation_z3)
S3_mast1_20241115_2045_2115_operation_z3 = 100*Q3_mast1_20241115_2045_2115_operation_z3/(Q1_mast1_20241115_2045_2115_operation_z3+Q2_mast1_20241115_2045_2115_operation_z3+Q3_mast1_20241115_2045_2115_operation_z3+Q4_mast1_20241115_2045_2115_operation_z3)
S4_mast1_20241115_2045_2115_operation_z3 = 100*Q4_mast1_20241115_2045_2115_operation_z3/(Q1_mast1_20241115_2045_2115_operation_z3+Q2_mast1_20241115_2045_2115_operation_z3+Q3_mast1_20241115_2045_2115_operation_z3+Q4_mast1_20241115_2045_2115_operation_z3)

S_ejections_mast1_20241115_2045_2115_operation_z3 = 100*ejections_mast1_20241115_2045_2115_operation_z3/(Q1_mast1_20241115_2045_2115_operation_z3+Q2_mast1_20241115_2045_2115_operation_z3+Q3_mast1_20241115_2045_2115_operation_z3+Q4_mast1_20241115_2045_2115_operation_z3)
S_outward_interactions_mast1_20241115_2045_2115_operation_z3 = 100*outward_interactions_mast1_20241115_2045_2115_operation_z3/(Q1_mast1_20241115_2045_2115_operation_z3+Q2_mast1_20241115_2045_2115_operation_z3+Q3_mast1_20241115_2045_2115_operation_z3+Q4_mast1_20241115_2045_2115_operation_z3)
S_sweeps_mast1_20241115_2045_2115_operation_z3 = 100*sweeps_mast1_20241115_2045_2115_operation_z3/(Q1_mast1_20241115_2045_2115_operation_z3+Q2_mast1_20241115_2045_2115_operation_z3+Q3_mast1_20241115_2045_2115_operation_z3+Q4_mast1_20241115_2045_2115_operation_z3)
S_inward_interactions_mast1_20241115_2045_2115_operation_z3 = 100*inward_interactions_mast1_20241115_2045_2115_operation_z3/(Q1_mast1_20241115_2045_2115_operation_z3+Q2_mast1_20241115_2045_2115_operation_z3+Q3_mast1_20241115_2045_2115_operation_z3+Q4_mast1_20241115_2045_2115_operation_z3)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S1_mast1_20241115_2045_2115_operation_z1,S1_mast1_20241115_2045_2115_operation_z2,S1_mast1_20241115_2045_2115_operation_z3],heights,marker='o',s=20, label='u+w+ (Q1)')    
plt.scatter([S2_mast1_20241115_2045_2115_operation_z1,S2_mast1_20241115_2045_2115_operation_z2,S2_mast1_20241115_2045_2115_operation_z3],heights,marker='s',s=20, label='u-w+ (Q2)')    
plt.scatter([S3_mast1_20241115_2045_2115_operation_z1,S3_mast1_20241115_2045_2115_operation_z2,S3_mast1_20241115_2045_2115_operation_z3],heights,marker='d',s=20, label='u-w- (Q3)')    
plt.scatter([S4_mast1_20241115_2045_2115_operation_z1,S4_mast1_20241115_2045_2115_operation_z2,S4_mast1_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='u+w- (Q4)')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 55)
plt.xticks([0,10,20,30,40,50])  
plt.ylim(0, 12)
plt.title('Operation mast1 (Nov 15, 2024)')    
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S_ejections_mast1_20241115_2045_2115_operation_z1,S_ejections_mast1_20241115_2045_2115_operation_z2,S_ejections_mast1_20241115_2045_2115_operation_z3],heights,marker='o',s=20, label='ejections')    
plt.scatter([S_outward_interactions_mast1_20241115_2045_2115_operation_z1,S_outward_interactions_mast1_20241115_2045_2115_operation_z2,S_outward_interactions_mast1_20241115_2045_2115_operation_z3],heights,marker='s',s=20, label='outward interactions')    
plt.scatter([S_sweeps_mast1_20241115_2045_2115_operation_z1,S_sweeps_mast1_20241115_2045_2115_operation_z2,S_sweeps_mast1_20241115_2045_2115_operation_z3],heights,marker='d',s=20, label='sweeps')    
plt.scatter([S_inward_interactions_mast1_20241115_2045_2115_operation_z1,S_inward_interactions_mast1_20241115_2045_2115_operation_z2,S_inward_interactions_mast1_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='inward interactions')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 100)
plt.ylim(0, 12)
plt.title('Operation mast1 (Nov 15, 2024)')     
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()




#%% Quadrant analysis (mast3 Nov 15, 2024)

Q1_mast3_20241115_2045_2115_operation_z1 = Q2_mast3_20241115_2045_2115_operation_z1 = Q3_mast3_20241115_2045_2115_operation_z1 = Q4_mast3_20241115_2045_2115_operation_z1 = 0
ejections_mast3_20241115_2045_2115_operation_z1 = outward_interactions_mast3_20241115_2045_2115_operation_z1 = sweeps_mast3_20241115_2045_2115_operation_z1 = inward_interactions_mast3_20241115_2045_2115_operation_z1 = 0

for i in range(0,len(W_corr_mast3_20241115_2045_2115_operation_z1)):
    if (U_corr_mast3_20241115_2045_2115_operation_z1[i]>0)&(W_corr_mast3_20241115_2045_2115_operation_z1[i]>0):
        Q1_mast3_20241115_2045_2115_operation_z1 += 1
        if (mast3_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            ejections_mast3_20241115_2045_2115_operation_z1 += 1
        elif (mast3_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            outward_interactions_mast3_20241115_2045_2115_operation_z1 += 1            
    elif (U_corr_mast3_20241115_2045_2115_operation_z1[i]>0)&(W_corr_mast3_20241115_2045_2115_operation_z1[i]<0):
        Q2_mast3_20241115_2045_2115_operation_z1 += 1
        if (mast3_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            sweeps_mast3_20241115_2045_2115_operation_z1 += 1
        elif (mast3_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            inward_interactions_mast3_20241115_2045_2115_operation_z1 += 1 
    elif (U_corr_mast3_20241115_2045_2115_operation_z1[i]<0)&(W_corr_mast3_20241115_2045_2115_operation_z1[i]<0):
        Q3_mast3_20241115_2045_2115_operation_z1 += 1
        if (mast3_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            sweeps_mast3_20241115_2045_2115_operation_z1 += 1
        elif (mast3_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            inward_interactions_mast3_20241115_2045_2115_operation_z1 += 1 
    elif (U_corr_mast3_20241115_2045_2115_operation_z1[i]<0)&(W_corr_mast3_20241115_2045_2115_operation_z1[i]>0):
        Q2_mast3_20241115_2045_2115_operation_z1 += 1
        if (mast3_uprimewprime_z1_20241115_2045_2115_operation[i]<0):
            ejections_mast3_20241115_2045_2115_operation_z1 += 1
        elif (mast3_uprimewprime_z1_20241115_2045_2115_operation[i]>0):
            outward_interactions_mast3_20241115_2045_2115_operation_z1 += 1 


S1_mast3_20241115_2045_2115_operation_z1 = 100*Q1_mast3_20241115_2045_2115_operation_z1/(Q1_mast3_20241115_2045_2115_operation_z1+Q2_mast3_20241115_2045_2115_operation_z1+Q3_mast3_20241115_2045_2115_operation_z1+Q4_mast3_20241115_2045_2115_operation_z1)
S2_mast3_20241115_2045_2115_operation_z1 = 100*Q2_mast3_20241115_2045_2115_operation_z1/(Q1_mast3_20241115_2045_2115_operation_z1+Q2_mast3_20241115_2045_2115_operation_z1+Q3_mast3_20241115_2045_2115_operation_z1+Q4_mast3_20241115_2045_2115_operation_z1)
S3_mast3_20241115_2045_2115_operation_z1 = 100*Q3_mast3_20241115_2045_2115_operation_z1/(Q1_mast3_20241115_2045_2115_operation_z1+Q2_mast3_20241115_2045_2115_operation_z1+Q3_mast3_20241115_2045_2115_operation_z1+Q4_mast3_20241115_2045_2115_operation_z1)
S4_mast3_20241115_2045_2115_operation_z1 = 100*Q4_mast3_20241115_2045_2115_operation_z1/(Q1_mast3_20241115_2045_2115_operation_z1+Q2_mast3_20241115_2045_2115_operation_z1+Q3_mast3_20241115_2045_2115_operation_z1+Q4_mast3_20241115_2045_2115_operation_z1)

S_ejections_mast3_20241115_2045_2115_operation_z1 = 100*ejections_mast3_20241115_2045_2115_operation_z1/(Q1_mast3_20241115_2045_2115_operation_z1+Q2_mast3_20241115_2045_2115_operation_z1+Q3_mast3_20241115_2045_2115_operation_z1+Q4_mast3_20241115_2045_2115_operation_z1)
S_outward_interactions_mast3_20241115_2045_2115_operation_z1 = 100*outward_interactions_mast3_20241115_2045_2115_operation_z1/(Q1_mast3_20241115_2045_2115_operation_z1+Q2_mast3_20241115_2045_2115_operation_z1+Q3_mast3_20241115_2045_2115_operation_z1+Q4_mast3_20241115_2045_2115_operation_z1)
S_sweeps_mast3_20241115_2045_2115_operation_z1 = 100*sweeps_mast3_20241115_2045_2115_operation_z1/(Q1_mast3_20241115_2045_2115_operation_z1+Q2_mast3_20241115_2045_2115_operation_z1+Q3_mast3_20241115_2045_2115_operation_z1+Q4_mast3_20241115_2045_2115_operation_z1)
S_inward_interactions_mast3_20241115_2045_2115_operation_z1 = 100*inward_interactions_mast3_20241115_2045_2115_operation_z1/(Q1_mast3_20241115_2045_2115_operation_z1+Q2_mast3_20241115_2045_2115_operation_z1+Q3_mast3_20241115_2045_2115_operation_z1+Q4_mast3_20241115_2045_2115_operation_z1)


Q1_mast3_20241115_2045_2115_operation_z2 = Q2_mast3_20241115_2045_2115_operation_z2 = Q3_mast3_20241115_2045_2115_operation_z2 = Q4_mast3_20241115_2045_2115_operation_z2 = 0
ejections_mast3_20241115_2045_2115_operation_z2 = outward_interactions_mast3_20241115_2045_2115_operation_z2 = sweeps_mast3_20241115_2045_2115_operation_z2 = inward_interactions_mast3_20241115_2045_2115_operation_z2 = 0

for i in range(0,len(W_corr_mast3_20241115_2045_2115_operation_z2)):
    if (U_corr_mast3_20241115_2045_2115_operation_z2[i]>0)&(W_corr_mast3_20241115_2045_2115_operation_z2[i]>0):
        Q1_mast3_20241115_2045_2115_operation_z2 += 1
        if (mast3_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            ejections_mast3_20241115_2045_2115_operation_z2 += 1
        elif (mast3_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            outward_interactions_mast3_20241115_2045_2115_operation_z2 += 1            
    elif (U_corr_mast3_20241115_2045_2115_operation_z2[i]<0)&(W_corr_mast3_20241115_2045_2115_operation_z2[i]>0):
        Q2_mast3_20241115_2045_2115_operation_z2 += 1
        if (mast3_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            ejections_mast3_20241115_2045_2115_operation_z2 += 1
        elif (mast3_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            outward_interactions_mast3_20241115_2045_2115_operation_z2 += 1 
    elif (U_corr_mast3_20241115_2045_2115_operation_z2[i]<0)&(W_corr_mast3_20241115_2045_2115_operation_z2[i]<0):
        Q3_mast3_20241115_2045_2115_operation_z2 += 1
        if (mast3_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            sweeps_mast3_20241115_2045_2115_operation_z2 += 1
        elif (mast3_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            inward_interactions_mast3_20241115_2045_2115_operation_z2 += 1 
    elif (U_corr_mast3_20241115_2045_2115_operation_z2[i]>0)&(W_corr_mast3_20241115_2045_2115_operation_z2[i]<0):
        Q4_mast3_20241115_2045_2115_operation_z2 += 1
        if (mast3_uprimewprime_z2_20241115_2045_2115_operation[i]<0):
            sweeps_mast3_20241115_2045_2115_operation_z2 += 1
        elif (mast3_uprimewprime_z2_20241115_2045_2115_operation[i]>0):
            inward_interactions_mast3_20241115_2045_2115_operation_z2 += 1 

S1_mast3_20241115_2045_2115_operation_z2 = 100*Q1_mast3_20241115_2045_2115_operation_z2/(Q1_mast3_20241115_2045_2115_operation_z2+Q2_mast3_20241115_2045_2115_operation_z2+Q3_mast3_20241115_2045_2115_operation_z2+Q4_mast3_20241115_2045_2115_operation_z2)
S2_mast3_20241115_2045_2115_operation_z2 = 100*Q2_mast3_20241115_2045_2115_operation_z2/(Q1_mast3_20241115_2045_2115_operation_z2+Q2_mast3_20241115_2045_2115_operation_z2+Q3_mast3_20241115_2045_2115_operation_z2+Q4_mast3_20241115_2045_2115_operation_z2)
S3_mast3_20241115_2045_2115_operation_z2 = 100*Q3_mast3_20241115_2045_2115_operation_z2/(Q1_mast3_20241115_2045_2115_operation_z2+Q2_mast3_20241115_2045_2115_operation_z2+Q3_mast3_20241115_2045_2115_operation_z2+Q4_mast3_20241115_2045_2115_operation_z2)
S4_mast3_20241115_2045_2115_operation_z2 = 100*Q4_mast3_20241115_2045_2115_operation_z2/(Q1_mast3_20241115_2045_2115_operation_z2+Q2_mast3_20241115_2045_2115_operation_z2+Q3_mast3_20241115_2045_2115_operation_z2+Q4_mast3_20241115_2045_2115_operation_z2)

S_ejections_mast3_20241115_2045_2115_operation_z2 = 100*ejections_mast3_20241115_2045_2115_operation_z2/(Q1_mast3_20241115_2045_2115_operation_z2+Q2_mast3_20241115_2045_2115_operation_z2+Q3_mast3_20241115_2045_2115_operation_z2+Q4_mast3_20241115_2045_2115_operation_z2)
S_outward_interactions_mast3_20241115_2045_2115_operation_z2 = 100*outward_interactions_mast3_20241115_2045_2115_operation_z2/(Q1_mast3_20241115_2045_2115_operation_z2+Q2_mast3_20241115_2045_2115_operation_z2+Q3_mast3_20241115_2045_2115_operation_z2+Q4_mast3_20241115_2045_2115_operation_z2)
S_sweeps_mast3_20241115_2045_2115_operation_z2 = 100*sweeps_mast3_20241115_2045_2115_operation_z2/(Q1_mast3_20241115_2045_2115_operation_z2+Q2_mast3_20241115_2045_2115_operation_z2+Q3_mast3_20241115_2045_2115_operation_z2+Q4_mast3_20241115_2045_2115_operation_z2)
S_inward_interactions_mast3_20241115_2045_2115_operation_z2 = 100*inward_interactions_mast3_20241115_2045_2115_operation_z2/(Q1_mast3_20241115_2045_2115_operation_z2+Q2_mast3_20241115_2045_2115_operation_z2+Q3_mast3_20241115_2045_2115_operation_z2+Q4_mast3_20241115_2045_2115_operation_z2)


Q1_mast3_20241115_2045_2115_operation_z3 = Q2_mast3_20241115_2045_2115_operation_z3 = Q3_mast3_20241115_2045_2115_operation_z3 = Q4_mast3_20241115_2045_2115_operation_z3 = 0
ejections_mast3_20241115_2045_2115_operation_z3 = outward_interactions_mast3_20241115_2045_2115_operation_z3 = sweeps_mast3_20241115_2045_2115_operation_z3 = inward_interactions_mast3_20241115_2045_2115_operation_z3 = 0

for i in range(0,len(W_corr_mast3_20241115_2045_2115_operation_z3)):
    if (U_corr_mast3_20241115_2045_2115_operation_z3[i]>0)&(W_corr_mast3_20241115_2045_2115_operation_z3[i]>0):
        Q1_mast3_20241115_2045_2115_operation_z3 += 1
        if (mast3_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            ejections_mast3_20241115_2045_2115_operation_z3 += 1
        elif (mast3_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            outward_interactions_mast3_20241115_2045_2115_operation_z3 += 1            
    elif (U_corr_mast3_20241115_2045_2115_operation_z3[i]<0)&(W_corr_mast3_20241115_2045_2115_operation_z3[i]>0):
        Q2_mast3_20241115_2045_2115_operation_z3 += 1
        if (mast3_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            ejections_mast3_20241115_2045_2115_operation_z3 += 1
        elif (mast3_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            outward_interactions_mast3_20241115_2045_2115_operation_z3 += 1 
    elif (U_corr_mast3_20241115_2045_2115_operation_z3[i]<0)&(W_corr_mast3_20241115_2045_2115_operation_z3[i]<0):
        Q3_mast3_20241115_2045_2115_operation_z3 += 1
        if (mast3_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            sweeps_mast3_20241115_2045_2115_operation_z3 += 1
        elif (mast3_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            inward_interactions_mast3_20241115_2045_2115_operation_z3 += 1 
    elif (U_corr_mast3_20241115_2045_2115_operation_z3[i]>0)&(W_corr_mast3_20241115_2045_2115_operation_z3[i]<0):
        Q4_mast3_20241115_2045_2115_operation_z3 += 1
        if (mast3_uprimewprime_z3_20241115_2045_2115_operation[i]<0):
            sweeps_mast3_20241115_2045_2115_operation_z3 += 1
        elif (mast3_uprimewprime_z3_20241115_2045_2115_operation[i]>0):
            inward_interactions_mast3_20241115_2045_2115_operation_z3 += 1 

S1_mast3_20241115_2045_2115_operation_z3 = 100*Q1_mast3_20241115_2045_2115_operation_z3/(Q1_mast3_20241115_2045_2115_operation_z3+Q2_mast3_20241115_2045_2115_operation_z3+Q3_mast3_20241115_2045_2115_operation_z3+Q4_mast3_20241115_2045_2115_operation_z3)
S2_mast3_20241115_2045_2115_operation_z3 = 100*Q2_mast3_20241115_2045_2115_operation_z3/(Q1_mast3_20241115_2045_2115_operation_z3+Q2_mast3_20241115_2045_2115_operation_z3+Q3_mast3_20241115_2045_2115_operation_z3+Q4_mast3_20241115_2045_2115_operation_z3)
S3_mast3_20241115_2045_2115_operation_z3 = 100*Q3_mast3_20241115_2045_2115_operation_z3/(Q1_mast3_20241115_2045_2115_operation_z3+Q2_mast3_20241115_2045_2115_operation_z3+Q3_mast3_20241115_2045_2115_operation_z3+Q4_mast3_20241115_2045_2115_operation_z3)
S4_mast3_20241115_2045_2115_operation_z3 = 100*Q4_mast3_20241115_2045_2115_operation_z3/(Q1_mast3_20241115_2045_2115_operation_z3+Q2_mast3_20241115_2045_2115_operation_z3+Q3_mast3_20241115_2045_2115_operation_z3+Q4_mast3_20241115_2045_2115_operation_z3)

S_ejections_mast3_20241115_2045_2115_operation_z3 = 100*ejections_mast3_20241115_2045_2115_operation_z3/(Q1_mast3_20241115_2045_2115_operation_z3+Q2_mast3_20241115_2045_2115_operation_z3+Q3_mast3_20241115_2045_2115_operation_z3+Q4_mast3_20241115_2045_2115_operation_z3)
S_outward_interactions_mast3_20241115_2045_2115_operation_z3 = 100*outward_interactions_mast3_20241115_2045_2115_operation_z3/(Q1_mast3_20241115_2045_2115_operation_z3+Q2_mast3_20241115_2045_2115_operation_z3+Q3_mast3_20241115_2045_2115_operation_z3+Q4_mast3_20241115_2045_2115_operation_z3)
S_sweeps_mast3_20241115_2045_2115_operation_z3 = 100*sweeps_mast3_20241115_2045_2115_operation_z3/(Q1_mast3_20241115_2045_2115_operation_z3+Q2_mast3_20241115_2045_2115_operation_z3+Q3_mast3_20241115_2045_2115_operation_z3+Q4_mast3_20241115_2045_2115_operation_z3)
S_inward_interactions_mast3_20241115_2045_2115_operation_z3 = 100*inward_interactions_mast3_20241115_2045_2115_operation_z3/(Q1_mast3_20241115_2045_2115_operation_z3+Q2_mast3_20241115_2045_2115_operation_z3+Q3_mast3_20241115_2045_2115_operation_z3+Q4_mast3_20241115_2045_2115_operation_z3)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S1_mast3_20241115_2045_2115_operation_z1,S1_mast3_20241115_2045_2115_operation_z2,S1_mast3_20241115_2045_2115_operation_z3],heights,marker='o',s=20, label='u+w+ (Q1)')    
plt.scatter([S2_mast3_20241115_2045_2115_operation_z1,S2_mast3_20241115_2045_2115_operation_z2,S2_mast3_20241115_2045_2115_operation_z3],heights,marker='s',s=20, label='u-w+ (Q2)')    
plt.scatter([S3_mast3_20241115_2045_2115_operation_z1,S3_mast3_20241115_2045_2115_operation_z2,S3_mast3_20241115_2045_2115_operation_z3],heights,marker='d',s=20, label='u-w- (Q3)')    
plt.scatter([S4_mast3_20241115_2045_2115_operation_z1,S4_mast3_20241115_2045_2115_operation_z2,S4_mast3_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='u+w- (Q4)')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 55)
plt.xticks([0,10,20,30,40,50])  
plt.ylim(0, 12)
plt.title('Operation mast3 (Nov 15, 2024)')    
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S_ejections_mast3_20241115_2045_2115_operation_z1,S_ejections_mast3_20241115_2045_2115_operation_z2,S_ejections_mast3_20241115_2045_2115_operation_z3],heights,marker='o',s=20, label='ejections')    
plt.scatter([S_outward_interactions_mast3_20241115_2045_2115_operation_z1,S_outward_interactions_mast3_20241115_2045_2115_operation_z2,S_outward_interactions_mast3_20241115_2045_2115_operation_z3],heights,marker='s',s=20, label='outward interactions')    
plt.scatter([S_sweeps_mast3_20241115_2045_2115_operation_z1,S_sweeps_mast3_20241115_2045_2115_operation_z2,S_sweeps_mast3_20241115_2045_2115_operation_z3],heights,marker='d',s=20, label='sweeps')    
plt.scatter([S_inward_interactions_mast3_20241115_2045_2115_operation_z1,S_inward_interactions_mast3_20241115_2045_2115_operation_z2,S_inward_interactions_mast3_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='inward interactions')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 100)
plt.ylim(0, 12)
plt.title('Operation mast3 (Nov 15, 2024)')     
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S4_inflow_20241115_2045_2115_operation_z1,S4_inflow_20241115_2045_2115_operation_z2,S4_inflow_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='inflow')    
plt.scatter([S4_mast1_20241115_2045_2115_operation_z1,S4_mast1_20241115_2045_2115_operation_z2,S4_mast1_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='mast1')    
plt.scatter([S4_mast3_20241115_2045_2115_operation_z1,S3_mast3_20241115_2045_2115_operation_z2,S3_mast3_20241115_2045_2115_operation_z3],heights,marker='d',s=20, label='mast3')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 55)
plt.xticks([0,10,20,30,40,50])  
plt.ylim(0, 12)
plt.title('Operation (Nov 15, 2024)')    
plt.xlabel("Sweeps (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S2_inflow_20241115_2045_2115_operation_z1,S2_inflow_20241115_2045_2115_operation_z2,S2_inflow_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='inflow')    
plt.scatter([S2_mast1_20241115_2045_2115_operation_z1,S2_mast1_20241115_2045_2115_operation_z2,S2_mast1_20241115_2045_2115_operation_z3],heights,marker='v',s=20, label='mast1')    
plt.scatter([S2_mast3_20241115_2045_2115_operation_z1,S3_mast3_20241115_2045_2115_operation_z2,S3_mast3_20241115_2045_2115_operation_z3],heights,marker='d',s=20, label='mast3')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 55)
plt.xticks([0,10,20,30,40,50])  
plt.ylim(0, 12)
plt.title('Operation (Nov 15, 2024)')    
plt.xlabel("Ejections (%)")
plt.ylabel("Height (m)")
plt.show()



#%% Quadrant analysis (inflow Nov 15, 2024)


Q1_inflow_20241115_2130_2200_stow_z1 = Q2_inflow_20241115_2130_2200_stow_z1 = Q3_inflow_20241115_2130_2200_stow_z1 = Q4_inflow_20241115_2130_2200_stow_z1 = 0
ejections_inflow_20241115_2130_2200_stow_z1 = outward_interactions_inflow_20241115_2130_2200_stow_z1 = sweeps_inflow_20241115_2130_2200_stow_z1 = inward_interactions_inflow_20241115_2130_2200_stow_z1 = 0

for i in range(0,len(W_corr_inflow_20241115_2130_2200_stow_z1)):
    if (U_corr_inflow_20241115_2130_2200_stow_z1[i]>0)&(W_corr_inflow_20241115_2130_2200_stow_z1[i]>0):
        Q1_inflow_20241115_2130_2200_stow_z1 += 1
        if (inflow_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            ejections_inflow_20241115_2130_2200_stow_z1 += 1
        elif (inflow_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            outward_interactions_inflow_20241115_2130_2200_stow_z1 += 1            
    elif (U_corr_inflow_20241115_2130_2200_stow_z1[i]>0)&(W_corr_inflow_20241115_2130_2200_stow_z1[i]<0):
        Q2_inflow_20241115_2130_2200_stow_z1 += 1
        if (inflow_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            sweeps_inflow_20241115_2130_2200_stow_z1 += 1
        elif (inflow_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            inward_interactions_inflow_20241115_2130_2200_stow_z1 += 1 
    elif (U_corr_inflow_20241115_2130_2200_stow_z1[i]<0)&(W_corr_inflow_20241115_2130_2200_stow_z1[i]<0):
        Q3_inflow_20241115_2130_2200_stow_z1 += 1
        if (inflow_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            sweeps_inflow_20241115_2130_2200_stow_z1 += 1
        elif (inflow_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            inward_interactions_inflow_20241115_2130_2200_stow_z1 += 1 
    elif (U_corr_inflow_20241115_2130_2200_stow_z1[i]<0)&(W_corr_inflow_20241115_2130_2200_stow_z1[i]>0):
        Q2_inflow_20241115_2130_2200_stow_z1 += 1
        if (inflow_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            ejections_inflow_20241115_2130_2200_stow_z1 += 1
        elif (inflow_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            outward_interactions_inflow_20241115_2130_2200_stow_z1 += 1 


S1_inflow_20241115_2130_2200_stow_z1 = 100*Q1_inflow_20241115_2130_2200_stow_z1/(Q1_inflow_20241115_2130_2200_stow_z1+Q2_inflow_20241115_2130_2200_stow_z1+Q3_inflow_20241115_2130_2200_stow_z1+Q4_inflow_20241115_2130_2200_stow_z1)
S2_inflow_20241115_2130_2200_stow_z1 = 100*Q2_inflow_20241115_2130_2200_stow_z1/(Q1_inflow_20241115_2130_2200_stow_z1+Q2_inflow_20241115_2130_2200_stow_z1+Q3_inflow_20241115_2130_2200_stow_z1+Q4_inflow_20241115_2130_2200_stow_z1)
S3_inflow_20241115_2130_2200_stow_z1 = 100*Q3_inflow_20241115_2130_2200_stow_z1/(Q1_inflow_20241115_2130_2200_stow_z1+Q2_inflow_20241115_2130_2200_stow_z1+Q3_inflow_20241115_2130_2200_stow_z1+Q4_inflow_20241115_2130_2200_stow_z1)
S4_inflow_20241115_2130_2200_stow_z1 = 100*Q4_inflow_20241115_2130_2200_stow_z1/(Q1_inflow_20241115_2130_2200_stow_z1+Q2_inflow_20241115_2130_2200_stow_z1+Q3_inflow_20241115_2130_2200_stow_z1+Q4_inflow_20241115_2130_2200_stow_z1)

S_ejections_inflow_20241115_2130_2200_stow_z1 = 100*ejections_inflow_20241115_2130_2200_stow_z1/(Q1_inflow_20241115_2130_2200_stow_z1+Q2_inflow_20241115_2130_2200_stow_z1+Q3_inflow_20241115_2130_2200_stow_z1+Q4_inflow_20241115_2130_2200_stow_z1)
S_outward_interactions_inflow_20241115_2130_2200_stow_z1 = 100*outward_interactions_inflow_20241115_2130_2200_stow_z1/(Q1_inflow_20241115_2130_2200_stow_z1+Q2_inflow_20241115_2130_2200_stow_z1+Q3_inflow_20241115_2130_2200_stow_z1+Q4_inflow_20241115_2130_2200_stow_z1)
S_sweeps_inflow_20241115_2130_2200_stow_z1 = 100*sweeps_inflow_20241115_2130_2200_stow_z1/(Q1_inflow_20241115_2130_2200_stow_z1+Q2_inflow_20241115_2130_2200_stow_z1+Q3_inflow_20241115_2130_2200_stow_z1+Q4_inflow_20241115_2130_2200_stow_z1)
S_inward_interactions_inflow_20241115_2130_2200_stow_z1 = 100*inward_interactions_inflow_20241115_2130_2200_stow_z1/(Q1_inflow_20241115_2130_2200_stow_z1+Q2_inflow_20241115_2130_2200_stow_z1+Q3_inflow_20241115_2130_2200_stow_z1+Q4_inflow_20241115_2130_2200_stow_z1)


Q1_inflow_20241115_2130_2200_stow_z2 = Q2_inflow_20241115_2130_2200_stow_z2 = Q3_inflow_20241115_2130_2200_stow_z2 = Q4_inflow_20241115_2130_2200_stow_z2 = 0
ejections_inflow_20241115_2130_2200_stow_z2 = outward_interactions_inflow_20241115_2130_2200_stow_z2 = sweeps_inflow_20241115_2130_2200_stow_z2 = inward_interactions_inflow_20241115_2130_2200_stow_z2 = 0

for i in range(0,len(W_corr_inflow_20241115_2130_2200_stow_z2)):
    if (U_corr_inflow_20241115_2130_2200_stow_z2[i]>0)&(W_corr_inflow_20241115_2130_2200_stow_z2[i]>0):
        Q1_inflow_20241115_2130_2200_stow_z2 += 1
        if (inflow_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            ejections_inflow_20241115_2130_2200_stow_z2 += 1
        elif (inflow_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            outward_interactions_inflow_20241115_2130_2200_stow_z2 += 1            
    elif (U_corr_inflow_20241115_2130_2200_stow_z2[i]<0)&(W_corr_inflow_20241115_2130_2200_stow_z2[i]>0):
        Q2_inflow_20241115_2130_2200_stow_z2 += 1
        if (inflow_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            ejections_inflow_20241115_2130_2200_stow_z2 += 1
        elif (inflow_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            outward_interactions_inflow_20241115_2130_2200_stow_z2 += 1 
    elif (U_corr_inflow_20241115_2130_2200_stow_z2[i]<0)&(W_corr_inflow_20241115_2130_2200_stow_z2[i]<0):
        Q3_inflow_20241115_2130_2200_stow_z2 += 1
        if (inflow_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            sweeps_inflow_20241115_2130_2200_stow_z2 += 1
        elif (inflow_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            inward_interactions_inflow_20241115_2130_2200_stow_z2 += 1 
    elif (U_corr_inflow_20241115_2130_2200_stow_z2[i]>0)&(W_corr_inflow_20241115_2130_2200_stow_z2[i]<0):
        Q4_inflow_20241115_2130_2200_stow_z2 += 1
        if (inflow_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            sweeps_inflow_20241115_2130_2200_stow_z2 += 1
        elif (inflow_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            inward_interactions_inflow_20241115_2130_2200_stow_z2 += 1 

S1_inflow_20241115_2130_2200_stow_z2 = 100*Q1_inflow_20241115_2130_2200_stow_z2/(Q1_inflow_20241115_2130_2200_stow_z2+Q2_inflow_20241115_2130_2200_stow_z2+Q3_inflow_20241115_2130_2200_stow_z2+Q4_inflow_20241115_2130_2200_stow_z2)
S2_inflow_20241115_2130_2200_stow_z2 = 100*Q2_inflow_20241115_2130_2200_stow_z2/(Q1_inflow_20241115_2130_2200_stow_z2+Q2_inflow_20241115_2130_2200_stow_z2+Q3_inflow_20241115_2130_2200_stow_z2+Q4_inflow_20241115_2130_2200_stow_z2)
S3_inflow_20241115_2130_2200_stow_z2 = 100*Q3_inflow_20241115_2130_2200_stow_z2/(Q1_inflow_20241115_2130_2200_stow_z2+Q2_inflow_20241115_2130_2200_stow_z2+Q3_inflow_20241115_2130_2200_stow_z2+Q4_inflow_20241115_2130_2200_stow_z2)
S4_inflow_20241115_2130_2200_stow_z2 = 100*Q4_inflow_20241115_2130_2200_stow_z2/(Q1_inflow_20241115_2130_2200_stow_z2+Q2_inflow_20241115_2130_2200_stow_z2+Q3_inflow_20241115_2130_2200_stow_z2+Q4_inflow_20241115_2130_2200_stow_z2)

S_ejections_inflow_20241115_2130_2200_stow_z2 = 100*ejections_inflow_20241115_2130_2200_stow_z2/(Q1_inflow_20241115_2130_2200_stow_z2+Q2_inflow_20241115_2130_2200_stow_z2+Q3_inflow_20241115_2130_2200_stow_z2+Q4_inflow_20241115_2130_2200_stow_z2)
S_outward_interactions_inflow_20241115_2130_2200_stow_z2 = 100*outward_interactions_inflow_20241115_2130_2200_stow_z2/(Q1_inflow_20241115_2130_2200_stow_z2+Q2_inflow_20241115_2130_2200_stow_z2+Q3_inflow_20241115_2130_2200_stow_z2+Q4_inflow_20241115_2130_2200_stow_z2)
S_sweeps_inflow_20241115_2130_2200_stow_z2 = 100*sweeps_inflow_20241115_2130_2200_stow_z2/(Q1_inflow_20241115_2130_2200_stow_z2+Q2_inflow_20241115_2130_2200_stow_z2+Q3_inflow_20241115_2130_2200_stow_z2+Q4_inflow_20241115_2130_2200_stow_z2)
S_inward_interactions_inflow_20241115_2130_2200_stow_z2 = 100*inward_interactions_inflow_20241115_2130_2200_stow_z2/(Q1_inflow_20241115_2130_2200_stow_z2+Q2_inflow_20241115_2130_2200_stow_z2+Q3_inflow_20241115_2130_2200_stow_z2+Q4_inflow_20241115_2130_2200_stow_z2)


Q1_inflow_20241115_2130_2200_stow_z3 = Q2_inflow_20241115_2130_2200_stow_z3 = Q3_inflow_20241115_2130_2200_stow_z3 = Q4_inflow_20241115_2130_2200_stow_z3 = 0
ejections_inflow_20241115_2130_2200_stow_z3 = outward_interactions_inflow_20241115_2130_2200_stow_z3 = sweeps_inflow_20241115_2130_2200_stow_z3 = inward_interactions_inflow_20241115_2130_2200_stow_z3 = 0

for i in range(0,len(W_corr_inflow_20241115_2130_2200_stow_z3)):
    if (U_corr_inflow_20241115_2130_2200_stow_z3[i]>0)&(W_corr_inflow_20241115_2130_2200_stow_z3[i]>0):
        Q1_inflow_20241115_2130_2200_stow_z3 += 1
        if (inflow_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            ejections_inflow_20241115_2130_2200_stow_z3 += 1
        elif (inflow_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            outward_interactions_inflow_20241115_2130_2200_stow_z3 += 1            
    elif (U_corr_inflow_20241115_2130_2200_stow_z3[i]<0)&(W_corr_inflow_20241115_2130_2200_stow_z3[i]>0):
        Q2_inflow_20241115_2130_2200_stow_z3 += 1
        if (inflow_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            ejections_inflow_20241115_2130_2200_stow_z3 += 1
        elif (inflow_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            outward_interactions_inflow_20241115_2130_2200_stow_z3 += 1 
    elif (U_corr_inflow_20241115_2130_2200_stow_z3[i]<0)&(W_corr_inflow_20241115_2130_2200_stow_z3[i]<0):
        Q3_inflow_20241115_2130_2200_stow_z3 += 1
        if (inflow_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            sweeps_inflow_20241115_2130_2200_stow_z3 += 1
        elif (inflow_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            inward_interactions_inflow_20241115_2130_2200_stow_z3 += 1 
    elif (U_corr_inflow_20241115_2130_2200_stow_z3[i]>0)&(W_corr_inflow_20241115_2130_2200_stow_z3[i]<0):
        Q4_inflow_20241115_2130_2200_stow_z3 += 1
        if (inflow_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            sweeps_inflow_20241115_2130_2200_stow_z3 += 1
        elif (inflow_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            inward_interactions_inflow_20241115_2130_2200_stow_z3 += 1 

S1_inflow_20241115_2130_2200_stow_z3 = 100*Q1_inflow_20241115_2130_2200_stow_z3/(Q1_inflow_20241115_2130_2200_stow_z3+Q2_inflow_20241115_2130_2200_stow_z3+Q3_inflow_20241115_2130_2200_stow_z3+Q4_inflow_20241115_2130_2200_stow_z3)
S2_inflow_20241115_2130_2200_stow_z3 = 100*Q2_inflow_20241115_2130_2200_stow_z3/(Q1_inflow_20241115_2130_2200_stow_z3+Q2_inflow_20241115_2130_2200_stow_z3+Q3_inflow_20241115_2130_2200_stow_z3+Q4_inflow_20241115_2130_2200_stow_z3)
S3_inflow_20241115_2130_2200_stow_z3 = 100*Q3_inflow_20241115_2130_2200_stow_z3/(Q1_inflow_20241115_2130_2200_stow_z3+Q2_inflow_20241115_2130_2200_stow_z3+Q3_inflow_20241115_2130_2200_stow_z3+Q4_inflow_20241115_2130_2200_stow_z3)
S4_inflow_20241115_2130_2200_stow_z3 = 100*Q4_inflow_20241115_2130_2200_stow_z3/(Q1_inflow_20241115_2130_2200_stow_z3+Q2_inflow_20241115_2130_2200_stow_z3+Q3_inflow_20241115_2130_2200_stow_z3+Q4_inflow_20241115_2130_2200_stow_z3)

S_ejections_inflow_20241115_2130_2200_stow_z3 = 100*ejections_inflow_20241115_2130_2200_stow_z3/(Q1_inflow_20241115_2130_2200_stow_z3+Q2_inflow_20241115_2130_2200_stow_z3+Q3_inflow_20241115_2130_2200_stow_z3+Q4_inflow_20241115_2130_2200_stow_z3)
S_outward_interactions_inflow_20241115_2130_2200_stow_z3 = 100*outward_interactions_inflow_20241115_2130_2200_stow_z3/(Q1_inflow_20241115_2130_2200_stow_z3+Q2_inflow_20241115_2130_2200_stow_z3+Q3_inflow_20241115_2130_2200_stow_z3+Q4_inflow_20241115_2130_2200_stow_z3)
S_sweeps_inflow_20241115_2130_2200_stow_z3 = 100*sweeps_inflow_20241115_2130_2200_stow_z3/(Q1_inflow_20241115_2130_2200_stow_z3+Q2_inflow_20241115_2130_2200_stow_z3+Q3_inflow_20241115_2130_2200_stow_z3+Q4_inflow_20241115_2130_2200_stow_z3)
S_inward_interactions_inflow_20241115_2130_2200_stow_z3 = 100*inward_interactions_inflow_20241115_2130_2200_stow_z3/(Q1_inflow_20241115_2130_2200_stow_z3+Q2_inflow_20241115_2130_2200_stow_z3+Q3_inflow_20241115_2130_2200_stow_z3+Q4_inflow_20241115_2130_2200_stow_z3)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S1_inflow_20241115_2130_2200_stow_z1,S1_inflow_20241115_2130_2200_stow_z2,S1_inflow_20241115_2130_2200_stow_z3],heights,marker='o',s=20, label='u+w+ (Q1)')    
plt.scatter([S2_inflow_20241115_2130_2200_stow_z1,S2_inflow_20241115_2130_2200_stow_z2,S2_inflow_20241115_2130_2200_stow_z3],heights,marker='s',s=20, label='u-w+ (Q2)')    
plt.scatter([S3_inflow_20241115_2130_2200_stow_z1,S3_inflow_20241115_2130_2200_stow_z2,S3_inflow_20241115_2130_2200_stow_z3],heights,marker='d',s=20, label='u-w- (Q3)')    
plt.scatter([S4_inflow_20241115_2130_2200_stow_z1,S4_inflow_20241115_2130_2200_stow_z2,S4_inflow_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='u+w- (Q4)')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 55)
plt.xticks([0,10,20,30,40,50])  
plt.ylim(0, 12)
plt.title('Stow inflow (Nov 15, 2024)')    
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S_ejections_inflow_20241115_2130_2200_stow_z1,S_ejections_inflow_20241115_2130_2200_stow_z2,S_ejections_inflow_20241115_2130_2200_stow_z3],heights,marker='o',s=20, label='ejections')    
plt.scatter([S_outward_interactions_inflow_20241115_2130_2200_stow_z1,S_outward_interactions_inflow_20241115_2130_2200_stow_z2,S_outward_interactions_inflow_20241115_2130_2200_stow_z3],heights,marker='s',s=20, label='outward interactions')    
plt.scatter([S_sweeps_inflow_20241115_2130_2200_stow_z1,S_sweeps_inflow_20241115_2130_2200_stow_z2,S_sweeps_inflow_20241115_2130_2200_stow_z3],heights,marker='d',s=20, label='sweeps')    
plt.scatter([S_inward_interactions_inflow_20241115_2130_2200_stow_z1,S_inward_interactions_inflow_20241115_2130_2200_stow_z2,S_inward_interactions_inflow_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='inward interactions')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 100)
plt.ylim(0, 12)
plt.title('Stow inflow (Nov 15, 2024)')     
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


#%% Quadrant analysis (mast1 Nov 15, 2024)

Q1_mast1_20241115_2130_2200_stow_z1 = Q2_mast1_20241115_2130_2200_stow_z1 = Q3_mast1_20241115_2130_2200_stow_z1 = Q4_mast1_20241115_2130_2200_stow_z1 = 0
ejections_mast1_20241115_2130_2200_stow_z1 = outward_interactions_mast1_20241115_2130_2200_stow_z1 = sweeps_mast1_20241115_2130_2200_stow_z1 = inward_interactions_mast1_20241115_2130_2200_stow_z1 = 0

for i in range(0,len(W_corr_mast1_20241115_2130_2200_stow_z1)):
    if (U_corr_mast1_20241115_2130_2200_stow_z1[i]>0)&(W_corr_mast1_20241115_2130_2200_stow_z1[i]>0):
        Q1_mast1_20241115_2130_2200_stow_z1 += 1
        if (mast1_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            ejections_mast1_20241115_2130_2200_stow_z1 += 1
        elif (mast1_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            outward_interactions_mast1_20241115_2130_2200_stow_z1 += 1            
    elif (U_corr_mast1_20241115_2130_2200_stow_z1[i]>0)&(W_corr_mast1_20241115_2130_2200_stow_z1[i]<0):
        Q2_mast1_20241115_2130_2200_stow_z1 += 1
        if (mast1_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            sweeps_mast1_20241115_2130_2200_stow_z1 += 1
        elif (mast1_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            inward_interactions_mast1_20241115_2130_2200_stow_z1 += 1 
    elif (U_corr_mast1_20241115_2130_2200_stow_z1[i]<0)&(W_corr_mast1_20241115_2130_2200_stow_z1[i]<0):
        Q3_mast1_20241115_2130_2200_stow_z1 += 1
        if (mast1_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            sweeps_mast1_20241115_2130_2200_stow_z1 += 1
        elif (mast1_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            inward_interactions_mast1_20241115_2130_2200_stow_z1 += 1 
    elif (U_corr_mast1_20241115_2130_2200_stow_z1[i]<0)&(W_corr_mast1_20241115_2130_2200_stow_z1[i]>0):
        Q2_mast1_20241115_2130_2200_stow_z1 += 1
        if (mast1_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            ejections_mast1_20241115_2130_2200_stow_z1 += 1
        elif (mast1_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            outward_interactions_mast1_20241115_2130_2200_stow_z1 += 1 


S1_mast1_20241115_2130_2200_stow_z1 = 100*Q1_mast1_20241115_2130_2200_stow_z1/(Q1_mast1_20241115_2130_2200_stow_z1+Q2_mast1_20241115_2130_2200_stow_z1+Q3_mast1_20241115_2130_2200_stow_z1+Q4_mast1_20241115_2130_2200_stow_z1)
S2_mast1_20241115_2130_2200_stow_z1 = 100*Q2_mast1_20241115_2130_2200_stow_z1/(Q1_mast1_20241115_2130_2200_stow_z1+Q2_mast1_20241115_2130_2200_stow_z1+Q3_mast1_20241115_2130_2200_stow_z1+Q4_mast1_20241115_2130_2200_stow_z1)
S3_mast1_20241115_2130_2200_stow_z1 = 100*Q3_mast1_20241115_2130_2200_stow_z1/(Q1_mast1_20241115_2130_2200_stow_z1+Q2_mast1_20241115_2130_2200_stow_z1+Q3_mast1_20241115_2130_2200_stow_z1+Q4_mast1_20241115_2130_2200_stow_z1)
S4_mast1_20241115_2130_2200_stow_z1 = 100*Q4_mast1_20241115_2130_2200_stow_z1/(Q1_mast1_20241115_2130_2200_stow_z1+Q2_mast1_20241115_2130_2200_stow_z1+Q3_mast1_20241115_2130_2200_stow_z1+Q4_mast1_20241115_2130_2200_stow_z1)

S_ejections_mast1_20241115_2130_2200_stow_z1 = 100*ejections_mast1_20241115_2130_2200_stow_z1/(Q1_mast1_20241115_2130_2200_stow_z1+Q2_mast1_20241115_2130_2200_stow_z1+Q3_mast1_20241115_2130_2200_stow_z1+Q4_mast1_20241115_2130_2200_stow_z1)
S_outward_interactions_mast1_20241115_2130_2200_stow_z1 = 100*outward_interactions_mast1_20241115_2130_2200_stow_z1/(Q1_mast1_20241115_2130_2200_stow_z1+Q2_mast1_20241115_2130_2200_stow_z1+Q3_mast1_20241115_2130_2200_stow_z1+Q4_mast1_20241115_2130_2200_stow_z1)
S_sweeps_mast1_20241115_2130_2200_stow_z1 = 100*sweeps_mast1_20241115_2130_2200_stow_z1/(Q1_mast1_20241115_2130_2200_stow_z1+Q2_mast1_20241115_2130_2200_stow_z1+Q3_mast1_20241115_2130_2200_stow_z1+Q4_mast1_20241115_2130_2200_stow_z1)
S_inward_interactions_mast1_20241115_2130_2200_stow_z1 = 100*inward_interactions_mast1_20241115_2130_2200_stow_z1/(Q1_mast1_20241115_2130_2200_stow_z1+Q2_mast1_20241115_2130_2200_stow_z1+Q3_mast1_20241115_2130_2200_stow_z1+Q4_mast1_20241115_2130_2200_stow_z1)


Q1_mast1_20241115_2130_2200_stow_z2 = Q2_mast1_20241115_2130_2200_stow_z2 = Q3_mast1_20241115_2130_2200_stow_z2 = Q4_mast1_20241115_2130_2200_stow_z2 = 0
ejections_mast1_20241115_2130_2200_stow_z2 = outward_interactions_mast1_20241115_2130_2200_stow_z2 = sweeps_mast1_20241115_2130_2200_stow_z2 = inward_interactions_mast1_20241115_2130_2200_stow_z2 = 0

for i in range(0,len(W_corr_mast1_20241115_2130_2200_stow_z2)):
    if (U_corr_mast1_20241115_2130_2200_stow_z2[i]>0)&(W_corr_mast1_20241115_2130_2200_stow_z2[i]>0):
        Q1_mast1_20241115_2130_2200_stow_z2 += 1
        if (mast1_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            ejections_mast1_20241115_2130_2200_stow_z2 += 1
        elif (mast1_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            outward_interactions_mast1_20241115_2130_2200_stow_z2 += 1            
    elif (U_corr_mast1_20241115_2130_2200_stow_z2[i]<0)&(W_corr_mast1_20241115_2130_2200_stow_z2[i]>0):
        Q2_mast1_20241115_2130_2200_stow_z2 += 1
        if (mast1_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            ejections_mast1_20241115_2130_2200_stow_z2 += 1
        elif (mast1_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            outward_interactions_mast1_20241115_2130_2200_stow_z2 += 1 
    elif (U_corr_mast1_20241115_2130_2200_stow_z2[i]<0)&(W_corr_mast1_20241115_2130_2200_stow_z2[i]<0):
        Q3_mast1_20241115_2130_2200_stow_z2 += 1
        if (mast1_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            sweeps_mast1_20241115_2130_2200_stow_z2 += 1
        elif (mast1_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            inward_interactions_mast1_20241115_2130_2200_stow_z2 += 1 
    elif (U_corr_mast1_20241115_2130_2200_stow_z2[i]>0)&(W_corr_mast1_20241115_2130_2200_stow_z2[i]<0):
        Q4_mast1_20241115_2130_2200_stow_z2 += 1
        if (mast1_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            sweeps_mast1_20241115_2130_2200_stow_z2 += 1
        elif (mast1_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            inward_interactions_mast1_20241115_2130_2200_stow_z2 += 1 

S1_mast1_20241115_2130_2200_stow_z2 = 100*Q1_mast1_20241115_2130_2200_stow_z2/(Q1_mast1_20241115_2130_2200_stow_z2+Q2_mast1_20241115_2130_2200_stow_z2+Q3_mast1_20241115_2130_2200_stow_z2+Q4_mast1_20241115_2130_2200_stow_z2)
S2_mast1_20241115_2130_2200_stow_z2 = 100*Q2_mast1_20241115_2130_2200_stow_z2/(Q1_mast1_20241115_2130_2200_stow_z2+Q2_mast1_20241115_2130_2200_stow_z2+Q3_mast1_20241115_2130_2200_stow_z2+Q4_mast1_20241115_2130_2200_stow_z2)
S3_mast1_20241115_2130_2200_stow_z2 = 100*Q3_mast1_20241115_2130_2200_stow_z2/(Q1_mast1_20241115_2130_2200_stow_z2+Q2_mast1_20241115_2130_2200_stow_z2+Q3_mast1_20241115_2130_2200_stow_z2+Q4_mast1_20241115_2130_2200_stow_z2)
S4_mast1_20241115_2130_2200_stow_z2 = 100*Q4_mast1_20241115_2130_2200_stow_z2/(Q1_mast1_20241115_2130_2200_stow_z2+Q2_mast1_20241115_2130_2200_stow_z2+Q3_mast1_20241115_2130_2200_stow_z2+Q4_mast1_20241115_2130_2200_stow_z2)

S_ejections_mast1_20241115_2130_2200_stow_z2 = 100*ejections_mast1_20241115_2130_2200_stow_z2/(Q1_mast1_20241115_2130_2200_stow_z2+Q2_mast1_20241115_2130_2200_stow_z2+Q3_mast1_20241115_2130_2200_stow_z2+Q4_mast1_20241115_2130_2200_stow_z2)
S_outward_interactions_mast1_20241115_2130_2200_stow_z2 = 100*outward_interactions_mast1_20241115_2130_2200_stow_z2/(Q1_mast1_20241115_2130_2200_stow_z2+Q2_mast1_20241115_2130_2200_stow_z2+Q3_mast1_20241115_2130_2200_stow_z2+Q4_mast1_20241115_2130_2200_stow_z2)
S_sweeps_mast1_20241115_2130_2200_stow_z2 = 100*sweeps_mast1_20241115_2130_2200_stow_z2/(Q1_mast1_20241115_2130_2200_stow_z2+Q2_mast1_20241115_2130_2200_stow_z2+Q3_mast1_20241115_2130_2200_stow_z2+Q4_mast1_20241115_2130_2200_stow_z2)
S_inward_interactions_mast1_20241115_2130_2200_stow_z2 = 100*inward_interactions_mast1_20241115_2130_2200_stow_z2/(Q1_mast1_20241115_2130_2200_stow_z2+Q2_mast1_20241115_2130_2200_stow_z2+Q3_mast1_20241115_2130_2200_stow_z2+Q4_mast1_20241115_2130_2200_stow_z2)


Q1_mast1_20241115_2130_2200_stow_z3 = Q2_mast1_20241115_2130_2200_stow_z3 = Q3_mast1_20241115_2130_2200_stow_z3 = Q4_mast1_20241115_2130_2200_stow_z3 = 0
ejections_mast1_20241115_2130_2200_stow_z3 = outward_interactions_mast1_20241115_2130_2200_stow_z3 = sweeps_mast1_20241115_2130_2200_stow_z3 = inward_interactions_mast1_20241115_2130_2200_stow_z3 = 0

for i in range(0,len(W_corr_mast1_20241115_2130_2200_stow_z3)):
    if (U_corr_mast1_20241115_2130_2200_stow_z3[i]>0)&(W_corr_mast1_20241115_2130_2200_stow_z3[i]>0):
        Q1_mast1_20241115_2130_2200_stow_z3 += 1
        if (mast1_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            ejections_mast1_20241115_2130_2200_stow_z3 += 1
        elif (mast1_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            outward_interactions_mast1_20241115_2130_2200_stow_z3 += 1            
    elif (U_corr_mast1_20241115_2130_2200_stow_z3[i]<0)&(W_corr_mast1_20241115_2130_2200_stow_z3[i]>0):
        Q2_mast1_20241115_2130_2200_stow_z3 += 1
        if (mast1_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            ejections_mast1_20241115_2130_2200_stow_z3 += 1
        elif (mast1_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            outward_interactions_mast1_20241115_2130_2200_stow_z3 += 1 
    elif (U_corr_mast1_20241115_2130_2200_stow_z3[i]<0)&(W_corr_mast1_20241115_2130_2200_stow_z3[i]<0):
        Q3_mast1_20241115_2130_2200_stow_z3 += 1
        if (mast1_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            sweeps_mast1_20241115_2130_2200_stow_z3 += 1
        elif (mast1_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            inward_interactions_mast1_20241115_2130_2200_stow_z3 += 1 
    elif (U_corr_mast1_20241115_2130_2200_stow_z3[i]>0)&(W_corr_mast1_20241115_2130_2200_stow_z3[i]<0):
        Q4_mast1_20241115_2130_2200_stow_z3 += 1
        if (mast1_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            sweeps_mast1_20241115_2130_2200_stow_z3 += 1
        elif (mast1_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            inward_interactions_mast1_20241115_2130_2200_stow_z3 += 1 

S1_mast1_20241115_2130_2200_stow_z3 = 100*Q1_mast1_20241115_2130_2200_stow_z3/(Q1_mast1_20241115_2130_2200_stow_z3+Q2_mast1_20241115_2130_2200_stow_z3+Q3_mast1_20241115_2130_2200_stow_z3+Q4_mast1_20241115_2130_2200_stow_z3)
S2_mast1_20241115_2130_2200_stow_z3 = 100*Q2_mast1_20241115_2130_2200_stow_z3/(Q1_mast1_20241115_2130_2200_stow_z3+Q2_mast1_20241115_2130_2200_stow_z3+Q3_mast1_20241115_2130_2200_stow_z3+Q4_mast1_20241115_2130_2200_stow_z3)
S3_mast1_20241115_2130_2200_stow_z3 = 100*Q3_mast1_20241115_2130_2200_stow_z3/(Q1_mast1_20241115_2130_2200_stow_z3+Q2_mast1_20241115_2130_2200_stow_z3+Q3_mast1_20241115_2130_2200_stow_z3+Q4_mast1_20241115_2130_2200_stow_z3)
S4_mast1_20241115_2130_2200_stow_z3 = 100*Q4_mast1_20241115_2130_2200_stow_z3/(Q1_mast1_20241115_2130_2200_stow_z3+Q2_mast1_20241115_2130_2200_stow_z3+Q3_mast1_20241115_2130_2200_stow_z3+Q4_mast1_20241115_2130_2200_stow_z3)

S_ejections_mast1_20241115_2130_2200_stow_z3 = 100*ejections_mast1_20241115_2130_2200_stow_z3/(Q1_mast1_20241115_2130_2200_stow_z3+Q2_mast1_20241115_2130_2200_stow_z3+Q3_mast1_20241115_2130_2200_stow_z3+Q4_mast1_20241115_2130_2200_stow_z3)
S_outward_interactions_mast1_20241115_2130_2200_stow_z3 = 100*outward_interactions_mast1_20241115_2130_2200_stow_z3/(Q1_mast1_20241115_2130_2200_stow_z3+Q2_mast1_20241115_2130_2200_stow_z3+Q3_mast1_20241115_2130_2200_stow_z3+Q4_mast1_20241115_2130_2200_stow_z3)
S_sweeps_mast1_20241115_2130_2200_stow_z3 = 100*sweeps_mast1_20241115_2130_2200_stow_z3/(Q1_mast1_20241115_2130_2200_stow_z3+Q2_mast1_20241115_2130_2200_stow_z3+Q3_mast1_20241115_2130_2200_stow_z3+Q4_mast1_20241115_2130_2200_stow_z3)
S_inward_interactions_mast1_20241115_2130_2200_stow_z3 = 100*inward_interactions_mast1_20241115_2130_2200_stow_z3/(Q1_mast1_20241115_2130_2200_stow_z3+Q2_mast1_20241115_2130_2200_stow_z3+Q3_mast1_20241115_2130_2200_stow_z3+Q4_mast1_20241115_2130_2200_stow_z3)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S1_mast1_20241115_2130_2200_stow_z1,S1_mast1_20241115_2130_2200_stow_z2,S1_mast1_20241115_2130_2200_stow_z3],heights,marker='o',s=20, label='u+w+ (Q1)')    
plt.scatter([S2_mast1_20241115_2130_2200_stow_z1,S2_mast1_20241115_2130_2200_stow_z2,S2_mast1_20241115_2130_2200_stow_z3],heights,marker='s',s=20, label='u-w+ (Q2)')    
plt.scatter([S3_mast1_20241115_2130_2200_stow_z1,S3_mast1_20241115_2130_2200_stow_z2,S3_mast1_20241115_2130_2200_stow_z3],heights,marker='d',s=20, label='u-w- (Q3)')    
plt.scatter([S4_mast1_20241115_2130_2200_stow_z1,S4_mast1_20241115_2130_2200_stow_z2,S4_mast1_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='u+w- (Q4)')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 55)
plt.xticks([0,10,20,30,40,50])  
plt.ylim(0, 12)
plt.title('Stow mast1 (Nov 15, 2024)')    
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S_ejections_mast1_20241115_2130_2200_stow_z1,S_ejections_mast1_20241115_2130_2200_stow_z2,S_ejections_mast1_20241115_2130_2200_stow_z3],heights,marker='o',s=20, label='ejections')    
plt.scatter([S_outward_interactions_mast1_20241115_2130_2200_stow_z1,S_outward_interactions_mast1_20241115_2130_2200_stow_z2,S_outward_interactions_mast1_20241115_2130_2200_stow_z3],heights,marker='s',s=20, label='outward interactions')    
plt.scatter([S_sweeps_mast1_20241115_2130_2200_stow_z1,S_sweeps_mast1_20241115_2130_2200_stow_z2,S_sweeps_mast1_20241115_2130_2200_stow_z3],heights,marker='d',s=20, label='sweeps')    
plt.scatter([S_inward_interactions_mast1_20241115_2130_2200_stow_z1,S_inward_interactions_mast1_20241115_2130_2200_stow_z2,S_inward_interactions_mast1_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='inward interactions')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 100)
plt.ylim(0, 12)
plt.title('Stow mast1 (Nov 15, 2024)')     
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()




#%% Quadrant analysis (mast3 Nov 15, 2024)

Q1_mast3_20241115_2130_2200_stow_z1 = Q2_mast3_20241115_2130_2200_stow_z1 = Q3_mast3_20241115_2130_2200_stow_z1 = Q4_mast3_20241115_2130_2200_stow_z1 = 0
ejections_mast3_20241115_2130_2200_stow_z1 = outward_interactions_mast3_20241115_2130_2200_stow_z1 = sweeps_mast3_20241115_2130_2200_stow_z1 = inward_interactions_mast3_20241115_2130_2200_stow_z1 = 0

for i in range(0,len(W_corr_mast3_20241115_2130_2200_stow_z1)):
    if (U_corr_mast3_20241115_2130_2200_stow_z1[i]>0)&(W_corr_mast3_20241115_2130_2200_stow_z1[i]>0):
        Q1_mast3_20241115_2130_2200_stow_z1 += 1
        if (mast3_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            ejections_mast3_20241115_2130_2200_stow_z1 += 1
        elif (mast3_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            outward_interactions_mast3_20241115_2130_2200_stow_z1 += 1            
    elif (U_corr_mast3_20241115_2130_2200_stow_z1[i]>0)&(W_corr_mast3_20241115_2130_2200_stow_z1[i]<0):
        Q2_mast3_20241115_2130_2200_stow_z1 += 1
        if (mast3_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            sweeps_mast3_20241115_2130_2200_stow_z1 += 1
        elif (mast3_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            inward_interactions_mast3_20241115_2130_2200_stow_z1 += 1 
    elif (U_corr_mast3_20241115_2130_2200_stow_z1[i]<0)&(W_corr_mast3_20241115_2130_2200_stow_z1[i]<0):
        Q3_mast3_20241115_2130_2200_stow_z1 += 1
        if (mast3_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            sweeps_mast3_20241115_2130_2200_stow_z1 += 1
        elif (mast3_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            inward_interactions_mast3_20241115_2130_2200_stow_z1 += 1 
    elif (U_corr_mast3_20241115_2130_2200_stow_z1[i]<0)&(W_corr_mast3_20241115_2130_2200_stow_z1[i]>0):
        Q2_mast3_20241115_2130_2200_stow_z1 += 1
        if (mast3_uprimewprime_z1_20241115_2130_2200_stow[i]<0):
            ejections_mast3_20241115_2130_2200_stow_z1 += 1
        elif (mast3_uprimewprime_z1_20241115_2130_2200_stow[i]>0):
            outward_interactions_mast3_20241115_2130_2200_stow_z1 += 1 


S1_mast3_20241115_2130_2200_stow_z1 = 100*Q1_mast3_20241115_2130_2200_stow_z1/(Q1_mast3_20241115_2130_2200_stow_z1+Q2_mast3_20241115_2130_2200_stow_z1+Q3_mast3_20241115_2130_2200_stow_z1+Q4_mast3_20241115_2130_2200_stow_z1)
S2_mast3_20241115_2130_2200_stow_z1 = 100*Q2_mast3_20241115_2130_2200_stow_z1/(Q1_mast3_20241115_2130_2200_stow_z1+Q2_mast3_20241115_2130_2200_stow_z1+Q3_mast3_20241115_2130_2200_stow_z1+Q4_mast3_20241115_2130_2200_stow_z1)
S3_mast3_20241115_2130_2200_stow_z1 = 100*Q3_mast3_20241115_2130_2200_stow_z1/(Q1_mast3_20241115_2130_2200_stow_z1+Q2_mast3_20241115_2130_2200_stow_z1+Q3_mast3_20241115_2130_2200_stow_z1+Q4_mast3_20241115_2130_2200_stow_z1)
S4_mast3_20241115_2130_2200_stow_z1 = 100*Q4_mast3_20241115_2130_2200_stow_z1/(Q1_mast3_20241115_2130_2200_stow_z1+Q2_mast3_20241115_2130_2200_stow_z1+Q3_mast3_20241115_2130_2200_stow_z1+Q4_mast3_20241115_2130_2200_stow_z1)

S_ejections_mast3_20241115_2130_2200_stow_z1 = 100*ejections_mast3_20241115_2130_2200_stow_z1/(Q1_mast3_20241115_2130_2200_stow_z1+Q2_mast3_20241115_2130_2200_stow_z1+Q3_mast3_20241115_2130_2200_stow_z1+Q4_mast3_20241115_2130_2200_stow_z1)
S_outward_interactions_mast3_20241115_2130_2200_stow_z1 = 100*outward_interactions_mast3_20241115_2130_2200_stow_z1/(Q1_mast3_20241115_2130_2200_stow_z1+Q2_mast3_20241115_2130_2200_stow_z1+Q3_mast3_20241115_2130_2200_stow_z1+Q4_mast3_20241115_2130_2200_stow_z1)
S_sweeps_mast3_20241115_2130_2200_stow_z1 = 100*sweeps_mast3_20241115_2130_2200_stow_z1/(Q1_mast3_20241115_2130_2200_stow_z1+Q2_mast3_20241115_2130_2200_stow_z1+Q3_mast3_20241115_2130_2200_stow_z1+Q4_mast3_20241115_2130_2200_stow_z1)
S_inward_interactions_mast3_20241115_2130_2200_stow_z1 = 100*inward_interactions_mast3_20241115_2130_2200_stow_z1/(Q1_mast3_20241115_2130_2200_stow_z1+Q2_mast3_20241115_2130_2200_stow_z1+Q3_mast3_20241115_2130_2200_stow_z1+Q4_mast3_20241115_2130_2200_stow_z1)


Q1_mast3_20241115_2130_2200_stow_z2 = Q2_mast3_20241115_2130_2200_stow_z2 = Q3_mast3_20241115_2130_2200_stow_z2 = Q4_mast3_20241115_2130_2200_stow_z2 = 0
ejections_mast3_20241115_2130_2200_stow_z2 = outward_interactions_mast3_20241115_2130_2200_stow_z2 = sweeps_mast3_20241115_2130_2200_stow_z2 = inward_interactions_mast3_20241115_2130_2200_stow_z2 = 0

for i in range(0,len(W_corr_mast3_20241115_2130_2200_stow_z2)):
    if (U_corr_mast3_20241115_2130_2200_stow_z2[i]>0)&(W_corr_mast3_20241115_2130_2200_stow_z2[i]>0):
        Q1_mast3_20241115_2130_2200_stow_z2 += 1
        if (mast3_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            ejections_mast3_20241115_2130_2200_stow_z2 += 1
        elif (mast3_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            outward_interactions_mast3_20241115_2130_2200_stow_z2 += 1            
    elif (U_corr_mast3_20241115_2130_2200_stow_z2[i]<0)&(W_corr_mast3_20241115_2130_2200_stow_z2[i]>0):
        Q2_mast3_20241115_2130_2200_stow_z2 += 1
        if (mast3_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            ejections_mast3_20241115_2130_2200_stow_z2 += 1
        elif (mast3_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            outward_interactions_mast3_20241115_2130_2200_stow_z2 += 1 
    elif (U_corr_mast3_20241115_2130_2200_stow_z2[i]<0)&(W_corr_mast3_20241115_2130_2200_stow_z2[i]<0):
        Q3_mast3_20241115_2130_2200_stow_z2 += 1
        if (mast3_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            sweeps_mast3_20241115_2130_2200_stow_z2 += 1
        elif (mast3_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            inward_interactions_mast3_20241115_2130_2200_stow_z2 += 1 
    elif (U_corr_mast3_20241115_2130_2200_stow_z2[i]>0)&(W_corr_mast3_20241115_2130_2200_stow_z2[i]<0):
        Q4_mast3_20241115_2130_2200_stow_z2 += 1
        if (mast3_uprimewprime_z2_20241115_2130_2200_stow[i]<0):
            sweeps_mast3_20241115_2130_2200_stow_z2 += 1
        elif (mast3_uprimewprime_z2_20241115_2130_2200_stow[i]>0):
            inward_interactions_mast3_20241115_2130_2200_stow_z2 += 1 

S1_mast3_20241115_2130_2200_stow_z2 = 100*Q1_mast3_20241115_2130_2200_stow_z2/(Q1_mast3_20241115_2130_2200_stow_z2+Q2_mast3_20241115_2130_2200_stow_z2+Q3_mast3_20241115_2130_2200_stow_z2+Q4_mast3_20241115_2130_2200_stow_z2)
S2_mast3_20241115_2130_2200_stow_z2 = 100*Q2_mast3_20241115_2130_2200_stow_z2/(Q1_mast3_20241115_2130_2200_stow_z2+Q2_mast3_20241115_2130_2200_stow_z2+Q3_mast3_20241115_2130_2200_stow_z2+Q4_mast3_20241115_2130_2200_stow_z2)
S3_mast3_20241115_2130_2200_stow_z2 = 100*Q3_mast3_20241115_2130_2200_stow_z2/(Q1_mast3_20241115_2130_2200_stow_z2+Q2_mast3_20241115_2130_2200_stow_z2+Q3_mast3_20241115_2130_2200_stow_z2+Q4_mast3_20241115_2130_2200_stow_z2)
S4_mast3_20241115_2130_2200_stow_z2 = 100*Q4_mast3_20241115_2130_2200_stow_z2/(Q1_mast3_20241115_2130_2200_stow_z2+Q2_mast3_20241115_2130_2200_stow_z2+Q3_mast3_20241115_2130_2200_stow_z2+Q4_mast3_20241115_2130_2200_stow_z2)

S_ejections_mast3_20241115_2130_2200_stow_z2 = 100*ejections_mast3_20241115_2130_2200_stow_z2/(Q1_mast3_20241115_2130_2200_stow_z2+Q2_mast3_20241115_2130_2200_stow_z2+Q3_mast3_20241115_2130_2200_stow_z2+Q4_mast3_20241115_2130_2200_stow_z2)
S_outward_interactions_mast3_20241115_2130_2200_stow_z2 = 100*outward_interactions_mast3_20241115_2130_2200_stow_z2/(Q1_mast3_20241115_2130_2200_stow_z2+Q2_mast3_20241115_2130_2200_stow_z2+Q3_mast3_20241115_2130_2200_stow_z2+Q4_mast3_20241115_2130_2200_stow_z2)
S_sweeps_mast3_20241115_2130_2200_stow_z2 = 100*sweeps_mast3_20241115_2130_2200_stow_z2/(Q1_mast3_20241115_2130_2200_stow_z2+Q2_mast3_20241115_2130_2200_stow_z2+Q3_mast3_20241115_2130_2200_stow_z2+Q4_mast3_20241115_2130_2200_stow_z2)
S_inward_interactions_mast3_20241115_2130_2200_stow_z2 = 100*inward_interactions_mast3_20241115_2130_2200_stow_z2/(Q1_mast3_20241115_2130_2200_stow_z2+Q2_mast3_20241115_2130_2200_stow_z2+Q3_mast3_20241115_2130_2200_stow_z2+Q4_mast3_20241115_2130_2200_stow_z2)


Q1_mast3_20241115_2130_2200_stow_z3 = Q2_mast3_20241115_2130_2200_stow_z3 = Q3_mast3_20241115_2130_2200_stow_z3 = Q4_mast3_20241115_2130_2200_stow_z3 = 0
ejections_mast3_20241115_2130_2200_stow_z3 = outward_interactions_mast3_20241115_2130_2200_stow_z3 = sweeps_mast3_20241115_2130_2200_stow_z3 = inward_interactions_mast3_20241115_2130_2200_stow_z3 = 0

for i in range(0,len(W_corr_mast3_20241115_2130_2200_stow_z3)):
    if (U_corr_mast3_20241115_2130_2200_stow_z3[i]>0)&(W_corr_mast3_20241115_2130_2200_stow_z3[i]>0):
        Q1_mast3_20241115_2130_2200_stow_z3 += 1
        if (mast3_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            ejections_mast3_20241115_2130_2200_stow_z3 += 1
        elif (mast3_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            outward_interactions_mast3_20241115_2130_2200_stow_z3 += 1            
    elif (U_corr_mast3_20241115_2130_2200_stow_z3[i]<0)&(W_corr_mast3_20241115_2130_2200_stow_z3[i]>0):
        Q2_mast3_20241115_2130_2200_stow_z3 += 1
        if (mast3_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            ejections_mast3_20241115_2130_2200_stow_z3 += 1
        elif (mast3_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            outward_interactions_mast3_20241115_2130_2200_stow_z3 += 1 
    elif (U_corr_mast3_20241115_2130_2200_stow_z3[i]<0)&(W_corr_mast3_20241115_2130_2200_stow_z3[i]<0):
        Q3_mast3_20241115_2130_2200_stow_z3 += 1
        if (mast3_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            sweeps_mast3_20241115_2130_2200_stow_z3 += 1
        elif (mast3_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            inward_interactions_mast3_20241115_2130_2200_stow_z3 += 1 
    elif (U_corr_mast3_20241115_2130_2200_stow_z3[i]>0)&(W_corr_mast3_20241115_2130_2200_stow_z3[i]<0):
        Q4_mast3_20241115_2130_2200_stow_z3 += 1
        if (mast3_uprimewprime_z3_20241115_2130_2200_stow[i]<0):
            sweeps_mast3_20241115_2130_2200_stow_z3 += 1
        elif (mast3_uprimewprime_z3_20241115_2130_2200_stow[i]>0):
            inward_interactions_mast3_20241115_2130_2200_stow_z3 += 1 

S1_mast3_20241115_2130_2200_stow_z3 = 100*Q1_mast3_20241115_2130_2200_stow_z3/(Q1_mast3_20241115_2130_2200_stow_z3+Q2_mast3_20241115_2130_2200_stow_z3+Q3_mast3_20241115_2130_2200_stow_z3+Q4_mast3_20241115_2130_2200_stow_z3)
S2_mast3_20241115_2130_2200_stow_z3 = 100*Q2_mast3_20241115_2130_2200_stow_z3/(Q1_mast3_20241115_2130_2200_stow_z3+Q2_mast3_20241115_2130_2200_stow_z3+Q3_mast3_20241115_2130_2200_stow_z3+Q4_mast3_20241115_2130_2200_stow_z3)
S3_mast3_20241115_2130_2200_stow_z3 = 100*Q3_mast3_20241115_2130_2200_stow_z3/(Q1_mast3_20241115_2130_2200_stow_z3+Q2_mast3_20241115_2130_2200_stow_z3+Q3_mast3_20241115_2130_2200_stow_z3+Q4_mast3_20241115_2130_2200_stow_z3)
S4_mast3_20241115_2130_2200_stow_z3 = 100*Q4_mast3_20241115_2130_2200_stow_z3/(Q1_mast3_20241115_2130_2200_stow_z3+Q2_mast3_20241115_2130_2200_stow_z3+Q3_mast3_20241115_2130_2200_stow_z3+Q4_mast3_20241115_2130_2200_stow_z3)

S_ejections_mast3_20241115_2130_2200_stow_z3 = 100*ejections_mast3_20241115_2130_2200_stow_z3/(Q1_mast3_20241115_2130_2200_stow_z3+Q2_mast3_20241115_2130_2200_stow_z3+Q3_mast3_20241115_2130_2200_stow_z3+Q4_mast3_20241115_2130_2200_stow_z3)
S_outward_interactions_mast3_20241115_2130_2200_stow_z3 = 100*outward_interactions_mast3_20241115_2130_2200_stow_z3/(Q1_mast3_20241115_2130_2200_stow_z3+Q2_mast3_20241115_2130_2200_stow_z3+Q3_mast3_20241115_2130_2200_stow_z3+Q4_mast3_20241115_2130_2200_stow_z3)
S_sweeps_mast3_20241115_2130_2200_stow_z3 = 100*sweeps_mast3_20241115_2130_2200_stow_z3/(Q1_mast3_20241115_2130_2200_stow_z3+Q2_mast3_20241115_2130_2200_stow_z3+Q3_mast3_20241115_2130_2200_stow_z3+Q4_mast3_20241115_2130_2200_stow_z3)
S_inward_interactions_mast3_20241115_2130_2200_stow_z3 = 100*inward_interactions_mast3_20241115_2130_2200_stow_z3/(Q1_mast3_20241115_2130_2200_stow_z3+Q2_mast3_20241115_2130_2200_stow_z3+Q3_mast3_20241115_2130_2200_stow_z3+Q4_mast3_20241115_2130_2200_stow_z3)


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S1_mast3_20241115_2130_2200_stow_z1,S1_mast3_20241115_2130_2200_stow_z2,S1_mast3_20241115_2130_2200_stow_z3],heights,marker='o',s=20, label='u+w+ (Q1)')    
plt.scatter([S2_mast3_20241115_2130_2200_stow_z1,S2_mast3_20241115_2130_2200_stow_z2,S2_mast3_20241115_2130_2200_stow_z3],heights,marker='s',s=20, label='u-w+ (Q2)')    
plt.scatter([S3_mast3_20241115_2130_2200_stow_z1,S3_mast3_20241115_2130_2200_stow_z2,S3_mast3_20241115_2130_2200_stow_z3],heights,marker='d',s=20, label='u-w- (Q3)')    
plt.scatter([S4_mast3_20241115_2130_2200_stow_z1,S4_mast3_20241115_2130_2200_stow_z2,S4_mast3_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='u+w- (Q4)')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 55)
plt.xticks([0,10,20,30,40,50])  
plt.ylim(0, 12)
plt.title('Stow mast3 (Nov 15, 2024)')    
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S_ejections_mast3_20241115_2130_2200_stow_z1,S_ejections_mast3_20241115_2130_2200_stow_z2,S_ejections_mast3_20241115_2130_2200_stow_z3],heights,marker='o',s=20, label='ejections')    
plt.scatter([S_outward_interactions_mast3_20241115_2130_2200_stow_z1,S_outward_interactions_mast3_20241115_2130_2200_stow_z2,S_outward_interactions_mast3_20241115_2130_2200_stow_z3],heights,marker='s',s=20, label='outward interactions')    
plt.scatter([S_sweeps_mast3_20241115_2130_2200_stow_z1,S_sweeps_mast3_20241115_2130_2200_stow_z2,S_sweeps_mast3_20241115_2130_2200_stow_z3],heights,marker='d',s=20, label='sweeps')    
plt.scatter([S_inward_interactions_mast3_20241115_2130_2200_stow_z1,S_inward_interactions_mast3_20241115_2130_2200_stow_z2,S_inward_interactions_mast3_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='inward interactions')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 100)
plt.ylim(0, 12)
plt.title('Stow mast3 (Nov 15, 2024)')     
plt.xlabel("Momentum flux statistics (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S4_inflow_20241115_2130_2200_stow_z1,S4_inflow_20241115_2130_2200_stow_z2,S4_inflow_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='inflow')    
plt.scatter([S4_mast1_20241115_2130_2200_stow_z1,S4_mast1_20241115_2130_2200_stow_z2,S4_mast1_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='mast1')    
plt.scatter([S4_mast3_20241115_2130_2200_stow_z1,S3_mast3_20241115_2130_2200_stow_z2,S3_mast3_20241115_2130_2200_stow_z3],heights,marker='d',s=20, label='mast3')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 65)
plt.xticks([0,10,20,30,40,50,60])  
plt.ylim(0, 12)
plt.title('Stow (Nov 15, 2024)')    
plt.xlabel("Sweeps (%)")
plt.ylabel("Height (m)")
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter([S2_inflow_20241115_2130_2200_stow_z1,S2_inflow_20241115_2130_2200_stow_z2,S2_inflow_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='inflow')    
plt.scatter([S2_mast1_20241115_2130_2200_stow_z1,S2_mast1_20241115_2130_2200_stow_z2,S2_mast1_20241115_2130_2200_stow_z3],heights,marker='v',s=20, label='mast1')    
plt.scatter([S2_mast3_20241115_2130_2200_stow_z1,S3_mast3_20241115_2130_2200_stow_z2,S3_mast3_20241115_2130_2200_stow_z3],heights,marker='d',s=20, label='mast3')    
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left', fontsize=8, borderaxespad=0.)
plt.xlim(0, 65)
plt.xticks([0,10,20,30,40,50,60])  
plt.ylim(0, 12)
plt.title('Stow (Nov 15, 2024)')    
plt.xlabel("Ejections (%)")
plt.ylabel("Height (m)")
plt.show()


#%% PSD analysis

heights = [2.75,5.5,11] 
fs = 20

# Spectra
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from numpy import hanning
import math

overlap = 0
nblock = len(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_inflow_20Hz_20241118_1840_1900_stow_z1, Pxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = welch(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = fu_loads_inflow_20Hz_20241118_1840_1900_stow_z1*heights[0]/H1_U_ax_20241118_1840_1900_stow_z1
nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = (fu_loads_inflow_20Hz_20241118_1840_1900_stow_z1*Pxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1)/loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.std()**2

fu_loads_inflow_20Hz_20241118_1840_1900_stow_z2, Pxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = welch(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = fu_loads_inflow_20Hz_20241118_1840_1900_stow_z2*heights[1]/H1_U_ax_20241118_1840_1900_stow_z2
nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = (fu_loads_inflow_20Hz_20241118_1840_1900_stow_z2*Pxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2)/loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.std()**2
 
fu_loads_inflow_20Hz_20241118_1840_1900_stow_z3, Pxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = welch(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = fu_loads_inflow_20Hz_20241118_1840_1900_stow_z3*heights[2]/H1_U_ax_20241118_1840_1900_stow_z3
nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = (fu_loads_inflow_20Hz_20241118_1840_1900_stow_z3*Pxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3)/loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.std()**2              
    
fw_loads_inflow_20Hz_20241118_1840_1900_stow_z1, Pxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = welch(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = fw_loads_inflow_20Hz_20241118_1840_1900_stow_z1*heights[0]/H1_W_ax_20241118_1840_1900_stow_z1
nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = (fw_loads_inflow_20Hz_20241118_1840_1900_stow_z1*Pxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1)/loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.std()**2

fw_loads_inflow_20Hz_20241118_1840_1900_stow_z2, Pxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = welch(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = fw_loads_inflow_20Hz_20241118_1840_1900_stow_z2*heights[1]/H1_W_ax_20241118_1840_1900_stow_z2
nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = (fw_loads_inflow_20Hz_20241118_1840_1900_stow_z2*Pxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2)/loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.std()**2
 
fw_loads_inflow_20Hz_20241118_1840_1900_stow_z3, Pxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = welch(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = fw_loads_inflow_20Hz_20241118_1840_1900_stow_z3*heights[2]/H1_W_ax_20241118_1840_1900_stow_z3
nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = (fw_loads_inflow_20Hz_20241118_1840_1900_stow_z3*Pxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3)/loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = list(np.where([abs(nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1[index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z1[0][0]:len(nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1)]
nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z1,200)
nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = [nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1[0:index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z1[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z1]

index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = list(np.where([abs(nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2[index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z2[0][0]:len(nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2)]
nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z2,200)
nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = [nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2[0:index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z2[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z2]

index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = list(np.where([abs(nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3[index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z3[0][0]:len(nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3)]
nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z3,200)
nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = [nPxxfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3[0:index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z3[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z3]

index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = list(np.where([abs(nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1[index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z1[0][0]:len(nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1)]
nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z1,200)
nPxxfw_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z1 = [nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1[0:index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z1[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z1]

index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = list(np.where([abs(nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2[index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z2[0][0]:len(nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2)]
nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z2,200)
nPxxfw_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z2 = [nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2[0:index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z2[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z2]

index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = list(np.where([abs(nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3[index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z3[0][0]:len(nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3)]
nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z3,200)
nPxxfw_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z3 = [nPxxfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3[0:index_highfreq_loads_inflow_20Hz_20241118_1840_1900_stow_z3[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241118_1840_1900_stow_z3]


plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z1[0:len(nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z2[0:len(nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241118_1840_1900_stow_z3[0:len(nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('inflow')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z1[0:len(nPxxfw_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z2[0:len(nPxxfw_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241118_1840_1900_stow_z3[0:len(nPxxfw_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241118_1840_1900_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('inflow')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()


#%% Extract data by height

U_corr_inflow_20241118_1840_1900_stow_z1 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low)
U_corr_inflow_20241118_1840_1900_stow_z2 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid)
U_corr_inflow_20241118_1840_1900_stow_z3 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top)

V_corr_inflow_20241118_1840_1900_stow_z1 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.V_ax_Low)
V_corr_inflow_20241118_1840_1900_stow_z2 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.V_ax_Mid)
V_corr_inflow_20241118_1840_1900_stow_z3 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.V_ax_Top)

W_corr_inflow_20241118_1840_1900_stow_z1 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low)
W_corr_inflow_20241118_1840_1900_stow_z2 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid)
W_corr_inflow_20241118_1840_1900_stow_z3 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top)

Ts_corr_inflow_20241118_1840_1900_stow_z1 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.Ts_Low)
Ts_corr_inflow_20241118_1840_1900_stow_z2 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.Ts_Mid)
Ts_corr_inflow_20241118_1840_1900_stow_z3 = pd.Series(loads_inflow_20Hz_20241118_1840_1900_stow.Ts_Top)

# Detrend
U_corr_inflow_20241118_1840_1900_stow_z1[U_corr_inflow_20241118_1840_1900_stow_z1.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241118_1840_1900_stow_z1.dropna()) 
U_corr_inflow_20241118_1840_1900_stow_z2[U_corr_inflow_20241118_1840_1900_stow_z2.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241118_1840_1900_stow_z2.dropna()) 
U_corr_inflow_20241118_1840_1900_stow_z3[U_corr_inflow_20241118_1840_1900_stow_z3.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241118_1840_1900_stow_z3.dropna()) 

V_corr_inflow_20241118_1840_1900_stow_z1[V_corr_inflow_20241118_1840_1900_stow_z1.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241118_1840_1900_stow_z1.dropna()) 
V_corr_inflow_20241118_1840_1900_stow_z2[V_corr_inflow_20241118_1840_1900_stow_z2.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241118_1840_1900_stow_z2.dropna()) 
V_corr_inflow_20241118_1840_1900_stow_z3[V_corr_inflow_20241118_1840_1900_stow_z3.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241118_1840_1900_stow_z3.dropna()) 

W_corr_inflow_20241118_1840_1900_stow_z1[W_corr_inflow_20241118_1840_1900_stow_z1.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241118_1840_1900_stow_z1.dropna()) 
W_corr_inflow_20241118_1840_1900_stow_z2[W_corr_inflow_20241118_1840_1900_stow_z2.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241118_1840_1900_stow_z2.dropna()) 
W_corr_inflow_20241118_1840_1900_stow_z3[W_corr_inflow_20241118_1840_1900_stow_z3.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241118_1840_1900_stow_z3.dropna()) 

Ts_corr_inflow_20241118_1840_1900_stow_z1[Ts_corr_inflow_20241118_1840_1900_stow_z1.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241118_1840_1900_stow_z1.dropna()) 
Ts_corr_inflow_20241118_1840_1900_stow_z2[Ts_corr_inflow_20241118_1840_1900_stow_z2.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241118_1840_1900_stow_z2.dropna()) 
Ts_corr_inflow_20241118_1840_1900_stow_z3[Ts_corr_inflow_20241118_1840_1900_stow_z3.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241118_1840_1900_stow_z3.dropna()) 

# Reynolds stresses and length scales (south2)

inflow_uv_z1_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z1*V_corr_inflow_20241118_1840_1900_stow_z1).mean()-(U_corr_inflow_20241118_1840_1900_stow_z1.mean()*V_corr_inflow_20241118_1840_1900_stow_z1.mean());
inflow_vw_z1_20241118_1840_1900_stow = (V_corr_inflow_20241118_1840_1900_stow_z1*W_corr_inflow_20241118_1840_1900_stow_z1).mean()-(V_corr_inflow_20241118_1840_1900_stow_z1.mean()*W_corr_inflow_20241118_1840_1900_stow_z1.mean());
inflow_uw_z1_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z1*W_corr_inflow_20241118_1840_1900_stow_z1).mean()-(U_corr_inflow_20241118_1840_1900_stow_z1.mean()*W_corr_inflow_20241118_1840_1900_stow_z1.mean());
inflow_wT_z1_20241118_1840_1900_stow = (W_corr_inflow_20241118_1840_1900_stow_z1*Ts_corr_inflow_20241118_1840_1900_stow_z1).mean()-(W_corr_inflow_20241118_1840_1900_stow_z1.mean()*Ts_corr_inflow_20241118_1840_1900_stow_z1.mean());

inflow_uv_z2_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z2*V_corr_inflow_20241118_1840_1900_stow_z2).mean()-(U_corr_inflow_20241118_1840_1900_stow_z2.mean()*V_corr_inflow_20241118_1840_1900_stow_z2.mean());
inflow_vw_z2_20241118_1840_1900_stow = (V_corr_inflow_20241118_1840_1900_stow_z2*W_corr_inflow_20241118_1840_1900_stow_z2).mean()-(V_corr_inflow_20241118_1840_1900_stow_z2.mean()*W_corr_inflow_20241118_1840_1900_stow_z2.mean());
inflow_uw_z2_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z2*W_corr_inflow_20241118_1840_1900_stow_z2).mean()-(U_corr_inflow_20241118_1840_1900_stow_z2.mean()*W_corr_inflow_20241118_1840_1900_stow_z2.mean());
inflow_wT_z2_20241118_1840_1900_stow = (W_corr_inflow_20241118_1840_1900_stow_z2*Ts_corr_inflow_20241118_1840_1900_stow_z2).mean()-(W_corr_inflow_20241118_1840_1900_stow_z2.mean()*Ts_corr_inflow_20241118_1840_1900_stow_z2.mean());

inflow_uv_z3_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z3*V_corr_inflow_20241118_1840_1900_stow_z3).mean()-(U_corr_inflow_20241118_1840_1900_stow_z3.mean()*V_corr_inflow_20241118_1840_1900_stow_z3.mean());
inflow_vw_z3_20241118_1840_1900_stow = (V_corr_inflow_20241118_1840_1900_stow_z3*W_corr_inflow_20241118_1840_1900_stow_z3).mean()-(V_corr_inflow_20241118_1840_1900_stow_z3.mean()*W_corr_inflow_20241118_1840_1900_stow_z3.mean());
inflow_uw_z3_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z3*W_corr_inflow_20241118_1840_1900_stow_z3).mean()-(U_corr_inflow_20241118_1840_1900_stow_z3.mean()*W_corr_inflow_20241118_1840_1900_stow_z3.mean());
inflow_wT_z3_20241118_1840_1900_stow = (W_corr_inflow_20241118_1840_1900_stow_z3*Ts_corr_inflow_20241118_1840_1900_stow_z3).mean()-(W_corr_inflow_20241118_1840_1900_stow_z3.mean()*Ts_corr_inflow_20241118_1840_1900_stow_z3.mean());

utau_z1_20241118_1840_1900_stow = (inflow_uw_z1_20241118_1840_1900_stow**2+inflow_vw_z1_20241118_1840_1900_stow**2)**(1/4) 
utau_z2_20241118_1840_1900_stow = (inflow_uw_z2_20241118_1840_1900_stow**2+inflow_vw_z2_20241118_1840_1900_stow**2)**(1/4) 
utau_z3_20241118_1840_1900_stow = (inflow_uw_z3_20241118_1840_1900_stow**2+inflow_vw_z3_20241118_1840_1900_stow**2)**(1/4) 

L_z1_20241118_1840_1900_stow = -1*(utau_z1_20241118_1840_1900_stow**3)/(0.4*(9.81/H1_Ts_20241118_1840_1900_stow_z1)*inflow_wT_z1_20241118_1840_1900_stow)
L_z2_20241118_1840_1900_stow = -1*(utau_z2_20241118_1840_1900_stow**3)/(0.4*(9.81/H1_Ts_20241118_1840_1900_stow_z2)*inflow_wT_z2_20241118_1840_1900_stow)
L_z3_20241118_1840_1900_stow = -1*(utau_z3_20241118_1840_1900_stow**3)/(0.4*(9.81/H1_Ts_20241118_1840_1900_stow_z3)*inflow_wT_z3_20241118_1840_1900_stow)

zL_z1_20241118_1840_1900_stow = heights[0]/L_z1_20241118_1840_1900_stow
zL_z2_20241118_1840_1900_stow = heights[1]/L_z2_20241118_1840_1900_stow
zL_z3_20241118_1840_1900_stow = heights[2]/L_z3_20241118_1840_1900_stow

inflow_uprimewprime_z1_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z1*W_corr_inflow_20241118_1840_1900_stow_z1);
inflow_uprimewprime_z2_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z2*W_corr_inflow_20241118_1840_1900_stow_z2);
inflow_uprimewprime_z3_20241118_1840_1900_stow = (U_corr_inflow_20241118_1840_1900_stow_z3*W_corr_inflow_20241118_1840_1900_stow_z3);


#%% LS exponential fit method

autocorr_inflow_20241118_1840_1900_stow = np.correlate(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241118_1840_1900_stow_z1)
Lux_20241118_1840_1900_stow_z1 = Lux_20241118_1840_1900_stow_z1[Lux_20241118_1840_1900_stow_z1>0]

autocorr_inflow_20241118_1840_1900_stow = np.correlate(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241118_1840_1900_stow_z2)
Lux_20241118_1840_1900_stow_z2 = Lux_20241118_1840_1900_stow_z2[Lux_20241118_1840_1900_stow_z2>0]

autocorr_inflow_20241118_1840_1900_stow = np.correlate(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241118_1840_1900_stow.U_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241118_1840_1900_stow_z3)
Lux_20241118_1840_1900_stow_z3 = Lux_20241118_1840_1900_stow_z3[Lux_20241118_1840_1900_stow_z3>0]

autocorr_inflow_20241118_1840_1900_stow = np.correlate(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241118_1840_1900_stow_z1)
Lwx_20241118_1840_1900_stow_z1 = Lwx_20241118_1840_1900_stow_z1[Lwx_20241118_1840_1900_stow_z1>0]

autocorr_inflow_20241118_1840_1900_stow = np.correlate(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241118_1840_1900_stow_z2)
Lwx_20241118_1840_1900_stow_z2 = Lwx_20241118_1840_1900_stow_z2[Lwx_20241118_1840_1900_stow_z2>0]

autocorr_inflow_20241118_1840_1900_stow = np.correlate(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241118_1840_1900_stow.W_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241118_1840_1900_stow_z3)
Lwx_20241118_1840_1900_stow_z3 = Lwx_20241118_1840_1900_stow_z3[Lwx_20241118_1840_1900_stow_z3>0]

Lux_profile_inflow_20241118_1840_1900_stow = pd.Series([Lux_20241118_1840_1900_stow_z1,Lux_20241118_1840_1900_stow_z2,Lux_20241118_1840_1900_stow_z3])
Lwx_profile_inflow_20241118_1840_1900_stow = pd.Series([Lwx_20241118_1840_1900_stow_z1,Lwx_20241118_1840_1900_stow_z2,Lwx_20241118_1840_1900_stow_z3])
 


#%% Mast 1

overlap = 0
nblock = len(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast1_20Hz_20241118_1840_1900_stow_z1, Pxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1 = fu_loads_mast1_20Hz_20241118_1840_1900_stow_z1*heights[0]/H2_U_ax_20241118_1840_1900_stow_z1
nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1 = (fu_loads_mast1_20Hz_20241118_1840_1900_stow_z1*Pxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1)/loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.std()**2

fu_loads_mast1_20Hz_20241118_1840_1900_stow_z2, Pxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2 = fu_loads_mast1_20Hz_20241118_1840_1900_stow_z2*heights[1]/H2_U_ax_20241118_1840_1900_stow_z2
nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2 = (fu_loads_mast1_20Hz_20241118_1840_1900_stow_z2*Pxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2)/loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.std()**2
 
fu_loads_mast1_20Hz_20241118_1840_1900_stow_z3, Pxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3 = fu_loads_mast1_20Hz_20241118_1840_1900_stow_z3*heights[2]/H2_U_ax_20241118_1840_1900_stow_z3
nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3 = (fu_loads_mast1_20Hz_20241118_1840_1900_stow_z3*Pxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3)/loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.std()**2              
    
fw_loads_mast1_20Hz_20241118_1840_1900_stow_z1, Pxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1 = fw_loads_mast1_20Hz_20241118_1840_1900_stow_z1*heights[0]/H2_W_ax_20241118_1840_1900_stow_z1
nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1 = (fw_loads_mast1_20Hz_20241118_1840_1900_stow_z1*Pxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1)/loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.std()**2

fw_loads_mast1_20Hz_20241118_1840_1900_stow_z2, Pxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2 = fw_loads_mast1_20Hz_20241118_1840_1900_stow_z2*heights[1]/H2_W_ax_20241118_1840_1900_stow_z2
nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2 = (fw_loads_mast1_20Hz_20241118_1840_1900_stow_z2*Pxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2)/loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.std()**2
 
fw_loads_mast1_20Hz_20241118_1840_1900_stow_z3, Pxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3 = fw_loads_mast1_20Hz_20241118_1840_1900_stow_z3*heights[2]/H2_W_ax_20241118_1840_1900_stow_z3
nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3 = (fw_loads_mast1_20Hz_20241118_1840_1900_stow_z3*Pxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3)/loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.std()**2              



#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1 = list(np.where([abs(nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1 = nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1[0][0]:len(nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1 = [nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2 = list(np.where([abs(nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2 = nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2[0][0]:len(nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2 = [nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3 = list(np.where([abs(nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3 = nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3[0][0]:len(nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3 = [nPxxfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1 = list(np.where([abs(nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1 = nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1[0][0]:len(nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1 = [nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2 = list(np.where([abs(nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2 = nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2[0][0]:len(nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2 = [nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3 = list(np.where([abs(nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3 = nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3[0][0]:len(nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3 = [nPxxfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241118_1840_1900_stow_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast1')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241118_1840_1900_stow_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast1')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()



#%% LS exponential fit method

autocorr_mast1_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241118_1840_1900_stow_z1)
Lux_mast1_20241118_1840_1900_stow_z1 = Lux_20241118_1840_1900_stow_z1[Lux_20241118_1840_1900_stow_z1>0]

autocorr_mast1_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241118_1840_1900_stow_z2)
Lux_mast1_20241118_1840_1900_stow_z2 = Lux_20241118_1840_1900_stow_z2[Lux_20241118_1840_1900_stow_z2>0]

autocorr_mast1_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m1_U_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241118_1840_1900_stow_z3)
Lux_mast1_20241118_1840_1900_stow_z3 = Lux_20241118_1840_1900_stow_z3[Lux_20241118_1840_1900_stow_z3>0]

autocorr_mast1_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241118_1840_1900_stow_z1)
Lwx_mast1_20241118_1840_1900_stow_z1 = Lwx_20241118_1840_1900_stow_z1[Lwx_20241118_1840_1900_stow_z1>0]

autocorr_mast1_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241118_1840_1900_stow_z2)
Lwx_mast1_20241118_1840_1900_stow_z2 = Lwx_20241118_1840_1900_stow_z2[Lwx_20241118_1840_1900_stow_z2>0]

autocorr_mast1_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m1_W_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241118_1840_1900_stow_z3)
Lwx_mast1_20241118_1840_1900_stow_z3 = Lwx_20241118_1840_1900_stow_z3[Lwx_20241118_1840_1900_stow_z3>0]

Lux_profile_mast1_20241118_1840_1900_stow = pd.Series([Lux_mast1_20241118_1840_1900_stow_z1,Lux_mast1_20241118_1840_1900_stow_z2,Lux_mast1_20241118_1840_1900_stow_z3])
Lwx_profile_mast1_20241118_1840_1900_stow = pd.Series([Lwx_mast1_20241118_1840_1900_stow_z1,Lwx_mast1_20241118_1840_1900_stow_z2,Lwx_mast1_20241118_1840_1900_stow_z3])
 


#%% Mast 3

overlap = 0
nblock = len(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast3_20Hz_20241118_1840_1900_stow_z1, Pxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1 = fu_loads_mast3_20Hz_20241118_1840_1900_stow_z1*heights[0]/H3_U_ax_20241118_1840_1900_stow_z1
nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1 = (fu_loads_mast3_20Hz_20241118_1840_1900_stow_z1*Pxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1)/loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.std()**2

fu_loads_mast3_20Hz_20241118_1840_1900_stow_z2, Pxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2 = fu_loads_mast3_20Hz_20241118_1840_1900_stow_z2*heights[1]/H3_U_ax_20241118_1840_1900_stow_z2
nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2 = (fu_loads_mast3_20Hz_20241118_1840_1900_stow_z2*Pxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2)/loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.std()**2
 
fu_loads_mast3_20Hz_20241118_1840_1900_stow_z3, Pxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3 = fu_loads_mast3_20Hz_20241118_1840_1900_stow_z3*heights[2]/H3_U_ax_20241118_1840_1900_stow_z3
nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3 = (fu_loads_mast3_20Hz_20241118_1840_1900_stow_z3*Pxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3)/loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.std()**2              
    
fw_loads_mast3_20Hz_20241118_1840_1900_stow_z1, Pxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1 = fw_loads_mast3_20Hz_20241118_1840_1900_stow_z1*heights[0]/H3_W_ax_20241118_1840_1900_stow_z1
nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1 = (fw_loads_mast3_20Hz_20241118_1840_1900_stow_z1*Pxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1)/loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.std()**2

fw_loads_mast3_20Hz_20241118_1840_1900_stow_z2, Pxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2 = fw_loads_mast3_20Hz_20241118_1840_1900_stow_z2*heights[1]/H3_W_ax_20241118_1840_1900_stow_z2
nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2 = (fw_loads_mast3_20Hz_20241118_1840_1900_stow_z2*Pxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2)/loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.std()**2
 
fw_loads_mast3_20Hz_20241118_1840_1900_stow_z3, Pxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3 = welch(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3 = fw_loads_mast3_20Hz_20241118_1840_1900_stow_z3*heights[2]/H3_W_ax_20241118_1840_1900_stow_z3
nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3 = (fw_loads_mast3_20Hz_20241118_1840_1900_stow_z3*Pxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3)/loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1 = list(np.where([abs(nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1 = nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1[0][0]:len(nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1 = [nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2 = list(np.where([abs(nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2 = nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2[0][0]:len(nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2 = [nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3 = list(np.where([abs(nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3 = nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3[0][0]:len(nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3 = [nPxxfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1 = list(np.where([abs(nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1 = nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1[0][0]:len(nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1 = [nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z1]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2 = list(np.where([abs(nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2 = nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2[0][0]:len(nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2 = [nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z2]

index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3 = list(np.where([abs(nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3 = nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3[index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3[0][0]:len(nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3 = [nPxxfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3[0:index_highfreq_loads_mast_20Hz_20241118_1840_1900_stow_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241118_1840_1900_stow_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241118_1840_1900_stow_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast3')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241118_1840_1900_stow_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241118_1840_1900_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast3')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()





#%% LS exponential fit method

autocorr_mast3_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241118_1840_1900_stow_z1)
Lux_mast3_20241118_1840_1900_stow_z1 = Lux_20241118_1840_1900_stow_z1[Lux_20241118_1840_1900_stow_z1>0]

autocorr_mast3_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241118_1840_1900_stow_z2)
Lux_mast3_20241118_1840_1900_stow_z2 = Lux_20241118_1840_1900_stow_z2[Lux_20241118_1840_1900_stow_z2>0]

autocorr_mast3_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m3_U_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241118_1840_1900_stow)
Lux_20241118_1840_1900_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241118_1840_1900_stow_z3)
Lux_mast3_20241118_1840_1900_stow_z3 = Lux_20241118_1840_1900_stow_z3[Lux_20241118_1840_1900_stow_z3>0]

autocorr_mast3_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241118_1840_1900_stow_z1)
Lwx_mast3_20241118_1840_1900_stow_z1 = Lwx_20241118_1840_1900_stow_z1[Lwx_20241118_1840_1900_stow_z1>0]

autocorr_mast3_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241118_1840_1900_stow_z2)
Lwx_mast3_20241118_1840_1900_stow_z2 = Lwx_20241118_1840_1900_stow_z2[Lwx_20241118_1840_1900_stow_z2>0]

autocorr_mast3_20241118_1840_1900_stow = np.correlate(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241118_1840_1900_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241118_1840_1900_stow.m3_W_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241118_1840_1900_stow)
Lwx_20241118_1840_1900_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241118_1840_1900_stow_z3)
Lwx_mast3_20241118_1840_1900_stow_z3 = Lwx_20241118_1840_1900_stow_z3[Lwx_20241118_1840_1900_stow_z3>0]

Lux_profile_mast3_20241118_1840_1900_stow = pd.Series([Lux_mast3_20241118_1840_1900_stow_z1,Lux_mast3_20241118_1840_1900_stow_z2,Lux_mast3_20241118_1840_1900_stow_z3])
Lwx_profile_mast3_20241118_1840_1900_stow = pd.Series([Lwx_mast3_20241118_1840_1900_stow_z1,Lwx_mast3_20241118_1840_1900_stow_z2,Lwx_mast3_20241118_1840_1900_stow_z3])
 

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241118_1840_1900_stow, heights, label='Lux')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_u^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10000)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241118_1840_1900_stow, heights, label='Lwx')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_w^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wspd_20241118_1840_1900_stow_z1,H1_wspd_20241118_1840_1900_stow_z2,H1_wspd_20241118_1840_1900_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wspd_20241118_1840_1900_stow_z1,H2_wspd_20241118_1840_1900_stow_z2,H2_wspd_20241118_1840_1900_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wspd_20241118_1840_1900_stow_z1,H3_wspd_20241118_1840_1900_stow_z2,H3_wspd_20241118_1840_1900_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind speed (m/s)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,15)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wdir_20241118_1840_1900_stow_z1,H1_wdir_20241118_1840_1900_stow_z2,H1_wdir_20241118_1840_1900_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wdir_20241118_1840_1900_stow_z1,H2_wdir_20241118_1840_1900_stow_z2,H2_wdir_20241118_1840_1900_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wdir_20241118_1840_1900_stow_z1,H3_wdir_20241118_1840_1900_stow_z2,H3_wdir_20241118_1840_1900_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind direction (deg)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(300,360)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iu_20241118_1840_1900_stow_z1,H1_Iu_20241118_1840_1900_stow_z2,H1_Iu_20241118_1840_1900_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iu_20241118_1840_1900_stow_z1,H2_Iu_20241118_1840_1900_stow_z2,H2_Iu_20241118_1840_1900_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iu_20241118_1840_1900_stow_z1,H3_Iu_20241118_1840_1900_stow_z2,H3_Iu_20241118_1840_1900_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_u$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iw_20241118_1840_1900_stow_z1,H1_Iw_20241118_1840_1900_stow_z2,H1_Iw_20241118_1840_1900_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iw_20241118_1840_1900_stow_z1,H2_Iw_20241118_1840_1900_stow_z2,H2_Iw_20241118_1840_1900_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iw_20241118_1840_1900_stow_z1,H3_Iw_20241118_1840_1900_stow_z2,H3_Iw_20241118_1840_1900_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_w$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.2)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241118_1840_1900_stow/11.23, heights, s=8,label='inflow')            
plt.scatter(Lux_profile_mast1_20241118_1840_1900_stow/11.23, heights, s=8,label='mast1')            
plt.scatter(Lux_profile_mast3_20241118_1840_1900_stow/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_u^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,150)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241118_1840_1900_stow/11.23, heights, s=8,label='inflow')            
plt.scatter(Lwx_profile_mast1_20241118_1840_1900_stow/11.23, heights, s=8,label='mast1')            
plt.scatter(Lwx_profile_mast3_20241118_1840_1900_stow/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_w^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()



#%% PSD analysis

heights = [2.75,5.5,11] 
fs = 20

# Spectra
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from numpy import hanning
import math

overlap = 0
nblock = len(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_inflow_20Hz_20241120_1800_1830_stow_z1, Pxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = welch(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = fu_loads_inflow_20Hz_20241120_1800_1830_stow_z1*heights[0]/H1_U_ax_20241120_1800_1830_stow_z1
nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = (fu_loads_inflow_20Hz_20241120_1800_1830_stow_z1*Pxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1)/loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.std()**2

fu_loads_inflow_20Hz_20241120_1800_1830_stow_z2, Pxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = welch(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = fu_loads_inflow_20Hz_20241120_1800_1830_stow_z2*heights[1]/H1_U_ax_20241120_1800_1830_stow_z2
nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = (fu_loads_inflow_20Hz_20241120_1800_1830_stow_z2*Pxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2)/loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.std()**2
 
fu_loads_inflow_20Hz_20241120_1800_1830_stow_z3, Pxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = welch(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = fu_loads_inflow_20Hz_20241120_1800_1830_stow_z3*heights[2]/H1_U_ax_20241120_1800_1830_stow_z3
nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = (fu_loads_inflow_20Hz_20241120_1800_1830_stow_z3*Pxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3)/loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.std()**2              
    
fw_loads_inflow_20Hz_20241120_1800_1830_stow_z1, Pxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = welch(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = fw_loads_inflow_20Hz_20241120_1800_1830_stow_z1*heights[0]/H1_W_ax_20241120_1800_1830_stow_z1
nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = (fw_loads_inflow_20Hz_20241120_1800_1830_stow_z1*Pxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1)/loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.std()**2

fw_loads_inflow_20Hz_20241120_1800_1830_stow_z2, Pxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = welch(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = fw_loads_inflow_20Hz_20241120_1800_1830_stow_z2*heights[1]/H1_W_ax_20241120_1800_1830_stow_z2
nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = (fw_loads_inflow_20Hz_20241120_1800_1830_stow_z2*Pxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2)/loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.std()**2
 
fw_loads_inflow_20Hz_20241120_1800_1830_stow_z3, Pxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = welch(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = fw_loads_inflow_20Hz_20241120_1800_1830_stow_z3*heights[2]/H1_W_ax_20241120_1800_1830_stow_z3
nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = (fw_loads_inflow_20Hz_20241120_1800_1830_stow_z3*Pxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3)/loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = list(np.where([abs(nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1[index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z1[0][0]:len(nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1)]
nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z1,200)
nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = [nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1[0:index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z1[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z1]

index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = list(np.where([abs(nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2[index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z2[0][0]:len(nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2)]
nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z2,200)
nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = [nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2[0:index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z2[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z2]

index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = list(np.where([abs(nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3[index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z3[0][0]:len(nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3)]
nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z3,200)
nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = [nPxxfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3[0:index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z3[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z3]

index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = list(np.where([abs(nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1[index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z1[0][0]:len(nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1)]
nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z1,200)
nPxxfw_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z1 = [nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1[0:index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z1[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z1]

index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = list(np.where([abs(nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2[index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z2[0][0]:len(nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2)]
nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z2,200)
nPxxfw_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z2 = [nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2[0:index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z2[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z2]

index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = list(np.where([abs(nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3[index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z3[0][0]:len(nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3)]
nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z3,200)
nPxxfw_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z3 = [nPxxfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3[0:index_highfreq_loads_inflow_20Hz_20241120_1800_1830_stow_z3[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241120_1800_1830_stow_z3]


plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z1[0:len(nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z2[0:len(nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241120_1800_1830_stow_z3[0:len(nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('inflow')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z1[0:len(nPxxfw_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z2[0:len(nPxxfw_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241120_1800_1830_stow_z3[0:len(nPxxfw_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241120_1800_1830_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('inflow')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()


#%% Extract data by height

U_corr_inflow_20241120_1800_1830_stow_z1 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low)
U_corr_inflow_20241120_1800_1830_stow_z2 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid)
U_corr_inflow_20241120_1800_1830_stow_z3 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top)

V_corr_inflow_20241120_1800_1830_stow_z1 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.V_ax_Low)
V_corr_inflow_20241120_1800_1830_stow_z2 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.V_ax_Mid)
V_corr_inflow_20241120_1800_1830_stow_z3 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.V_ax_Top)

W_corr_inflow_20241120_1800_1830_stow_z1 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low)
W_corr_inflow_20241120_1800_1830_stow_z2 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid)
W_corr_inflow_20241120_1800_1830_stow_z3 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top)

Ts_corr_inflow_20241120_1800_1830_stow_z1 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.Ts_Low)
Ts_corr_inflow_20241120_1800_1830_stow_z2 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.Ts_Mid)
Ts_corr_inflow_20241120_1800_1830_stow_z3 = pd.Series(loads_inflow_20Hz_20241120_1800_1830_stow.Ts_Top)

# Detrend
U_corr_inflow_20241120_1800_1830_stow_z1[U_corr_inflow_20241120_1800_1830_stow_z1.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241120_1800_1830_stow_z1.dropna()) 
U_corr_inflow_20241120_1800_1830_stow_z2[U_corr_inflow_20241120_1800_1830_stow_z2.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241120_1800_1830_stow_z2.dropna()) 
U_corr_inflow_20241120_1800_1830_stow_z3[U_corr_inflow_20241120_1800_1830_stow_z3.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241120_1800_1830_stow_z3.dropna()) 

V_corr_inflow_20241120_1800_1830_stow_z1[V_corr_inflow_20241120_1800_1830_stow_z1.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241120_1800_1830_stow_z1.dropna()) 
V_corr_inflow_20241120_1800_1830_stow_z2[V_corr_inflow_20241120_1800_1830_stow_z2.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241120_1800_1830_stow_z2.dropna()) 
V_corr_inflow_20241120_1800_1830_stow_z3[V_corr_inflow_20241120_1800_1830_stow_z3.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241120_1800_1830_stow_z3.dropna()) 

W_corr_inflow_20241120_1800_1830_stow_z1[W_corr_inflow_20241120_1800_1830_stow_z1.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241120_1800_1830_stow_z1.dropna()) 
W_corr_inflow_20241120_1800_1830_stow_z2[W_corr_inflow_20241120_1800_1830_stow_z2.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241120_1800_1830_stow_z2.dropna()) 
W_corr_inflow_20241120_1800_1830_stow_z3[W_corr_inflow_20241120_1800_1830_stow_z3.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241120_1800_1830_stow_z3.dropna()) 

Ts_corr_inflow_20241120_1800_1830_stow_z1[Ts_corr_inflow_20241120_1800_1830_stow_z1.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241120_1800_1830_stow_z1.dropna()) 
Ts_corr_inflow_20241120_1800_1830_stow_z2[Ts_corr_inflow_20241120_1800_1830_stow_z2.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241120_1800_1830_stow_z2.dropna()) 
Ts_corr_inflow_20241120_1800_1830_stow_z3[Ts_corr_inflow_20241120_1800_1830_stow_z3.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241120_1800_1830_stow_z3.dropna()) 

# Reynolds stresses and length scales (south2)

inflow_uv_z1_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z1*V_corr_inflow_20241120_1800_1830_stow_z1).mean()-(U_corr_inflow_20241120_1800_1830_stow_z1.mean()*V_corr_inflow_20241120_1800_1830_stow_z1.mean());
inflow_vw_z1_20241120_1800_1830_stow = (V_corr_inflow_20241120_1800_1830_stow_z1*W_corr_inflow_20241120_1800_1830_stow_z1).mean()-(V_corr_inflow_20241120_1800_1830_stow_z1.mean()*W_corr_inflow_20241120_1800_1830_stow_z1.mean());
inflow_uw_z1_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z1*W_corr_inflow_20241120_1800_1830_stow_z1).mean()-(U_corr_inflow_20241120_1800_1830_stow_z1.mean()*W_corr_inflow_20241120_1800_1830_stow_z1.mean());
inflow_wT_z1_20241120_1800_1830_stow = (W_corr_inflow_20241120_1800_1830_stow_z1*Ts_corr_inflow_20241120_1800_1830_stow_z1).mean()-(W_corr_inflow_20241120_1800_1830_stow_z1.mean()*Ts_corr_inflow_20241120_1800_1830_stow_z1.mean());

inflow_uv_z2_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z2*V_corr_inflow_20241120_1800_1830_stow_z2).mean()-(U_corr_inflow_20241120_1800_1830_stow_z2.mean()*V_corr_inflow_20241120_1800_1830_stow_z2.mean());
inflow_vw_z2_20241120_1800_1830_stow = (V_corr_inflow_20241120_1800_1830_stow_z2*W_corr_inflow_20241120_1800_1830_stow_z2).mean()-(V_corr_inflow_20241120_1800_1830_stow_z2.mean()*W_corr_inflow_20241120_1800_1830_stow_z2.mean());
inflow_uw_z2_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z2*W_corr_inflow_20241120_1800_1830_stow_z2).mean()-(U_corr_inflow_20241120_1800_1830_stow_z2.mean()*W_corr_inflow_20241120_1800_1830_stow_z2.mean());
inflow_wT_z2_20241120_1800_1830_stow = (W_corr_inflow_20241120_1800_1830_stow_z2*Ts_corr_inflow_20241120_1800_1830_stow_z2).mean()-(W_corr_inflow_20241120_1800_1830_stow_z2.mean()*Ts_corr_inflow_20241120_1800_1830_stow_z2.mean());

inflow_uv_z3_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z3*V_corr_inflow_20241120_1800_1830_stow_z3).mean()-(U_corr_inflow_20241120_1800_1830_stow_z3.mean()*V_corr_inflow_20241120_1800_1830_stow_z3.mean());
inflow_vw_z3_20241120_1800_1830_stow = (V_corr_inflow_20241120_1800_1830_stow_z3*W_corr_inflow_20241120_1800_1830_stow_z3).mean()-(V_corr_inflow_20241120_1800_1830_stow_z3.mean()*W_corr_inflow_20241120_1800_1830_stow_z3.mean());
inflow_uw_z3_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z3*W_corr_inflow_20241120_1800_1830_stow_z3).mean()-(U_corr_inflow_20241120_1800_1830_stow_z3.mean()*W_corr_inflow_20241120_1800_1830_stow_z3.mean());
inflow_wT_z3_20241120_1800_1830_stow = (W_corr_inflow_20241120_1800_1830_stow_z3*Ts_corr_inflow_20241120_1800_1830_stow_z3).mean()-(W_corr_inflow_20241120_1800_1830_stow_z3.mean()*Ts_corr_inflow_20241120_1800_1830_stow_z3.mean());

utau_z1_20241120_1800_1830_stow = (inflow_uw_z1_20241120_1800_1830_stow**2+inflow_vw_z1_20241120_1800_1830_stow**2)**(1/4) 
utau_z2_20241120_1800_1830_stow = (inflow_uw_z2_20241120_1800_1830_stow**2+inflow_vw_z2_20241120_1800_1830_stow**2)**(1/4) 
utau_z3_20241120_1800_1830_stow = (inflow_uw_z3_20241120_1800_1830_stow**2+inflow_vw_z3_20241120_1800_1830_stow**2)**(1/4) 

L_z1_20241120_1800_1830_stow = -1*(utau_z1_20241120_1800_1830_stow**3)/(0.4*(9.81/H1_Ts_20241120_1800_1830_stow_z1)*inflow_wT_z1_20241120_1800_1830_stow)
L_z2_20241120_1800_1830_stow = -1*(utau_z2_20241120_1800_1830_stow**3)/(0.4*(9.81/H1_Ts_20241120_1800_1830_stow_z2)*inflow_wT_z2_20241120_1800_1830_stow)
L_z3_20241120_1800_1830_stow = -1*(utau_z3_20241120_1800_1830_stow**3)/(0.4*(9.81/H1_Ts_20241120_1800_1830_stow_z3)*inflow_wT_z3_20241120_1800_1830_stow)

zL_z1_20241120_1800_1830_stow = heights[0]/L_z1_20241120_1800_1830_stow
zL_z2_20241120_1800_1830_stow = heights[1]/L_z2_20241120_1800_1830_stow
zL_z3_20241120_1800_1830_stow = heights[2]/L_z3_20241120_1800_1830_stow

inflow_uprimewprime_z1_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z1*W_corr_inflow_20241120_1800_1830_stow_z1);
inflow_uprimewprime_z2_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z2*W_corr_inflow_20241120_1800_1830_stow_z2);
inflow_uprimewprime_z3_20241120_1800_1830_stow = (U_corr_inflow_20241120_1800_1830_stow_z3*W_corr_inflow_20241120_1800_1830_stow_z3);


#%% LS exponential fit method

autocorr_inflow_20241120_1800_1830_stow = np.correlate(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241120_1800_1830_stow_z1)
Lux_20241120_1800_1830_stow_z1 = Lux_20241120_1800_1830_stow_z1[Lux_20241120_1800_1830_stow_z1>0]

autocorr_inflow_20241120_1800_1830_stow = np.correlate(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241120_1800_1830_stow_z2)
Lux_20241120_1800_1830_stow_z2 = Lux_20241120_1800_1830_stow_z2[Lux_20241120_1800_1830_stow_z2>0]

autocorr_inflow_20241120_1800_1830_stow = np.correlate(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241120_1800_1830_stow.U_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241120_1800_1830_stow_z3)
Lux_20241120_1800_1830_stow_z3 = Lux_20241120_1800_1830_stow_z3[Lux_20241120_1800_1830_stow_z3>0]

autocorr_inflow_20241120_1800_1830_stow = np.correlate(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241120_1800_1830_stow_z1)
Lwx_20241120_1800_1830_stow_z1 = Lwx_20241120_1800_1830_stow_z1[Lwx_20241120_1800_1830_stow_z1>0]

autocorr_inflow_20241120_1800_1830_stow = np.correlate(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241120_1800_1830_stow_z2)
Lwx_20241120_1800_1830_stow_z2 = Lwx_20241120_1800_1830_stow_z2[Lwx_20241120_1800_1830_stow_z2>0]

autocorr_inflow_20241120_1800_1830_stow = np.correlate(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna(), loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241120_1800_1830_stow.W_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241120_1800_1830_stow_z3)
Lwx_20241120_1800_1830_stow_z3 = Lwx_20241120_1800_1830_stow_z3[Lwx_20241120_1800_1830_stow_z3>0]

Lux_profile_inflow_20241120_1800_1830_stow = pd.Series([Lux_20241120_1800_1830_stow_z1,Lux_20241120_1800_1830_stow_z2,Lux_20241120_1800_1830_stow_z3])
Lwx_profile_inflow_20241120_1800_1830_stow = pd.Series([Lwx_20241120_1800_1830_stow_z1,Lwx_20241120_1800_1830_stow_z2,Lwx_20241120_1800_1830_stow_z3])
 


#%% Mast 1

overlap = 0
nblock = len(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast1_20Hz_20241120_1800_1830_stow_z1, Pxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1 = fu_loads_mast1_20Hz_20241120_1800_1830_stow_z1*heights[0]/H2_U_ax_20241120_1800_1830_stow_z1
nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1 = (fu_loads_mast1_20Hz_20241120_1800_1830_stow_z1*Pxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1)/loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.std()**2

fu_loads_mast1_20Hz_20241120_1800_1830_stow_z2, Pxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2 = fu_loads_mast1_20Hz_20241120_1800_1830_stow_z2*heights[1]/H2_U_ax_20241120_1800_1830_stow_z2
nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2 = (fu_loads_mast1_20Hz_20241120_1800_1830_stow_z2*Pxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2)/loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.std()**2
 
fu_loads_mast1_20Hz_20241120_1800_1830_stow_z3, Pxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3 = fu_loads_mast1_20Hz_20241120_1800_1830_stow_z3*heights[2]/H2_U_ax_20241120_1800_1830_stow_z3
nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3 = (fu_loads_mast1_20Hz_20241120_1800_1830_stow_z3*Pxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3)/loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.std()**2              
    
fw_loads_mast1_20Hz_20241120_1800_1830_stow_z1, Pxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1 = fw_loads_mast1_20Hz_20241120_1800_1830_stow_z1*heights[0]/H2_W_ax_20241120_1800_1830_stow_z1
nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1 = (fw_loads_mast1_20Hz_20241120_1800_1830_stow_z1*Pxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1)/loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.std()**2

fw_loads_mast1_20Hz_20241120_1800_1830_stow_z2, Pxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2 = fw_loads_mast1_20Hz_20241120_1800_1830_stow_z2*heights[1]/H2_W_ax_20241120_1800_1830_stow_z2
nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2 = (fw_loads_mast1_20Hz_20241120_1800_1830_stow_z2*Pxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2)/loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.std()**2
 
fw_loads_mast1_20Hz_20241120_1800_1830_stow_z3, Pxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3 = fw_loads_mast1_20Hz_20241120_1800_1830_stow_z3*heights[2]/H2_W_ax_20241120_1800_1830_stow_z3
nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3 = (fw_loads_mast1_20Hz_20241120_1800_1830_stow_z3*Pxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3)/loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.std()**2              



#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1 = list(np.where([abs(nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1 = nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1[0][0]:len(nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1 = [nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2 = list(np.where([abs(nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2 = nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2[0][0]:len(nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2 = [nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3 = list(np.where([abs(nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3 = nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3[0][0]:len(nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3 = [nPxxfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1 = list(np.where([abs(nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1 = nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1[0][0]:len(nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1 = [nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2 = list(np.where([abs(nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2 = nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2[0][0]:len(nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2 = [nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3 = list(np.where([abs(nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3 = nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3[0][0]:len(nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3 = [nPxxfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241120_1800_1830_stow_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast1')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241120_1800_1830_stow_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast1')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()



#%% LS exponential fit method

autocorr_mast1_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241120_1800_1830_stow_z1)
Lux_mast1_20241120_1800_1830_stow_z1 = Lux_20241120_1800_1830_stow_z1[Lux_20241120_1800_1830_stow_z1>0]

autocorr_mast1_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241120_1800_1830_stow_z2)
Lux_mast1_20241120_1800_1830_stow_z2 = Lux_20241120_1800_1830_stow_z2[Lux_20241120_1800_1830_stow_z2>0]

autocorr_mast1_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m1_U_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241120_1800_1830_stow_z3)
Lux_mast1_20241120_1800_1830_stow_z3 = Lux_20241120_1800_1830_stow_z3[Lux_20241120_1800_1830_stow_z3>0]

autocorr_mast1_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241120_1800_1830_stow_z1)
Lwx_mast1_20241120_1800_1830_stow_z1 = Lwx_20241120_1800_1830_stow_z1[Lwx_20241120_1800_1830_stow_z1>0]

autocorr_mast1_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241120_1800_1830_stow_z2)
Lwx_mast1_20241120_1800_1830_stow_z2 = Lwx_20241120_1800_1830_stow_z2[Lwx_20241120_1800_1830_stow_z2>0]

autocorr_mast1_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m1_W_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241120_1800_1830_stow_z3)
Lwx_mast1_20241120_1800_1830_stow_z3 = Lwx_20241120_1800_1830_stow_z3[Lwx_20241120_1800_1830_stow_z3>0]

Lux_profile_mast1_20241120_1800_1830_stow = pd.Series([Lux_mast1_20241120_1800_1830_stow_z1,Lux_mast1_20241120_1800_1830_stow_z2,Lux_mast1_20241120_1800_1830_stow_z3])
Lwx_profile_mast1_20241120_1800_1830_stow = pd.Series([Lwx_mast1_20241120_1800_1830_stow_z1,Lwx_mast1_20241120_1800_1830_stow_z2,Lwx_mast1_20241120_1800_1830_stow_z3])
 


#%% Mast 3

overlap = 0
nblock = len(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast3_20Hz_20241120_1800_1830_stow_z1, Pxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1 = fu_loads_mast3_20Hz_20241120_1800_1830_stow_z1*heights[0]/H3_U_ax_20241120_1800_1830_stow_z1
nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1 = (fu_loads_mast3_20Hz_20241120_1800_1830_stow_z1*Pxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1)/loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.std()**2

fu_loads_mast3_20Hz_20241120_1800_1830_stow_z2, Pxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2 = fu_loads_mast3_20Hz_20241120_1800_1830_stow_z2*heights[1]/H3_U_ax_20241120_1800_1830_stow_z2
nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2 = (fu_loads_mast3_20Hz_20241120_1800_1830_stow_z2*Pxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2)/loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.std()**2
 
fu_loads_mast3_20Hz_20241120_1800_1830_stow_z3, Pxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3 = fu_loads_mast3_20Hz_20241120_1800_1830_stow_z3*heights[2]/H3_U_ax_20241120_1800_1830_stow_z3
nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3 = (fu_loads_mast3_20Hz_20241120_1800_1830_stow_z3*Pxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3)/loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.std()**2              
    
fw_loads_mast3_20Hz_20241120_1800_1830_stow_z1, Pxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1 = fw_loads_mast3_20Hz_20241120_1800_1830_stow_z1*heights[0]/H3_W_ax_20241120_1800_1830_stow_z1
nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1 = (fw_loads_mast3_20Hz_20241120_1800_1830_stow_z1*Pxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1)/loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.std()**2

fw_loads_mast3_20Hz_20241120_1800_1830_stow_z2, Pxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2 = fw_loads_mast3_20Hz_20241120_1800_1830_stow_z2*heights[1]/H3_W_ax_20241120_1800_1830_stow_z2
nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2 = (fw_loads_mast3_20Hz_20241120_1800_1830_stow_z2*Pxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2)/loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.std()**2
 
fw_loads_mast3_20Hz_20241120_1800_1830_stow_z3, Pxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3 = welch(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3 = fw_loads_mast3_20Hz_20241120_1800_1830_stow_z3*heights[2]/H3_W_ax_20241120_1800_1830_stow_z3
nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3 = (fw_loads_mast3_20Hz_20241120_1800_1830_stow_z3*Pxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3)/loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1 = list(np.where([abs(nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1 = nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1[0][0]:len(nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1 = [nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2 = list(np.where([abs(nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2 = nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2[0][0]:len(nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2 = [nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3 = list(np.where([abs(nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3 = nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3[0][0]:len(nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3 = [nPxxfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1 = list(np.where([abs(nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1 = nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1[0][0]:len(nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1 = [nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z1]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2 = list(np.where([abs(nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2 = nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2[0][0]:len(nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2 = [nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z2]

index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3 = list(np.where([abs(nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3 = nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3[index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3[0][0]:len(nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3 = [nPxxfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3[0:index_highfreq_loads_mast_20Hz_20241120_1800_1830_stow_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241120_1800_1830_stow_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241120_1800_1830_stow_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast3')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241120_1800_1830_stow_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241120_1800_1830_stow_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast3')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()





#%% LS exponential fit method

autocorr_mast3_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241120_1800_1830_stow_z1)
Lux_mast3_20241120_1800_1830_stow_z1 = Lux_20241120_1800_1830_stow_z1[Lux_20241120_1800_1830_stow_z1>0]

autocorr_mast3_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241120_1800_1830_stow_z2)
Lux_mast3_20241120_1800_1830_stow_z2 = Lux_20241120_1800_1830_stow_z2[Lux_20241120_1800_1830_stow_z2>0]

autocorr_mast3_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m3_U_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241120_1800_1830_stow)
Lux_20241120_1800_1830_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241120_1800_1830_stow_z3)
Lux_mast3_20241120_1800_1830_stow_z3 = Lux_20241120_1800_1830_stow_z3[Lux_20241120_1800_1830_stow_z3>0]

autocorr_mast3_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241120_1800_1830_stow_z1)
Lwx_mast3_20241120_1800_1830_stow_z1 = Lwx_20241120_1800_1830_stow_z1[Lwx_20241120_1800_1830_stow_z1>0]

autocorr_mast3_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241120_1800_1830_stow_z2)
Lwx_mast3_20241120_1800_1830_stow_z2 = Lwx_20241120_1800_1830_stow_z2[Lwx_20241120_1800_1830_stow_z2>0]

autocorr_mast3_20241120_1800_1830_stow = np.correlate(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241120_1800_1830_stow /= np.sqrt(np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241120_1800_1830_stow.m3_W_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241120_1800_1830_stow)
Lwx_20241120_1800_1830_stow_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241120_1800_1830_stow_z3)
Lwx_mast3_20241120_1800_1830_stow_z3 = Lwx_20241120_1800_1830_stow_z3[Lwx_20241120_1800_1830_stow_z3>0]

Lux_profile_mast3_20241120_1800_1830_stow = pd.Series([Lux_mast3_20241120_1800_1830_stow_z1,Lux_mast3_20241120_1800_1830_stow_z2,Lux_mast3_20241120_1800_1830_stow_z3])
Lwx_profile_mast3_20241120_1800_1830_stow = pd.Series([Lwx_mast3_20241120_1800_1830_stow_z1,Lwx_mast3_20241120_1800_1830_stow_z2,Lwx_mast3_20241120_1800_1830_stow_z3])
 

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241120_1800_1830_stow, heights, label='Lux')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_u^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10000)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241120_1800_1830_stow, heights, label='Lwx')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_w^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wspd_20241120_1800_1830_stow_z1,H1_wspd_20241120_1800_1830_stow_z2,H1_wspd_20241120_1800_1830_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wspd_20241120_1800_1830_stow_z1,H2_wspd_20241120_1800_1830_stow_z2,H2_wspd_20241120_1800_1830_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wspd_20241120_1800_1830_stow_z1,H3_wspd_20241120_1800_1830_stow_z2,H3_wspd_20241120_1800_1830_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind speed (m/s)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wdir_20241120_1800_1830_stow_z1,H1_wdir_20241120_1800_1830_stow_z2,H1_wdir_20241120_1800_1830_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wdir_20241120_1800_1830_stow_z1,H2_wdir_20241120_1800_1830_stow_z2,H2_wdir_20241120_1800_1830_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wdir_20241120_1800_1830_stow_z1,H3_wdir_20241120_1800_1830_stow_z2,H3_wdir_20241120_1800_1830_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind direction (deg)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(120,180)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iu_20241120_1800_1830_stow_z1,H1_Iu_20241120_1800_1830_stow_z2,H1_Iu_20241120_1800_1830_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iu_20241120_1800_1830_stow_z1,H2_Iu_20241120_1800_1830_stow_z2,H2_Iu_20241120_1800_1830_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iu_20241120_1800_1830_stow_z1,H3_Iu_20241120_1800_1830_stow_z2,H3_Iu_20241120_1800_1830_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_u$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iw_20241120_1800_1830_stow_z1,H1_Iw_20241120_1800_1830_stow_z2,H1_Iw_20241120_1800_1830_stow_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iw_20241120_1800_1830_stow_z1,H2_Iw_20241120_1800_1830_stow_z2,H2_Iw_20241120_1800_1830_stow_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iw_20241120_1800_1830_stow_z1,H3_Iw_20241120_1800_1830_stow_z2,H3_Iw_20241120_1800_1830_stow_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_w$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.2)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241120_1800_1830_stow/11.23, heights, s=8,label='inflow')            
plt.scatter(Lux_profile_mast1_20241120_1800_1830_stow/11.23, heights, s=8,label='mast1')            
plt.scatter(Lux_profile_mast3_20241120_1800_1830_stow/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_u^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,100)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241120_1800_1830_stow/11.23, heights, s=8,label='inflow')            
plt.scatter(Lwx_profile_mast1_20241120_1800_1830_stow/11.23, heights, s=8,label='mast1')            
plt.scatter(Lwx_profile_mast3_20241120_1800_1830_stow/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_w^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()




#%% PSD analysis

heights = [2.75,5.5,11] 
fs = 20

# Spectra
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from numpy import hanning
import math

overlap = 0
nblock = len(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1, Pxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = welch(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1*heights[0]/H1_U_ax_20241121_0000_0030_stow1_z1
nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = (fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1*Pxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1)/loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.std()**2

fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2, Pxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = welch(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2*heights[1]/H1_U_ax_20241121_0000_0030_stow1_z2
nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = (fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2*Pxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2)/loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.std()**2
 
fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3, Pxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = welch(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3*heights[2]/H1_U_ax_20241121_0000_0030_stow1_z3
nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = (fu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3*Pxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3)/loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.std()**2              
    
fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1, Pxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = welch(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1*heights[0]/H1_W_ax_20241121_0000_0030_stow1_z1
nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = (fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1*Pxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1)/loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.std()**2

fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2, Pxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = welch(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2*heights[1]/H1_W_ax_20241121_0000_0030_stow1_z2
nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = (fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2*Pxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2)/loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.std()**2
 
fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3, Pxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = welch(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3*heights[2]/H1_W_ax_20241121_0000_0030_stow1_z3
nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = (fw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3*Pxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3)/loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = list(np.where([abs(nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[0][0]:len(nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1)]
nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z1,200)
nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = [nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[0:index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z1]

index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = list(np.where([abs(nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[0][0]:len(nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2)]
nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z2,200)
nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = [nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[0:index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z2]

index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = list(np.where([abs(nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[0][0]:len(nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3)]
nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z3,200)
nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = [nPxxfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[0:index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z3]

index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = list(np.where([abs(nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[0][0]:len(nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1)]
nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z1,200)
nPxxfw_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z1 = [nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[0:index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z1]

index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = list(np.where([abs(nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[0][0]:len(nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2)]
nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z2,200)
nPxxfw_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z2 = [nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[0:index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z2]

index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = list(np.where([abs(nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[0][0]:len(nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3)]
nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z3,200)
nPxxfw_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z3 = [nPxxfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[0:index_highfreq_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241121_0000_0030_stow1_z3]


plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[0:len(nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[0:len(nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[0:len(nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('inflow')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[0:len(nPxxfw_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[0:len(nPxxfw_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[0:len(nPxxfw_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0000_0030_stow1_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('inflow')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()


#%% Extract data by height

U_corr_inflow_20241121_0000_0030_stow1_z1 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low)
U_corr_inflow_20241121_0000_0030_stow1_z2 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid)
U_corr_inflow_20241121_0000_0030_stow1_z3 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top)

V_corr_inflow_20241121_0000_0030_stow1_z1 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.V_ax_Low)
V_corr_inflow_20241121_0000_0030_stow1_z2 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.V_ax_Mid)
V_corr_inflow_20241121_0000_0030_stow1_z3 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.V_ax_Top)

W_corr_inflow_20241121_0000_0030_stow1_z1 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low)
W_corr_inflow_20241121_0000_0030_stow1_z2 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid)
W_corr_inflow_20241121_0000_0030_stow1_z3 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top)

Ts_corr_inflow_20241121_0000_0030_stow1_z1 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.Ts_Low)
Ts_corr_inflow_20241121_0000_0030_stow1_z2 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.Ts_Mid)
Ts_corr_inflow_20241121_0000_0030_stow1_z3 = pd.Series(loads_inflow_20Hz_20241121_0000_0030_stow1.Ts_Top)

# Detrend
U_corr_inflow_20241121_0000_0030_stow1_z1[U_corr_inflow_20241121_0000_0030_stow1_z1.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241121_0000_0030_stow1_z1.dropna()) 
U_corr_inflow_20241121_0000_0030_stow1_z2[U_corr_inflow_20241121_0000_0030_stow1_z2.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241121_0000_0030_stow1_z2.dropna()) 
U_corr_inflow_20241121_0000_0030_stow1_z3[U_corr_inflow_20241121_0000_0030_stow1_z3.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241121_0000_0030_stow1_z3.dropna()) 

V_corr_inflow_20241121_0000_0030_stow1_z1[V_corr_inflow_20241121_0000_0030_stow1_z1.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241121_0000_0030_stow1_z1.dropna()) 
V_corr_inflow_20241121_0000_0030_stow1_z2[V_corr_inflow_20241121_0000_0030_stow1_z2.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241121_0000_0030_stow1_z2.dropna()) 
V_corr_inflow_20241121_0000_0030_stow1_z3[V_corr_inflow_20241121_0000_0030_stow1_z3.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241121_0000_0030_stow1_z3.dropna()) 

W_corr_inflow_20241121_0000_0030_stow1_z1[W_corr_inflow_20241121_0000_0030_stow1_z1.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241121_0000_0030_stow1_z1.dropna()) 
W_corr_inflow_20241121_0000_0030_stow1_z2[W_corr_inflow_20241121_0000_0030_stow1_z2.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241121_0000_0030_stow1_z2.dropna()) 
W_corr_inflow_20241121_0000_0030_stow1_z3[W_corr_inflow_20241121_0000_0030_stow1_z3.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241121_0000_0030_stow1_z3.dropna()) 

Ts_corr_inflow_20241121_0000_0030_stow1_z1[Ts_corr_inflow_20241121_0000_0030_stow1_z1.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241121_0000_0030_stow1_z1.dropna()) 
Ts_corr_inflow_20241121_0000_0030_stow1_z2[Ts_corr_inflow_20241121_0000_0030_stow1_z2.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241121_0000_0030_stow1_z2.dropna()) 
Ts_corr_inflow_20241121_0000_0030_stow1_z3[Ts_corr_inflow_20241121_0000_0030_stow1_z3.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241121_0000_0030_stow1_z3.dropna()) 

# Reynolds stresses and length scales (south2)

inflow_uv_z1_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z1*V_corr_inflow_20241121_0000_0030_stow1_z1).mean()-(U_corr_inflow_20241121_0000_0030_stow1_z1.mean()*V_corr_inflow_20241121_0000_0030_stow1_z1.mean());
inflow_vw_z1_20241121_0000_0030_stow1 = (V_corr_inflow_20241121_0000_0030_stow1_z1*W_corr_inflow_20241121_0000_0030_stow1_z1).mean()-(V_corr_inflow_20241121_0000_0030_stow1_z1.mean()*W_corr_inflow_20241121_0000_0030_stow1_z1.mean());
inflow_uw_z1_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z1*W_corr_inflow_20241121_0000_0030_stow1_z1).mean()-(U_corr_inflow_20241121_0000_0030_stow1_z1.mean()*W_corr_inflow_20241121_0000_0030_stow1_z1.mean());
inflow_wT_z1_20241121_0000_0030_stow1 = (W_corr_inflow_20241121_0000_0030_stow1_z1*Ts_corr_inflow_20241121_0000_0030_stow1_z1).mean()-(W_corr_inflow_20241121_0000_0030_stow1_z1.mean()*Ts_corr_inflow_20241121_0000_0030_stow1_z1.mean());

inflow_uv_z2_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z2*V_corr_inflow_20241121_0000_0030_stow1_z2).mean()-(U_corr_inflow_20241121_0000_0030_stow1_z2.mean()*V_corr_inflow_20241121_0000_0030_stow1_z2.mean());
inflow_vw_z2_20241121_0000_0030_stow1 = (V_corr_inflow_20241121_0000_0030_stow1_z2*W_corr_inflow_20241121_0000_0030_stow1_z2).mean()-(V_corr_inflow_20241121_0000_0030_stow1_z2.mean()*W_corr_inflow_20241121_0000_0030_stow1_z2.mean());
inflow_uw_z2_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z2*W_corr_inflow_20241121_0000_0030_stow1_z2).mean()-(U_corr_inflow_20241121_0000_0030_stow1_z2.mean()*W_corr_inflow_20241121_0000_0030_stow1_z2.mean());
inflow_wT_z2_20241121_0000_0030_stow1 = (W_corr_inflow_20241121_0000_0030_stow1_z2*Ts_corr_inflow_20241121_0000_0030_stow1_z2).mean()-(W_corr_inflow_20241121_0000_0030_stow1_z2.mean()*Ts_corr_inflow_20241121_0000_0030_stow1_z2.mean());

inflow_uv_z3_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z3*V_corr_inflow_20241121_0000_0030_stow1_z3).mean()-(U_corr_inflow_20241121_0000_0030_stow1_z3.mean()*V_corr_inflow_20241121_0000_0030_stow1_z3.mean());
inflow_vw_z3_20241121_0000_0030_stow1 = (V_corr_inflow_20241121_0000_0030_stow1_z3*W_corr_inflow_20241121_0000_0030_stow1_z3).mean()-(V_corr_inflow_20241121_0000_0030_stow1_z3.mean()*W_corr_inflow_20241121_0000_0030_stow1_z3.mean());
inflow_uw_z3_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z3*W_corr_inflow_20241121_0000_0030_stow1_z3).mean()-(U_corr_inflow_20241121_0000_0030_stow1_z3.mean()*W_corr_inflow_20241121_0000_0030_stow1_z3.mean());
inflow_wT_z3_20241121_0000_0030_stow1 = (W_corr_inflow_20241121_0000_0030_stow1_z3*Ts_corr_inflow_20241121_0000_0030_stow1_z3).mean()-(W_corr_inflow_20241121_0000_0030_stow1_z3.mean()*Ts_corr_inflow_20241121_0000_0030_stow1_z3.mean());

utau_z1_20241121_0000_0030_stow1 = (inflow_uw_z1_20241121_0000_0030_stow1**2+inflow_vw_z1_20241121_0000_0030_stow1**2)**(1/4) 
utau_z2_20241121_0000_0030_stow1 = (inflow_uw_z2_20241121_0000_0030_stow1**2+inflow_vw_z2_20241121_0000_0030_stow1**2)**(1/4) 
utau_z3_20241121_0000_0030_stow1 = (inflow_uw_z3_20241121_0000_0030_stow1**2+inflow_vw_z3_20241121_0000_0030_stow1**2)**(1/4) 

L_z1_20241121_0000_0030_stow1 = -1*(utau_z1_20241121_0000_0030_stow1**3)/(0.4*(9.81/H1_Ts_20241121_0000_0030_stow1_z1)*inflow_wT_z1_20241121_0000_0030_stow1)
L_z2_20241121_0000_0030_stow1 = -1*(utau_z2_20241121_0000_0030_stow1**3)/(0.4*(9.81/H1_Ts_20241121_0000_0030_stow1_z2)*inflow_wT_z2_20241121_0000_0030_stow1)
L_z3_20241121_0000_0030_stow1 = -1*(utau_z3_20241121_0000_0030_stow1**3)/(0.4*(9.81/H1_Ts_20241121_0000_0030_stow1_z3)*inflow_wT_z3_20241121_0000_0030_stow1)

zL_z1_20241121_0000_0030_stow1 = heights[0]/L_z1_20241121_0000_0030_stow1
zL_z2_20241121_0000_0030_stow1 = heights[1]/L_z2_20241121_0000_0030_stow1
zL_z3_20241121_0000_0030_stow1 = heights[2]/L_z3_20241121_0000_0030_stow1

inflow_uprimewprime_z1_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z1*W_corr_inflow_20241121_0000_0030_stow1_z1);
inflow_uprimewprime_z2_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z2*W_corr_inflow_20241121_0000_0030_stow1_z2);
inflow_uprimewprime_z3_20241121_0000_0030_stow1 = (U_corr_inflow_20241121_0000_0030_stow1_z3*W_corr_inflow_20241121_0000_0030_stow1_z3);


#%% LS exponential fit method

autocorr_inflow_20241121_0000_0030_stow1 = np.correlate(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0000_0030_stow1_z1)
Lux_20241121_0000_0030_stow1_z1 = Lux_20241121_0000_0030_stow1_z1[Lux_20241121_0000_0030_stow1_z1>0]

autocorr_inflow_20241121_0000_0030_stow1 = np.correlate(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0000_0030_stow1_z2)
Lux_20241121_0000_0030_stow1_z2 = Lux_20241121_0000_0030_stow1_z2[Lux_20241121_0000_0030_stow1_z2>0]

autocorr_inflow_20241121_0000_0030_stow1 = np.correlate(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241121_0000_0030_stow1.U_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0000_0030_stow1_z3)
Lux_20241121_0000_0030_stow1_z3 = Lux_20241121_0000_0030_stow1_z3[Lux_20241121_0000_0030_stow1_z3>0]

autocorr_inflow_20241121_0000_0030_stow1 = np.correlate(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0000_0030_stow1_z1)
Lwx_20241121_0000_0030_stow1_z1 = Lwx_20241121_0000_0030_stow1_z1[Lwx_20241121_0000_0030_stow1_z1>0]

autocorr_inflow_20241121_0000_0030_stow1 = np.correlate(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0000_0030_stow1_z2)
Lwx_20241121_0000_0030_stow1_z2 = Lwx_20241121_0000_0030_stow1_z2[Lwx_20241121_0000_0030_stow1_z2>0]

autocorr_inflow_20241121_0000_0030_stow1 = np.correlate(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna(), loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241121_0000_0030_stow1.W_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0000_0030_stow1_z3)
Lwx_20241121_0000_0030_stow1_z3 = Lwx_20241121_0000_0030_stow1_z3[Lwx_20241121_0000_0030_stow1_z3>0]

Lux_profile_inflow_20241121_0000_0030_stow1 = pd.Series([Lux_20241121_0000_0030_stow1_z1,Lux_20241121_0000_0030_stow1_z2,Lux_20241121_0000_0030_stow1_z3])
Lwx_profile_inflow_20241121_0000_0030_stow1 = pd.Series([Lwx_20241121_0000_0030_stow1_z1,Lwx_20241121_0000_0030_stow1_z2,Lwx_20241121_0000_0030_stow1_z3])
 


#%% Mast 1

overlap = 0
nblock = len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1, Pxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1 = fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1*heights[0]/H2_U_ax_20241121_0000_0030_stow1_z1
nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1 = (fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1*Pxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1)/loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.std()**2

fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2, Pxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2 = fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2*heights[1]/H2_U_ax_20241121_0000_0030_stow1_z2
nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2 = (fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2*Pxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2)/loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.std()**2
 
fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3, Pxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3 = fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3*heights[2]/H2_U_ax_20241121_0000_0030_stow1_z3
nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3 = (fu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3*Pxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3)/loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.std()**2              
    
fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1, Pxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1 = fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1*heights[0]/H2_W_ax_20241121_0000_0030_stow1_z1
nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1 = (fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1*Pxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1)/loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.std()**2

fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2, Pxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2 = fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2*heights[1]/H2_W_ax_20241121_0000_0030_stow1_z2
nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2 = (fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2*Pxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2)/loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.std()**2
 
fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3, Pxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3 = fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3*heights[2]/H2_W_ax_20241121_0000_0030_stow1_z3
nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3 = (fw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3*Pxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3)/loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.std()**2              



#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = list(np.where([abs(nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1[0][0]:len(nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = [nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = list(np.where([abs(nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2[0][0]:len(nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = [nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = list(np.where([abs(nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3[0][0]:len(nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = [nPxxfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = list(np.where([abs(nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1[0][0]:len(nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = [nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = list(np.where([abs(nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2[0][0]:len(nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = [nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = list(np.where([abs(nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3[0][0]:len(nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = [nPxxfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241121_0000_0030_stow1_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast1')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241121_0000_0030_stow1_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast1')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()



#%% LS exponential fit method

autocorr_mast1_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0000_0030_stow1_z1)
Lux_mast1_20241121_0000_0030_stow1_z1 = Lux_20241121_0000_0030_stow1_z1[Lux_20241121_0000_0030_stow1_z1>0]

autocorr_mast1_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0000_0030_stow1_z2)
Lux_mast1_20241121_0000_0030_stow1_z2 = Lux_20241121_0000_0030_stow1_z2[Lux_20241121_0000_0030_stow1_z2>0]

autocorr_mast1_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_U_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0000_0030_stow1_z3)
Lux_mast1_20241121_0000_0030_stow1_z3 = Lux_20241121_0000_0030_stow1_z3[Lux_20241121_0000_0030_stow1_z3>0]

autocorr_mast1_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0000_0030_stow1_z1)
Lwx_mast1_20241121_0000_0030_stow1_z1 = Lwx_20241121_0000_0030_stow1_z1[Lwx_20241121_0000_0030_stow1_z1>0]

autocorr_mast1_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0000_0030_stow1_z2)
Lwx_mast1_20241121_0000_0030_stow1_z2 = Lwx_20241121_0000_0030_stow1_z2[Lwx_20241121_0000_0030_stow1_z2>0]

autocorr_mast1_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m1_W_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0000_0030_stow1_z3)
Lwx_mast1_20241121_0000_0030_stow1_z3 = Lwx_20241121_0000_0030_stow1_z3[Lwx_20241121_0000_0030_stow1_z3>0]

Lux_profile_mast1_20241121_0000_0030_stow1 = pd.Series([Lux_mast1_20241121_0000_0030_stow1_z1,Lux_mast1_20241121_0000_0030_stow1_z2,Lux_mast1_20241121_0000_0030_stow1_z3])
Lwx_profile_mast1_20241121_0000_0030_stow1 = pd.Series([Lwx_mast1_20241121_0000_0030_stow1_z1,Lwx_mast1_20241121_0000_0030_stow1_z2,Lwx_mast1_20241121_0000_0030_stow1_z3])
 


#%% Mast 3

overlap = 0
nblock = len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1, Pxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1 = fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1*heights[0]/H3_U_ax_20241121_0000_0030_stow1_z1
nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1 = (fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1*Pxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1)/loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.std()**2

fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2, Pxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2 = fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2*heights[1]/H3_U_ax_20241121_0000_0030_stow1_z2
nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2 = (fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2*Pxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2)/loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.std()**2
 
fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3, Pxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3 = fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3*heights[2]/H3_U_ax_20241121_0000_0030_stow1_z3
nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3 = (fu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3*Pxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3)/loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.std()**2              
    
fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1, Pxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1 = fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1*heights[0]/H3_W_ax_20241121_0000_0030_stow1_z1
nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1 = (fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1*Pxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1)/loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.std()**2

fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2, Pxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2 = fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2*heights[1]/H3_W_ax_20241121_0000_0030_stow1_z2
nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2 = (fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2*Pxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2)/loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.std()**2
 
fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3, Pxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3 = welch(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3 = fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3*heights[2]/H3_W_ax_20241121_0000_0030_stow1_z3
nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3 = (fw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3*Pxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3)/loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = list(np.where([abs(nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1[0][0]:len(nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = [nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = list(np.where([abs(nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2[0][0]:len(nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = [nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = list(np.where([abs(nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3[0][0]:len(nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = [nPxxfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = list(np.where([abs(nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1[0][0]:len(nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1 = [nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z1]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = list(np.where([abs(nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2[0][0]:len(nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2 = [nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z2]

index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = list(np.where([abs(nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3[index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3[0][0]:len(nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3 = [nPxxfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3[0:index_highfreq_loads_mast_20Hz_20241121_0000_0030_stow1_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0000_0030_stow1_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241121_0000_0030_stow1_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast3')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241121_0000_0030_stow1_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0000_0030_stow1_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast3')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()





#%% LS exponential fit method

autocorr_mast3_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0000_0030_stow1_z1)
Lux_mast3_20241121_0000_0030_stow1_z1 = Lux_20241121_0000_0030_stow1_z1[Lux_20241121_0000_0030_stow1_z1>0]

autocorr_mast3_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0000_0030_stow1_z2)
Lux_mast3_20241121_0000_0030_stow1_z2 = Lux_20241121_0000_0030_stow1_z2[Lux_20241121_0000_0030_stow1_z2>0]

autocorr_mast3_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_U_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241121_0000_0030_stow1)
Lux_20241121_0000_0030_stow1_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0000_0030_stow1_z3)
Lux_mast3_20241121_0000_0030_stow1_z3 = Lux_20241121_0000_0030_stow1_z3[Lux_20241121_0000_0030_stow1_z3>0]

autocorr_mast3_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0000_0030_stow1_z1)
Lwx_mast3_20241121_0000_0030_stow1_z1 = Lwx_20241121_0000_0030_stow1_z1[Lwx_20241121_0000_0030_stow1_z1>0]

autocorr_mast3_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0000_0030_stow1_z2)
Lwx_mast3_20241121_0000_0030_stow1_z2 = Lwx_20241121_0000_0030_stow1_z2[Lwx_20241121_0000_0030_stow1_z2>0]

autocorr_mast3_20241121_0000_0030_stow1 = np.correlate(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241121_0000_0030_stow1 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241121_0000_0030_stow1.m3_W_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241121_0000_0030_stow1)
Lwx_20241121_0000_0030_stow1_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0000_0030_stow1_z3)
Lwx_mast3_20241121_0000_0030_stow1_z3 = Lwx_20241121_0000_0030_stow1_z3[Lwx_20241121_0000_0030_stow1_z3>0]

Lux_profile_mast3_20241121_0000_0030_stow1 = pd.Series([Lux_mast3_20241121_0000_0030_stow1_z1,Lux_mast3_20241121_0000_0030_stow1_z2,Lux_mast3_20241121_0000_0030_stow1_z3])
Lwx_profile_mast3_20241121_0000_0030_stow1 = pd.Series([Lwx_mast3_20241121_0000_0030_stow1_z1,Lwx_mast3_20241121_0000_0030_stow1_z2,Lwx_mast3_20241121_0000_0030_stow1_z3])
 

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241121_0000_0030_stow1, heights, label='Lux')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_u^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10000)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241121_0000_0030_stow1, heights, label='Lwx')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_w^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wspd_20241121_0000_0030_stow1_z1,H1_wspd_20241121_0000_0030_stow1_z2,H1_wspd_20241121_0000_0030_stow1_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wspd_20241121_0000_0030_stow1_z1,H2_wspd_20241121_0000_0030_stow1_z2,H2_wspd_20241121_0000_0030_stow1_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wspd_20241121_0000_0030_stow1_z1,H3_wspd_20241121_0000_0030_stow1_z2,H3_wspd_20241121_0000_0030_stow1_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind speed (m/s)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wdir_20241121_0000_0030_stow1_z1,H1_wdir_20241121_0000_0030_stow1_z2,H1_wdir_20241121_0000_0030_stow1_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wdir_20241121_0000_0030_stow1_z1,H2_wdir_20241121_0000_0030_stow1_z2,H2_wdir_20241121_0000_0030_stow1_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wdir_20241121_0000_0030_stow1_z1,H3_wdir_20241121_0000_0030_stow1_z2,H3_wdir_20241121_0000_0030_stow1_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind direction (deg)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(120,180)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iu_20241121_0000_0030_stow1_z1,H1_Iu_20241121_0000_0030_stow1_z2,H1_Iu_20241121_0000_0030_stow1_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iu_20241121_0000_0030_stow1_z1,H2_Iu_20241121_0000_0030_stow1_z2,H2_Iu_20241121_0000_0030_stow1_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iu_20241121_0000_0030_stow1_z1,H3_Iu_20241121_0000_0030_stow1_z2,H3_Iu_20241121_0000_0030_stow1_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_u$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iw_20241121_0000_0030_stow1_z1,H1_Iw_20241121_0000_0030_stow1_z2,H1_Iw_20241121_0000_0030_stow1_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iw_20241121_0000_0030_stow1_z1,H2_Iw_20241121_0000_0030_stow1_z2,H2_Iw_20241121_0000_0030_stow1_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iw_20241121_0000_0030_stow1_z1,H3_Iw_20241121_0000_0030_stow1_z2,H3_Iw_20241121_0000_0030_stow1_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_w$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.2)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241121_0000_0030_stow1/11.23, heights, s=8,label='inflow')            
plt.scatter(Lux_profile_mast1_20241121_0000_0030_stow1/11.23, heights, s=8,label='mast1')            
plt.scatter(Lux_profile_mast3_20241121_0000_0030_stow1/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_u^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,150)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241121_0000_0030_stow1/11.23, heights, s=8,label='inflow')            
plt.scatter(Lwx_profile_mast1_20241121_0000_0030_stow1/11.23, heights, s=8,label='mast1')            
plt.scatter(Lwx_profile_mast3_20241121_0000_0030_stow1/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_w^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()



#%% PSD analysis

heights = [2.75,5.5,11] 
fs = 20

# Spectra
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from numpy import hanning
import math

overlap = 0
nblock = len(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1, Pxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = welch(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1*heights[0]/H1_U_ax_20241121_0300_0330_stow2_z1
nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = (fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1*Pxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1)/loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.std()**2

fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2, Pxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = welch(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2*heights[1]/H1_U_ax_20241121_0300_0330_stow2_z2
nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = (fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2*Pxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2)/loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.std()**2
 
fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3, Pxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = welch(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3*heights[2]/H1_U_ax_20241121_0300_0330_stow2_z3
nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = (fu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3*Pxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3)/loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.std()**2              
    
fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1, Pxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = welch(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1*heights[0]/H1_W_ax_20241121_0300_0330_stow2_z1
nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = (fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1*Pxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1)/loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.std()**2

fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2, Pxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = welch(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2*heights[1]/H1_W_ax_20241121_0300_0330_stow2_z2
nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = (fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2*Pxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2)/loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.std()**2
 
fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3, Pxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = welch(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3*heights[2]/H1_W_ax_20241121_0300_0330_stow2_z3
nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = (fw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3*Pxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3)/loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = list(np.where([abs(nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[0][0]:len(nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1)]
nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z1,200)
nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = [nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[0:index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z1]

index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = list(np.where([abs(nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[0][0]:len(nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2)]
nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z2,200)
nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = [nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[0:index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z2]

index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = list(np.where([abs(nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3)>0.3]))
nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[0][0]:len(nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3)]
nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = runningMeanFast(nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z3,200)
nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = [nPxxfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[0:index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[0][0]-1],nPxxfu_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z3]

index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = list(np.where([abs(nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[0][0]:len(nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1)]
nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z1,200)
nPxxfw_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z1 = [nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[0:index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z1]

index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = list(np.where([abs(nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[0][0]:len(nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2)]
nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z2,200)
nPxxfw_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z2 = [nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[0:index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z2]

index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = list(np.where([abs(nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3)>0.3]))
nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[0][0]:len(nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3)]
nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = runningMeanFast(nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z3,200)
nPxxfw_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z3 = [nPxxfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[0:index_highfreq_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[0][0]-1],nPxxfw_smooth_loads_inflow_20Hz_20241121_0300_0330_stow2_z3]


plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[0:len(nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[0:len(nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[0:len(nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('inflow')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[0:len(nPxxfw_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[0:len(nPxxfw_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[0:len(nPxxfw_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[1])]), nPxxfu_mod_loads_inflow_20Hz_20241121_0300_0330_stow2_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('inflow')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()


#%% Extract data by height

U_corr_inflow_20241121_0300_0330_stow2_z1 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low)
U_corr_inflow_20241121_0300_0330_stow2_z2 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid)
U_corr_inflow_20241121_0300_0330_stow2_z3 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top)

V_corr_inflow_20241121_0300_0330_stow2_z1 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.V_ax_Low)
V_corr_inflow_20241121_0300_0330_stow2_z2 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.V_ax_Mid)
V_corr_inflow_20241121_0300_0330_stow2_z3 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.V_ax_Top)

W_corr_inflow_20241121_0300_0330_stow2_z1 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low)
W_corr_inflow_20241121_0300_0330_stow2_z2 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid)
W_corr_inflow_20241121_0300_0330_stow2_z3 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top)

Ts_corr_inflow_20241121_0300_0330_stow2_z1 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.Ts_Low)
Ts_corr_inflow_20241121_0300_0330_stow2_z2 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.Ts_Mid)
Ts_corr_inflow_20241121_0300_0330_stow2_z3 = pd.Series(loads_inflow_20Hz_20241121_0300_0330_stow2.Ts_Top)

# Detrend
U_corr_inflow_20241121_0300_0330_stow2_z1[U_corr_inflow_20241121_0300_0330_stow2_z1.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241121_0300_0330_stow2_z1.dropna()) 
U_corr_inflow_20241121_0300_0330_stow2_z2[U_corr_inflow_20241121_0300_0330_stow2_z2.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241121_0300_0330_stow2_z2.dropna()) 
U_corr_inflow_20241121_0300_0330_stow2_z3[U_corr_inflow_20241121_0300_0330_stow2_z3.isna()==False] = scipy.signal.detrend(U_corr_inflow_20241121_0300_0330_stow2_z3.dropna()) 

V_corr_inflow_20241121_0300_0330_stow2_z1[V_corr_inflow_20241121_0300_0330_stow2_z1.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241121_0300_0330_stow2_z1.dropna()) 
V_corr_inflow_20241121_0300_0330_stow2_z2[V_corr_inflow_20241121_0300_0330_stow2_z2.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241121_0300_0330_stow2_z2.dropna()) 
V_corr_inflow_20241121_0300_0330_stow2_z3[V_corr_inflow_20241121_0300_0330_stow2_z3.isna()==False] = scipy.signal.detrend(V_corr_inflow_20241121_0300_0330_stow2_z3.dropna()) 

W_corr_inflow_20241121_0300_0330_stow2_z1[W_corr_inflow_20241121_0300_0330_stow2_z1.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241121_0300_0330_stow2_z1.dropna()) 
W_corr_inflow_20241121_0300_0330_stow2_z2[W_corr_inflow_20241121_0300_0330_stow2_z2.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241121_0300_0330_stow2_z2.dropna()) 
W_corr_inflow_20241121_0300_0330_stow2_z3[W_corr_inflow_20241121_0300_0330_stow2_z3.isna()==False] = scipy.signal.detrend(W_corr_inflow_20241121_0300_0330_stow2_z3.dropna()) 

Ts_corr_inflow_20241121_0300_0330_stow2_z1[Ts_corr_inflow_20241121_0300_0330_stow2_z1.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241121_0300_0330_stow2_z1.dropna()) 
Ts_corr_inflow_20241121_0300_0330_stow2_z2[Ts_corr_inflow_20241121_0300_0330_stow2_z2.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241121_0300_0330_stow2_z2.dropna()) 
Ts_corr_inflow_20241121_0300_0330_stow2_z3[Ts_corr_inflow_20241121_0300_0330_stow2_z3.isna()==False] = scipy.signal.detrend(Ts_corr_inflow_20241121_0300_0330_stow2_z3.dropna()) 

# Reynolds stresses and length scales (south2)

inflow_uv_z1_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z1*V_corr_inflow_20241121_0300_0330_stow2_z1).mean()-(U_corr_inflow_20241121_0300_0330_stow2_z1.mean()*V_corr_inflow_20241121_0300_0330_stow2_z1.mean());
inflow_vw_z1_20241121_0300_0330_stow2 = (V_corr_inflow_20241121_0300_0330_stow2_z1*W_corr_inflow_20241121_0300_0330_stow2_z1).mean()-(V_corr_inflow_20241121_0300_0330_stow2_z1.mean()*W_corr_inflow_20241121_0300_0330_stow2_z1.mean());
inflow_uw_z1_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z1*W_corr_inflow_20241121_0300_0330_stow2_z1).mean()-(U_corr_inflow_20241121_0300_0330_stow2_z1.mean()*W_corr_inflow_20241121_0300_0330_stow2_z1.mean());
inflow_wT_z1_20241121_0300_0330_stow2 = (W_corr_inflow_20241121_0300_0330_stow2_z1*Ts_corr_inflow_20241121_0300_0330_stow2_z1).mean()-(W_corr_inflow_20241121_0300_0330_stow2_z1.mean()*Ts_corr_inflow_20241121_0300_0330_stow2_z1.mean());

inflow_uv_z2_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z2*V_corr_inflow_20241121_0300_0330_stow2_z2).mean()-(U_corr_inflow_20241121_0300_0330_stow2_z2.mean()*V_corr_inflow_20241121_0300_0330_stow2_z2.mean());
inflow_vw_z2_20241121_0300_0330_stow2 = (V_corr_inflow_20241121_0300_0330_stow2_z2*W_corr_inflow_20241121_0300_0330_stow2_z2).mean()-(V_corr_inflow_20241121_0300_0330_stow2_z2.mean()*W_corr_inflow_20241121_0300_0330_stow2_z2.mean());
inflow_uw_z2_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z2*W_corr_inflow_20241121_0300_0330_stow2_z2).mean()-(U_corr_inflow_20241121_0300_0330_stow2_z2.mean()*W_corr_inflow_20241121_0300_0330_stow2_z2.mean());
inflow_wT_z2_20241121_0300_0330_stow2 = (W_corr_inflow_20241121_0300_0330_stow2_z2*Ts_corr_inflow_20241121_0300_0330_stow2_z2).mean()-(W_corr_inflow_20241121_0300_0330_stow2_z2.mean()*Ts_corr_inflow_20241121_0300_0330_stow2_z2.mean());

inflow_uv_z3_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z3*V_corr_inflow_20241121_0300_0330_stow2_z3).mean()-(U_corr_inflow_20241121_0300_0330_stow2_z3.mean()*V_corr_inflow_20241121_0300_0330_stow2_z3.mean());
inflow_vw_z3_20241121_0300_0330_stow2 = (V_corr_inflow_20241121_0300_0330_stow2_z3*W_corr_inflow_20241121_0300_0330_stow2_z3).mean()-(V_corr_inflow_20241121_0300_0330_stow2_z3.mean()*W_corr_inflow_20241121_0300_0330_stow2_z3.mean());
inflow_uw_z3_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z3*W_corr_inflow_20241121_0300_0330_stow2_z3).mean()-(U_corr_inflow_20241121_0300_0330_stow2_z3.mean()*W_corr_inflow_20241121_0300_0330_stow2_z3.mean());
inflow_wT_z3_20241121_0300_0330_stow2 = (W_corr_inflow_20241121_0300_0330_stow2_z3*Ts_corr_inflow_20241121_0300_0330_stow2_z3).mean()-(W_corr_inflow_20241121_0300_0330_stow2_z3.mean()*Ts_corr_inflow_20241121_0300_0330_stow2_z3.mean());

utau_z1_20241121_0300_0330_stow2 = (inflow_uw_z1_20241121_0300_0330_stow2**2+inflow_vw_z1_20241121_0300_0330_stow2**2)**(1/4) 
utau_z2_20241121_0300_0330_stow2 = (inflow_uw_z2_20241121_0300_0330_stow2**2+inflow_vw_z2_20241121_0300_0330_stow2**2)**(1/4) 
utau_z3_20241121_0300_0330_stow2 = (inflow_uw_z3_20241121_0300_0330_stow2**2+inflow_vw_z3_20241121_0300_0330_stow2**2)**(1/4) 

L_z1_20241121_0300_0330_stow2 = -1*(utau_z1_20241121_0300_0330_stow2**3)/(0.4*(9.81/H1_Ts_20241121_0300_0330_stow2_z1)*inflow_wT_z1_20241121_0300_0330_stow2)
L_z2_20241121_0300_0330_stow2 = -1*(utau_z2_20241121_0300_0330_stow2**3)/(0.4*(9.81/H1_Ts_20241121_0300_0330_stow2_z2)*inflow_wT_z2_20241121_0300_0330_stow2)
L_z3_20241121_0300_0330_stow2 = -1*(utau_z3_20241121_0300_0330_stow2**3)/(0.4*(9.81/H1_Ts_20241121_0300_0330_stow2_z3)*inflow_wT_z3_20241121_0300_0330_stow2)

zL_z1_20241121_0300_0330_stow2 = heights[0]/L_z1_20241121_0300_0330_stow2
zL_z2_20241121_0300_0330_stow2 = heights[1]/L_z2_20241121_0300_0330_stow2
zL_z3_20241121_0300_0330_stow2 = heights[2]/L_z3_20241121_0300_0330_stow2

inflow_uprimewprime_z1_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z1*W_corr_inflow_20241121_0300_0330_stow2_z1);
inflow_uprimewprime_z2_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z2*W_corr_inflow_20241121_0300_0330_stow2_z2);
inflow_uprimewprime_z3_20241121_0300_0330_stow2 = (U_corr_inflow_20241121_0300_0330_stow2_z3*W_corr_inflow_20241121_0300_0330_stow2_z3);


#%% LS exponential fit method

autocorr_inflow_20241121_0300_0330_stow2 = np.correlate(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0300_0330_stow2_z1)
Lux_20241121_0300_0330_stow2_z1 = Lux_20241121_0300_0330_stow2_z1[Lux_20241121_0300_0330_stow2_z1>0]

autocorr_inflow_20241121_0300_0330_stow2 = np.correlate(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0300_0330_stow2_z2)
Lux_20241121_0300_0330_stow2_z2 = Lux_20241121_0300_0330_stow2_z2[Lux_20241121_0300_0330_stow2_z2>0]

autocorr_inflow_20241121_0300_0330_stow2 = np.correlate(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241121_0300_0330_stow2.U_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0300_0330_stow2_z3)
Lux_20241121_0300_0330_stow2_z3 = Lux_20241121_0300_0330_stow2_z3[Lux_20241121_0300_0330_stow2_z3>0]

autocorr_inflow_20241121_0300_0330_stow2 = np.correlate(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna(), mode='full') 
autocorr_inflow_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna()) * np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna()) + 1, len(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Low.dropna()))
Y = (lags, autocorr_inflow_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0300_0330_stow2_z1)
Lwx_20241121_0300_0330_stow2_z1 = Lwx_20241121_0300_0330_stow2_z1[Lwx_20241121_0300_0330_stow2_z1>0]

autocorr_inflow_20241121_0300_0330_stow2 = np.correlate(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna(), mode='full') 
autocorr_inflow_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna()) * np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna()) + 1, len(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Mid.dropna()))
Y = (lags, autocorr_inflow_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0300_0330_stow2_z2)
Lwx_20241121_0300_0330_stow2_z2 = Lwx_20241121_0300_0330_stow2_z2[Lwx_20241121_0300_0330_stow2_z2>0]

autocorr_inflow_20241121_0300_0330_stow2 = np.correlate(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna(), mode='full') 
autocorr_inflow_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna()) * np.dot(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna(), loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna()) + 1, len(loads_inflow_20Hz_20241121_0300_0330_stow2.W_ax_Top.dropna()))
Y = (lags, autocorr_inflow_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H1_wspd_20241121_0300_0330_stow2_z3)
Lwx_20241121_0300_0330_stow2_z3 = Lwx_20241121_0300_0330_stow2_z3[Lwx_20241121_0300_0330_stow2_z3>0]

Lux_profile_inflow_20241121_0300_0330_stow2 = pd.Series([Lux_20241121_0300_0330_stow2_z1,Lux_20241121_0300_0330_stow2_z2,Lux_20241121_0300_0330_stow2_z3])
Lwx_profile_inflow_20241121_0300_0330_stow2 = pd.Series([Lwx_20241121_0300_0330_stow2_z1,Lwx_20241121_0300_0330_stow2_z2,Lwx_20241121_0300_0330_stow2_z3])
 


#%% Mast 1

overlap = 0
nblock = len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1, Pxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1 = fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1*heights[0]/H2_U_ax_20241121_0300_0330_stow2_z1
nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1 = (fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1*Pxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1)/loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.std()**2

fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2, Pxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2 = fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2*heights[1]/H2_U_ax_20241121_0300_0330_stow2_z2
nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2 = (fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2*Pxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2)/loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.std()**2
 
fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3, Pxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3 = fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3*heights[2]/H2_U_ax_20241121_0300_0330_stow2_z3
nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3 = (fu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3*Pxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3)/loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.std()**2              
    
fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1, Pxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1 = fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1*heights[0]/H2_W_ax_20241121_0300_0330_stow2_z1
nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1 = (fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1*Pxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1)/loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.std()**2

fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2, Pxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2 = fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2*heights[1]/H2_W_ax_20241121_0300_0330_stow2_z2
nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2 = (fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2*Pxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2)/loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.std()**2
 
fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3, Pxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3 = fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3*heights[2]/H2_W_ax_20241121_0300_0330_stow2_z3
nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3 = (fw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3*Pxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3)/loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.std()**2              



#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = list(np.where([abs(nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1[0][0]:len(nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = [nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = list(np.where([abs(nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2[0][0]:len(nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = [nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = list(np.where([abs(nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3[0][0]:len(nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = [nPxxfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = list(np.where([abs(nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1[0][0]:len(nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = [nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = list(np.where([abs(nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2[0][0]:len(nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = [nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = list(np.where([abs(nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3[0][0]:len(nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = [nPxxfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast1_20Hz_20241121_0300_0330_stow2_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast1')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast1_20Hz_20241121_0300_0330_stow2_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast1')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()



#%% LS exponential fit method

autocorr_mast1_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0300_0330_stow2_z1)
Lux_mast1_20241121_0300_0330_stow2_z1 = Lux_20241121_0300_0330_stow2_z1[Lux_20241121_0300_0330_stow2_z1>0]

autocorr_mast1_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0300_0330_stow2_z2)
Lux_mast1_20241121_0300_0330_stow2_z2 = Lux_20241121_0300_0330_stow2_z2[Lux_20241121_0300_0330_stow2_z2>0]

autocorr_mast1_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_U_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0300_0330_stow2_z3)
Lux_mast1_20241121_0300_0330_stow2_z3 = Lux_20241121_0300_0330_stow2_z3[Lux_20241121_0300_0330_stow2_z3>0]

autocorr_mast1_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna(), mode='full') 
autocorr_mast1_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Low.dropna()))
Y = (lags, autocorr_mast1_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0300_0330_stow2_z1)
Lwx_mast1_20241121_0300_0330_stow2_z1 = Lwx_20241121_0300_0330_stow2_z1[Lwx_20241121_0300_0330_stow2_z1>0]

autocorr_mast1_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna(), mode='full') 
autocorr_mast1_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast1_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0300_0330_stow2_z2)
Lwx_mast1_20241121_0300_0330_stow2_z2 = Lwx_20241121_0300_0330_stow2_z2[Lwx_20241121_0300_0330_stow2_z2>0]

autocorr_mast1_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna(), mode='full') 
autocorr_mast1_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m1_W_ax_Top.dropna()))
Y = (lags, autocorr_mast1_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H2_wspd_20241121_0300_0330_stow2_z3)
Lwx_mast1_20241121_0300_0330_stow2_z3 = Lwx_20241121_0300_0330_stow2_z3[Lwx_20241121_0300_0330_stow2_z3>0]

Lux_profile_mast1_20241121_0300_0330_stow2 = pd.Series([Lux_mast1_20241121_0300_0330_stow2_z1,Lux_mast1_20241121_0300_0330_stow2_z2,Lux_mast1_20241121_0300_0330_stow2_z3])
Lwx_profile_mast1_20241121_0300_0330_stow2 = pd.Series([Lwx_mast1_20241121_0300_0330_stow2_z1,Lwx_mast1_20241121_0300_0330_stow2_z2,Lwx_mast1_20241121_0300_0330_stow2_z3])
 


#%% Mast 3

overlap = 0
nblock = len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low)
win = np.hamming(math.floor(nblock/10))

fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1, Pxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1 = fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1*heights[0]/H3_U_ax_20241121_0300_0330_stow2_z1
nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1 = (fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1*Pxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1)/loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.std()**2

fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2, Pxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2 = fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2*heights[1]/H3_U_ax_20241121_0300_0330_stow2_z2
nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2 = (fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2*Pxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2)/loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.std()**2
 
fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3, Pxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3 = fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3*heights[2]/H3_U_ax_20241121_0300_0330_stow2_z3
nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3 = (fu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3*Pxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3)/loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.std()**2              
    
fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1, Pxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1 = fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1*heights[0]/H3_W_ax_20241121_0300_0330_stow2_z1
nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1 = (fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1*Pxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1)/loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.std()**2

fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2, Pxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2 = fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2*heights[1]/H3_W_ax_20241121_0300_0330_stow2_z2
nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2 = (fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2*Pxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2)/loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.std()**2
 
fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3, Pxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3 = welch(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna(), fs, window=win, noverlap=overlap, nfft=nblock, detrend='constant', return_onesided=True)
nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3 = fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3*heights[2]/H3_W_ax_20241121_0300_0330_stow2_z3
nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3 = (fw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3*Pxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3)/loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.std()**2              


#%% Smooth high frequency region

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = list(np.where([abs(nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1[0][0]:len(nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = [nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = list(np.where([abs(nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2[0][0]:len(nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = [nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = list(np.where([abs(nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3)>0.3]))
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3[0][0]:len(nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3)]
nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = runningMeanFast(nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3,200)
nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = [nPxxfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3[0][0]-1],nPxxfu_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = list(np.where([abs(nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1[0][0]:len(nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1 = [nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z1[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z1]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = list(np.where([abs(nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2[0][0]:len(nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2 = [nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z2[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z2]

index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = list(np.where([abs(nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3)>0.3]))
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3[index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3[0][0]:len(nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3)]
nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = runningMeanFast(nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3,200)
nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3 = [nPxxfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3[0:index_highfreq_loads_mast_20Hz_20241121_0300_0330_stow2_z3[0][0]-1],nPxxfw_smooth_loads_mast_20Hz_20241121_0300_0330_stow2_z3]



plt.figure()
plt.subplot(1, 2, 1)
plt.loglog(abs(nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z1[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1[1], label='2.75m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z2[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2[1], label='5m')            
plt.loglog(abs(nfu_loads_mast3_20Hz_20241121_0300_0330_stow2_z3[0:len(nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3[1], label='7m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_u/\sigma_u$")
plt.title('mast3')
plt.xlim(10e-3, 10e1)
plt.ylim(10e-4, 5*10e-2)
plt.show()
    
plt.subplot(1, 2, 2)
plt.loglog(abs(nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z1[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z1[1], label='2.75m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z2[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z2[1], label='5.5m')            
plt.loglog(abs(nfw_loads_mast3_20Hz_20241121_0300_0330_stow2_z3[0:len(nPxxfw_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3[1])]), nPxxfu_mod_loads_mast_20Hz_20241121_0300_0330_stow2_z3[1], label='11m')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$fz/U$")
plt.ylabel("$fS_w/\sigma_w$")
plt.title('mast3')
plt.xlim(10e-2, 10e2)
plt.ylim(10e-4, 5*10e-2)
plt.show()





#%% LS exponential fit method

autocorr_mast3_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0300_0330_stow2_z1)
Lux_mast3_20241121_0300_0330_stow2_z1 = Lux_20241121_0300_0330_stow2_z1[Lux_20241121_0300_0330_stow2_z1>0]

autocorr_mast3_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0300_0330_stow2_z2)
Lux_mast3_20241121_0300_0330_stow2_z2 = Lux_20241121_0300_0330_stow2_z2[Lux_20241121_0300_0330_stow2_z2>0]

autocorr_mast3_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_U_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241121_0300_0330_stow2)
Lux_20241121_0300_0330_stow2_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0300_0330_stow2_z3)
Lux_mast3_20241121_0300_0330_stow2_z3 = Lux_20241121_0300_0330_stow2_z3[Lux_20241121_0300_0330_stow2_z3>0]

autocorr_mast3_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna(), mode='full') 
autocorr_mast3_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Low.dropna()))
Y = (lags, autocorr_mast3_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z1 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0300_0330_stow2_z1)
Lwx_mast3_20241121_0300_0330_stow2_z1 = Lwx_20241121_0300_0330_stow2_z1[Lwx_20241121_0300_0330_stow2_z1>0]

autocorr_mast3_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna(), mode='full') 
autocorr_mast3_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Mid.dropna()))
Y = (lags, autocorr_mast3_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z2 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0300_0330_stow2_z2)
Lwx_mast3_20241121_0300_0330_stow2_z2 = Lwx_20241121_0300_0330_stow2_z2[Lwx_20241121_0300_0330_stow2_z2>0]

autocorr_mast3_20241121_0300_0330_stow2 = np.correlate(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna(), mode='full') 
autocorr_mast3_20241121_0300_0330_stow2 /= np.sqrt(np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna()) * np.dot(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna(), loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna()))  # Normalize the result
lags = np.arange(-len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna()) + 1, len(loads_mast_20Hz_20241121_0300_0330_stow2.m3_W_ax_Top.dropna()))
Y = (lags, autocorr_mast3_20241121_0300_0330_stow2)
Lwx_20241121_0300_0330_stow2_z3 = Y[0][np.where(Y[1]==find_nearest(Y[1], value=1/np.e))]*(1/fs)*abs(H3_wspd_20241121_0300_0330_stow2_z3)
Lwx_mast3_20241121_0300_0330_stow2_z3 = Lwx_20241121_0300_0330_stow2_z3[Lwx_20241121_0300_0330_stow2_z3>0]

Lux_profile_mast3_20241121_0300_0330_stow2 = pd.Series([Lux_mast3_20241121_0300_0330_stow2_z1,Lux_mast3_20241121_0300_0330_stow2_z2,Lux_mast3_20241121_0300_0330_stow2_z3])
Lwx_profile_mast3_20241121_0300_0330_stow2 = pd.Series([Lwx_mast3_20241121_0300_0330_stow2_z1,Lwx_mast3_20241121_0300_0330_stow2_z2,Lwx_mast3_20241121_0300_0330_stow2_z3])
 

plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241121_0300_0330_stow2, heights, label='Lux')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_u^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10000)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241121_0300_0330_stow2, heights, label='Lwx')            
plt.legend(loc='upper right',fontsize=8)
plt.xlabel("$L_w^x$ (m)")
plt.ylabel("$z$ (m)")
plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wspd_20241121_0300_0330_stow2_z1,H1_wspd_20241121_0300_0330_stow2_z2,H1_wspd_20241121_0300_0330_stow2_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wspd_20241121_0300_0330_stow2_z1,H2_wspd_20241121_0300_0330_stow2_z2,H2_wspd_20241121_0300_0330_stow2_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wspd_20241121_0300_0330_stow2_z1,H3_wspd_20241121_0300_0330_stow2_z2,H3_wspd_20241121_0300_0330_stow2_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind speed (m/s)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,10)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_wdir_20241121_0300_0330_stow2_z1,H1_wdir_20241121_0300_0330_stow2_z2,H1_wdir_20241121_0300_0330_stow2_z3], heights, s=8,label='inflow')            
plt.scatter([H2_wdir_20241121_0300_0330_stow2_z1,H2_wdir_20241121_0300_0330_stow2_z2,H2_wdir_20241121_0300_0330_stow2_z3], heights, s=8,label='mast1')            
plt.scatter([H3_wdir_20241121_0300_0330_stow2_z1,H3_wdir_20241121_0300_0330_stow2_z2,H3_wdir_20241121_0300_0330_stow2_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("Wind direction (deg)")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(120,180)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iu_20241121_0300_0330_stow2_z1,H1_Iu_20241121_0300_0330_stow2_z2,H1_Iu_20241121_0300_0330_stow2_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iu_20241121_0300_0330_stow2_z1,H2_Iu_20241121_0300_0330_stow2_z2,H2_Iu_20241121_0300_0330_stow2_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iu_20241121_0300_0330_stow2_z1,H3_Iu_20241121_0300_0330_stow2_z2,H3_Iu_20241121_0300_0330_stow2_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_u$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter([H1_Iw_20241121_0300_0330_stow2_z1,H1_Iw_20241121_0300_0330_stow2_z2,H1_Iw_20241121_0300_0330_stow2_z3], heights, s=8,label='inflow')            
plt.scatter([H2_Iw_20241121_0300_0330_stow2_z1,H2_Iw_20241121_0300_0330_stow2_z2,H2_Iw_20241121_0300_0330_stow2_z3], heights, s=8,label='mast1')            
plt.scatter([H3_Iw_20241121_0300_0330_stow2_z1,H3_Iw_20241121_0300_0330_stow2_z2,H3_Iw_20241121_0300_0330_stow2_z3], heights, s=8,label='mast3')            
plt.legend(loc='lower left',fontsize=8)
plt.xlabel("$I_w$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.2)
plt.ylim(0,12)
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(Lux_profile_inflow_20241121_0300_0330_stow2/11.23, heights, s=8,label='inflow')            
plt.scatter(Lux_profile_mast1_20241121_0300_0330_stow2/11.23, heights, s=8,label='mast1')            
plt.scatter(Lux_profile_mast3_20241121_0300_0330_stow2/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_u^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,100)
plt.ylim(0,12)
plt.show()

plt.figure()
plt.subplot(1, 2, 2)
plt.scatter(Lwx_profile_inflow_20241121_0300_0330_stow2/11.23, heights, s=8,label='inflow')            
plt.scatter(Lwx_profile_mast1_20241121_0300_0330_stow2/11.23, heights, s=8,label='mast1')            
plt.scatter(Lwx_profile_mast3_20241121_0300_0330_stow2/11.23, heights, s=8,label='mast3')            
plt.legend(loc='lower right',fontsize=8)
plt.xlabel("$L_w^x/c$")
plt.ylabel("$z$ (m)")
#plt.title('inflow')
plt.xlim(0,0.4)
plt.ylim(0,12)
plt.show()





#%% Plot histogram of load coefficients (October 28, 2024)

plt.figure()
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H1_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_CF_Lift']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H2_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_CF_Lift']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H3_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_CF_Lift']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Operation (11:20-11:50, October 28, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H1_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_CF_Lift']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H2_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_CF_Lift']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H3_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_CF_Lift']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, October 28, 2024)')
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Operation (11:20-11:50, October 28, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, October 28, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Operation (11:20-11:50, October 28, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, October 28, 2024)')
plt.xticks([-0.1,-0.05,0,0.05,0.1])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Operation (11:20-11:50, October 28, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, October 28, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241028_1820_1850_operation['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Operation (11:20-11:50, October 28, 2024)')
plt.xticks([-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241028_2030_2100_stow['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, October 28, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()




#%% Plot histogram of load coefficients (November 15, 2024)

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H1_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_CF_Lift']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H2_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_CF_Lift']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H3_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_CF_Lift']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Operation (12:45-13:15, November 15, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H1_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_CF_Lift']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H2_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_CF_Lift']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H3_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_CF_Lift']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, November 15, 2024)')
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Operation (12:45-13:15, November 15, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, November 15, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Operation (12:45-13:15, November 15, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, November 15, 2024)')
plt.xticks([-0.1,-0.05,0,0.05,0.1])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Operation (12:45-13:15, November 15, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, November 15, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_2045_2115_operation['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Operation (12:45-13:15, November 15, 2024)')
plt.xticks([-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_2130_2200_stow['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Stow (13:30-14:00, November 15, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()



plt.figure()
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_CF_Lift']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_CF_Lift']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_CF_Lift']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Stow H1H2 (10:00-10:30, November 15, 2024)')
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow H1H2 (10:00-10:30, November 15, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow H1H2 (10:00-10:30, November 15, 2024)')
plt.xticks([-0.1,-0.05,0,0.05,0.1])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Stow H1H2 (10:00-10:30, November 15, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241115_1800_1830_stowH1H2['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Stow H1H2 (10:00-10:30, November 15, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()



#%% Plot histogram of load coefficients (November 18, 2024)

plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H1_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_CF_Lift']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H2_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_CF_Lift']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H3_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_CF_Lift']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:40-09:00, November 18, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H1_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_CF_Lift']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H2_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_CF_Lift']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H3_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_CF_Lift']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:40-11:00, November 18, 2024)')
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:40-09:00, November 18, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:40-11:00, November 18, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:40-09:00, November 18, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:40-11:00, November 18, 2024)')
plt.xticks([-0.1,-0.05,0,0.05,0.1])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 0.5, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:40-09:00, November 18, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:40-11:00, November 18, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241118_1640_1700_operation['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:40-09:00, November 18, 2024)')
plt.xticks([-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241118_1840_1900_stow['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:40-11:00, November 18, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()


#%% Plot histogram of load coefficients (November 20, 2024)

plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H1_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_CF_Lift']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H2_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_CF_Lift']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H3_CF_Lift'], bins=np.arange(-3, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_CF_Lift']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:00-08:30, November 20, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H1_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_CF_Lift']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H2_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_CF_Lift']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H3_CF_Lift'], bins=np.arange(-1, 1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_CF_Lift']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:00-10:30, November 20, 2024)')
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.5, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:00-08:30, November 20, 2024)')
plt.xticks([-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:00-10:30, November 20, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Torque_coefficient'], bins=np.arange(-1, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Torque_coefficient'], bins=np.arange(-1, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Torque_coefficient'], bins=np.arange(-1, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:00-08:30, November 20, 2024)')
plt.xticks([-1,-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.1, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:00-10:30, November 20, 2024)')
plt.xticks([-0.1,-0.05,0,0.05,0.1])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-3, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:00-08:30, November 20, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:00-10:30, November 20, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-3, 3, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-3, 3, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-3, 3, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241120_1600_1630_operation['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Operation (08:00-08:30, November 20, 2024)')
plt.xticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241120_1800_1830_stow['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Stow (10:00-10:30, November 20, 2024)')
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4])
plt.legend(loc='upper left',fontsize=10)
plt.show()


#%% Plot histogram of load coefficients (November 21, 2024)

plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_CF_Lift'], bins=np.arange(-1.5, 1.5, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_CF_Lift']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_CF_Lift'], bins=np.arange(-1.5, 1.5, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_CF_Lift']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_CF_Lift'], bins=np.arange(-1.5, 1.5, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_CF_Lift']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Stow1 (16:00-16:30, November 20, 2024)')
plt.xticks([-1.5,-1,-0.5,0,0.5,1,1.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_CF_Lift'], bins=np.arange(-1.5, 1.5, 0.01), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_CF_Lift']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_CF_Lift']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_CF_Lift'], bins=np.arange(-1.5, 1.5, 0.01), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_CF_Lift']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_CF_Lift']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_CF_Lift'], bins=np.arange(-1.5, 1.5, 0.01), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_CF_Lift']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_CF_Lift']),density=False,alpha=0.3,label='H3')
plt.xlabel('Lift force coefficient')
plt.ylabel('Frequency')
plt.title('Stow2 (19:00-19:30, November 21, 2024)')
plt.xticks([-1.5,-1,-0.5,0,0.5,1,1.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow1 (16:00-16:30, November 20, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Torque_Tube_Torque_Left_coefficient'], bins=np.arange(-0.2, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Torque_Tube_Torque_Left_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Torque_Tube_Torque_Left_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Hinge moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow2 (19:00-19:30, November 21, 2024)')
plt.xticks([-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.3, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.3, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.3, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow1 (16:00-16:30, November 20, 2024)')
plt.xticks([-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.3, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.3, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Torque_coefficient'], bins=np.arange(-0.1, 0.3, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Torque_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Torque_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Azimuth moment coefficient')
plt.ylabel('Frequency')
plt.title('Stow2 (19:00-19:30, November 21, 2024)')
plt.xticks([-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3])
plt.legend(loc='upper left',fontsize=10)
plt.show()


plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Stow1 (16:00-16:30, November 20, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Bend_1_coefficient'], bins=np.arange(-0.5, 0.5, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Bend_1_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Bend_1_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 1 coefficient')
plt.ylabel('Frequency')
plt.title('Stow2 (19:00-19:30, November 21, 2024)')
plt.xticks([-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241121_0000_0030_stow1['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Stow1 (16:00-16:30, November 20, 2024)')
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4])
plt.legend(loc='upper left',fontsize=10)
plt.show()

plt.figure()
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#1f77b4', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H1_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H1')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#ff7f0e', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H2_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H2')
plt.hist(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Bend_2_coefficient'], bins=np.arange(-1, 0.4, 0.001), color='#2ca02c', edgecolor='none',weights=np.ones(len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Bend_2_coefficient']))/len(loads_inflow_20Hz_20241121_0300_0330_stow2['H3_Pedestal_Bend_2_coefficient']),density=False,alpha=0.3,label='H3')
plt.xlabel('Overturning moment 2 coefficient')
plt.ylabel('Frequency')
plt.title('Stow2 (19:00-19:30, November 21, 2024)')
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4])
plt.legend(loc='upper left',fontsize=10)
plt.show()



