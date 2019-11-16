'''
2
Vẽ đồ thị hàm sin,cos,tan trong khoảng -2𝜋 -> 2𝜋
'''

import numpy as np
import matplotlib.pyplot as plt
import pylab
# %matplotlib inline

x = np.linspace(-np.pi*2,np.pi*2)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.plot(x,np.tan(x))
pylab.show()