from sqlite3 import enable_callback_tracebacks
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#相对正常场校正
#neh坐标读取
neh = pd.read_csv('重力部分/正常场校正/20220730#.txt')
N = neh['N']
N_G = N[120]
N_poumian = N[1:119].to_numpy()
#latlon读取
latlonh = pd.read_csv('重力部分/正常场校正/20220730.txt')
lat = latlonh['lat'].to_list()
Lat = []
for i in range(len(lat)):
    loc = lat[i].split(':')
    lat_=float(loc[0])+float(loc[1])/60+float(''.join(list(loc[2])[0:8]))/3600
    Lat.append(lat_)
Lat_G = Lat[120]
Lat_poumian = np.array(Lat[1:119])
#校正
e_Z = []
for i in range(len(Lat_poumian)):
    e = -0.000814*np.sin(2*(np.deg2rad(Lat_G)))*(N_poumian[i]-N_G)
    e_Z.append(e)
poumian = pd.read_csv('重力部分/剖面去漂移数据/poumian.csv')
value = poumian['value'].to_numpy()
no = poumian['no'].to_numpy()
e_Z = np.array(e_Z)
value_Z = value + e_Z
#相对正常场校正
plt.figure(figsize=(10,4))
ax2 = plt.subplot(121)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value,label='Origin')
plt.plot(no,value_Z,label='After process')
ax2.set_title('Comparison of gravity profiles \n before and after correction')
plt.legend(fontsize=10)
plt.ylabel('Relavtive Grav/mGal',fontsize=14)
plt.xlabel('No',fontsize=14)
plt.xlim(100,316)
plt.grid(True)
ax1 = plt.subplot(122)
plt.plot(no,e_Z)
ax1.set_title('Relative normal field correction value')
plt.xlim(100,316)
plt.grid(True)
plt.xlabel('No',fontsize=14)
savepath = '重磁报告/fig/grav'
filename = 'jz_zcchang.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
#自由空间校正
h = pd.read_csv('重力部分/正常场校正/height.txt')
height = h['height'].to_numpy()
e_H = 0.3086*(height-20)
value_H = value_Z + e_H
plt.figure(figsize=(10,4))
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
ax2 = plt.subplot(121)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_Z,label='Origin')
plt.plot(no,value_H,label='After process')
ax2.set_title('Comparison of gravity profiles \n before and after correction')
plt.legend(fontsize=10)
plt.ylabel('Relavtive Grav/mGal',fontsize=14)
plt.xlabel('No',fontsize=14)
plt.xlim(100,316)
plt.grid(True)
ax1 = plt.subplot(122)
plt.plot(no,e_H)
ax1.set_title('Free space correction value')
plt.xlim(100,316)
plt.grid(True)
plt.xlabel('No',fontsize=14)
savepath = '重磁报告/fig/grav'
filename = 'jz_ziyou.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
#中间层校正
e_B = -0.0419*2.67*(height-20)
t = np.sqrt((height-20)*(height-20)+270*270)
e_B_1 = -0.0419*2.67*(1-(height-20)/t)*(height-20)
value_B = value_H + e_B_1
plt.figure(figsize=(10,6))
plt.plot(no,e_B_1,color='red',label='Origin')
plt.plot(no,e_B,color='blue',label='Simple')
plt.grid(True)
plt.xlabel('No',fontsize=14)
plt.ylabel('Intermediate layer correction value/mGal',fontsize=14)
savepath = '重磁报告/fig/grav'
filename = 'jz_zjduibi.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
print(t)
plt.figure(figsize=(10,4))
ax2 = plt.subplot(121)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_H,label='Origin')
plt.plot(no,value_B,label='After process')
ax2.set_title('Comparison of gravity profiles \n before and after correction')
plt.legend(fontsize=10)
plt.ylabel('Relavtive Grav/mGal',fontsize=14)
plt.xlabel('No',fontsize=14)
plt.xlim(100,316)
plt.grid(True)
ax1 = plt.subplot(122)
plt.plot(no,e_B)
ax1.set_title('Intermediate layer correction')
plt.xlim(100,316)
plt.grid(True)
plt.xlabel('No',fontsize=14)
savepath = '重磁报告/fig/grav'
filename = 'jz_zjcen.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
#地形校正
dg = pd.read_csv('重力部分/正常场校正/digai.csv')
e_dg = dg['e_dg']
value_D = value_B - e_dg
plt.figure(figsize=(10,4))
ax2 = plt.subplot(121)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_B,label='Origin')
plt.plot(no,value_D,label='After process')
ax2.set_title('Comparison of gravity profiles \n before and after correction')
plt.legend(fontsize=10)
plt.ylabel('Relavtive Grav/mGal',fontsize=14)
plt.xlabel('No',fontsize=14)
plt.xlim(100,316)
plt.grid(True)
ax1 = plt.subplot(122)
plt.plot(no,e_dg)
ax1.set_title('Terrain correction')
plt.xlim(100,316)
plt.grid(True)
plt.xlabel('No',fontsize=14)
savepath = '重磁报告/fig/grav'
filename = 'jz_dxing.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
# 布格重力异常
plt.figure(figsize=(10,4))
plt.plot(no,value_D,linewidth=2)
plt.xlim(100,316)
plt.grid(True)
plt.xlabel('No',fontsize=14)
plt.ylabel('Relative Grav/mGal',fontsize=14)
plt.title('Bouguer Gravity Anomaly',fontsize=16)
savepath = '重磁报告/fig/grav'
filename = 'bg_yichang.jpg'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()

