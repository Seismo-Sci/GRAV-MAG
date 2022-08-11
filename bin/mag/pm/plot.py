import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
data = pd.read_csv('磁力部分/poumian.csv')
v15 = data['origin15']
v20 = data['origin20']
v25 = data['origin25']
no = data['no']
plt.figure(figsize=(10,4))
plt.xlim(100,316)
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,v15,color='blue',label='1.5m',linewidth=2)
plt.plot(no,v20,color='red',label='2.0m',linewidth=2)
plt.plot(no,v25,color='green',label='2.5m',linewidth=2)
plt.xlabel('No',fontsize=14)
plt.ylabel('nT',fontsize=14)
plt.title('Origin',fontsize=16)
plt.legend(fontsize=10,loc='upper right')
filename='pm_origin.jpg'
savepath = '重磁报告/fig/mag'
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
c15 = data['correct15']
c20 = data['correct20']
c25 = data['correct25']
plt.figure(figsize=(10,4))
plt.xlim(100,316)
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,c15,color='blue',label='1.5m',linewidth=2)
plt.plot(no,c20,color='red',label='2.0m',linewidth=2)
plt.plot(no,c25,color='green',label='2.5m',linewidth=2)
plt.xlabel('No',fontsize=14)
plt.ylabel('nT',fontsize=14)
plt.title('Correct value',fontsize=16)
plt.legend(fontsize=10,loc='upper right')
filename='pm_correct_value.jpg'
savepath = '重磁报告/fig/mag'
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
p15 = data['process15']
p20 = data['process20']
p25 = data['process25']
plt.figure(figsize=(10,4))
plt.xlim(100,316)
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,p15,color='blue',label='1.5m',linewidth=2)
plt.plot(no,p20,color='red',label='2.0m',linewidth=2)
plt.plot(no,p25,color='green',label='2.5m',linewidth=2)
plt.xlabel('No',fontsize=14)
plt.ylabel('nT',fontsize=14)
plt.title('After Correct',fontsize=16)
plt.legend(fontsize=10,loc='upper right')
filename='pm_correct.jpg'
savepath = '重磁报告/fig/mag'
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
ck15 = data['cankao15']
ck20 = data['cankao20']
ck25 = data['cankao25']
plt.figure(figsize=(10,4))
plt.xlim(100,316)
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,ck15,color='blue',label='1.5m',linewidth=2)
plt.xlabel('No',fontsize=14)
plt.ylabel('nT',fontsize=14)
plt.title('IGRF13',fontsize=16)
filename='pm_cankao.jpg'
savepath = '重磁报告/fig/mag'
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
yc15 = data['yichang15']
yc20 = data['yichang20']
yc25 = data['yichang25']
plt.figure(figsize=(10,4))
plt.xlim(100,316)
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,yc15,color='blue',label='1.5m',linewidth=2)
plt.plot(no,yc20,color='red',label='2.0m',linewidth=2)
plt.plot(no,yc25,color='green',label='2.5m',linewidth=2)
plt.xlabel('No',fontsize=14)
plt.ylabel('nT',fontsize=14)
plt.title('Magnetic anomaly',fontsize=16)
plt.legend(fontsize=10,loc='upper right')
filename='pm_yichang.jpg'
savepath = '重磁报告/fig/mag'
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
jg = pd.read_csv('重力部分/剖面原始数据/jgai.csv')
nojg = jg['nojg']
value_jg = []
for i in range(len(nojg)):
    value_jg.append(0)
plt.figure(figsize=(10,4))
plt.xlim(100,316)
plt.grid(True)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,yc15,color='blue',label='1.5m',linewidth=2)
plt.plot(no,yc20,color='red',label='2.0m',linewidth=2)
plt.plot(no,yc25,color='green',label='2.5m',linewidth=2)
plt.scatter(nojg,value_jg,color='red',label='Special Object')
plt.xlabel('No',fontsize=14)
plt.ylabel('nT',fontsize=14)
plt.title('Magnetic anomaly',fontsize=16)
plt.legend(fontsize=10,loc='upper right')
filename='pm_yichang_jg.jpg'
savepath = '重磁报告/fig/mag'
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
