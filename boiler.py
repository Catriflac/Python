# -*- coding: utf-8 -*-
import random

#A fejlécben a használt modulok, kódolás, stb. mindig a kód elején vannak!

#Változó deklarálása és kiírása
msg = "Hello Világ"
print(msg + "\nTípus: " + str(type(msg)) + "\n")

#Változó beolvasása és típuskonverziós kiírása
szam = int(input("Adj meg egy számot: "))
#szam = szam+10
print("Hozzáadtam 10-et. Szívesen: " + str(szam+10) + "\n")

#Tömb deklarálása és kiírása
koktel = [
    "Gin",
    "Rum",
    "Kóla",
    "Narancslé",
    "Szóda",
    "Málnaszörp",
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

#Alprogram készítése és hívása
def mixer():
    x = random.randint(0,len(mennyiseg)-1)
    y = random.randint(0,len(koktel)-1)
    z = random.randint(1,10)
    print(str(z) + mennyiseg[x] + koktel[y])
    koktel.pop(y)

def pincer():
    print("A recept a professzor híres koktéljához:")
    recept_hossz = random.randint(1,len(koktel))
    for i in range(recept_hossz):
        mixer()
    print(veletlen_osszetevo[rand])

print("További receptekért kövesd az oldalam és jeletkezz fel az értesítési listára!")
