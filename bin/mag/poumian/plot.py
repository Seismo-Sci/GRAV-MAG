import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
poumian = pd.read_csv('磁力部分/磁法剖面.csv')
value_15_raw = poumian['1.5m观测值']
value_20_raw = poumian['2m观测值']
value_25_raw = poumian['2.5m观测值']
no = poumian['点号']
# plt.figure(figsize=(10,4))
# plt.grid(True)
# plt.xlabel('No',fontsize=14)
# plt.ylabel('Magentic/nT',fontsize=14)
# plt.plot(no,value_15_raw,label='1.5m')
# plt.plot(no,value_20_raw,label='2.0m')
# plt.plot(no,value_25_raw,label='2.5m')
# plt.legend(fontsize=10)
# filename='pm_origin.jpg'
# savepath = '重磁报告/fig/mag'
# plt.title('Origin',fontsize=16)
# plt.xlim(100,316)
# plt.savefig(os.path.join(savepath,filename),dpi=600)
# plt.show()
correct15 = poumian['日变校正值']
correct20 = poumian['日变校正值.1']
correct25 = poumian['日变校正值.2']
# plt.figure(figsize=(10,4))
# plt.grid(True)
# plt.xlabel('No',fontsize=14)
# plt.ylabel('Magentic/nT',fontsize=14)
# plt.plot(no,correct15,label='1.5m')
# plt.plot(no,correct20,label='2.0m')
# plt.plot(no,correct25,label='2.5m')
# plt.legend(fontsize=10)
# filename='pm_correct_value.jpg'
# savepath = '重磁报告/fig/mag'
# plt.title('Correct value',fontsize=16)
# plt.xlim(100,316)
# plt.savefig(os.path.join(savepath,filename),dpi=600)
# plt.show()

# plt.figure(figsize=(10,4))
# plt.grid(True)
# plt.xlabel('No',fontsize=14)
# plt.ylabel('Magentic/nT',fontsize=14)
# plt.plot(no,value_15_raw-correct15,label='1.5m')
# plt.plot(no,value_20_raw-correct20,label='2.0m')
# plt.plot(no,value_25_raw-correct25,label='2.5m')
# plt.legend(fontsize=10)
# filename='pm_correct.jpg'
# savepath = '重磁报告/fig/mag'
# plt.title('After correct',fontsize=16)
# plt.xlim(100,316)
# plt.savefig(os.path.join(savepath,filename),dpi=600)
# plt.show()
yc15 = poumian['1.5m磁异常（13校正）']
yc20 = poumian['2m磁异常（13校正）']
yc25 = poumian['2.5m磁异常（13校正）']
# plt.figure(figsize=(10,4))
# plt.grid(True)
# plt.xlabel('No',fontsize=14)
# plt.ylabel('Magentic/nT',fontsize=14)
# plt.plot(no,yc15,label='1.5m')
# plt.plot(no,yc20,label='2.0m')
# plt.plot(no,yc25,label='2.5m')
# plt.legend(fontsize=10)
# filename='pm_yichang.jpg'
# savepath = '重磁报告/fig/mag'
# plt.title('Magnetic anomalies',fontsize=16)
# plt.xlim(100,316)
# plt.savefig(os.path.join(savepath,filename),dpi=600)
# plt.show()
jg = pd.read_csv('重力部分/剖面原始数据/jgai.csv')
nojg = jg['nojg']
value_jg = []
for i in range(len(nojg)):
    value_jg.append(4000)
# plt.figure(figsize=(10,4))
# plt.grid(True)
# plt.xlabel('No',fontsize=14)
# plt.ylabel('Magentic/nT',fontsize=14)
# plt.plot(no,yc15,label='1.5m')
# plt.plot(no,yc20,label='2.0m')
# plt.plot(no,yc25,label='2.5m')
# plt.scatter(nojg,value_jg,color='red',label='Special Object')
# plt.legend(fontsize=10,loc='upper right')
# filename='pm_yichang_jg.jpg'
# savepath = '重磁报告/fig/mag'
# plt.title('Magnetic anomalies',fontsize=16)
# plt.xlim(100,316)
# plt.savefig(os.path.join(savepath,filename),dpi=600)
# plt.show()

