import numpy
import scipy
import os
import math
from random import seed
from random import randint
import matplotlib.pyplot as plt


def menu():         ##Dodać jakieś inne funkcje
    print ("""\n\n\n
    Wybierz opcje aby obliczyć char.geometryczne!
    [1] Prostokat
    [2] Trojkat
    [3] Kolo
    
    [4] Katownik
    [5] Teownik
    [6] Dwuteownik
    [7] Ceownik
    
    [0] Exit
    
    Numer opcji:""")
    opt = input()
    

    if opt == '1':
        prostokat()
    elif opt == '2':
        trojkat()
    elif opt == '3':
        kolo()
    elif opt == '4':
        katownik()
    elif opt == '5':            
        teownik()
    elif opt == '6':
        dwuteownik()
    elif opt == '7':
        ceownik()
    elif opt == '0':
        return()
    else:
        print ("Wpisales zla liczbe \nWcinij ENTER aby powrócić")
        input()
        menu()


def prostokat():
    print("Wybrales prostokat!\n")
    b = float(input("Szerokosc: b = "))
    h = float(input("Wysokosć: h = "))
    x = float(0)
    y = float(0)
                                    
    square(h,b,x,y)
    A, xc, yc, Jxc, Jyc, Jxyc = square(h,b,x,y)
    J0 = int(Jxc + Jyc)
    wyniki(A,xc,yc,Jxc,Jyc,Jxyc,J0)
    dewiacja(Jxc,Jyc,Jxyc)
    input("Powrót do menu \n")
    menu()
    
def trojkat():  #Dla trojkata prostokatnego
    print("Podaj wymiary trójkąta prostokątnego")
    
    b = float(input("Wymiar pierwszej przyprostokątnej: "))
    h = float(input("Wymiar drugiej przyprostokątnej"))
    
    A = (b * h) / 2    
    xc = 1/3 * b
    yc = 1/3 * h
    
    Jx = (b * h**3) / 36
    Jy = (h * b**3) / 36
    Jxy = - (((b**2) * (h**2)) / 72)
    J0 = Jx + Jy
    
    wyniki(A, xc, yc, Jx, Jy, Jxy, J0)
    dewiacja(Jx, Jy, Jxy)          
    input("Powrót do menu \n")
    menu()
    
def kolo():
    print("Wybrałes przekrój kolisty \n")
    R = float(input("Podaj srednice zewnętrzną: R = "))
    r = float(input("Podaj srednice wewnetrzna: r = "))
    
    if r > R: 
        print("\n\nSrednica wew > zew \nBledne dane \nWcisnij ENTER aby powrocic")
        input()
        kolo()
    else: 
        AR = R ** 2 * 3.1415
        Ar = r ** 2 * 3.1415
        A = AR-Ar
        xc = 0
        yc = 0
        Jxc = (3.1415 * (R-r)**4)/4
        Jyc = Jxc
        Jxyc = 0
        J0 = int(Jxc+Jyc)
        
        wyniki(A,xc,yc,Jxc,Jyc,Jxyc,J0)       
        input("Powrót do menu \n")
        menu()   

def katownik():
    print("Wybrałes kątownik! \n\nPodaj wymiary:")
    kat_h = float(input("Podaj wysokosc katownika: h = "))
    kat_b = float(input("Podaj szerokosc katownika: b = "))
    gr_h = float(input("Podaj grubosc --poziomej-- czesci: gr_h = "))
    gr_b = float(input("Podaj grubosc | pionowej | czesci: gr_b = "))
    
    h1 = kat_h
    b1 = gr_b
    x1 = 0
    y1 = 0
    square(h1,b1,x1,y1)
    A1,xc1,yc1,Jxc1,Jyc1,Jxyc1 = square(h1,b1,x1,y1) 
    ###Tu mamy dane na temat pionowej czesci katownika
    
    h2 = gr_h
    b2 = kat_b - gr_b
    x2 = gr_b
    y2 = 0
    square(h2,b2,x2,y2)
    A2,xc2,yc2,Jxc2,Jyc2,Jxyc2 = square(h2,b2,x2,y2)
    ###Tu mamy dane na temat poziomej czesci katownika
    
    A,xc,yc,Jx,Jy,Jxy = steiner(A1,A2,xc1,xc2,yc1,yc2,Jxc1,Jxc2,Jyc1,Jyc2,Jxyc1,Jxyc2)
    J0 = int(Jx + Jy)
    
    wyniki(A,xc,yc,Jx,Jy,Jxy,J0) 
    dewiacja(Jx,Jy,Jxy)
    ### Wyniki, z momentem dewiacji i w głownych
    
    input("Powrót do menu \n")
    menu()    

