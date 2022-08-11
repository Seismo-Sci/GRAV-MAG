import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
savepath = '重磁报告\\fig\\grav'
data = pd.read_csv('重力部分\\静态实验\\#916.csv')
temp = data['TEMP']
time = data['DEC.TIME+DATE']
# temp = temp-temp[0]
#temperature profile
# plt.figure(figsize=(10,8))
# bwith = 2
# ax = plt.gca()
# ax.spines['bottom'].set_linewidth(bwith)
# ax.spines['left'].set_linewidth(bwith)
# ax.spines['top'].set_linewidth(bwith)
# ax.spines['right'].set_linewidth(bwith)
# plt.plot(time,temp,linewidth=0.6)
# plt.grid(True)
# plt.xlabel('time (DEC.TIME+DATE)',fontsize=14)
# plt.ylabel('Temperature/°c',fontsize=14)
# plt.title('#916 Temperature Profile',fontsize=16)
# filename = 'jt_temp.jpg'
# plt.savefig(os.path.join(savepath,filename),dpi=600)
# plt.show()



##jingtaishiyanquxian
grav = data['GRAV.'].to_numpy()
time = data['DEC.TIME+DATE'].to_numpy()
grav_mean = grav.mean()
time_mean = time.mean()
ssxy = (grav-grav_mean)*(time-time_mean)
ssxx = (time-time_mean)*(time-time_mean)
b = ssxy.sum()/ssxx.sum()
a = grav.mean()-b*time.mean()
y = a+b*time
cancha = grav-y
# plt.plot(time,y)
# plt.scatter(time,grav,c='red',s=0.1)
# plt.plot(time,cancha,color='blue')
# plt.show()
# fig,ax = plt.subplots(figsize=(10,8))
# plt.grid(True)
# lin1 = ax.plot(time,y,label='Fitting line',linewidth=1)
# lin2 = ax.scatter(time,grav,c='red',s=0.2,label='Observation')
# ax.set_xlabel('Time (DEC.TIME+DATE)',fontsize=14)
# ax.set_ylabel('Grav/mGal',fontsize=14)
# plt.grid(True)
# plt.legend(fontsize=10)

# ax2 = ax.twinx()
# lin3 = ax2.plot(time,cancha,color='blue',label='Residual',linewidth=0.6)
# ax2.set_ylabel('Residual/mGal',fontsize=14)
# plt.legend(fontsize=10)
# filename = 'jt_shiyan.jpg'
# plt.title('#916 Static test',fontsize=16)
# bwith = 2
# ax = plt.gca()
# ax.spines['bottom'].set_linewidth(bwith)
# ax.spines['left'].set_linewidth(bwith)
# ax.spines['top'].set_linewidth(bwith)
# ax.spines['right'].set_linewidth(bwith)
# plt.savefig(os.path.join(savepath,filename),dpi=600)
# plt.show()

# plt.plot(range(len(cancha)),cancha)
# plt.show()

from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
# Number of sample points
fs = 1
N = len(cancha)
f, t, Zxx = signal.stft(cancha, fs, nperseg=256)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=0.0001, shading='gouraud')
plt.title('STFT Magnitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
