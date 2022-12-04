adatok = []

with open("beosztas.txt", "r") as f:
    for line in f.readlines():
        if (line.replace("\n", "")).isnumeric() :
            adatok.append(int((line.replace("\n", ""))))
        else:
            adatok.append(line.replace("\n", ""))


def fel1():    
    print(len(adatok))


def fel2():
    oraszam = 0
    for i in range(3,len(adatok),4):
        oraszam += int(adatok[i])
    
    x = 0
    for i in range(3,len(adatok),4):
        x += int(adatok[i])
    print(x)


def fel3():
    orak = 0
    tanarNev = input("Adja meg a keresett tanár nevét: ")
    for i in range(len(adatok)):
        if adatok[i] == tanarNev:
            #orak += int(adatok[i + 3])
            orak += adatok[i + 3]
    print(orak)


def fel3plus():
    # beolvasásnál is használható módszer
    for i in range(3,len(adatok),4):
        adatok[i] = int(adatok[i]) 

def fel4():
    of = []
    f = open("of.txt", "w")
    for i in range(len(adatok)):
        if adatok[i] == "osztalyfonoki":
            of.append(adatok[i+1])
            of.append(adatok[i-1])

    for i in range(0, len(of), 2):
        f.write(of[i])
        f.write(" - ")
        f.write(of[i+1])
        f.write("\n")
    f.close()


def fel5():
    osztaly = input("Osztály: ")
    tantargy = input("Tantárgy: ") 

    if osztaly[2] == ".":
        if osztaly[3] == "x":
            print(osztaly + " evfolyamszintu felbontásban tanulja a " + tantargy + " tárgyat")
    elif osztaly[2] == "x":
        print(osztaly + " evfolyamszintu felbontásban tanulja a " + tantargy + " tárgyat")
        print("A %s osztály evfolyamszintu felbontásban tanulja a %s tárgyat" % (osztaly, tantargy))
    else:
        print(osztaly + " csoportbontas tanulja a " + tantargy + " tárgyat")


def fel6():
    tanarok = []
    for i in range(0, len(adatok),4):
        if adatok[i] not in tanarok:
            tanarok.append(adatok[i])
    print("Az iskolában %d tanár tanít." % len(tanarok))

           




##################################################################################################
def ellenorzes():
    while(True):
        try:    
            feladatSzam = input("(Kilépés: 0) Add meg a feladat számát: ")
            function = globals()["fel" + feladatSzam] #inputból rakja össze az alprogram nevét

            print("\n\n" + feladatSzam + ". feladat:")
            function()
            print("\n")

        except KeyError:    #vagy simán except: <- de ez ctrl+c-re sem fog engedni kilépni
            if feladatSzam == str(0):
                break
            print("Nincs ilyen feladat.")

ellenorzes()



"""
B: N eleme term, ora eleme term x N
K: oraszam eleme term
Ef:
Uf: oraszam = az összes előforduló óraszám összege
"""