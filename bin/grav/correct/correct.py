import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#相对正常场校正
#neh坐标读取
neh = pd.read_csv('重力部分\\正常场校正\\20220730#.txt')
N = neh['N']
N_G = N[120]
N_poumian = N[1:119].to_numpy()
#latlon读取
latlonh = pd.read_csv('重力部分\\正常场校正\\20220730.txt')
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
    e = -0.000814*np.sin(2*(Lat_poumian[i]))*(N_poumian[i]-N_G)
    e_Z.append(e)
poumian = pd.read_csv('重力部分\\剖面去漂移数据\\poumian.csv')
value = poumian['value'].to_numpy()
no = poumian['no'].to_numpy()
valued1 = value+np.array(e_Z)
# plt.plot(no,valued1)
# plt.show()
#自由空间校正
#by height-after
height = pd.read_csv('重力部分\\正常场校正\\height.txt')
h = height['height'].to_numpy()
e_gf = 0.3086*h
valued2 = valued1+e_gf
#by height-raw
h_2 = neh['H'][1:119].to_numpy()
e_gf_2 = 0.3086*h_2
valued2_2 = valued1+e_gf_2
# plt.subplot(211)
# plt.plot(no,valued2)
# plt.subplot(212)
# plt.plot(no,valued2_2)
# plt.show()
##中间层校正2.67
e_bg = (0.3086-0.0419*2.67)*(h-20)
valued3 = valued1+e_bg
# plt.plot(no,valued3)
# plt.show()
# plt.plot(no,e_bg)
# plt.show()
dg = pd.read_csv('重力部分\\正常场校正\\digai.csv')
e_dg = dg['e_dg']
valued4 = valued3 + e_dg
plt.plot(no,valued4)
plt.show()
