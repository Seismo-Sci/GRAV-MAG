import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
fkd = pd.read_csv('重力部分/防空洞/fkd.csv')
print(fkd)
v65_1 = fkd['1465_1']
v65_2 = fkd['1465_2'][0:8]
v66_1 = fkd['1466_1']
v66_2 = fkd['1466_2'][0:8]
plt.figure(figsize=(10,4))
plt.plot(range(1,len(v65_1)+1),v65_1,label='#1465',marker='o',linewidth=2,color='blue')
plt.plot(range(1,len(v66_1)+1),v66_1,label='#1466',marker='o',linewidth=2,color='red')
plt.legend(fontsize=10,loc='upper right')
plt.xlabel('No',fontsize=14)
plt.xlim(1,9)
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
filename='dt_1.jpg'
savepath = '重磁报告/fig/grav'
plt.savefig(os.path.join(savepath,filename))
plt.show()

plt.figure(figsize=(10,4))
plt.plot(range(1,len(v65_2)+1),v65_2,label='#1465',marker='o',linewidth=2,color='blue')
plt.plot(range(1,len(v66_2)+1),v66_2,label='#1466',marker='o',linewidth=2,color='red')
plt.legend(fontsize=10,loc='upper right')
plt.xlabel('No',fontsize=14)
plt.xlim(1,8)
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
filename='dt_2.jpg'
savepath = '重磁报告/fig/grav'
plt.savefig(os.path.join(savepath,filename))
plt.show()