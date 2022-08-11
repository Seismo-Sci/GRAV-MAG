import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
neh = pd.read_csv('重力部分\\正常场校正\\20220730.txt')[1:119]
h_origin = neh['h']
no = neh['no']
plt.figure(figsize=(10,8))
plt.grid(True)
plt.scatter(no,h_origin,label='Origin',color='red')
h = pd.read_csv('重力部分\正常场校正\height.txt')
h = h['height']
plt.plot(no,h,color='blue',label='After process',linewidth=2)
plt.xlabel('No',fontsize=14)
plt.ylabel('Height/m',fontsize=14)
plt.legend(fontsize=10)
v211x = [211,211]
v211y = [0,50]
v195x = [195,195]
v195y = [0,50]
plt.plot(v211x,v211y,color='black')
plt.plot(v195x,v195y,color='black')
plt.ylim(h_origin.min(),h_origin.max()+5)
plt.xlim(100,316)
savepath = '重磁报告\\fig\\grav'
filename = 'h_compare.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()