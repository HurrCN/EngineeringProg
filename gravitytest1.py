import matplotlib.pyplot as plt
import numpy as np

v0 = 5
g = 9.81
t = np.linspace(0, 1, 1001)
y = v0*t - 0.5*g*t**2
plt.plot(t, y)
plt.xlabel ('time (s)')	#Give label for x-axis
plt.ylabel ('height (m)')	#Give label for y-axis
plt.grid (b=True, which = 'major', color='#666666', linestyle='-')  #Draw grid from major ticks
plt.minorticks_on() #Draw minor ticks on both axis
plt.grid(b=True, which = 'minor', color = '#666666', linestyle='-', alpha=0.1) #Draw grid from minor ticks
plt.show()