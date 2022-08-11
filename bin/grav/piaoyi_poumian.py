import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#First
data1 = pd.read_csv('重力部分/剖面原始数据/first.csv')
value1 = data1['G1'].to_numpy()[0]
value2 = data1['G2'].to_numpy()[0]
hour1 = data1['hour1'].to_numpy()
hour2 = data1['hour2'].to_numpy()
min1 = data1['min1'].to_numpy()
min2 = data1['min2'].to_numpy()
h1 = hour1[0]+min1[0]/60
h2 = hour2[0]+min2[0]/60
#漂移系数
k = (value2-value1)/(h2-h1)
value = data1['value'].to_numpy()
hour = data1['hour'].to_numpy()
min = data1['min'].to_numpy()
hour = hour+min/60
Grav1 = []
for i in range(len(value)):
    valued = value[i]-k*(hour[i]-h1)-value1
    Grav1.append(valued)
no = data1['no']
G1 = []
for i in range(len(no)):
    g1 = []
    g1.append(str(no[i]))
    g1.append(',')
    g1.append(str(Grav1[i]))
    G1.append(g1)
# plt.plot(range(len(Grav)),Grav)
# plt.show()  
#Second
data2 = pd.read_csv('重力部分/剖面原始数据/second.csv')
value1 = data2['Gvalue1'][0]
value2 = data2['Gvalue2'][0]
t1 = data2['Gtime1'][0]
t2 = data2['Gtime2'][0]
t1 = float(t1.split(':')[0])+float(t1.split(':')[1])/60
t2 = float(t2.split(':')[0])+float(t2.split(':')[1])/60
k = (value2-value1)/(t2-t1)
time = data2['time']
T = []
for i in range(0,len(time)):
    t = float(time[i].split(':')[0])+float(time[i].split(':')[1])/60
    T.append(t)
value = data2['value']
Grav2 = []
for i in range(len(value)):
    valued = value[i]-k*(T[i]-t1)-value1
    Grav2.append(valued)
# plt.plot(range(len(Grav2)),Grav2)
# plt.show()
no = data2['no']
G2 = []
for i in range(len(no)):
    g2 = []
    g2.append(str(no[i]))
    g2.append(',')
    g2.append(str(Grav2[i]))
    G2.append(g2)


data3 = pd.read_csv('重力部分/剖面原始数据/third.csv')
value1 = data3['Gvalue1'][0]
value2 = data3['Gvalue2'][0]
t1 = data3['Gtime1'][0]
t2 = data3['Gtime2'][0]
t1 = float(t1.split(':')[0])+float(t1.split(':')[1])/60
t2 = float(t2.split(':')[0])+float(t2.split(':')[1])/60
k = (value2-value1)/(t2-t1)
time = data3['time']
T = []
for i in range(0,len(time)):
    t = float(time[i].split(':')[0])+float(time[i].split(':')[1])/60
    T.append(t)
value = data3['value']
Grav3 = []
for i in range(len(value)):
    valued = value[i]-k*(T[i]-t1)-value1
    Grav3.append(valued)
no = data3['no']
G3 = []
for i in range(len(no)):
    g3 = []
    g3.append(str(no[i]))
    g3.append(',')
    g3.append(str(Grav3[i]))
    G3.append(g3)
# plt.plot(range(len(Grav3)),Grav3)
# plt.show()
file_write_obj = open('1.txt', 'w')
for var in G1:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

file_write_obj = open('2.txt', 'w')
for var in G2:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

file_write_obj = open('3.txt', 'w')
for var in G3:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()