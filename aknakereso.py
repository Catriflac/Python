import random    
import os
import time
import math

string_peldaSzoveg = "Ez egy szöveg"        # A string szöveg, ami ha belegondolunk, akkor karakterek véges hosszú tömbje
int_peldaInteger = 42                       # Az int egész szám, ami a matematikában ismert egész számokat jelenti
float_peldaFloat = 3.14                     # A float lebegőpontos szám, ami a matematikában ismert racionális számokat jelenti (véges törtek)
bool_peldaBool = True                       # A bool logikai érték, ami a logikai igaz/hamis értékeket jelenti. Nagyon hasznos átláthatóság szempontjából.
list_peldaLista = [1, 2, 3, 4, 5]           # A list lista, ami egy tetszőleges hosszúságú tömböt jelent
tuple_peldaTuple = (1, 2, 3, 4, 5)          # A tuple tuple, ami egy tetszőleges hosszúságú, de nem módosítható tömböt jelent
set_peldaSet = {1, 2, 3, 4, 5}              # A set halmaz, ami egy tetszőleges hosszúságú, de nem rendezett tömböt jelent
dict_peldaDict = {'a': 1, 'b': 2, 'c': 3}   # A dict dictionary, ami kulcs-érték párokat tartalmazó tömböt jelent

#konkatenáció (összefűzés)
newString = string_peldaSzoveg + " és még egy szöveg"           # Itt létrehozunk egy stringet (newString), aminek egyből értéket is adunk. A + operátor a stringeket összefűzi
print(newString)

#típuskonverzió és összefűzés
print(type(int_peldaInteger))                                   # Az int_peldaInteger változó típusát kiírjuk a type() függvénnyel
newString += " és egy szám: " + str(int_peldaInteger)                  # Itt a newString már létezik, ezért az új értéket a += operátorral fűzzük hozzá. Az int_peldaInteger-t stringgé konvertáljuk a str() függvénnyel
print(newString)

#string formázás
newString = f"{newString} és még egy szám: {float_peldaFloat}"  # Itt a f-string formázást használjuk, ami egy nagyon kényelmes módja a stringek formázásának

#string metódusok
print(newString.upper())                                        # Az upper() metódus a stringet nagybetűssé alakítja
print(newString.lower())                                        # Az lower() metódus a stringet kisbetűssé alakítja
print(newString.split(" "))                                     # A split() metódus a stringet a megadott paraméter mentén (itt space) bontja fel, és egy listába rakja a részeket
print(newString.replace("és", "vagy"))                          # Az replace() metódus a stringben egy adott részt (1. paraméter) kicserél egy másikra (2. paraméter)
print(f"A szöveg hossza: {len(newString)} karakter")            # Ez az f-string formázás és a len() függvény kombinációja, ami a string hosszát adja meg


# Oké, de hogy használjuk ezeket a gyakorlatban?

def osszeadas(arrayOfInts):                                     # Egy egyszerű függvény, ami n számot összead
    sum = 0
    for number in arrayOfInts:                                  # A for ciklus végigiterál az arrayOfInts listán
        sum += number
    return sum

def randomSzamGenerator(n):                                     # Egy függvény, ami n db random számot generál
    szamok = []
    for i in range(n):
        szamok.append(random.randint(0, 20))                    # Az append() metódus hozzáad egy elemet a listához

    return szamok                                               # A függvény visszaadja a generált számokat. A return kulcsszóval térünk vissza a függvényből, ez egyben le is zárja a futását. Ha egy hibaágban térünk vissza valamilyen return értékkel, akkor a többi ág nem fog lefutni.

def fejSzamolas():
    time.sleep(5)                                                   # Várunk 5 másodpercet, hogy látszódjanak az eddig kiírtak...
    userLife = 3                                                    # A felhasználó élete, amit a játék során veszít, ha rossz választ ad
    gameOver = False
    while (not gameOver):                                           # A while ciklus addig fut, amíg a gameOver változó értéke nem True (itt megfordítottuk a működését a "not" szóval, alapvetően a while ciklus addig fut, amíg a feltétel igaz. Itt ugye azért igaz, mert a "nem hamis" az "igaz" :D)
        os.system('cls' if os.name == 'nt' else 'clear')            # A képernyő törlése. Ez a sor a Windows és Linux operációs rendszerekre is működik
        for i in range(0, userLife):
            print("♥ ", end="")                                     # A print() függvény end paraméterével megváltoztathatjuk, hogy a sor végén mi legyen. Alapértelmezetten a sor végére kerül egy új sor karakter, de itt egy szóköz kerül a sor végére
        szamok = randomSzamGenerator(random.randint(2,5))           # A randomSzamGenerator függvény meghívása, 2-5 db random szám generálása
        print(f"\nSzámold ki az alábbi számok összegét: \n{szamok}")
        userEredmeny = int(input("Eredmény: "))                     # A felhasználótól bekérjük az eredményt és int típusúvá alakítjuk
        if userEredmeny == osszeadas(szamok):                       # Ha a felhasználó által megadott eredmény megegyezik az osszeadas() függvény által kiszámolt eredménnyel
            print("Helyes válasz!")                                 # Kiírjuk, hogy helyes a válasz
            time.sleep(1)                                           # Várunk 1 másodpercet
        else:
            print("Helytelen válasz!")                              # Ha nem egyezik meg, akkor helytelen válasz
            userLife -= 1                                           # És a felhasználó élete csökken
            time.sleep(1)                                           # Várunk 1 másodpercet
            if userLife == 0:                                       # Ha a felhasználó élete 0, akkor vége a játéknak
                gameOver = True
                print("Vesztettél!")                                # Kiírjuk, hogy vesztett

