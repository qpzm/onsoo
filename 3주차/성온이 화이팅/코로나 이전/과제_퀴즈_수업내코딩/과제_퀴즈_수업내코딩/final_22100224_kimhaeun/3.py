#kimhaeun
#22100224
#3

import matplotlib.pyplot as plt
import numpy as np

x=np.array(['a','b','c','d','e'])
y=np.array([75,70,90,60,90])

plt.plot(x,y,c='r',marker='o',mfc='b')
plt.title("Score-display marker")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.ylim([50,100])
plt.show()
