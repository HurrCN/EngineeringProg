print("PEMROGRAMAN TEKNIK-02")
print("TUGAS 5.1 INTEGRAL NUMERIK METODE TITIK TENGAH")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

import matplotlib.pyplot as plt
import numpy as np
import time as t

# Input Data
print("==========INTEGRAL METODE TITIK TENGAH==========")
a = float(input('Titik Batas x1 : '))
b = float(input('Titik batas x2 : '))
seg = float(input('Banyak segmen : '))
interval = float(abs((b-a)/seg))
firstUpperBoundary = float(a+interval)
firstMidPoint = (a+firstUpperBoundary)/2
print('Interval : %0.9f' %(interval))
print('Batas Atas Pertama : %0.9f' %(firstUpperBoundary))
print('Titik Tengah Pertama : %0.8f' %(firstMidPoint))

startTime = t.time()

# Definisi Fungsi yang akan Diintegrasikan
def f(x):
    # ini persamaannya 1*x**9 +0*x**6 + 3*x**5 + 6*x**1 + 9*x**1
    return x**9 + 3*x**5 + 15*x
# Definisi persamaan yang terintegrasi secara analitik
def F(s):
    return (1/10)*s**10 + (3/6)*s**6 + (15/2)*s**2

if f(a)*f(b) < 0:
    res_analitis = float(F(b) + F(a))
else :
    res_analitis = float(F(b) - F(a))

# Model Operasi Metode Titik Tengah
def operationMidPoint(a,b,seg,interval,firstMidPoint):
    sumArea = float(0)
    i = 1
    iterasi = True
    while iterasi:
        Xi = (interval*(i-1)) + firstMidPoint
        X1 = a+(interval*(i-1))
        X2 = a+(interval*(i))
        area = abs(float(interval*f(Xi)))
        sumArea = abs(sumArea + area)
        print('i= %d, X1= %0.3f, Xi= %0.3f, X2= %0.3f, f(Xi)= %0.8f, AREA= %0.8f, SUM= %0.8f' % (i,X1,Xi,X2,f(Xi),area,sumArea))
        i = i + 1
        iterasi = Xi <= b and i <= seg
        """
        SKEMA INDEXING TITIK
        |c   d|
        |b   a|
        """
                                # FORMAT (UNTUK PENGINGAT)
        dot_a = [X2,0]          # dot_a = [dot_a[0], dot_a[1]]
        dot_b = [X1,0]          # dot_b = [dot_b[0], dot_b[1]]
        dot_c = [X1,f(Xi)]      # dot_c = [dot_c[0], dot_c[1]]
        dot_d = [X2,f(Xi)]      # dot_d = [dot_d[0], dot_d[1]]
        """
        SKEMA INDEXING GARIS
              upper
              ____  
         left |  | right
              |  | 
            Xo|__|Xi
             below
        """
        # PENENTUAN TITIK-TITIK PADA TIAP GARIS
        line_below_x  =  [dot_a[0],dot_b[0]]
        line_below_y  =  [dot_a[1],dot_b[1]]
        line_left_x   =  [dot_b[0],dot_c[0]]
        line_left_y   =  [dot_b[1],dot_c[1]]
        line_upper_x  =  [dot_d[0],dot_c[0]]
        line_upper_y  =  [dot_d[1],dot_c[1]]
        line_right_x  =  [dot_a[0],dot_d[0]]
        line_right_y  =  [dot_a[1],dot_d[1]]
        plt.plot(line_below_x, line_below_y, color='blue')
        plt.plot(line_left_x, line_left_y, color='blue')
        plt.plot(line_upper_x, line_upper_y, color='blue')
        plt.plot(line_right_x, line_right_y, color='blue')
        plt.fill_between(line_below_x, line_below_y, line_upper_y, facecolor = 'lightskyblue')
        plt.pause(0.00001)
    return sumArea

res_numerik = operationMidPoint(a,b,seg,interval,firstMidPoint)
error = float(abs((res_numerik - res_analitis)/res_analitis)*100)
print('Luas Permukaan Numerik :%0.15f' %(res_numerik))
print('Luas Permukaan Analitis :%0.15f' %(res_analitis))
print('Besar simpangan : %0.3f' %(error),"%")

xValue = np.linspace(a,b,10000)
plt.plot(xValue,f(xValue),color='red')

endTime = t.time()
print(f"Waktu komputasi yang dibutuhkan (sekon): {endTime-startTime}")
print("Semua pemrograman ini dibuat secara orisinil oleh MUHAMMAD HURRICANE 1906356191")

plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.title('Latihan Integral Midpoint Biasa')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
plt.show() #agar plot terakhir tetap ditampilkan