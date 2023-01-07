import matplotlib.pyplot as plt
import numpy as np

t0 = 2
dt = 0.55
cutoff = 50
def JeanMain(t0, dt, cutoff):
    step = 0
    condition = True
    while condition:
        t = t0 + step*dt
        g = t*np.sin(t)
        print('t = %0.6f and g = %0.6f' % (t,g))
        step = step + 1
        condition = step < cutoff

JeanMain(t0, dt, cutoff)