fejSzamolas()                                                       # A fejSzamolas() függvény meghívása. Ha kikommenteled ezt a sort, akkor a játék nem fog lefutni


# Amikor programozunk, arra törekszünk, hogy a kódunk minél átláthatóbb és könnyebben érthető legyen. Ezért fontos, hogy a változóink ne legyenek nehezen értelmezhetőek, és a függvényeink ne legyenek túl hosszúak. A kommentek segítenek a kód értelmezésében, de a kód maga is beszédes legyen. A változók és függvények nevei legyenek beszédesek, és a kódolási konvenciókat kövessük. A kódolási konvenciók segítenek abban, hogy a kódunk egységes legyen, és könnyebben olvasható.

# Kódolási konvenció például, hogy a változók és függvények kisbetűvel kezdődnek és szóköz helyett aláhúzást (game_over_state = false) vagy camelCase-t (gameOverState = False) használunk. Minden esetben érdemes rászánni az időt, hogy egyértelmű nevet találjunk ki a változóknak és függvényeknek, adott esetben visszamenőlegesen is megváltoztathatjuk, ha a szerepük módosul

# Kódolási konvenció az is, hogy ahol lehet, kerüljük el az ismétlődő kódrészleteket. Ha egy kódrészletet többször is használunk, akkor érdemes azt egy függvénybe kiszervezni, és ahol szükség van rá, ott meghívni. Ezáltal a kódunk rövidebb lesz, és könnyebben karbantartható.


# Legyen itt valami komplexebb dolog, mondjuk egymásba ágyazott listák (2D lista)

array2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]                       # Egy 2D lista, ami 3 db 3 elemű listát tartalmaz
for array in array2D:
    print(array)                                                  # Ez már hasonlít pl egy játéktáblához
print("^^^ ez már hasonlít egy játéktáblára\nMit tudunk vele kezdeni?")

###
### Aknakereső példa
###


# Inicializálom a globálisan használadnó változókat. A szimbólumokat szeretném, hogy nyugodtan és szabadon kezelje bármelyik függvény
global symbols                                                    # A global kulcsszóval globális változóvá tesszük a symbols változót, így a függvények is elérhetik anélkül, hogy paraméterként át kellene adni
symbols = {"mine" : "☠ ", "empty" : "⛶ ", "flag" : "⚑ "}        # Egy dictionary, ami a játékban használt szimbólumokat tartalmazza. Van egy extra space is a szimbólumok előtt, hogy szebb legyen a megjelenítés
# https://symbl.cc/en/unicode-table/#miscellaneous-symbols   <- itt találsz használható unicode szimbólumokat, és elég csak itt kicserélni őket

# Ezzel a függvénnyel generálunk egy n*n-es aknakereső táblát (kitöltött és üres), és visszaadjuk a két táblát és az aknák számát
def generateTable(n):

    global symbols

    tableFilled = [[symbols["empty"]] * n for i in range(n)]      # Egy n * n-es üres szimbólumos tábla létrehozása
    numberOfMines = random.randint(math.floor(n), n*2)            # Random számú akna generálása (min n, max 2*n)
    for i in range(numberOfMines):
        x = random.randint(0, n-1)                                # Random valid x koordináta
        y = random.randint(0, n-1)                                # Random valid y koordináta
        tableFilled[x][y] = symbols["mine"]                       # Az akna elhelyezése a táblán

    tableEmpty = []                                               # Ez az üres tábla lesz megjelenítve a játékosnak, itt még nincsenek felfedezve a mezők
    for i in range(n):
        row = []                                                  # Egy üres sor létrehozása
        for j in range(n):
            row.append([str(i)+str(j)])                           # A mezők és koordinátáik hozzáadása a sorhoz
        tableEmpty.append(row)                                    # A sor hozzáadása a táblához

    return tableFilled, tableEmpty, numberOfMines                 # A függvény visszaadja a két táblát és az aknák számát

