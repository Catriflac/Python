import random
#Szükséges hozzá a 22_10_28_datasheet.txt fájl!

def feladat_1():
    """
    Kérjen be egy egész számot a felhasználótól, ez legyen N! Hozzon létre egy N elemű, egész számokból álló listát!
    Kérdezze meg a felhasználótól, hogy milyen intervallumból töltse fel a program a listát véletlenszámokkal! Ezek
    legyenek a és b. Ügyeljen rá, hogy 'a' kisebb legyen mint 'b'! Töltse fel a listát véletlenszámokkal az [a; b]
    intervallumból. Írja ki a lista elemeit a képernyőre a sorszámukkal és az előjelükkel együtt, táblázatszerűen!
    Egy menü segítségével kérdezze meg a felhasználót, hogy mit szeretne csinálni a lista elemeivel! (Innentől kezdve
    ismételje a programot egészen addig, amíg a felhasználó a kilépést nem választja!)
    a) Növelni
    b) Csökkenteni
    c) Szorozni
    d) Kilépni
    """


    lista1D = []
    N = int (input("Adja meg a lista méretét: "))
    a = 10
    b= 0

    while not (a < b):
        print("Adja meg a minimum értéket: ", end="")
        a = int(input())
        print("Adja meg a maximum értéket: ", end="")
        b = int(input())
    print()


    for i in range (0 , N):
        lista1D.append(random.randint(a,b))
        #print(str(i+1) + ": " + str(lista[i]))

    #Legyen inkább 2D lista!
    #Gyors inicializálás: minden eleme 0 * oszlopok száma * sorok száma
    lista2D = [[0]*2]*N
    print(lista2D)

    #Ez a példa hibás: a random adni fog egy értékpárt, ami a továbbiakban nem lesz megváltoztatva
    lista2D = [[random.randint(a,b)]*2]*N
    print(lista2D)

    #Helyes módszer
    lista2D = [[random.randint(a,b) for i in range(2) ] for j in range(N) ] 
    print(lista2D)

    #Figyelj! Kiírásnál és műveleteknél lista2D [sor] [oszlop] az indexelés!
    for i in range (0,N):
        print(str(i+1) + ": " + str(lista2D[i][0]), end=" ")
        print(lista2D[i][1])


    #Boolean érték
    d = False
    while d == False:

        opcio = input("Válassz opciót: ")
        # "!="" nem működik a while argumentumaként, "while not" használandó 
        while not (opcio == "a" or opcio == "b" or opcio == "c" or opcio == "d"):
            opcio = input("HIBA! Válassz opciót (a/b/c): ")

        if opcio == "a":
            for i in range(N):
                print(str(i+1) + ": " + str(lista2D[i][0]) + " + " + str(lista2D[i][1]) + " = " + str(lista2D[i][0] + lista2D[i][1]))

        elif opcio == "b":
            for i in range(N):
                print(str(i+1) + ": " + str(lista2D[i][0]) + " - " + str(lista2D[i][1]) + " = " + str(lista2D[i][0] - lista2D[i][1]))

        elif opcio == "c":
            for i in range(N):
                print(str(i+1) + ": " + str(lista2D[i][0]) + " * " + str(lista2D[i][1]) + " = " + str(lista2D[i][0] * lista2D[i][1]))

        else:
            d = True
            print("Viszlát!")






def feladat_2():
    """
    Olvassunk be egy fájlból adatot és tároljuk az értékeit többdimenziós tömbben
    """

    adatok2D = []

    with open("22_10_28_datasheet.txt", "r") as f:
        for line in f.readlines():
            adatok2D.append(line.split(";"))

    adatok2D.pop(0) #címsor fölösleges
    print(adatok2D)

    """
    Keressünk mérési hibát és írjuk ki, melyik napon volt (hiba, ha az értékingás > 50)
    """

    sorok = len(adatok2D)   #sorok száma összesen
    oszlopok = len(adatok2D[0]) #csak az adott sor oszlopszáma

    for i in range(sorok):  #minden sorra
        oszlopok = len(adatok2D[i]) #adott sor oszlopszáma
        #print(oszlopok)


        if oszlopok > 1:    #legalább két érték kell az összehasonlításhoz!
            for j in range(1,oszlopok-1): #minden oszlop kivéve az első (nap), előrefele ellenőrzés
                ertekkulonbseg = abs( float(adatok2D[i][j]) - float(adatok2D[i][j+1]) ) #Vannak tört értékek is! A különbség abszolút értékével számolunk
                if ertekkulonbseg > 50:    
                    print("Hibás mérés ezen a napon: " + adatok2D[i][0] + "\t\t//kiugró értékkülönbség: " + str("%.2f" % ertekkulonbseg))
                    j+=1







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