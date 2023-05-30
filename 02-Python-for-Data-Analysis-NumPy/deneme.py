import matplotlib.pyplot as plt

import numpy as np
 
x = np.linspace(0,5,11)
print(x)
y = x ** 2

plt.plot(x,y,'r')
plt.show()