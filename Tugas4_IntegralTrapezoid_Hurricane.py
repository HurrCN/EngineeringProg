print("PEMROGRAMAN TEKNIK-02")
print("TUGAS 4   : INTEGRAL NUMERIK METODE TRAPEZOID")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

import numpy as np
import matplotlib.pyplot as plt
import time as t

# Penginputan batas dan segmen
a = float(input('Batas 1: '))
b = float(input('Batas 2: '))
seg = int(input('Banyak segmen: '))

startTime = t.time()

interval = float(abs((b-a)/seg))
Xo = float(a)

# Definisi persamaan yang ingin diintegrasi
def f(x):
    # ini persamaannya 1*x**9 +0*x**6 + 3*x**5 + 6*x**1 + 9*x**1
    return x**9 + 3*x**5 + 15*x
# Definisi persamaan yang terintegrasi secara analitik
def F(s):
    return (1/10)*s**10 + (3/6)*s**6 + (15/2)*s**2

# Menghindari peniadaan hasil antara zona di atas dan di bawah sumbu x
if f(a)*f(b) < 0:
    res_analitis = float(F(b) + F(a))
else :
    res_analitis = float(F(b) - F(a))

# Codingan Trapezoid Biasa
def Trapezoid(a,b,seg,interval,Xo):
    totalArea = float(0)                                # Luas awal = 0
    i = 1                                               # Pasang step awal di n = 1
    iterasi = True
    while iterasi:
        Xi = float(a + (interval*i))                    # Jadi nilai batas atas pada tiap segmen
        area_n = float(abs(((f(Xo)+f(Xi))/2)*interval))    # Luas per segmen = Luas trapesium
        totalArea = float(totalArea + area_n)           # Proses akumulasi hasil
        print('i= %d, Xo= %0.8f, Xi= %0.8f, f(Xo)= %0.8f, f(Xi)= %0.8f, AREA= %0.8f, SUM= %0.8f' % (i,Xo,Xi,f(Xo),f(Xi),area_n,totalArea))
        i = i + 1
        iterasi = i <= seg
        """
        SKEMA INDEXING TITIK
        |c   d|
        |b   a|
        """
                                # FORMAT (UNTUK PENGINGAT)
        dot_a = [Xi,0]          # dot_a = [dot_a[0], dot_a[1]]
        dot_b = [Xo,0]          # dot_b = [dot_b[0], dot_b[1]]
        dot_c = [Xo,f(Xo)]      # dot_c = [dot_c[0], dot_c[1]]
        dot_d = [Xi,f(Xi)]      # dot_d = [dot_d[0], dot_d[1]]
        """
        SKEMA INDEXING GARIS
                /|
        slide  / |
              /  |
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
        line_slide_x  =  [dot_d[0],dot_c[0]]
        line_slide_y  =  [dot_d[1],dot_c[1]]
        line_right_x  =  [dot_a[0],dot_d[0]]
        line_right_y  =  [dot_a[1],dot_d[1]]
        plt.plot(line_below_x, line_below_y, color='blue')
        plt.plot(line_left_x, line_left_y, color='blue')
        plt.plot(line_slide_x, line_slide_y, color='blue')
        plt.plot(line_right_x, line_right_y, color='blue')
        plt.fill_between(line_below_x, line_below_y, line_slide_y, facecolor = 'lightskyblue')
        Xo = Xi
        plt.pause(0.00001)
    return totalArea

res_numerik = float(Trapezoid(a,b,seg,interval,Xo))
error = float(abs((res_numerik - res_analitis)/res_analitis)*100)
print('Luas Permukaan Numerik :%0.15f' %(res_numerik))
print('Luas Permukaan Analitis :%0.15f' %(res_analitis))
print('Besar simpangan : %0.3f' %(error),"%")

xValue = np.linspace(a,b,10000)
plt.plot(xValue,f(xValue),color='red')

endTime = t.time()
print("Durasi kalkulasi (sekon) : %0.20f" %(float(endTime-startTime)))
print("Semua pemrograman ini dibuat secara orisinil oleh MUHAMMAD HURRICANE 1906356191")

plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.title('Latihan Integral Trapezoid')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
plt.show() #agar plot terakhir tetap ditampilkan
