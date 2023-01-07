print("PEMROGRAMAN TEKNIK-02")
print("TUGAS 6.2 DOUBLE AND TRIPLE INTEGRAL METODE TRAPESIUM")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

import matplotlib.pyplot as plt
import sympy as sp
import time as t

print("========== DOUBLE INTEGRAL ==========")
a1 = float(input('Titik Batas x1 : '))
b1 = float(input('Titik batas x2 : '))
c1 = float(input('Titik Batas y1 : '))
d1 = float(input('Titik batas y2 : '))
#nx = int(input('Banyak segmen pada x : '))

print("\n========== TRIPLE INTEGRAL  ==========")
a2 = float(input('Titik Batas x1 : '))
b2 = float(input('Titik batas x2 : '))
c2 = float(input('Titik Batas y1 : '))
d2 = float(input('Titik batas y2 : '))
e2 = float(input('Titik Batas z1 : '))
f2 = float(input('Titik batas z2 : '))
#ny = int(input('Banyak segmen pada y : '))
n = 100

print("\n==== DURASI KALKULASI ====")
# Persamaan untuk Integral Lipat Dua
def f(x,y):
    # ini persamaannya 1*x**9 +0*y**6 + 3*x**5 + 6*y**1 + 9*y**1
    return x**9 + 3*x**5 + 15*y
# Persamaan untuk Integral Lipat Tiga
def g(x,y,z):
    # ini persamaannya 1*x**9 + 0*y**6 + 3*y**5 + 6*z**1 + 9*z**1
    return x**9 + 3*y**5 + 15*z

def doubleIntegral_trap(a1,b1,c1,d1,n):
    startTime = t.time()
    hx = float(abs(a1-b1)/n)
    hy = float(abs(c1-d1)/n)
    luas2D = 0
    for i in range (n):
        for j in range (n):
            xo = a1 + i*hx
            xi = a1 + (i+1)*hx
            yo = c1 + j*hy
            yi = c1 + (j+1)*hy
            luas2D += (f(xo,yo)+f(xi,yi))*hx*hy/2
    endTime = t.time()
    print("Durasi Double Integral (sekon) : %0.20f" %(float(endTime-startTime)))
    return luas2D

def tripleIntegral_trap(a2,b2,c2,d2,e2,f2,n):
    startTime = t.time()
    hx = float(abs(a2-b2)/n)
    hy = float(abs(c2-d2)/n)
    hz = float(abs(e2-f2)/n)
    luas3D = 0
    for i in range (n):
        for j in range (n):
            for k in range (n):
                xo = a2 + i*hx
                xi = a2 + (i+1)*hx
                yo = c2 + j*hy
                yi = c2 + (j+1)*hy
                zo = e2 + k*hz
                zi = e2 + (k+1)*hz
                luas3D += (g(xo,yo,zo)+g(xi,yi,zi))*hx*hy*hz/2
    endTime = t.time()
    print("Durasi Triple Integral (sekon) : %0.20f" %(float(endTime-startTime)))
    return luas3D

def analitisDouble(a1,b1,c1,d1):
    x, y = sp.symbols('x  y')
    luas2D = sp.integrate(f(x,y),(x,a1,b1),(y,c1,d1))
    return luas2D

def analitisTriple(a2,b2,c2,d2,e2,f2):
    x, y, z = sp.symbols('x  y  z')
    luas3D = sp.integrate(g(x,y,z),(x,a2,b2),(y,c2,d2),(z,e2,f2))
    return luas3D

res_numerik1 = doubleIntegral_trap(a1,b1,c1,d1,n)
res_analitis1 = analitisDouble(a1,b1,c1,d1)
res_numerik2 = tripleIntegral_trap(a2,b2,c2,d2,e2,f2,n)
res_analitis2 = analitisTriple(a2,b2,c2,d2,e2,f2)
print("\n==== HASIL DOUBLE INTEGRAL ====")
print(f"Hasil Double Integral Numerik : {res_numerik1} satuan luas")
print(f"Hasil Double Integral Analitis : {res_analitis1} satuan luas")
print(f"Besar error : {float((abs(res_analitis1-res_numerik1)/res_analitis1)*100)} %")

print("\n==== HASIL TRIPLE INTEGRAL ====")
print(f"Hasil Triple Integral Numerik : {res_numerik2} satuan luas")
print(f"Hasil Triple Integral Analitis : {res_analitis2} satuan luas")
print(f"Besar error : {float((abs(res_analitis2-res_numerik2)/res_analitis2)*100)} %")
