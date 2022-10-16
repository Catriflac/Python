# -*- coding: utf-8 -*-
import random

#A fejlécben a használt modulok, kódolás, stb. mindig a kód elején vannak!

#Változó deklarálása és kiírása
msg = "Hello Világ"
print(msg + "\nTípus: " + str(type(msg)) + "\n")

#Változó beolvasása és típuskonverziós kiírása
szam = int(input("Adj meg egy számot: "))
print("Hozzáadtam 10-et. Szívesen: " + str(szam+10) + "\n")
szam = szam + 2.54123549846
print("Hozzáadtam 2.54-et, mert bizony ilyet is tudok: %.2f\n" % (szam))

#Tömb deklarálása és kiírása
koktel = [
    "Gin",
    "Rum",
    "Málnaszörp",
    "Kóla",
    "Narancslé",
    "Szóda",
    ]


print("Ezekből az összetevőkből próbálta a professzor megalkotni a tökéletes koktélt:")

for x in range(len(koktel)):  
    print(koktel[x])

#Tömb egy elemének kiírása random függvénnyel
veletlen_osszetevo = [
    "az X-vegyszer",
    "egy koktélesernyő",
    "egy marék selyemhernyó",
    "három bajuszszál egy tarka macska orra mellől",
    "egy löttyintés nagypapa híres tyúkhúsleveséből",
    ]
rand = random.randint(0,len(veletlen_osszetevo)-1)
print("De egy véletlen folytán belekerült még egy hozzávaló: " + veletlen_osszetevo[rand] + "!\n")

#Példaműveletek tömbbel
mennyiseg = []
mennyiseg.append(" ml ")
mennyiseg.append(" cl ")
mennyiseg.append(" dl ")
mennyiseg.append(" l ")
mennyiseg.append(" hl ")
mennyiseg.remove(" hl ") #mennyiseg.pop(4)

#Alprogram definiálása és hívása
#Ez az alprogram egy olyan másik alprogramot hív meg, amely még nincs definiálva a hívás pillanatában
#Futtatásnál ebből nem lesz probléma, mert mire ez az előre definiált alprogram hívásra kerül, már létezik a mixer()
def pincer():   
    print("A recept a professzor híres koktéljához:")
    recept_hossz = random.randint(1,len(koktel))    #A recept hossza legyen mindig változó
    for i in range(recept_hossz):   #És annyiszor hívja meg a mixert hozzáadni egy összetevőt
        mixer()
    print(veletlen_osszetevo[rand]) #Végül egyszer adjunk hozzá egy véletlen összetevőt

def mixer():
    y = random.randint(0,len(koktel)-1)
    
    if (koktel[y] == "Gin") or (koktel[y] == "Rum") or (koktel[y] == "Málnaszörp"):  #legyünk mértékletesek a töményekkel
        x = random.randint(0,1)
    else:
        x = random.randint(0,len(mennyiseg)-1)

    z = random.randint(1,10)
    
    print(str(z) + mennyiseg[x] + koktel[y])
    koktel.pop(y)   #Az aktuális indexet töröljük is, hogy ne lehessen kétszer hívni valamit

#Itt hívjuk az alprogramunkat
#A hívás pillanatában már definiált kell, hogy legyen minden résztvevő
pincer()


print("További receptekért kövesd az oldalam és jeletkezz fel az értesítési listára!")
