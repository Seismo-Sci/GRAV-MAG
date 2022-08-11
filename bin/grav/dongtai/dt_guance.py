import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
savepath = '重磁报告\\fig\\grav'
data = pd.read_csv('重力部分\\动态试验\\#916.csv')
######时间######
t = data['TIME']
TIME = []
for i in range(len(t)):
    hour = t[i].split(':')[0]
    min = t[i].split(':')[1]
    sec = t[i].split(':')[2]
    TIME.append(float(hour)+float(min)/60+float(sec)/3600)
#####往返观测######
value = data['GRAV.'].to_numpy()
time = data['DEC.TIME+DATE']
value1 = []
for i in range(18,-1,-1):
    value1.append(value[i])
value2 = []
for i in range(20,39,):
    value2.append(value[i])
v1 = np.array(value1)
v2 = np.array(value2)
vres = v2-v1
vres = np.array(vres)
time = np.array(TIME[20:39])

ssxy = (vres-vres.mean())*(time-time.mean())
ssxx = (time-time.mean())*(time-time.mean())
b = ssxy.sum()/ssxx.sum()
a = vres.mean()-b*time.mean()
y = a+b*time
cancha = vres-y
#plot
fig,ax = plt.subplots(figsize=(10,8))
plt.grid(True)
lin1 = ax.plot(time,y,label='Fitting line',color='red')
lin2 = ax.plot(time,vres,label='Observation',marker='o',color='steelblue')
ax.set_xlabel('Time (DEC.TIME+DATE)',fontsize=14)
ax.set_ylabel('Grav/mGal',fontsize=14)
plt.grid(True)

ax2 = ax.twinx()
lin3 = ax2.plot(time,cancha,color='blue',label='Residual',marker='o')
ax2.set_ylabel('Residual/mGal',fontsize=14)
lin = lin1+lin2+lin3
labs = [l.get_label() for l in lin]
plt.ylim(-0.04,0.04)
ax.legend(lin,labs,fontsize=10,loc='upper right')
filename = 'jt_shiyan.jpg'
plt.title('#916 Dynamic test',fontsize=16)
filename = 'dt_shiyan.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()