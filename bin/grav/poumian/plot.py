import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
poumian = pd.read_csv('重力部分/剖面去漂移数据/poumian.csv')
no = poumian['no']
value = poumian['value']
# plt.plot(no,value)
# plt.show()
height = pd.read_csv('重力部分/正常场校正/height.txt')
h = height['height']
# plt.plot(no,h)
# plt.show()
fig,ax = plt.subplots(figsize=(10,8))
plt.grid(True)
lin1 = ax.plot(no,value,label='Relative Grav',linewidth=3)
ax.set_xlabel('No',fontsize=14)
ax.set_ylabel('Relative Grav/mGal',fontsize=14)
plt.grid(True)
plt.legend(fontsize=10)

ax2 = ax.twinx()
lin2 = ax2.plot(no,h,color='blue',label='Height',linewidth=3)
ax2.set_ylabel('Height/m',fontsize=14)
lin = lin1+lin2
labs = [l.get_label() for l in lin]
ax.legend(lin,labs,fontsize=10,loc='upper left')
filename = 'xd_grav_height.jpg'
savepath = '重磁报告/fig/grav'
plt.xlim(100,316)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()