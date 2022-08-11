import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
data = pd.read_csv('重力部分/联合反演/poumian.csv')
print(data)
nobu = data['nobu']
buge = data['buge']
noci = data['noci'][0:109]
ci = data['ci'][0:109]
fig,ax = plt.subplots(figsize=(10,4))
plt.grid(True)
lin1 = ax.plot(nobu,buge,label='Bouguer gravity anomaly',color='red')
ax.set_xlabel('No',fontsize=14)
ax.set_ylabel('mGal',fontsize=14)
plt.grid(True)

ax2 = ax.twinx()
lin3 = ax2.plot(noci,ci,color='blue',label='Magnetic anomaly')
ax2.set_ylabel('nT',fontsize=14)
lin = lin1+lin3
labs = [l.get_label() for l in lin]
ax.legend(lin,labs,fontsize=10,loc='upper left')
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
filename = 'zc.jpg'
savepath = '重磁报告/fig/grav'
plt.savefig(os.path.join(savepath,filename))
plt.show()

fig,ax = plt.subplots(figsize=(6,4))
plt.grid(True)
lin1 = ax.plot(nobu,buge,label='Bouguer gravity anomaly',color='red')
ax.set_xlabel('No',fontsize=14)
ax.set_ylabel('mGal',fontsize=14)
plt.grid(True)

ax2 = ax.twinx()
lin3 = ax2.plot(noci,ci,color='blue',label='Magnetic anomaly')
ax2.set_ylabel('nT',fontsize=14)
lin = lin1+lin3
labs = [l.get_label() for l in lin]
ax.legend(lin,labs,fontsize=10,loc='upper left')
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
filename = 'zc_1.jpg'
savepath = '重磁报告/fig/grav'
plt.title('100-160',fontsize=16)
plt.xlim(100,160)
plt.savefig(os.path.join(savepath,filename))
plt.show()

fig,ax = plt.subplots(figsize=(6,4))
plt.grid(True)
lin1 = ax.plot(nobu,buge,label='Bouguer gravity anomaly',color='red')
ax.set_xlabel('No',fontsize=14)
ax.set_ylabel('mGal',fontsize=14)
plt.grid(True)

ax2 = ax.twinx()
lin3 = ax2.plot(noci,ci,color='blue',label='Magnetic anomaly')
ax2.set_ylabel('nT',fontsize=14)
lin = lin1+lin3
labs = [l.get_label() for l in lin]
ax.legend(lin,labs,fontsize=10,loc='upper left')
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
filename = 'zc_2.jpg'
savepath = '重磁报告/fig/grav'
plt.title('160-250',fontsize=16)
plt.xlim(160,250)
plt.savefig(os.path.join(savepath,filename))
plt.show()
fig,ax = plt.subplots(figsize=(6,4))
plt.grid(True)
lin1 = ax.plot(nobu,buge,label='Bouguer gravity anomaly',color='red')
ax.set_xlabel('No',fontsize=14)
ax.set_ylabel('mGal',fontsize=14)
plt.grid(True)

ax2 = ax.twinx()
lin3 = ax2.plot(noci,ci,color='blue',label='Magnetic anomaly')
ax2.set_ylabel('nT',fontsize=14)
lin = lin1+lin3
labs = [l.get_label() for l in lin]
ax.legend(lin,labs,fontsize=10,loc='upper left')
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
filename = 'zc_3.jpg'
savepath = '重磁报告/fig/grav'
plt.title('250-286',fontsize=16)
plt.xlim(250,286)
plt.savefig(os.path.join(savepath,filename))
plt.show()
fig,ax = plt.subplots(figsize=(6,4))
plt.grid(True)
lin1 = ax.plot(nobu,buge,label='Bouguer gravity anomaly',color='red')
ax.set_xlabel('No',fontsize=14)
ax.set_ylabel('mGal',fontsize=14)
plt.grid(True)

ax2 = ax.twinx()
lin3 = ax2.plot(noci,ci,color='blue',label='Magnetic anomaly')
ax2.set_ylabel('nT',fontsize=14)
lin = lin1+lin3
labs = [l.get_label() for l in lin]
ax.legend(lin,labs,fontsize=10,loc='upper left')
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
filename = 'zc_4.jpg'
savepath = '重磁报告/fig/grav'
plt.title('250-316',fontsize=16)
plt.xlim(250,316)
plt.savefig(os.path.join(savepath,filename))
plt.show()