import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
savepath = '重磁报告/fig/grav'
data_raw = pd.read_csv('重力部分/剖面原始数据/poumian.csv')
value_raw = data_raw['value']
no = data_raw['no']
# plt.plot(no,value_raw)
data = pd.read_csv('重力部分/剖面去漂移数据/poumian.csv')
value = data['value']
no = data['no']
# plt.show()
#零漂曲线
#第一段
pm1 = pd.read_csv('重力部分/剖面原始数据/first.csv')
h1 = pm1['hour'].to_numpy()
m1 = pm1['min'].to_numpy()
hg1 = pm1['hour1'].to_numpy()[0]
min1 = pm1['min1'].to_numpy()[0]
hg2 = pm1['hour2'].to_numpy()[0]
min2 = pm1['min2'].to_numpy()[0]
Gv1 = pm1['G1'][0]
Gv2 = pm1['G2'][0]
hour1 = hg1+min1/60
hour2 = hg2+min2/60
k = (Gv2-Gv1)/(hour2-hour1)
hour = h1+m1/60
pm1_py = hour*k
no1 = pm1['no']
#第二段
pm2 = pd.read_csv('重力部分/剖面原始数据/second.csv')
time = pm2['time'].to_list()
T = []
for i in range(len(time)):
    t = time[i].split(':')
    T.append(float(t[0])+float(t[1])/60)
T = np.array(T)
t = pm2['Gtime1'].to_list()[0]
t = t.split(':')
hg1 = float(t[0])+float(t[1])/60
t = pm2['Gtime2'].to_list()[0]
t = t.split(':')
hg2 = float(t[0])+float(t[1])/60
Gv1 = pm2['Gvalue1'][0]
Gv2 = pm2['Gvalue2'][0]
k = (Gv2-Gv1)/(hg2-hg1)
pm2_py = T*k
no2 = pm2['no']
#第三段
pm3 = pd.read_csv('重力部分/剖面原始数据/third.csv')
time = pm3['time'].to_list()
T = []
for i in range(len(time)):
    t = time[i].split(':')
    T.append(float(t[0])+float(t[1])/60)
T = np.array(T)
t = pm3['Gtime1'].to_list()[0]
t = t.split(':')
hg1 = float(t[0])+float(t[1])/60
t = pm3['Gtime2'].to_list()[0]
t = t.split(':')
hg2 = float(t[0])+float(t[1])/60
Gv1 = pm3['Gvalue1'][0]
Gv2 = pm3['Gvalue2'][0]
k = (Gv2-Gv1)/(hg2-hg1)
pm3_py = T*k
no3 = pm3['no']
#检查
pmjc = pd.read_csv('重力部分/剖面原始数据/jiancha.csv')
time = pmjc['time'].to_numpy()
hg1 = pmjc['Gtime1'].to_numpy()[0]
hg2 = pmjc['Gtime2'].to_numpy()[0]
Gv1 = pmjc['Gvalue1'][0]
Gv2 = pmjc['Gvalue2'][0]
k = (Gv2-Gv1)/(hg2-hg1)
pmjc_py = T*k
#########plot
fig,ax = plt.subplots(figsize=(10,8))
plt.grid(True)
lin1 = ax.plot(no,value_raw,label='origin',linewidth=3)
lin2 = ax.plot(no,value,label='after process',linewidth=3)
ax.set_xlabel('No',fontsize=14)
ax.set_ylabel('Relative Grav/mGal',fontsize=14)
ax2 = ax.twinx()
lin3 = ax2.plot(no1,pm1_py,label='1st Drift value')
lin4 = ax2.plot(no2,pm2_py,label='2nd Drift value')
lin5 = ax2.plot(no3,pm3_py,label='3rd Drift value')
nojc = range(195,213,2)
lin6 = ax2.plot(nojc,pmjc_py[0:len(nojc)],label='Exam Drift value')
ax2.set_ylabel('Drift value/mGal',fontsize=14)
lin = lin1+lin2+lin3+lin4+lin5+lin6
labs = [l.get_label() for l in lin]
ax.legend(lin,labs,fontsize=10,loc='upper right')
filename = 'xiangdui.jpg'
plt.xlim(100,316)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
