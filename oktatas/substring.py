"""
A feladatok tematikája a substring-kezelés. A string formátumú értékeket tudjuk karakterenként kezelni, elvégre a string típus eredendően egy karakterekből álló tömb, C-ben konkrétan a 
char[13] string_neve = "Ez egy string";
egy 13 karakter típusú elemből álló tömb. Ez persze addig működik, amíg string típussal folgalkozunk.

Tehát string = karaktertömb
"""

##############################################################
# SZÁMJEGYEK ÖSSZEGE

def feladat_1():
    szam = str(input("Adj meg egy számot: "))   # stringként olvassuk és kezeljük összeadásig, bár ez asszem a str() nélkül is így történne alapból

    stringHossz = len(szam) # kapott string karakterszáma
    osszeg = 0  # megoldás változója

    # most tudunk iterálni a string minden egyes karakterére
    for i in range(stringHossz):
        osszeg += int(szam[i])  # értékek hozzáadása minden egyes string/karaktertömb elemre
    print("A számjegyek összege: " + str(osszeg))

##############################################################
# 5 SZÓ INPUT TÁROLÁSA TÖMBBEN  

def feladat_2():
    szolista = [""]*5
    for i in range(5):
        szolista[i] = input("Adj meg egy szót (" + str(i+1) + "/5): ")
    print(szolista)

#############################################################

# többi feladat számára globális változóban egy fix szólista:
szolista = [
        "vérfarkas",
        "véreb",
        "szekrény",
        "szekta",
        "python",
        "Azerbajdzsán",
        "Limuzin",
        "anekdotákkal"
    ]


##############################################################
# HÁNY SZÓ KEZDŐDIK AZ ADOTT SZÓRÉSZLETTEL

def feladat_3():

    substring = "szek"
    mennyi = 0

    print("\nA \"" + substring + "\" részletet tartalmazó szavak: ")

    for i in range(len(szolista)):
        if (szolista[i].startswith(substring) == True):    
            # igen, "startswith", konkrétan van ilyen... :D ráadásul boolean értéket ad vissza
            print(szolista[i], end=" ")
            mennyi += 1

    print(" // összesen " + str(mennyi) + " szó.")

##############################################################
# LEGHOSSZABB SZÓ A LISTÁBAN

def feladat_4():
    max = 0

    print("\nA lista leghosszabb szava / szavai: ", end="")
    # első teljes iterálással megkeressük, mennyi a leghosszab karakterán(ok) hossza
    # itt most visszafelé ellenőrzöm, ezért indul 1-től és nem 0-tól
    for i in range(1, len(szolista)):
        if ( len(szolista[i]) > len(szolista[i-1]) ):
            max = len(szolista[i])

    # a következő iterálással leghosszabb karakterlánc(oka)t printeljük
    for i in range(len(szolista)):
        if (len(szolista[i]) == max):
            print(szolista[i], end=", ")

    print()

###############################################################
# HÁNY MAGÁNHANGZÓ VAN A SZÓBAN

def feladat_5():
    maganhangzok = [
        "a",
        "á",
        "e",
        "é",
        "i",
        "í",
        "u",
        "ú",
        "ü",
        "ű",
        "o",
        "ó",
        "ö",
        "ő"
    ]

    print("\nMagánhangzók száma az egyes szavakban:")

    for i in range(len(szolista)):  # minden szó esetén...
        maganhangzok_szama = 0

        for j in range(len(maganhangzok)):  # megszámoljuk a massalhangzok lista minden eselmét...
            # case insensitiven (myString.upper() <- mindent nagybetűként kezel és számol majd) 
            # számolunk (myString.count(substring))
            maganhangzok_szama += szolista[i].upper().count(maganhangzok[j].upper())
            
        print(szolista[i] + ": " + str(maganhangzok_szama))

########################################################
# MAGAS HANGRENDŰ SZAVAK SZÁMA

def feladat_6():
    print("\nMagas hangrendű szavak száma: ", end="")
    magas = 0

    # magas hangredű szavak keresése egy összetettebb paranccsal:
    # itt a ".__contains__" eljárást használom, aminek a visszatérése boolean érték
    # pl "Hajrá Fradi!".__contains__("Hajrá") == True

    for i in range(len(szolista)):
        if ( 
        (szolista[i].lower().__contains__("a") == False) and
        (szolista[i].lower().__contains__("á") == False) and
        (szolista[i].lower().__contains__("o") == False) and
        (szolista[i].lower().__contains__("ó") == False) and
        (szolista[i].lower().__contains__("u") == False) and
        (szolista[i].lower().__contains__("ú") == False)
        ):
            magas += 1

    print(magas)
    print()
    
###############################################################
# HIBÁSAN ÍRT NEVEK

def feladat_7():
    """
    Itt csak formai követelmények vannak a lista elemeivel szemben. Tehát minden elem legyen 2 szavas space-szel elválasztva, és mind2 szó kezdődjön nagybetűvel. Pl a "Andtzns Brthrs" is jó megoldás.
    """

    nevek = [
        "Csengő Zoli",
        "Pumped Gabó",
        "Sanyi",
        "édes Anna",
        "nemecsek",
        "Sós Mihály Kelemen"    # bizony, valakinek van több keresztneve
    ]
    hiba = 0

    # itt pl tök jól jön a kétdimenziós tömb

    for i in range(len(nevek)):
        nevek[i] = nevek[i].split(" ")

    # ugye a split eleve egy tömbbel tér vissza, ezt nézzük meg printelve:
    print(nevek)
    print()

    # ilyesmit már csináltunk:
    for i in range(len(nevek)):

        # ha csak 1 név van, ne is ellenőrizzen mást, az már hiba
        if ( len(nevek[i]) == 1 ):
            hiba += 1
        else:

            # ha legalább kételemű a név, akkor...
            for j in range(len(nevek[i])):
                if ( nevek[i][j][0].isupper() == False):
                    hiba += 1

    # egy kicsit értelmezzük ezt:
    # mivel a string ugye karaktertömb, a nevek technikailag 3D tömb lesz
    # tehát a nevek tömb i-edik sorának (rekord) a j-edik oszlopának (mező) a legelső eleme (karakter) ha nagybetű...
    # tehát minden egyes szó nagybetűvel kezdődik-e

    print("Hibás elemek száma: " + str(hiba))















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