def teownik():  
    print("\nPodaj wymiary Teownika:")
    h = float(input("Długość środnika:"))
    b = float(input("Szerokość stopki:"))
    dh = float(input("Grubość stopki:"))
    db = float(input("Grubosc środnika:"))
    
    x1 = (b/2) - (db/2)
    y1 = 0
    A1, xc1, yc1, Jxc1, Jyc1, Jxyc1 = square(h,db,x1,y1)  #Dla srodnika
    
    x2 = 0
    y2 = h 
    A2, xc2, yc2, Jxc2, Jyc2, Jxyc2 = square(dh,b,x2,y2)    #Dla stopki
    
    A, xc, yc, Jx, Jy, Jxy = steiner(A1,A2,xc1,xc2,yc1,yc2,Jxc1,Jxc2,Jyc1,Jyc2,Jxyc1,Jxyc2) #Dla teownika
    J0 = int(Jx + Jy)
    wyniki(A,xc,yc,Jx,Jy,Jxy,J0)
    J1, J2, tanamax, alfa = dewiacja(Jx,Jy,Jxy)
    input("Powrót do menu \n")
    menu()    
    
def dwuteownik(): 
    print("\nPodaj wymiary Teownika:")
    h = float(input("Długość środnika:"))
    b1 = float(input("Szerokość stopki górnej:"))
    b2 = float(input("Szerokość stopki dolnej:"))
    
    dh = float(input("Grubość środnika:"))
    db1 = float(input("Grubość stopki górnej:"))
    db2 = float(input("Grubosc stopki dolnej:"))
    
    if b1 > b2:
        x1 = (b1/2) - (dh/2)
    else: x1 = (b2/2) - (dh/2)      #Określelie x dla srodnika
    
    y1 = b2
    
    A1, xc1, yc1, Jxc1, Jyc1, Jxyc1 = square(h,dh,x1,y1)  #Dla srodnika
    
    x2 = xc1 - b1/2
    y2 = h + b2 
    A2, xc2, yc2, Jxc2, Jyc2, Jxyc2 = square(db1,b1,x2,y2)    #Dla stopki górnej
    
    x3 = xc1 - b2/2
    y3 = 0
    A3, xc3, yc3, Jxc3, Jyc3, Jxyc3 = square(db2,b2,x3,y3)    #Dla stopki dolnej
    
    A13, xc13, yc13, Jx13, Jy13, Jxy13 = steiner(A1,A3,xc1,xc3,yc1,yc3,Jxc1,Jxc3,Jyc1,Jyc3,Jxyc1,Jxyc3) #Dla srodnika + stopki dolnej
    A, xc, yc, Jx, Jy, Jxy = steiner(A13,A2,xc13,xc2,yc13,yc2,Jx13,Jxc2,Jy13,Jyc2,Jxy13,Jxyc2) #Dla 2teownika
    J0 = int(Jx + Jy)
    
    wyniki(A,xc,yc,Jx,Jy,Jxy,J0)
    J1, J2, tanamax, alfa = dewiacja(Jx,Jy,Jxy)
    input("Powrót do menu \n")
    menu()   
    
