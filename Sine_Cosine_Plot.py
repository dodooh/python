# Generating a sine vs cosine curve

# For this project, you will have a generate a sine vs cosine curve. 
# You will need to use the numpy library to access the sine and cosine functions.
#  You will also need to use the matplotlib library to draw the curve. 
#  To make this more difficult, make the graph go from -360° to 360°, 
#  with there being a 180° difference between each point on the x-axis

import numpy as np
import matplotlib.pylab as plt
plt.show()
# values from -4pi to 4pi
x=np.arange(-4*np.pi,4*np.pi,0.05)
y_sin=np.sin(x)
y_cos=np.cos(x)

#Drawing sin and cos functions
plt.plot(x,y_sin,color='red',linewidth=1.5, label="Sin(x)")
plt.plot(x,y_cos,color='blue', label="Cos(x)")
plt.title("Sin vs Cos graph")
plt.xlabel('Angles in radian')
plt.ylabel('sin(x) and cos(x)')
plt.legend(['sin(x)','cos(x)'])
plt.show()