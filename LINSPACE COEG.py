import numpy as np

a = float(input('a: '))
b = float(input('b: '))
seg = int(input('seg: '))
h = float(abs((a-b)/seg))
h12 = float(0.5*h)
x = np.linspace(a+h12, b-h12, seg, dtype=float)
print(x)


#x = np.linspace(0,20,10,dtype=float)
#print(x)