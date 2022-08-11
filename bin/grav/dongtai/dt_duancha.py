import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import os
savepath = '重磁报告\\fig\\grav'
data = pd.read_csv('重力部分\\动态试验\\dc_two.csv')
duancha = data['two'].to_numpy()
duancha_two = duancha-duancha.mean()
data = pd.read_csv('重力部分\\动态试验\\dc_back.csv')
duancha = data['back'].to_numpy()
duancha_back = duancha-duancha.mean()
plt.figure(figsize=(10,8))
ax1 = plt.subplot(211)
plt.grid(True)
x = MultipleLocator(1)
ax1.xaxis.set_major_locator(x)
ax1.plot(range(1,len(duancha_two)+1),duancha_two)
plt.xlim(1,37)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
ax2 = plt.subplot(212)
plt.grid(True)
x = MultipleLocator(1)
ax2.xaxis.set_major_locator(x)
ax2.plot(range(1,len(duancha_back)+1),duancha_back)
plt.xlim(1,18)
plt.xlabel('No',fontsize=14)
filename = 'dt_duancha.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()