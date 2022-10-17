#Hasonlóan elnevezve megoldod a feladataidat:
def feladat_1():
    print("Ez az első feladat.")

def feladat_2():
    print("Ez a második feladat.")

def feladat_3():
    print("Ez a harmadik feladat.")

def feladat_PONTOS_NEV():
    def PONTOS_NEV():
        print("Ebben a feladatban azt kérték, hogy ennek az alprogramnak pontosan a PONTOS_NEV legyen a neve. A feladat_PONTOS_NEV tehát nem lenne jó megoldása a feladatnak, mert az eltér a kért névtől. Alapvteően ez így nem működne az ellenőrző ciklussal. Az azonban nincs megszabva, hogy az így jól megoldott, egyedi névvel ellátott alprogramot becsomagoljam egy szinttel feljebb egy számomra is megfelelő nevű alprogramba. Csak el ne felejtsem utána meghívni ugyanezen belül.")
    PONTOS_NEV()

#Példafeladat: user input alapján készítsen a program egy méretezhető, váltakozó mintázatú táblát kerettel
#Ennek az értelmezésével egyelőre ne feltétlen foglalkozz, a lényeg a lenti ellenorzes() alprogram lesz
def feladat_tabla():

    tabla = int(input("Add meg a tábla méretét: "))

    def vizszintes_keret():
        print(" ", end="")
        for i in range(0,tabla):
            print(" -", end="")
        print(" ")
      
    def pepita(maradek):
        for j in range(0, tabla):
            if j % 2 == maradek:
                print(" #", end="")
            else:
                print(" O", end="")

    vizszintes_keret()

    for i in range(0, tabla):
        print("|", end="")
        if i % 2 == 0:  # modulo (maradékos osztás), eredmény az osztási maradék (páros szám esetén 0)       
            pepita(0)
        else:
            pepita(1)
        print(" |")

    vizszintes_keret()


"""
Ellenőrző alprogram pl a tanárod számára (vagy neked, átlátható ellenőrzéshez sok feladat esetén):
Végtelen főcilkus (kilépésig vagy hibáig fut (pl nem létező feladat)).
Try...except hibakezelővel fut le (ha hibába szalad, nem pánikol és lép ki csúnya hibakóddal):
    Try alatti rész fut le, hacsak nem ad hibát a runtime alatt
    De az except alatti rész fut le (KeyError) hiba esetén 

Ebben a programban az inputként megadható feladatnevek jelenleg: 1; 2; 3; PONTOS_NEV; tabla.
"""
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
