import inline as inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
print(matplotlib._get_version())
#%matplotlib inline

x=np.arange(0,4*np.pi, 0.1)
y =np.sin(x)

plt.plot(x,y)
plt.show()