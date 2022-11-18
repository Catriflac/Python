"""
Kérjen be a felhasználótól egy mondatot! 
    Határozza meg, hogy hány szóból áll a mondat! 
    Írja ki a képernyőre a mondatban lévő leghosszabb szót! 
    Írja ki a mondatban lévő magas hangrendű szavakat a képernyőre.(magas: e,é,i,í,ö,ő, ü,ű), (mély: a,á, o,ó, 
        u,ú) 
    Hány olyan szó van a mondatban, ami nem magánhangzóval kezdődik? 
    Írja ki a mondatban lévő 4. szót csupa nagybetűvel. Ha nem volt a mondatban 4. szó, akkor írja ki, hogy 
        „nincs ennyi szó a mondatban.”, és addig kérjen be új mondatot, míg nincs legalább 4 szó a mondatban, 
        ezután természetesen írja ki csupa nagybetűvel a 4.-et. 
    A mondatban minden második szót cserélje le ***** karaktersorozatra.
"""



szavak = []
szoeleje = 0
leghosszabb = 0
leghosszabb_Temp = 0
mondat = ""

while ( len(mondat.split(' ')) < 4 ):
    mondat = input("Add meg a mondatot (legalább 4 szó): ")

szavak = mondat.split(' ')

kizaro_karakterek = ".?!,-_;:"

for i in range(0, len(szavak)):
    for karakter in kizaro_karakterek:
        szavak[i] = szavak[i].replace(karakter, "")
    

print(szavak)

for i in range(0, len(szavak)):

    leghosszabb_Temp = len(szavak[i])
    if (leghosszabb_Temp > leghosszabb ):
        leghosszabb = leghosszabb_Temp
        print(leghosszabb)

for i in range(0, len(szavak)):
    if ( len(szavak[i]) == leghosszabb ):
        print("Leghosszabb szó: " + szavak[i], end=' ')
        if ( szavak[i][0] == 'k' ):
            print("K-val kezdődik.")

massalh = 0

for i in range(0, len(szavak)):
    if ( len(szavak[i]) > 0 ):
        if ( 
        szavak[i][0].lower() != 'a' and 
        szavak[i][0].lower() != 'á' and 
        szavak[i][0].lower() != 'e' and 
        szavak[i][0].lower() != 'é' and 
        szavak[i][0].lower() != 'i' and 
        szavak[i][0].lower() != 'í' and 
        szavak[i][0].lower() != 'o' and 
        szavak[i][0].lower() != 'ó' and 
        szavak[i][0].lower() != 'ü' and 
        szavak[i][0].lower() != 'ű' and 
        szavak[i][0].lower() != 'u' and 
        szavak[i][0].lower() != 'ú' ):
            massalh += 1

print("Nem magánhangzóval kezdődő szavak száma: " + str(massalh))

if ( len(szavak) < 3):
    print(szavak[3].upper())
    #lowercase
    #uppercase

for i in range(0, len(szavak)):
    hossz = len(szavak[i])
    if ( i % 2 != 0):
        szavak[i] = "*" * hossz

print(szavak)