import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
data = pd.read_csv('磁力部分/Jingtai-raw.csv')
v11 = data['value11']
v12 = data['value12']
v13 = data['value13']
v14 = data['value14']
v15 = data['value15']
q11 = data['quality11']
q12 = data['quality12']
q13 = data['quality13']
q14 = data['quality14']
q15 = data['quality15']
time = data['time']
# for i in range(len(v11)):
#     if q11[i] != 99 or q12[i] != 99 or q13[i] != 99 or q14[i] != 99 or q15[i] != 99:
#         v11.pop(i)
#         v12.pop(i)
#         v13.pop(i)
#         v14.pop(i)
#         v15.pop(i)
#         time.pop(i)
t = np.linspace(0,10.05,len(v11))
plt.figure(figsize=(14,6))
plt.grid(True)
plt.xlabel('Time [min]',fontsize=14)
plt.ylabel('Magnetic/nT')
plt.plot(t,v11,linewidth=1,label='Gem_11')
plt.plot(t,v12,linewidth=1,label='Gem_12')
plt.plot(t,v13,linewidth=1,label='Gem_13')
plt.plot(t,v14,linewidth=1,label='Gem_14')
plt.plot(t,v15,linewidth=1,label='Gem_15')
plt.legend(fontsize=10,loc='upper left')
plt.xlim(0,10.05)
filename = 'jt_plot.jpg'
savepath = '重磁报告/fig/mag'
plt.savefig(os.path.join(savepath,filename))
plt.show()
cor11_13 = v13.corr(v11)
cor12_13 = v13.corr(v12)
cor14_13 = v13.corr(v14)
# print(cor11_13)
# print(cor12_13)
# print(cor14_13)

cor11_15 = v15.corr(v11)
cor12_15 = v15.corr(v12)
cor14_15 = v15.corr(v14)
# print(cor11_15)
# print(cor12_15)
# print(cor14_15)
##########噪声
v11 = np.array(v11)
v12 = np.array(v12)
v13 = np.array(v13)
v14 = np.array(v14)
v15 = np.array(v15)
v11_0 = v11[0]
v12_0 = v12[0]
v13_0 = v13[0]
v14_0 = v14[0]
v15_0 = v15[0]
v11_1 = v11 - v11_0
v12_1 = v12 - v12_0
v13_1 = v13 - v13_0
v14_1 = v14 - v14_0
v15_1 = v15 - v15_0
dv = (v11_1+v12_1+v13_1+v14_1+v15_1)/5
dx = [v11_1,v12_1,v13_1,v14_1,v15_1]
for i in dx:
    S = np.sqrt(((dx-dv)*(dx-dv)).sum()/(len(dx)-2))
    print(S)
