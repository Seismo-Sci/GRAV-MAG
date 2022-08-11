import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
poumian = pd.read_csv('重力部分/剖面去漂移数据/poumian.csv')
no = poumian['no']
value = poumian['value']
no = no[45:68]
value = value[45:68]
plt.figure(figsize=(20,4))
plt.plot(no,value,linewidth=3)
v211x = [211,211]
v211y = [0,0.5]
v195x = [195,195]
v195y = [0,0.5]
plt.plot(v211x,v211y,color='red')
plt.plot(v195x,v195y,color='red')
plt.ylim(value.min(),value.max())
plt.xlim(190,216)
plt.xlabel('No',fontsize=14)
plt.ylabel('Relative Grav/mGal',fontsize=14)
print(no)
savepath = '重磁报告/fig/grav'
filename = 'xd_jiami.jpg'
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()