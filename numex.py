import numpy
import scipy
import os
import math
from random import seed
from random import randint
import matplotlib.pyplot as plt


def tensor():   #Randomowy tensor naprezenia
    
    zakres_naprezen = 20        #Zakres
    sx = randint(-zakres_naprezen, zakres_naprezen)
    sy = randint(-zakres_naprezen, zakres_naprezen)
    sz = randint(-zakres_naprezen, zakres_naprezen)
    txy = randint(-zakres_naprezen, zakres_naprezen)
    txz = randint(-zakres_naprezen, zakres_naprezen)
    tyz = randint(-zakres_naprezen, zakres_naprezen)
    
    Ts = numpy.array([[sx, txy, txz], [txy, sy, tyz],[txz, tyz, sz]])    #Macierz napreżeń
    return(Ts)

def wersory():  #Zbiór wersorów
    pow = 3000                    #Powtórzenia, ilość wersorów
    zakres = 50                 #Zakres wartosci poszczegolnego wersora
    versors = numpy.array([])   #Zbior wersorów
    for r in range(pow):
        
        x = randint(-zakres,zakres )
        y = randint(-zakres,zakres )    #Skladowe wektora
        z = randint(-zakres,zakres )
        
        length_xyz = math.sqrt((x**2) + (y**2) + (z**2))    #Dlugosc wektora
        versor_xyz = numpy.array([x/length_xyz, y/length_xyz, z/length_xyz])    #Wersor
        
        versors = numpy.append(versors, versor_xyz, axis=0)     #Zbior wersorów 1D
        
    versors = numpy.reshape(versors, (-1, 3))                   #Zbiór wersorów 2D 3 x pow
    return(pow, versors)

def wektory():
    Ts = tensor()                           #importowanie Tensora 
    pow, versors = wersory()                #importowanie powtorzen i wersorów
    wektory_naprezenia = numpy.array([])    #Zbior wektorow naprezenia
    
    for r in range(pow):
        wektor_napreżenia = Ts @ versors[r,:]   #wektor naprezenia
        wektory_naprezenia = numpy.append(wektory_naprezenia, wektor_napreżenia, axis=0)
    
    wektory_naprezenia = numpy.reshape(wektory_naprezenia, (-1, 3))     #Zbiór wektorow naprezenia 2D 3 x pow
    
    
    SIGMA = numpy.array ([])        #Zbior naprezen normalnych
    TAU = numpy.array([])           #Zbior naprezen stycznych
    
    for rr in range(pow):
        sigma = numpy.array([(wektory_naprezenia[rr,0] * versors[rr,0]) + (wektory_naprezenia[rr,1] * versors[rr,1]) + (wektory_naprezenia[rr,2] * versors[rr,2])])
        wek_napr_sq = (wektory_naprezenia[rr,0] * wektory_naprezenia[rr,0]) + (wektory_naprezenia[rr,1] * wektory_naprezenia[rr,1]) + (wektory_naprezenia[rr,2] * wektory_naprezenia[rr,2])
        tau = numpy.array([math.sqrt(wek_napr_sq - (sigma**2))])
        
        SIGMA = numpy.append(SIGMA, sigma, axis=0)
        TAU = numpy.append(TAU, tau, axis=0)
    
    
    return(SIGMA, TAU)


SIGMA, TAU = wektory()
plt.plot(SIGMA, TAU, 'b+')         #os_x, os_y, 'ro'
plt.axis([-50, 50, -5, 50])
plt.xlabel('Sigma')
plt.ylabel('Tau')
plt.show()