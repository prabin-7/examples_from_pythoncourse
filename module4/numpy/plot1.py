import numpy as np
import matplotlib.pyplot as plt
x= np.linspace(0,2*np.pi,10)
y= np.sin(x)
# % matplotlib inline
plt.plot(x,y)

#config and show the plot
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], 
           ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']) # FIRST ARGUMENTS GIVE POSITION OF THE TICKS AND THE SECOND GIVES THE LABEL OF THE TICKS

plt.title('this is the sinewave plot')
plt.xlabel(' 0 to 2pi')
plt.ylabel("value of sine fxn")
plt.show()