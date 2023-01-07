print("PEMROGRAMAN TEKNIK-02")
print("PEKAN 2 : BASIC CONSTRUCTION TUGAS 2")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191")

from math import sqrt
h = int(input('Batas bawah: '))
k = int(input('Batas atas: '))
i = int(input('Interval: '))

def f(x,y):
    return 3*sqrt(x)*y**2
def Main(h,k):
    for a in range(h,k+1,i):
        for b in range (k,h-1,-1*i):
            if a >= 0 :
                res = f(a,b)
                print('f(%d,%d) = %0.3f' % (a,b,res))
            else:
                print('f(%d,%d) = Tak terdefinisi' % (a,b))
Main(h,k)