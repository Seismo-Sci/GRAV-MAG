import pandas as pd
import numpy as np
data = pd.read_csv('mag\\ribian.csv')
q13 = data['quality13']
q15 = data['quality15']
v13 = data['value13']
v15 = data['value15']
for i in range(len(v13)):
    if q13[i] != 99 or q15[i] != 99:
        v13.pop(i)
        v15.pop(i)
v13 = v13.to_numpy()
v15 = v15.to_numpy()
V13 = []
V15 = []
for i in range(len(v13)):
    V13.append(v13[i]-v13[0])
    V15.append(v15[i]-v15[0])
V13 = np.array(V13)
V15 = np.array(V15)
Vmean = (V13+V15)/2
T13 = (V13 - Vmean)*(V13-Vmean)
s13 = np.sqrt(T13.sum()/(len(v13)-1))
T15 = (V15 - Vmean)*(V15-Vmean)
s15 = np.sqrt(T15.sum()/(len(v15)-1))
print(s13)
print(s15)