print(poumian)

plt.figure(figsize=(10,4))
plt.plot(no,value_D,linewidth=2)
plt.xlim(100,316)
plt.grid(True)
plt.xlabel('No',fontsize=14)
plt.ylabel('Relative Grav/mGal',fontsize=14)
plt.title('Bouguer Gravity Anomaly',fontsize=16)
plt.scatter(no[16],value_D[16],color='red',label='132')
plt.scatter(no[20],value_D[20],color='yellow',label='140')
plt.scatter(no[27],value_D[27],color='blue',label='154')
plt.scatter(no[46],value_D[46],color='orange',label='192')
plt.scatter(no[65],value_D[65],color='brown',label='212')
plt.scatter(no[65],value_D[65],color='green',label='192')
plt.scatter(no[80],value_D[80],color='black',label='242')
plt.scatter(no[86],value_D[86],color='pink',label='254')
savepath = '重磁报告/fig/grav'
filename = 'bg_yichang_fx.jpg'
plt.legend(fontsize=10,loc='upper right')
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename),dpi=600)
plt.show()
data = pd.read_csv('重力部分/延拓圆滑/smooth.csv')
data3 = data['3']
data5 = data['5']
data7 = data['7']
print(data)
plt.figure(figsize=(12,8))
plt.subplot(311)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.title('3 5 7 Points Smoothing',fontsize=16)
plt.plot(no,value_D,label='Origin',linewidth=2)
plt.plot(no,data3,color='red',label='3 Points Smooth',linewidth=2)
plt.legend(fontsize=10,loc='lower left')
plt.ylabel('Relative Grav/mGal',fontsize=14)
plt.xticks([])
plt.subplot(312)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_D,label='Origin',linewidth=2)
plt.plot(no,data5,color='red',label='5 Points Smooth',linewidth=2)
plt.legend(fontsize=10,loc='lower left')
plt.ylabel('Relative Grav/mGal',fontsize=14)
plt.xticks([])
plt.subplot(313)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_D,label='Origin',linewidth=2)
plt.plot(no,data7,color='red',label='7 Points Smooth',linewidth=2)
plt.legend(fontsize=10,loc='lower left')
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0, hspace=0)
plt.xlabel('No',fontsize=14)
plt.ylabel('Relative Grav/mGal',fontsize=14)
filename = 'pc_smooth.jpg'
savepath = '重磁报告/fig/grav'
plt.savefig(os.path.join(savepath,filename))
plt.show()
data = pd.read_csv('重力部分/延拓圆滑/yantuo.csv')
data5 = data['5']
data50 = data['50']
data100 = data['100']
data150 = data['150']
plt.figure(figsize=(12,8))
plt.suptitle('Upward continuation',fontsize=16)
plt.subplot(221)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_D,label='Origin')
plt.plot(no,data5,color='red',label='5m')
plt.legend(fontsize=10,loc='lower left')
plt.ylabel('Relative Grav/mGal',fontsize=14)
plt.subplot(222)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_D,label='Origin',linewidth=2)
plt.plot(no,data50,color='red',label='50m',linewidth=2)
plt.legend(fontsize=10,loc='lower left')
plt.yticks([])
plt.subplot(223)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_D,label='Origin',linewidth=2)
plt.plot(no,data100,color='red',label='100m',linewidth=2)
plt.legend(fontsize=10,loc='lower left')
plt.ylabel('Relative Grav/mGal',fontsize=14)
plt.xlabel('No',fontsize=14)
plt.subplot(224)
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.plot(no,value_D,label='Origin',linewidth=2)
plt.plot(no,data150,color='red',label='150m',linewidth=2)
plt.legend(fontsize=10,loc='lower left')
plt.yticks([])
plt.xlabel('No',fontsize=14)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,wspace=0, hspace=0)
filename = 'pc_yantuo.jpg'
savepath = '重磁报告/fig/grav'
plt.savefig(os.path.join(savepath,filename))
plt.show()
plt.figure(figsize=(10,4))
plt.plot(no,value_D,label='Origin',linewidth=2)
plt.plot(no,value_D-data150,label='Local field',linewidth=2,color='red')
plt.plot(no,data150,label='Regional field',linewidth=2)
plt.grid(True)
plt.xlabel('No',fontsize=14)
plt.ylabel('Relavtive Grav',fontsize=14)
plt.title('Potential field separation',fontsize=16)
plt.legend(fontsize=10,loc='lower left')
filename = 'pc_fenli.jpg'
savepath = '重磁报告/fig/grav'
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.savefig(os.path.join(savepath,filename))
plt.show()
plt.figure(figsize=(10,4))
bwith = 2
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)
plt.grid(True)
plt.plot(no,value_D-data150,linewidth=2,color='red')
plt.xlabel('No',fontsize=14)
plt.ylabel('Relative Grav',fontsize=14)
plt.title('Residual Bouguer gravity anomaly',fontsize=16)
filename = 'pc_shengyu.jpg'
savepath = '重磁报告/fig/grav'
plt.savefig(os.path.join(savepath,filename))
plt.show()
