import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('重力部分\\剖面原始数据\\first.csv')
value = data['value'].to_numpy()
G1 = data['G1'].to_numpy()[0]
no = data['no'].to_numpy()
valued = value-G1
g = []
for i in range(0,len(valued)):
    G = []
    G.append(str(no[i]))
    G.append(',')
    G.append(str(valued[i]))
    g.append(G)
file_write_obj = open('01.txt', 'w')
for var in g:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

data = pd.read_csv('重力部分\\剖面原始数据\\second.csv')
value = data['value'].to_numpy()
G1 = data['Gvalue1'].to_numpy()[0]
no = data['no'].to_numpy()
valued = value-G1
g = []
for i in range(0,len(valued)):
    G = []
    G.append(str(no[i]))
    G.append(',')
    G.append(str(valued[i]))
    g.append(G)
file_write_obj = open('02.txt', 'w')
for var in g:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

data = pd.read_csv('重力部分\\剖面原始数据\\third.csv')
value = data['value'].to_numpy()
G1 = data['Gvalue1'].to_numpy()[0]
no = data['no'].to_numpy()
valued = value-G1
g = []
for i in range(0,len(valued)):
    G = []
    G.append(str(no[i]))
    G.append(',')
    G.append(str(valued[i]))
    g.append(G)
file_write_obj = open('03.txt', 'w')
for var in g:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()

data = pd.read_csv('重力部分\\剖面原始数据\\jiancha.csv')
value = data['value'].to_numpy()
G1 = data['Gvalue1'].to_numpy()[0]
no = data['no'].to_numpy()
valued = value-G1
g = []
for i in range(0,len(valued)):
    G = []
    G.append(str(no[i]))
    G.append(',')
    G.append(str(valued[i]))
    g.append(G)
file_write_obj = open('04.txt', 'w')
for var in g:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()
