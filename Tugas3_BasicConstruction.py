print("PEMROGRAMAN TEKNIK-02")
print("PEKAN 2 : BASIC CONSTRUCTION TUGAS 3")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

from pandas import read_csv
import matplotlib.pyplot as plt
from math import sqrt
url = 'https://raw.githubusercontent.com/HurrCN/PemrogramanTeknik02/MyProject/PEMROTEK-02_Muhammad%20Hurricane_DataReadingInput.csv'
dataframe = read_csv(url, header=None, sep=';')
data = dataframe.values
h, k = data[:, 0], data[:, 1]
n = len(h)
print("\nBerikut adalah data inputnya:")
print(dataframe.head(9))

def f(x,y):
    return 3*sqrt(x)*y**2
def Main(h,k,n):
    for i in range (0,n,1):
        a = h[i]
        b = k[i]
        if a < 0 :
            print('f(%d,%d) = Tak terdefinisi' % (a,b))
        else:
            res = f(a,b)
            print('f(%d,%d) = %0.3f' % (a,b,res))
Main(h,k,n)
