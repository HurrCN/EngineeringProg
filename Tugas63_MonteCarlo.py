from scipy import random
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import time as t

print("========== SINGLE INTEGRAL ==========")
a = float(input('Titik Batas x1 : '))
b = float(input('Titik batas x2 : '))

print("========== DOUBLE INTEGRAL ==========")
a1 = float(input('Titik Batas x1 : '))
b1 = float(input('Titik batas x2 : '))
c1 = float(input('Titik Batas y1 : '))
d1 = float(input('Titik batas y2 : '))

print("\n========== TRIPLE INTEGRAL  ==========")
a2 = float(input('Titik Batas x1 : '))
b2 = float(input('Titik batas x2 : '))
c2 = float(input('Titik Batas y1 : '))
d2 = float(input('Titik batas y2 : '))
e2 = float(input('Titik Batas z1 : '))
f2 = float(input('Titik batas z2 : '))

N = 100 # jumlah segmen pada area tinjauan

def e(x):
    return x**9 + 3*x**5 + 15*x

# Persamaan untuk Integral Lipat Dua
def f(x,y):
    # ini persamaannya 1*x**9 +0*y**6 + 3*x**5 + 6*y**1 + 9*y**1
    return x**9 + 3*x**5 + 15*y
# Persamaan untuk Integral Lipat Tiga
def g(x,y,z):
    # ini persamaannya 1*x**9 + 0*y**6 + 3*y**5 + 6*z**1 + 9*z**1
    return x**9 + 3*y**5 + 15*z

def MonteCarlo_single(a,b,N):
    mulai = t.time()
    f_star = float(0.0) # sebagai akumulator
    X = np.zeros(N)
    counter_in = 0
    for i in range(len(X)):
        X[i] = random.uniform(a,b)
    for i in range (N):
        if e(X[i]) >= 0:
            counter_in += 1
            f_star += e(X[i])
    f_res = f_star/float(counter_in)
    area = counter_in/float(N) * (b-a)
    stop = t.time()
    print("Single Integral Monte Carlo : %0.20f" %(float(stop-mulai)))
    return area*f_res

def MonteCarlo_double(a1,b1,c1,d1,N):
    mulai = t.time()
    f_star = float(0.0) # sebagai akumulator
    X = np.zeros(N)
    Y = np.zeros(N)
    counter_in = 0
    for i in range(N):
        X[i] = random.uniform(a1,b1)
        Y[i] = random.uniform(c1,d1)
    for i in range (N):
        if f(X[i],Y[i]) >= 0:
            counter_in += 1
            f_star += f(X[i],Y[i])
    f_res = f_star/float(counter_in)
    area = (counter_in/float(N)) *(b1-a1)*(d1-c1)
    stop = t.time()
    print("Double Integral Monte Carlo : %0.20f" %(float(stop-mulai)))
    return area*f_res

def MonteCarlo_triple(a2,b2,c2,d2,e2,f2,N):
    mulai = t.time()
    f_star = float(0.0) # sebagai akumulator
    X = np.zeros(N)
    Y = np.zeros(N)
    Z = np.zeros(N)
    counter_in = 0
    for i in range(N):
        X[i] = random.uniform(a2,b2)
        Y[i] = random.uniform(c2,d2)
        Z[i] = random.uniform(e2,f2)
    for i in range (N):
        if g(X[i],Y[i],Z[i]) >= 0:
            counter_in += 1
            f_star += g(X[i],Y[i],Z[i])
    f_res = f_star/float(counter_in)
    area = (counter_in/float(N)) *(b2-a2)*(d2-c2)*(f2-e2)
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

res_numerik30 = MonteCarlo_single(a,b,N)
res_numerik31 = MonteCarlo_double(a1,b1,c1,d1,N)
res_numerik32 = MonteCarlo_triple(a2,b2,c2,d2,e2,f2,N)

res_analitis0 = analitisSingle(a,b)
res_analitis1 = analitisDouble(a1,b1,c1,d1)
res_analitis2 = analitisTriple(a2,b2,c2,d2,e2,f2)

print(f"\nHasil Single Integral Analitis : {res_analitis0} satuan luas")
print(f"Hasil Single Integral Monte Carlo : {res_numerik30} satuan luas | Error : {float((abs(res_analitis0-res_numerik30)/res_analitis0)*100)} %")

print(f"\nHasil Double Integral Analitis : {res_analitis1} satuan luas")
print(f"Hasil Double Integral Monte Carlo : {res_numerik31} satuan luas | Error : {float((abs(res_analitis1-res_numerik31)/res_analitis1)*100)} %")

print(f"\nHasil Triple Integral Analitis : {res_analitis2} satuan luas")
print(f"Hasil Triple Integral Monte Carlo : {res_numerik32} satuan luas | Error : {float((abs(res_analitis2-res_numerik32)/res_analitis2)*100)} %")