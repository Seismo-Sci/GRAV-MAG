from re import A
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('重力部分\\剖面去漂移数据\\yzx.csv')
g1465 = 0.999286
g1466 = 1.000060
g1467 = 0.999612
g916 = 0.99981
#1465
pm1 = data['poumian1'][0:3].to_numpy()*g1465
jc1 = data['jiancha1'][0:3].to_numpy()
mean = (pm1+jc1)/2
a = pm1-mean
A = a*a
e1465 = np.sqrt(A.sum()/2)
print(e1465)
#1466
pm2 = data['poumian2'].to_numpy()*g1466
jc2 = data['jiancha2'].to_numpy()
mean = (pm2+jc2)/2
a = pm2-mean
A = a*a
e1466 = np.sqrt(A.sum()/2)
print(e1466)
#1467
pm3 = data['poumian3'][0:3].to_numpy()*g1467
jc3 = data['jiancha3'][0:3].to_numpy()
mean = (pm3+jc3)/2
a = pm3-mean
A = a*a
e1467 = np.sqrt(A.sum()/2)
print(e1467)