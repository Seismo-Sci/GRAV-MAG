import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
data = pd.read_csv('磁力部分/静态实验.csv')
print(data)
d11 = data['11']
d12 = data['12']
d13 = data['13']
d14 = data['14']
d15 = data['15']
t = data['时间']
plt.figure(figsize=(10,4))
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(t,d11,label='Gem_11',linewidth=1)
plt.plot(t,d12,label='Gem_12',linewidth=1)
plt.plot(t,d13,label='Gem_13',linewidth=1)
plt.plot(t,d14,label='Gem_14',linewidth=1)
plt.plot(t,d15,label='Gem_15',linewidth=1)
plt.xlim(0,10)
plt.xlabel('Time [min]',fontsize=14)
plt.ylabel('nT',fontsize=14)
plt.legend(fontsize=10,loc='upper right')
filename = 'jt_plot.jpg'
savepath = '重磁报告/fig/mag'
plt.savefig(os.path.join(savepath,filename))
plt.show()