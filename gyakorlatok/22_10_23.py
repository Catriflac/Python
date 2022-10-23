"""
Hozzon létre egy 10 elemű, egész számokból álló listát, majd töltse fel véletlenszerűen 5-25 közötti számokkal!
a) Írja ki a lista elemeit a megadás sorrendjében!
b) Írja ki a lista elemeit fordított sorrendben!
c) Írja ki a lista minden második elemét a képernyőre!
d) Kérjen be a felhasználótól egy számot 1 és 10 között, majd írja ki a lista felhasználó által megadott elemét a képernyőre! Ismételje addig a bekérést, míg felhasználó nem a megfelelő értéket adja meg!
"""
from cmath import sqrt
import random
import math

def feladat_1():
    szamok = [1,2,3,4,5,6,7,8,9,10]

    for i in range(0,10):
        szamok[i] = random.randint(5,25)
        print(szamok[i], end=" ")

    print()
    szamok.reverse()
    print(szamok, end=" ")
    print()
    szamok.reverse()


    for i in range(1,10,2):
        print(szamok[i], end=" ")
    print()
    #<-->
    for i in range(0,10):
        if i % 2 != 0:
            print(szamok[i], end=" ")
    print()

    while(True):
        try:
            index = input("Kérem, adjon meg egy értéket 1 és 10 között: ")
            print(szamok[int(index)-1])
        except IndexError:
            print("Nincs ilyen sorszámú elem!")
            break
        
"""
Írjon programot, amely összeadja két, valós számokat tartalmazó lista megfelelő elemeit, és az eredményeket egy
harmadik listában helyezi el!
"""    

def feladat_2():
    lista1 = [-1, 0.5486 ,math.sqrt(2) ,105.7869, math.pi]
    lista2 = [99, -105.78563, 0.97867, 59, -17.565]
    eredmeny = lista1

    for i in range(0, len(lista1)):
        eredmeny[i] = float(lista1[i]) + float(lista2[i])
        #print(eredmeny[i], end=" ")
        print("%.5f" % eredmeny[i], end=" ")


##################################################################################################
def ellenorzes():
    while(True):
        try:    
            feladatSzam = input("(Kilépés: 0) Add meg a feladat számát: ")
            function = globals()["feladat_"+feladatSzam] #inputból rakja össze az alprogram nevét

            print("\n\n" + feladatSzam + ". feladat:")
            function()
            print("\n")

        except KeyError:    #vagy simán except: <- de ez ctrl+c-re sem fog engedni kilépni
            if feladatSzam == str(0):
                break
            print("Nincs ilyen feladat.")

ellenorzes()