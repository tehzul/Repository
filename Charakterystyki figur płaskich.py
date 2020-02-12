import numpy
import scipy
import os
from PIL import Image
import math

def menu():
    print ("\n\n\nWybierz opcje aby obliczyć char.geometryczne! \n")
    print ("[1] Prostokat \n[2] Trojkat \n[3] Kolo \n \n[4] Katownik \n[5] Teownik \n[6] Dwuteownik \n[7] Ceownik \n \n[0] Exit \n")
    print ("Wprowadz numer opcji")
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
menu()
 

def prostokat():
    print("Wybrales prostokat!\n")
 #  print("Wskaz dane wedlug pokazanego schematu")
 #  Image.open(r'c:\Users\micha\Desktop\Python\MomentyBezwladnosci\prostokat.pdf').show()
    b = float(input("Szerokosc: b = "))
    h = float(input("Wysokosć: h = "))
    x = float(0)
    y = float(0)
    
    square(h,b,x,y)
    A, xc, yc, Jxc, Jyc, Jxyc = square(h,b,x,y)
    J0 = Jxc + Jyc
    wyniki(A,xc,yc,Jxc,Jyc,Jxyc,J0)
    input("Powrót do menu \n")
    menu()
    
def trojkat():
    print("""Wybrałes trojkat! \nNa twoje nieszczęscie jest WIP \n
          Za niedlugo bedzie \nProsimy o cierpliwosc\n""") 
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
        J0 = Jxc + Jyc
        Jxyc = 0
        
        wyniki(A,xc,yc,Jxc,Jyc,Jxyc,J0)       
        input("Powrót do menu \n")
        menu()   

def katownik():
    print("Wybrałes kątownik! \n\nPodaj wymiary:")
    kat_h = float(input("Podaj wysokosc katownika: h = "))
    kat_b = float(input("Podaj szerokosc katownika: b = "))
    gr_h = float(input("Podaj grubosc --horyzontalnej-- czesci: gr_h = "))
    gr_b = float(input("Podaj grubosc | vertykalnej | czesci: gr_b = "))
    
    h1 = kat_h
    b1 = gr_b
    x1 = 0
    y1 = 0
    square(h1,b1,x1,y1)
    A1,xc1,yc1,Jxc1,Jyc1,Jxyc1 = square(h1,b1,x1,y1) 
    """Tu mamy dane na temat pionowej czesci katownika"""
    
    h2 = gr_h
    b2 = kat_b - gr_b
    x2 = gr_b
    y2 = 0
    square(h2,b2,x2,y2)
    A2,xc2,yc2,Jxc2,Jyc2,Jxyc2 = square(h2,b2,x2,y2)
    '''Tu mamy dane na temat poziomen czesci katownika'''
    
    A,xc,yc,Jx,Jy,Jxy = steiner(A1,A2,xc1,xc2,yc1,yc2,Jxc1,Jxc2,Jyc1,Jyc2,Jxyc1,Jxyc2)
    J0 = Jx + Jy
    
    wyniki(A,xc,yc,Jx,Jy,Jxy,J0) 
    dewiacja(Jx,Jy,Jxy)
    """ Wyniki, z momentem dewiacji i w głownych"""
    
    input("Powrót do menu \n")
    menu()    

def teownik():
    print("Wybrałes Teownik!") 
    input("Powrót do menu \n")
    menu()    
    
def dwuteownik():
    print("Wybrałes Dwuteownik")
    input("Powrót do menu \n")
    menu()   
    
def ceownik():
    print("Wybrałes Ceownik")
    input("Powrót do menu \n")
    menu()    
    
    
def square(h,b,x,y):
    """Funkcja square ma liczyc pole, srodek ciezkosci i M.Bezw prostokątow"""
    A = h * b
    xc = x + (b/2)
    yc = y + (h/2)
    Jxc = (b * h**3)/12
    Jyc = (h * b**3)/12
    Jxyc = 0
    return (A,xc,yc,Jxc,Jyc,Jxyc)

def wyniki(A,xc,yc,Jxc,Jyc,Jxyc,J0):
    """Funkcja wyniki ma pokazywac typowe wyniki obliczen"""
    print("====================================================")
    print("\nPole powierzchni:\nA: ",A)
    print("\n\nPolożenie srodka ciezkosci (wzgl.xyz):\nxc: ",xc,"\nyc: ",yc)
    print("\nMomenty bezwladnosci:\nJx: ",Jxc,"\nJy: ",Jyc,"\nJxy: ",Jxyc)
    print("\n\nBiegunowy moment bezwładnosci \nJ0: ",J0)
        
def steiner(A1,A2,xc1,xc2,yc1,yc2,Jx1,Jx2,Jy1,Jy2,Jxy1,Jxy2):
    ###Funkcja steiner ma za zadanie obliczyc dla 2 prostokatow
    ###pola sr.ciezkosci i momenty bezwladnosci
    """Pola powierzchni"""
    A = A1 + A2
    """Środki ciezkosci"""
    xc = (xc1*A1 + xc2*A2)/A
    yc = (yc1*A1 + yc2*A2)/A
    """M.Bezw wg osi xc"""
    Jx = (Jx1 + ((yc - yc1)**2) * A1) + (Jx2 + ((yc - yc2)**2) * A2)
    """M.Bezw wg osi yc"""
    Jy = (Jy1 + ((xc - xc1)**2) * A1) + (Jy2 + ((xc - xc2)**2) * A2)
    """M.Dewiacji"""
    Jxy = (Jxy1 + (yc-yc1) * (xc-xc1) * A1) + (Jxy2 + (yc-yc1) * (xc-xc1) * A2)
            
    return (A,xc,yc,Jx,Jy,Jxy)

def dewiacja(Jx,Jy,Jxy):
    """Funkcja dewiacja majaca zworic nam momenty glowne oraz kąt"""
    """o jaki nalezy obrocic uklad wsp"""
    J1 = ((Jx+Jy)/2) + math.sqrt(((Jx - Jy)/2)**2 +(Jxy**2))
    J2 = ((Jx+Jy)/2) - math.sqrt(((Jx - Jy)/2)**2 +(Jxy**2))
    tanamax = Jxy/(Jy-J1)
    alfa = int(math.degrees(math.atan(tanamax)))
    print("Glowne momenty bezwladnosci: \nJ1: ",J1,"\nJ2: ",J2,"\n\nTangens kata alfa: ",tanamax,"\nKat alfa: ",alfa )
    return(J1,J2,tanamax,alfa)
    