# Ezzel a függvénnyel felfedjük a játékos által kiválasztott mezőt, és ellenőrizzük, hogy vége van-e a játéknak
def revealCell_CheckGameOver(tableFilled, tableEmpty, x, y):      # A játékos által kijelölt mező felfedése
    
    # Meghívom használatra a globális változókat, amiket olvasni vagy írni szeretnék
    global symbols
    global playerLife
    
    tableEmpty[x][y] = tableFilled[x][y]                          # A felfedett mező értékét beállítjuk a referencia táblán lévő értékre
    
    # Ha aknát talál...
    if tableFilled[x][y] == symbols["mine"]:                      # Ha az adott mezőn akna van, akkor -1HP
        playerLife -= 1
        if playerLife == 0:                                       # Ha 0HP, akkor Game Over
            print("Game over!")
            return True                                           # A függvény egyben azt is visszaadja, hogy vége a játéknak...
        return False                                              # ...vagy folytatódhat a játék
    
    # Ha nincs akna a kiválasztott mezőn (de mellette pl lehet...)
    else:                                                         # Ha nincs akna az adott mezőn, akkor kezeljük le a megjelenítést
        originalX, originalY = x, y
        surroundingCells = [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]     # Az adott mező környező mezőinek koordinátái egy tuple listában
        for cell in surroundingCells:
            x, y = cell                                           # Unpacking a cell tuple-ből, ugye a listában kételemű tuple-k vannak
            if x >= 0 and x < len(tableFilled) and y >= 0 and y < len(tableFilled):     # Ha a mező a tábla határain belül van
                if tableFilled[x][y] == symbols["mine"]:          
                    tableEmpty[originalX][originalY] = symbols["flag"]              # Ha a környező mezőn van akna, akkor a felfedett mezőt jelöljük meg
        return False

# Ezzel rajzoljuk ki a teljes játékteret minden körben
def drawBoardState(tableEmpty):

    # Kiírjuk a játékos életét és a jelmagyarázatot
    for i in range(0, playerLife):
        print("♥ ", end="")
    print(f"\nJelmagyarázat: \n{symbols['empty']}: biztonságos mező\n ##: felfedezetlen mező\n{symbols['mine']}: akna\n{symbols['flag']}: akna környezetében (vízszintesen vagy függőlegesen) lévő mező\n")
    
    # Kirajzoljuk a táblát
    for row in tableEmpty:
        for cell in row:
            if isinstance(cell, list):                  # Ha a cell egy lista, akkor a koordinátákat tartalmazza, ezért kiírjuk az első elemét
                print(cell[0], end=" ")
            else:                                       # Ha nem lista, akkor a mező értékét
                print(cell, end=" ")
        print()

# Minden kör elején ellenőrizzük azt is, hogy a játékos nyert-e
def isWon(tableEmpty, n, numberOfMines):

    safeCellsFound = 0
    allCells = n * n

    for row in tableEmpty:
        for cell in row:
            # Ha üres (simán üres vagy zászlóval jelölt), akkor biztonságos mezőnek számít (nem akna)
            if cell is symbols["flag"] or cell is symbols["empty"]:
                safeCellsFound += 1

    print(f"Biztonságos cellák megtalálva: {safeCellsFound} / {allCells - numberOfMines}, aknák száma: {numberOfMines}")
    return (safeCellsFound == allCells - numberOfMines)                          # Ez itt király! A visszatérési érték itt boolean. Miért? Mivel a == operátor visszaad egy igaz/hamis értéket, és ezt a függvény visszaadja

def mineSweeper():

    # Játék változóinak inicializálása
    time.sleep(5)
    global playerLife
    playerLife = 3
    gameOver = False

    # Játék indítása
    print("Üdvözöllek az aknakeresőben!")
    n = 0
    while (n < 3 or n > 10):
        n = int(input("Add meg a tábla méretét (3-10): "))
    tableFilled, tableEmpty, numberOfMines = generateTable(n)

    # Játékmenet
    while (not gameOver):
        os.system('cls' if os.name == 'nt' else 'clear')
        if isWon(tableEmpty, n, numberOfMines):
            print("Nyertél!")
            return 0
        drawBoardState(tableEmpty)
        userChoice = input("Add meg a koordinátákat (xy): ")
        x, y = int(userChoice[0]), int(userChoice[1])
        gameOver = revealCell_CheckGameOver(tableFilled, tableEmpty, x, y)

    # Játék vége
    print("Vége a játéknak!")


mineSweeper()                                                       # Ha kikommenteled ezt a sort, akkor az aknakereső nem fog lefutni
