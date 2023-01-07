print("PEMROGRAMAN TEKNIK-02")
print("TUGAS 5.2 INTEGRAL NUMERIK METODE MIDPOINT VECTORIZED")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

import matplotlib.pyplot as plt
import numpy as np
import time as t

# Input Data
print("==========INTEGRAL METODE TITIK TENGAH==========")
a = float(input('Batas bawah: '))
b = float(input('Batas atas: '))
seg = int(input('Jumlah segmen: '))

startTime = t.time()

h = float(abs((a-b)/seg))
h12 = float(0.5*h)
xReal = np.linspace(a,b,10000,dtype=float)
xData = np.linspace(a+h12, b-h12, seg, dtype=float)
#print(xData)

# Definisi Fungsi yang akan Diintegrasikan
def f(x):
    # ini persamaannya 1*x**9 +0*x**6 + 3*x**5 + 6*x**1 + 9*x**1
    return x**9 + 3*x**5 + 15*x
# Definisi persamaan yang terintegrasi secara analitik
def F(s):
    return (1/10)*s**10 + (3/6)*s**6 + (15/2)*s**2
if f(a)*f(b) < 0: res_analitis = float(F(b) + F(a))
else : res_analitis = float(F(b) - F(a))

integralMidpoint = h*abs(f(xData))
res_numerik = sum(integralMidpoint)
print(f"Hasil integrasi : {res_numerik}")
endTime = t.time()
print(f"Nilai error : {abs((res_numerik-res_analitis)/res_analitis)*100}%")
print("Durasi kalkulasi (sekon) : %0.10f" %(float(endTime-startTime)))
print("Semua pemrograman ini dibuat secara orisinil oleh MUHAMMAD HURRICANE 1906356191")

plt.plot(xData,f(xData),color='blue')
plt.plot(xReal,f(xReal),color='red')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.title('Latihan Integral Trapezoid Vectorized')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
plt.show() #agar plot terakhir tetap ditampilkan
