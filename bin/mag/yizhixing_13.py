import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('mag\\日变校正by13\\ribian_by13.csv')
v11 = data['value11']
v12 = data['value12']
v14 = data['value14']
q11 = data['quality11']
q12 = data['quality12']
q14 = data['quality14']
for i in range(len(q11)):
    if q11[i] != 99 or q12[i] != 99 or q14[i] != 99:
        v11.pop(i)
        v12.pop(i)
        v14.pop(i)
mean = (v11+v12+v14)/3
mean = mean.to_numpy()
#11
v11 = v11.to_numpy()
V11 = []
for i in range(len(v11)):
    V11.append(v11[i]-mean[i])
V11 = np.array(V11)
V2_11 = V11*V11
#12
v12 = v12.to_numpy()
V12 = []
for i in range(len(v12)):
    V12.append(v12[i]-mean[i])
V12 = np.array(V12)
V2_12 = V12*V12
#14
v14 = v14.to_numpy()
V14 = []
for i in range(len(v14)):
    V14.append(v14[i]-mean[i])
V14 = np.array(V14)
V2_14 = V14*V14
#sum
Vtotal = V2_11 + V2_12 + V2_14
A = Vtotal.sum()
e = np.sqrt(A/(3*len(v11)-len(v11)))
print(e)