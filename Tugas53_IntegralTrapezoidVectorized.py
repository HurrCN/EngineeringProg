print("PEMROGRAMAN TEKNIK-02")
print("TUGAS 5.3 INTEGRAL NUMERIK METODE TRAPEZOID VECTORIZED")
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
xReal = np.linspace(a,b,10000,dtype=float)
xData = np.linspace(a,b,seg+1, dtype=float)

# Definisi Fungsi yang akan Diintegrasikan
def f(x):
    # ini persamaannya 1*x**9 +0*x**6 + 3*x**5 + 6*x**1 + 9*x**1
    return x**9 + 3*x**5 + 15*x
# Definisi persamaan yang terintegrasi secara analitik
def F(s):
    return (1/10)*s**10 + (3/6)*s**6 + (15/2)*s**2
if f(a)*f(b) < 0: res_analitis = float(F(b) + F(a))
else : res_analitis = float(F(b) - F(a))

integralTrapezoid = h*(sum(abs(f(xData)))-(0.5*f(a))-(0.5*f(b)))
res_numerik = integralTrapezoid
print(f"Hasil integrasi : {res_numerik}")
endTime = t.time()
print(f"Nilai error : {abs((res_numerik-res_analitis)/res_analitis)*100}%")
print("Durasi kalkulasi (sekon) : %0.20f" %(float(endTime-startTime)))
print("Semua pemrograman ini dibuat secara orisinil oleh MUHAMMAD HURRICANE 1906356191")

plt.plot(xData,f(xData),color='blue')
plt.plot(xReal,f(xReal),color='red')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.title('Latihan Integral Midpoint Vectorized')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
plt.show() #agar plot terakhir tetap ditampilkan