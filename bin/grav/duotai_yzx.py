import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('重力部分/剖面去漂移数据/yzx.csv')
g1465 = 0.999286
g1466 = 1.000060
g1467 = 0.999612
g916 = 0.99981
pm1 = data['poumian1'][0:3].to_numpy()*g1465
jc1 = data['jiancha1'][0:3].to_numpy()
pj = (pm1+jc1)/2
v = (pm1-pj)*(pm1-pj)+(jc1-pj)*(jc1-pj)
e = np.sqrt(v.sum()/(2*4-4))
print(e)
pm1 = data['poumian2'].to_numpy()*g1466
jc1 = data['jiancha2'].to_numpy()
pj = (pm1+jc1)/2
v = (pm1-pj)*(pm1-pj)+(jc1-pj)*(jc1-pj)
e = np.sqrt(v.sum()/(2*8-8))
print(e)
pm1 = data['poumian3'][0:3].to_numpy()*g1467
jc1 = data['jiancha3'][0:3].to_numpy()
pj = (pm1+jc1)/2
v = (pm1-pj)*(pm1-pj)+(jc1-pj)*(jc1-pj)
e = np.sqrt(v.sum()/(2*4-4))
print(e)