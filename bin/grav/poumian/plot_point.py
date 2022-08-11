import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
poumian = pd.read_csv('重力部分/剖面去漂移数据/poumian.csv')
no = poumian['no']
value = poumian['value']
jinggai = pd.read_csv('重力部分/剖面原始数据/jgai.csv')
nojg = jinggai['nojg']
vjg = jinggai['value']
plt.figure(figsize=(10,8))
plt.plot(no,value,label='Relative Grav',linewidth=3)
plt.scatter(nojg,vjg,color='red',label='Manhole Cover')
plt.grid(True)
dx = [195,211]
dy = [0.125,0.125]
plt.plot(dx,dy,color='red',label='Platform',linewidth=3)
plt.legend(fontsize=10,loc='upper right')
plt.ylabel('Relative Grav/mGal',fontsize=14)
plt.xlabel('No',fontsize=14)
plt.xlim(100,316)
savepath = '重磁报告/fig/grav'
filename = 'xd_jg.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