def ceownik():      ##Do zrobienia
    print("\nPodaj wymiary Ceownika:")
    h = float(input("Wysokość:"))
    b1 = float(input("Szerokość stopki górnej:"))
    b2 = float(input("Szerokość stopki dolnej:"))
    dh = float(input("Grubość srodnika:"))
    db1 = float(input("Grubość stopki gornej:"))
    db2 = float(input("Grubosc stopki dolnej:"))
    
    x1 = 0
    y1 = 0
    A1, xc1, yc1, Jx1, Jy1, Jxy1 = square(h,dh,x1,y1)  #Dla srodnika
    
    x2 = dh
    y2 = h - db1 
    A2, xc2, yc2, Jx2, Jy2, Jxy2 = square(db1,b1-dh,x2,y2)    #Dla stopki gornej
    
    x3 = dh
    y3 = 0 
    A3, xc3, yc3, Jx3, Jy3, Jxy3 = square(db2,b2-dh,x3,y3)    #Dla stopki dolnej
    
    A12, xc12, yc12, Jx12, Jy12, Jxy12 = steiner(A1,A2,xc1,xc2,yc1,yc2,Jx1,Jx2,Jy1,Jy2,Jxy1,Jxy2) #Dla srodnika i polki gornej
    A, xc, yc, Jx, Jy, Jxy = steiner(A12,A3,xc12,xc3,yc12,yc3,Jx12,Jx3,Jy12,Jy3,Jxy12,Jxy3) #Dla ceownika całego
    J0 = int(Jx + Jy)
    wyniki(A,xc,yc,Jx,Jy,Jxy,J0)
    J1, J2, tanamax, alfa = dewiacja(Jx,Jy,Jxy)
    input("Powrót do menu \n")
    menu()    
    
    
def square(h,b,x,y):    #Zwraca (A,xc,yc,Jxc,Jyc,Jxyc) dla prostokata

    A = h * b
    xc = x + (b/2)
    yc = y + (h/2)
    Jxc = (b * h**3)/12
    Jyc = (h * b**3)/12
    Jxyc = 0
    return (A,xc,yc,Jxc,Jyc,Jxyc)

def wyniki(A,xc,yc,Jxc,Jyc,Jxyc,J0):    #Funkcja wyniki ma pokazywac typowe wyniki obliczen
    print("====================================================")
    print("\nPole powierzchni:\nA: ",A)
    print("\n\nPolożenie srodka ciezkosci (wzgl.xyz):\nxc: ",xc,"\nyc: ",yc)
    print("\nMomenty bezwladnosci:\nJx: ",int(Jxc),"\nJy: ",int(Jyc),"\nJxy: ",int(Jxyc))
    print("\n\nBiegunowy moment bezwładnosci \nJ0: ",J0)
        
def steiner(A1,A2,xc1,xc2,yc1,yc2,Jx1,Jx2,Jy1,Jy2,Jxy1,Jxy2):   #Dla 2 prostokatow zwraca (A,xc,yc,Jx,Jy,Jxy)
    ###Funkcja steiner ma za zadanie obliczyc dla 2 prostokatow
    ###pola sr.ciezkosci i momenty bezwladnosci
    ###Pola powierzchni###
    A = A1 + A2
    ###Środki ciezkosci###
    xc = (xc1*A1 + xc2*A2)/A
    yc = (yc1*A1 + yc2*A2)/A
    ###M.Bezw wg osi xc###
    Jx = (Jx1 + ((yc - yc1)**2) * A1) + (Jx2 + ((yc - yc2)**2) * A2)
    ###M.Bezw wg osi yc###
    Jy = (Jy1 + ((xc - xc1)**2) * A1) + (Jy2 + ((xc - xc2)**2) * A2)
    ###M.Dewiacji###
    Jxy = (Jxy1 + (yc-yc1) * (xc-xc1) * A1) + (Jxy2 + (yc-yc1) * (xc-xc1) * A2)
            
    return (A,xc,yc,Jx,Jy,Jxy)

def dewiacja(Jx,Jy,Jxy):    #Zwraca (J1,J2,tanamax,alfa)
    
    J1 = int(((Jx+Jy)/2) + math.sqrt(((Jx - Jy)/2)**2 +(Jxy**2)))
    J2 = int(((Jx+Jy)/2) - math.sqrt(((Jx - Jy)/2)**2 +(Jxy**2)))
    if int(Jy - J1) == 0:
        tanamax = "Inf."
        alfa = 0
    else:
        tanamax = Jxy/(Jy-J1)
        alfa = int(math.degrees(math.atan(tanamax)))
        
    print("\nGlowne momenty bezwladnosci: \nJ1: ",J1,"\nJ2: ",J2,"\n\nTangens kata alfa:",tanamax,"\nKat alfa: ",alfa,"\n" )
    return(J1,J2,tanamax,alfa)


menu()