print("PEMROGRAMAN TEKNIK-02")
print("TUGAS 6 DOUBLE AND TRIPLE INTEGRAL + MONTE CARLO")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

from scipy import random
import sympy as sp
import numpy as np
import time as t

print("\n########## BAGIAN INPUT DATA ##########")
print("========== SINGLE INTEGRAL ==========")
a = float(input('Titik Batas x1 : '))
b = float(input('Titik batas x2 : '))

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

n = int(input('Banyak segmen tinjauan pada setiap dimensi : '))

print("\n==== DURASI KALKULASI (SEKON) ====")
# Koefisien persamaan dibuat dari NPM mahasiswa
# Persamaan untuk Integral Lipat 1
def e(x):
    # ini persamaannya 1*x**9 +0*x**6 + 3*x**5 + 6*x**1 + 9*x**1
    return x**9 + 3*x**5 + 15*x

# Persamaan untuk Integral Lipat Dua
def f(x,y):
    # ini persamaannya 1*x**9 +0*y**6 + 3*x**5 + 6*y**1 + 9*y**1
    return x**9 + 3*x**5 + 15*y

def g(x,y,z):
    # ini persamaannya 1*x**9 + 0*y**6 + 3*y**5 + 6*z**1 + 9*z**1
    return x**9 + 3*y**5 + 15*z

def MonteCarlo_single(a,b,n):
    mulai = t.time()
    f_star = float(0.0) # sebagai akumulator
    X = np.zeros(n)
    counter_in = 0
    for i in range(n):
        X[i] = random.uniform(a,b)
    for i in range (n):
        if e(X[i]) >= 0:
            counter_in += 1
            f_star += e(X[i])
    f_res = f_star/float(counter_in)
    area = counter_in/float(n) * (b-a)
    stop = t.time()
    print("Single Integral Monte Carlo : %0.20f" %(float(stop-mulai)))
    return area*f_res

def doubleIntegral_trap(a1,b1,c1,d1,n):
    mulai = t.time()
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
    stop = t.time()
    print("\nDouble Integral Trapesium : %0.20f" %(float(stop-mulai)))
    return luas2D

def doubleIntegral_midpoint(a1,b1,c1,d1,n):
    mulai = t.time()
    hx = float(abs(a1-b1)/n)
    hy = float(abs(c1-d1)/n)
    luas2D = 0
    for i in range (n):
        for j in range (n):
            xi = a1 + i*hx + 0.5*hx
            yj = c1 + j*hy + 0.5*hy
            luas2D += hx*hy*f(xi,yj)
            #print(f"Hingga (x,y) = ({xi},{yj}), didapatkan luas daerah = {luas2D}")
    stop = t.time()
    print("Double Integral Midpoint : %0.20f" %(float(stop-mulai)))
    return luas2D

def MonteCarlo_double(a1,b1,c1,d1,n):
    mulai = t.time()
    f_star = float(0.0) # sebagai akumulator
    X = np.zeros(n)
    Y = np.zeros(n)
    counter_in = 0
    for i in range(n):
        X[i] = random.uniform(a1,b1)
        Y[i] = random.uniform(c1,d1)
    for i in range (n):
        if f(X[i],Y[i]) >= 0:
            counter_in += 1
            f_star += f(X[i],Y[i])
    f_res = f_star/float(counter_in)
    area = (counter_in/float(n)) *(b1-a1)*(d1-c1)
    stop = t.time()
    print("Double Integral Monte Carlo : %0.20f" %(float(stop-mulai)))
    return area*f_res

def tripleIntegral_trap(a2,b2,c2,d2,e2,f2,n):
    mulai = t.time()
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
    stop = t.time()
    print("\nTriple Integral Trapesium : %0.20f" %(float(stop-mulai)))
    return luas3D

def tripleIntegral_midpoint(a2,b2,c2,d2,e2,f2,n):
    mulai = t.time()
    hx = float(abs(a2-b2)/n)
    hy = float(abs(c2-d2)/n)
    hz = float(abs(e2-f2)/n)
    luas3D = 0
    for i in range (n):
        for j in range (n):
            for k in range (n):
                xi = a2 + i*hx + 0.5*hx
                yj = c2 + j*hy + 0.5*hy
                zk = e2 + k*hz + 0.5*hz
                luas3D += hx*hy*hz*g(xi,yj,zk)
                #print(f"Hingga (x,y) = ({xi},{yj}), didapatkan luas daerah = {luas2D}")
    stop = t.time()
    print("Triple Integral Midpoint : %0.20f" %(float(stop-mulai)))
    return luas3D

