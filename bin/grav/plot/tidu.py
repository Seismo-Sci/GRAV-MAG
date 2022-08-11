import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
tidu = pd.read_csv('重力部分/其他数据/梯度.csv')
no = tidu['no']
tidu = tidu['tidu']
plt.figure(figsize=(10,4))
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,tidu,color='blue',label='Gravity gradient',linewidth=2,marker='o')
plt.xlabel('No',fontsize=14)
plt.ylabel('Gravity gradient/mGal',fontsize=14)
plt.title('Gravity gradient from 192 to 214',fontsize=16)
plt.xlim(192,214)
plt.grid(True)
filename = 'td.jpg'
savepath = '重磁报告/fig/grav'
plt.savefig(os.path.join(savepath,filename))
plt.show()