##########tidu
jg = pd.read_csv('重力部分/剖面原始数据/jgai.csv')
nojg = jg['nojg']
value_jg = []
for i in range(len(nojg)):
    value_jg.append(0)
v15 = np.array(value_15_raw-correct15)
v20 = np.array(value_20_raw-correct20)
v25 = np.array(value_25_raw-correct25)
d2015 = (v20-v15)/0.5
d2520 = (v25-v20)/0.5
d2515 = (v25-v15)/1

plt.figure(figsize=(10,4))
plt.grid(True)
plt.plot(no,abs(d2015),label='1.5m-2.0m',color='red')
plt.plot(no,abs(d2520),label='2.0m-2.5m',color='blue')
plt.plot(no,abs(d2515),label='1.5m-2.5m',color='green')
plt.xlim(100,316)
plt.xlabel('No',fontsize=14)
plt.ylabel('nT/m',fontsize=14)
plt.title('Absolute magnetic field gradient',fontsize=16)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.legend(fontsize=10,loc='upper right')
filename='pm_abstidu.jpg'
savepath = '重磁报告/fig/mag'
plt.plot([140,140],[0,5000],color='black',linewidth=2,linestyle='--')
plt.plot([175,175],[0,5000],color='black',linewidth=2,linestyle='--')
plt.plot([260,260],[0,5000],color='black',linewidth=2,linestyle='--')
plt.ylim(0,4000)
plt.savefig(os.path.join(savepath,filename))
plt.show()







# plt.figure(figsize=(12,6))
# plt.subplot(311)
# bwith = 2
# ax = plt.gca()
# ax.spines['bottom'].set_linewidth(bwith)
# ax.spines['left'].set_linewidth(bwith)
# ax.spines['top'].set_linewidth(bwith)
# ax.spines['right'].set_linewidth(bwith)
# plt.title('Magnetic gradient\n1.5m-2.0m 2.0m-2.5m 1.5m-2.5m',fontsize=16)
# plt.grid(True)
# plt.plot(no,d2015,label='1.5m-2.0m',color='black')
# plt.scatter(nojg,value_jg,color='red',label='Manhole Cover')
# plt.legend(fontsize=10,loc='lower right')
# plt.ylabel('nT')
# plt.subplot(312)
# bwith = 2
# ax = plt.gca()
# ax.spines['bottom'].set_linewidth(bwith)
# ax.spines['left'].set_linewidth(bwith)
# ax.spines['top'].set_linewidth(bwith)
# ax.spines['right'].set_linewidth(bwith)
# plt.grid(True)
# plt.plot(no,d2520,label='2.0m-2.5m',color='blue')
# plt.scatter(nojg,value_jg,color='red',label='Manhole Cover')
# plt.legend(fontsize=10,loc='lower right')
# plt.ylabel('nT')
# plt.subplot(313)
# bwith = 2
# ax = plt.gca()
# ax.spines['bottom'].set_linewidth(bwith)
# ax.spines['left'].set_linewidth(bwith)
# ax.spines['top'].set_linewidth(bwith)
# ax.spines['right'].set_linewidth(bwith)
# plt.grid(True)
# plt.plot(no,d2515,label='1.5m-2.5m',color='green')
# plt.scatter(nojg,value_jg,color='red',label='Manhole Cover')
# plt.legend(fontsize=10,loc='lower right')
# plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0, hspace=0)
# plt.xlabel('No',fontsize=14)
# plt.ylabel('nT')
# filename = 'pm_tidu.jpg'
# savepath = '重磁报告/fig/mag'
# plt.savefig(os.path.join(savepath,filename),dpi=600)
# plt.show()