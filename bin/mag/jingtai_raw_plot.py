import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('mag/Jingtai-raw.csv')
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
t = np.linspace(0,8.9,len(v11))
plt.plot(t,v11,color='red',label='Gem_11')
plt.plot(t,v12,color='blue',label='Gem_12')
plt.plot(t,v14,color='green',label='Gem_14')
plt.xlim(0,8.9)
plt.xlabel('Time (min)')
plt.legend()
plt.title('Before diurnal correction')
plt.show()