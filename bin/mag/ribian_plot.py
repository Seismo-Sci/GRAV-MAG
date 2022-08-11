import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
data = pd.read_csv('mag\\ribian.csv')
time = data['time13']
data13 = data['value13']
data15 = data['value15']
quality13 = data['quality13']
quality15 = data['quality15']

for i in range(len(quality13)):
    if quality13[i] != 99 or quality15[i] != 99:
        data13.pop(i)
        data15.pop(i)
t13 = np.linspace(0,4.6,len(data13))
t15 = np.linspace(0,4.6,len(data15))
plt.figure(figsize=(10,4))
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(t13,data13,color='red',label='Gem_13')
plt.plot(t15,data15,color='blue',label='Gem_15')
plt.xlim(0,4.6)
plt.xlabel('Time (Hour)',fontsize=14)
plt.legend(fontsize=10,loc='upper right')
savepath = '重磁报告/fig/mag'
filename = 'rb_guance.jpg'
plt.savefig(os.path.join(savepath,filename))
plt.show()