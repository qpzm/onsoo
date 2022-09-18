#Kimhaeun
#22100224
#Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x1=np.array([10,20,30])
y1=np.array([130,120,70])

x2=np.array([10,20,30,40])
y2=np.array([150,100,90,80])


plt.title('Two lines plot with legends')
plt.xlabel("x-axis, age")
plt.ylabel("y-axis, power")
plt.xlim([8,42])
plt.ylim([68,152])
plt.plot(x1,y1,'y',label='first line')
plt.plot(x2,y2,'b',label='second line')
plt.legend()
plt.show()


