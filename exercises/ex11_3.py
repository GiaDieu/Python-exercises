'''
3
Vẽ đồ thị hàm x = y**2 và x = y trên cùng 1 trục toạ độ.
'''
import numpy as np
import matplotlib.pyplot as plt
import pylab

def solve():
    x = np.arange(-5,5,0.3)
    plt.style.use('ggplot')
    plt.plot(x,x**2)
    plt.plot(x,x)
    plt.legend(['x=y**2','x=y'])
    pylab.show()
solve()