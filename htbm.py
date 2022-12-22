"""
greet = "Hello Világ!"
cls()
for i in range(len(greet)):
    print(greet[i], end="", flush=True)
    time.sleep(0.3)

def myPrint(szoveg):
    for i in range(len(szoveg)):
        print(szoveg[i], end="", flush=True)
        time.sleep(0.3)

myPrint("Viszlát kegyetlen világ!")

print("MARKER")
#!/usr/bin/python
import myPy

    def leghosszabbValaszok(betu):
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
"""

import random
import time
import os

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


def ujKerdes():

    global felezesek

    cls()
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



for i in range(len(nyeremenyek)):
    ujKerdes()
    print("A jelenlegi nyereményed: " + nyeremenyek[counter])
    if counter != len(nyeremenyek)-1:
        print("A következő nyereményed: " + nyeremenyek[counter+1])
        time.sleep(4)
        counter += 1
    else:
        print("Gratulálok, nyertél!")
        exit()
    if i % 5 == 0:
        felezesek += 1
