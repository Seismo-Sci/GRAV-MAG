import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
poumian = pd.read_csv('重力部分\\剖面去漂移数据\\poumian.csv')
no = poumian['no']
value = poumian['value']
plt.plot(no,value)
plt.show()
no_mi = poumian['no'][48:65]
value_mi = poumian['value'][48:65]
# plt.plot(no_mi,value_mi)
# plt.show()