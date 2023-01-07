print("PEMROGRAMAN TEKNIK-02")
print("LATIHAN PLOTTING DENGAN PENGOLAHAN PARAMETER X-Y")
print("Nama      : MUHAMMAD HURRICANE")
print("NPM       : 1906356191") 

import matplotlib.pyplot as plt
import math


b = float(input('\nBatas bawah (jam): '))
a = float(input('Batas atas (jam): '))
seg = int(input('Jumlah segmen area tinjauan: '))
v = float(input('Volume Awal : '))
h = abs(a-b)/seg #sebagai interval

#Definisi persamaan diferensial yang akan ditinjau
def dVdt(t) :
    return (42*t*math.e**(-0.273*t))+10*math.cos(2*math.pi*t)

#Definisi Operasi ODE
#Metode yang dipakai : Metode Euler
def ODEops(a,b,seg,v,h):
    Vo = v #mula-mula
    def Discharge():
        if 0 < 0.75*0.2*(Vo-4000)**2 <= 25 and Vo > 4000:
            return 0.75*0.2*(Vo-4000)**2
        elif 25 < 0.8*0.2*(Vo-4000)**2 <= 50 and Vo > 4000:
            return 0.8*0.2*(Vo-4000)**2
        elif 50 < 0.85*0.2*(Vo-4000)**2 <= 75 and Vo > 4000:
            return 0.85*0.2*(Vo-4000)**2
        elif 75 < 0.75*0.2*(Vo-4000)**2 and Vo > 4000:
            return 0.9*0.2*(Vo-4000)**2
        else :
            return 0
    iterState = True
    step = 0
    while iterState:
        time = b + step*h
        Vi = Vo + (dVdt(time)-Discharge())*h
        step = step + 1
        iterState = step < 100 
        print('step = %d | t = %0.4f jam | V = %0.10f m^3 | D = %0.3f' %(step,time,Vo,Discharge()))
        plt.scatter(time,Vi,color='b') #Color = biru
        plt.plot(time,Vi) #Color = biru
        Vo = Vi
        plt.pause(0.00001)
    print('Volume Akhir setelah %0.4f jam adalah %0.10f' %(time,Vo))
    plt.legend(['ODE plot (Iterasi %i kali)' %(step)], loc="upper left", fontsize="x-small")
    

ODEops(a,b,seg,v,h)
plt.xlabel('waktu (jam)')
plt.ylabel('Volume (m^3)')
plt.title('Volume Air dalam Resorvoir')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
plt.show() #agar plot terakhir tetap ditampilkan