def MonteCarlo_triple(a2,b2,c2,d2,e2,f2,n):
    mulai = t.time()
    f_star = float(0.0) # sebagai akumulator
    X = np.zeros(n)
    Y = np.zeros(n)
    Z = np.zeros(n)
    counter_in = 0
    for i in range(n):
        X[i] = random.uniform(a2,b2)
        Y[i] = random.uniform(c2,d2)
        Z[i] = random.uniform(e2,f2)
    for i in range (n):
        if g(X[i],Y[i],Z[i]) >= 0:
            counter_in += 1
            f_star += g(X[i],Y[i],Z[i])
    f_res = f_star/float(counter_in)
    area = (counter_in/float(n)) *(b2-a2)*(d2-c2)*(f2-e2)
    stop = t.time()
    print("Triple Integral Monte Carlo : %0.20f" %(float(stop-mulai)))
    return area*f_res

def analitisSingle(a,b):
    x = sp.symbols('x')
    luas1D = sp.integrate(e(x),(x,a,b))
    return luas1D

def analitisDouble(a1,b1,c1,d1):
    x, y = sp.symbols('x  y')
    luas2D = sp.integrate(f(x,y),(x,a1,b1),(y,c1,d1))
    return luas2D

def analitisTriple(a2,b2,c2,d2,e2,f2):
    x, y, z = sp.symbols('x  y  z')
    luas3D = sp.integrate(g(x,y,z),(x,a2,b2),(y,c2,d2),(z,e2,f2))
    return luas3D

res_numerik30 = MonteCarlo_single(a,b,n)
res_analitis0 = analitisSingle(a,b)

res_numerik11 = doubleIntegral_trap(a1,b1,c1,d1,n)
res_numerik12 = doubleIntegral_midpoint(a1,b1,c1,d1,n)
res_numerik31 = MonteCarlo_double(a1,b1,c1,d1,n)
res_analitis1 = analitisDouble(a1,b1,c1,d1)

res_numerik21 = tripleIntegral_trap(a2,b2,c2,d2,e2,f2,n)
res_numerik22 = tripleIntegral_midpoint(a2,b2,c2,d2,e2,f2,n)
res_numerik32 = MonteCarlo_triple(a2,b2,c2,d2,e2,f2,n)
res_analitis2 = analitisTriple(a2,b2,c2,d2,e2,f2)

print("\n########## BAGIAN OUTPUT DATA ##########")
print("==== HASIL SINGLE INTEGRAL ====")
print(f"Hasil Single Integral Analitis : {res_analitis0} satuan luas")
print(f"Hasil Single Integral Monte Carlo : {res_numerik30} satuan luas | Error : {float((abs(res_analitis0-res_numerik30)/res_analitis0)*100)} %")

print("\n==== HASIL DOUBLE INTEGRAL ====")
print(f"Hasil Double Integral Analitis : {res_analitis1} satuan luas")
print(f"Hasil Double Integral Trapesium : {res_numerik11} satuan luas | Error : {float((abs(res_analitis1-res_numerik11)/res_analitis1)*100)} %")
print(f"Hasil Double Integral Midpoint : {res_numerik12} satuan luas | Error : {float((abs(res_analitis1-res_numerik12)/res_analitis1)*100)} %")
print(f"Hasil Double Integral Monte Carlo : {res_numerik31} satuan luas | Error : {float((abs(res_analitis1-res_numerik31)/res_analitis1)*100)} %")

print("\n==== HASIL TRIPLE INTEGRAL ====")
print(f"Hasil Triple Integral Analitis : {res_analitis2} satuan luas")
print(f"Hasil Triple Integral Trapesium : {res_numerik21} satuan luas | Error : {float((abs(res_analitis2-res_numerik21)/res_analitis2)*100)} %")
print(f"Hasil Triple Integral Midpoint : {res_numerik22} satuan luas | Error : {float((abs(res_analitis2-res_numerik22)/res_analitis2)*100)} %")
print(f"Hasil Triple Integral Monte Carlo : {res_numerik32} satuan luas | Error : {float((abs(res_analitis2-res_numerik32)/res_analitis2)*100)} %")