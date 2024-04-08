"""
Random dolgok:

greet = "Hello Világ!"
cls()
for i in range(len(greet)):
    print(greet[i], end="", flush=True) # Karakterenként ír ki szöveget
    time.sleep(0.3)

def myPrint(szoveg):        # Karakterenként írja ki a paraméterként kapott szöveget
    for i in range(len(szoveg)):
        print(szoveg[i], end="", flush=True)
        time.sleep(0.3)

myPrint("Viszlát kegyetlen világ!")

print("MARKER")
#!/usr/bin/python       # interpreter meghívása
import myPy             # külső py futtatása

def leghosszabbValaszok(betu):      # keressük meg a leghosszabb válaszokat...
max = 0
for i in range(len(dataList)):
    if len(eval("dataList[i]." + betu)) > max:
        max = len(eval("dataList[i]." + betu))
print("Leghosszabb válasz " + betu + ": " + str(max))

leghosszabbValaszok("A")    #30
leghosszabbValaszok("B")    #32
leghosszabbValaszok("C")    #32
leghosszabbValaszok("D")    #35
exit()


# Ez a példa kiír nekünk 3 random kérdést a helyes válasz betűjelével és a helyes válasszal
def peldaKiiras():
    for i in range(3):
        j = random.randint(0,len(dataList))
        helyesValaszBetujele = dataList[j].helyes           # Ez a helyes válasz betűjele (pl.: "B")
        print(
            dataList[j].kerdes + 
            "\nA helyes válasz: " + 
            dataList[j].helyes + 
            " (" +
            # Ennek a következő sornak az eredménye pl.: "dataList[i].B" és az eval() fx változóként meg fogja hívni a kiíráshoz:
            eval("dataList[j]." + helyesValaszBetujele) +   
            ")" )
        dataList.pop(j)     # Nem akarunk ismétlődő kérdéseket...
"""

import random
import time
import os
import datetime

# Cross-platform konzoltisztító
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Objektum felépítése (self fix, a többi a hasznos paraméter)
class kerdesek:
    def __init__(self, ID, kerdes, A, B, C, D, helyes, kategoria):
        self.ID = ID
        self.kerdes = kerdes
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.helyes = helyes
        self.kategoria = kategoria

# Létrehozzuk a listát, ami összefogja az egyes rekordokat    
dataList = []

# Forrásfájl feldolgozása
with open('kerdes.txt', 'r') as f:      # Olvasás módban megnyitjuk a fájlt
    contents = f.read()                 # Tartalom beolvasása
    lines = contents.split('\n')        # Felosztás sorokra
    for line in lines:                  # Minden sorra...
        values = line.split(';')        # Minden sort értékekre bontunk az elválasztó karakter mentén 
        obj = kerdesek(                 # A kapott tömb értékeit az objektumba illesztjük...
            values[0], 
            values[1], 
            values[2], 
            values[3], 
            values[4], 
            values[5], 
            values[6], 
            values[7])
        dataList.append(obj)            # ...majd listába

# Kész is a beolvasás és feldolgozás
# Az egyes adatokat pl így érjük el:
"""
i = 42
print(dataList[i].kerdes)
"""

# Most következnek a globális változók
# A nyeremenyek lista adja majd meg az egész játék hosszát (a játék addig fut, amíg a nyeremények el nem fogynak vagy a felhasználó meg nem szakítja a játékot)
# A felezesek és counter induló értékeket tartalmaznak, így azokat mindenképp a "global scope"-ban tartjuk
nyeremenyek = [
    "Egy szem rumos szaloncukor",
    "4000 Ft (...tudsz ötösből visszaadni?)",
    "\"Bástya\" petpalackos borválogatás",
    "Páros belépő Zámbó Jimmy emlékkoncertre",
    "100 000 Ft",
    "Használt Swift (1999, 1.3 GLX)",
    "300 000 Ft",
    "500 000 Ft",
    "800 000 Ft",
    "1 500 000 Ft",
    "3 000 000 Ft",
    "5 000 000 Ft",
    "Három gyerek",
    "20 000 000 Ft",
    "40 000 000 Ft"
    ]

felezesek = 3
counter = 0

# Most pedig elkészítjük a segédfüggvényeinket, mert nem akarjuk a main ciklust telespammelni olyan modulokkal, amik köszönik szépen, jól érzik magukat szegregálva is...


def intro():
    cls()

    def myPrint(szoveg):        # Karakterenként írja ki a paraméterként kapott szöveget
        for i in range(len(szoveg)):
            print(szoveg[i], end="", flush=True)
            time.sleep(0.05)
        print()
        time.sleep(1)
    
    today = datetime.date.today()
    myPrint("Isten hozott a Legyen Ön is Milliomos " + today.strftime("%Y %b %d") + "-i adásában!")
    myPrint("A feladatod az egyes kérdések helyes megválaszolása.")
    myPrint("Három felezési lehetőséged van, azonban az 5. és 10. kérdésnél kapsz még egyet-egyet.")
    myPrint("Indulhat a játék?\n")

    for i in range(3,0,-1):
        myPrint(str(i) + "...")
    
    print("A játék indul!")
    time.sleep(2)

