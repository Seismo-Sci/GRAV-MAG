import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('重力部分/剖面原始数据/jiancha.csv')
value1 = data['Gvalue1'][0]
value2 = data['Gvalue2'][0]
t1 = data['Gtime1'][0]
t2 = data['Gtime2'][0]
k = (value2-value1)/(t2-t1)
value = data['value']
time = data['time']
Grav = []
for i in range(0,len(value)):
    valued = value[i]-k*(time[i]-t1)-value1
    Grav.append(valued)
no = data['no']
G = []
for i in range(0,len(data)):
    g = []
    g.append(str(no[i]))
    g.append(',')
    g.append(str(Grav[i]))
    G.append(g)
file_write_obj = open('jiancha.txt', 'w')
for var in G:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()
print(k)