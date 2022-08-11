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
v11 = v11.to_numpy()
v12 = v12.to_numpy()
v14 = v14.to_numpy()
vmean = (v11 + v12 + v14)/3
t = np.linspace(0,8.9,len(v11))
plt.plot(t,v11-vmean,color='red',label='Gem_11')
plt.plot(t,v12-vmean,color='blue',label='Gem_12')
plt.plot(t,v14-vmean,color='green',label='Gem_14')
plt.legend()
plt.xlim(0,8.9)
plt.show()