# Az ujKerdes feltesz egy új kérdést, kiírja a lehetséges válaszokat és be is olvassa a felhasználó által adott választ. Utóbbi függvényében hívja tovább a felezo() vagy valaszEllenorzo() segédfüggvényeket
def ujKerdes():

    global felezesek

    cls()
    if i <= 5:
        ran = random.randint(0,100)
    elif i <= 10:
        ran = random.randint(0,1500)
    else:
        ran = random.randint(0,len(dataList))

    valasz = "valasz"

    print(dataList[ran].kerdes)
    print("A: %35s B: %35s \nC: %35s D: %35s" % 
    (dataList[ran].A.ljust(35), dataList[ran].B.ljust(35), dataList[ran].C.ljust(35), dataList[ran].D.ljust(35)))

    print("\nF: felezések száma: ", end="")
    for j in range(felezesek):
        print("▉", end=" ")
    print()

    while valasz not in ["A", "B", "C", "D", "F"]:
        valasz = input("A válaszod: ").upper()

        if valasz == "F":
            if felezesek > 0:
                felezesek = felezesek-1
                valasz = felezo(ran)
            else:
                valasz = "valasz"

    valaszEllenorzo(ran, valasz)

# A felezo() fx paraméterként megkapja az adott kérdés azonosítóját és újra kiírja, immár felezett válaszlehetőségekkel, valamint visszaadja (return) az új választ (anélkül maradna "F", amivel a felezo() meg lett hívva.)
def felezo(kerdesSzam):
    
    cls()

    print(dataList[kerdesSzam].kerdes)

    valaszok_temp = ["A", "B", "C", "D"]
    delete = 0
    for j in range(2):
        while valaszok_temp[delete] == dataList[kerdesSzam].helyes:
            delete = random.randint(0,len(valaszok_temp)-1) 
        valaszok_temp.pop(delete)
            
    valasz = "valasz"

    for i in range(2):
        print(valaszok_temp[i] + " " + eval("dataList[kerdesSzam]." + valaszok_temp[i]))

    while valasz not in ["A", "B", "C", "D"]:
        valasz = input("A válaszod: ").upper()
    
    return valasz

# A valaszEllenorzo() fx paraméterként megkapja a kérdés azonosítóját és az adott választ, majd azt kiértékeli. Rossz válasz esetén megadja, hogy mi lett volna a helyes, majd elköszön és kilép. Jó válasz esetén folytatódik a főciklus.
def valaszEllenorzo(kerdesSzam, valasz):

    if valasz == dataList[kerdesSzam].helyes:
        print("Helyes!")
        dataList.pop(kerdesSzam)
        time.sleep(2)
    else:
        print("Nem jóóóó!")
        print("A helyes válasz: " + dataList[kerdesSzam].helyes + " - " + eval("dataList[kerdesSzam]."+dataList[kerdesSzam].helyes))
        if counter == 0:
            print("A nyereményed egy nagy semmi lett volna amúgy is.")
        else:
            print("A nyereményed " + nyeremenyek[counter-1] + " lett volna.")
        exit()

# A folytatas_megallas lehetőséget ad a helyesen megválaszolt kérdés után megtartani a nyereményt vagy kockáztatni és tovább haladni.
def folytatas_megallas():

    global counter

    time.sleep(1)
    cls()

    print("A jelenlegi nyereményed: " + nyeremenyek[counter])
    if counter != len(nyeremenyek)-1:
        print("A következő nyereményed: " + nyeremenyek[counter+1])

        folytatas = "folytatas"
        while folytatas not in ["M", "F"]:
            folytatas = input("\nFolytatáshoz nyomj F betűt,\nha inkább megállsz a jelenlegi nyereményednél, nyomj M billentyűt: ").upper()

        if folytatas == "F":
            counter += 1
        else:
            print("Abbahagytad a játékot! A nyereményed: " + nyeremenyek[counter] + "\nGratulálunk hozzá!")
            exit()
        
    else:
        print("Gratulálok, nyertél!")
        exit()
    if i % 5 == 0 and i != 0:
        felezesek += 1


# Ez a főciklus, ide a leglényegesebb dolgok kerülnek és igyekszünk nagyon tisztán tartani. Hogy a kódismétlést elkerüljük, minden lényeges feladatot a segédfüggvényekkel végeztetünk el.

intro()

for i in range(len(nyeremenyek)):

    ujKerdes()

    folytatas_megallas()    
