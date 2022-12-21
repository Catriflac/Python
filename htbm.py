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
    "40 000 000 Ft",
    ]

felezesek = 3

def ujKerdes():
    global felezesek
    cls()
    i = random.randint(0,len(dataList))
    valasz = "valasz"

    print(dataList[i].kerdes)
    print("A: " + dataList[i].A, end="\t\t")
    print("B: " + dataList[i].B)
    print("C: " + dataList[i].C, end="\t\t")
    print("D: " + dataList[i].D)

    print("\nF: felezések száma: ", end="")
    for j in range(felezesek):
        print("▉", end=" ")
    print()

    while valasz not in ["A", "B", "C", "D", "F"]:
        valasz = input("A válaszod: ").upper()

    if valasz == "F":
        if felezesek > 0:
            felezesek = felezesek-1
            felezo(i)

    if valasz == dataList[i].helyes:
        print("Helyes!")
        dataList.pop(i)
        time.sleep(2)
        ujKerdes()
    else:
        print("Nem jóóóó!")
        print("A helyes válasz: " + dataList[i].helyes + " - " + eval("dataList[i]."+dataList[i].helyes))

def felezo(i):
    
    cls()

    print(dataList[i].kerdes)

    valaszok_fix = ["A", "B", "C", "D"]
    valaszok_temp = valaszok_fix
    delete = 0
    for j in range(2):
        while valaszok_temp[delete] == dataList[i].helyes:
            delete = random.randint(0,len(valaszok_temp)-1)
        valaszok_temp.pop(delete)
            
    valasz = "valasz"

    
    print(valaszok_temp[0] + " " + eval("dataList[i]." + valaszok_temp[0]))
    print(valaszok_temp[1] + " " + eval("dataList[i]." + valaszok_temp[1]))

    while valasz not in ["A", "B", "C", "D", "F"]:
        valasz = input("A válaszod: ").upper()

    if valasz == "F":
        print("Már feleztünk!")

    if valasz == dataList[i].helyes:
        print("Helyes!")
        dataList.pop(i)
        time.sleep(2)
        ujKerdes()
    else:
        print("Nem jóóóó!")
        print("A helyes válasz: " + dataList[i].helyes + " - " + eval("dataList[i]."+dataList[i].helyes))

    return felezesek

ujKerdes()