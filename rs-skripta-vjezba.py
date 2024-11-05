# 1. VARIJABLE
"""
a = 5
b = 10

print(a + b) #15
"""
"""
a = "Hello, "
b = "World!"

print(a+b) #Hello, World

"""

"""
a = 5
a = "Hello, World!" #može i s jednostrukim navodnicima

print(a)
"""

# Varijable u Pythonu mogu sadržavati slova, brojeve i znak _, ali ne smiju započinjati brojem.

"""
# Ovo je ispravno
my_variable = 5
myVariable = 10
myVariable2 = 15

# Ovo je neispravno
2myVariabe = 5 # ne može započinjati brojem
my-Variable = 10 # ne može sadržavati znak -
my Variable = 15 # ne može sadržavati razmak

"""

# Varijable u Pythonu su case-sensitive, što znači da razlikuju velika i mala slova
my_variable = 5
My_Variable = 10
MY_VARIABLE = 15

print(my_variable) # 5
print(My_Variable) # 10
print(MY_VARIABLE) # 15

# Moguće je specificirati tip varijable koristeći tzv. Casting
a = 5
# ili 
a = int(5)

# Rezultat će biti isti, no ovime se naglašava tip varijable
x = str(3)
y = int(3)
z = float(3)

print(type(x)) # <class 'str'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'float'>

# Prilikom imenovanja varijabli s više riječi, može se koristiti tehnika po izboru
# međutim u Pythonu je uobičajeno koristiti Camel Case ili Snake Case notaciju

# CAMEL CASE
myVariable = 5

# PASCAL CASE
MyVariable = 5

# SNAKE CASE
my_variable = 5

# Python dozvoljava i tzv. Multiple Assignment, odnosno dodjeljivanje više vrijednosti
# više varijabli u jednoj liniji koda: 
a, b, c = 5, 10, 15

print(a) # 5
print(b) # 10
print(c) # 15

# Može se koristiti i s drugim tipovima varijabli
a, b, c = "Hello", 5, 3.14

print(a) # Hello
print(b) # 5
print(c) # 3.14

# Moguće je i dodjeljivanje iste vrijednosti više varijabli:
a = b = c = "same value"

print(a) # same value
print(b) # same value
print(c) # same value

# Moguće je i ispisati vrijednosti varijabli u jednom redu koristeći print() funkciju:
a = 5
b = 10
c = 15

print(a, b, c) # 5 10 15

# Konkatenacija varijabli
a = "Moje "
b = "ime "
c = "je "
d = "Mirna"

print(a + b + c+ d) # Moje ime je Mirna

# Drugi način
a = "Moje"
b = "ime"
c = "je"
d = "Mirna"

print(a, b, c, d) # Moje ime je Mirna

# Koristeći sep argument
a = "Moje"
b = "ime"
c = "je"
d = "Mirna"

print(a, b, c, d, sep="-") # Moje-ime-je-Mirna

# 2. LOGIČKI IZRAZI
a = 5
b = 3

print(a + b) # 8
print(a - b) # 2
print(a * b) # 15
print(a / b) # 1.6666666666666667 (float)
print(a // b) # 1 (int)
print(a % b) # 2
print(a ** b) # 125

# funkcije nad realnim brojevima
print(abs(-5)) # 5 (apsolutna vrijednost)
print(round(3.14159, 2)) # 3.14 (zaokruživanje na n decimala)
print(max(1, 2, 3, 4, 5)) # 5 (maksimalna vrijednost)
print(min(1, 2, 3, 4, 5)) # 1 (minimalna vrijednost)

import math

print(math.sqrt(16)) # 4.0 (kvadratni korijen)
print(math.pow(2, 3)) # 8.0 (potenciranje)

print(math.exp(1)) # 2.718281828459045
print(math.log(10)) # 2.302585092994046

print(math.trunc(3.14)) # 3 (odbacuje decimalni dio)
print(math.ceil(3.14)) # 4 (zaokružuje prema gore)
print(math.floor(3.14)) # 3 (zaokružuje prema dolje)

# Nekoliko praktičnih funkcija za testiranje konačnosti realnih brojeva koje su dostupne u math biblioteke
import math

print(math.isfinite(1.0)) # True (je li broj konačan)
print(math.isinf(1.0)) # False (je li broj beskonačan tj. neizmjerno velik)

print(math.isnan(1.0)) # False (je li broj NaN, tj. Not a Number)

## OPERATORI USPOREDBE ##
a = 5
b = 10

print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

## FUNKCIJE ZA USPOREDBU REALNIH BROJEVA ##
import fractions

print(fractions.Fraction(5, 3) == 1 + fractions.Fraction(2, 3)) # True

import decimal

print(decimal.Decimal('0.1') * 3 == decimal.Decimal('0.3')) # True

## LOGIČKI OPERATORI ##
print(not True) # False
print(5 and 3) # 3 - jer je 5 True, a 3 je zadnji argument
print(0 and 3) # 0 - jer je 0 False, a 3 se neće ni provjeravati
print(5 or 3) # 5 - jer je 5 True, a 3 se neće ni provjeravati
print(0 or 3) # 3 - jer je 0 False, a 3 je zadnji argument

## OPERATORI PRIPRADNOSTI ##
a = [1, 2, 3, 4, 5]

print(1 in a) # True
print(6 in a) # False
print(1 not in a) # False
print(6 not in a) #True

iks = 'x'
print(iks in 'cvrčak') # False

samoglasnici = 'aeiou'

print('a' in samoglasnici) # True
print('b' in samoglasnici) # False

stabla = ['hrast' , 'bukva' , 'jar', 'bor']

print('bukva' in stabla) # True
print('jela' not in stabla) # True

# 3. SELEKCIJE
# if, elif, else 
"""if <logički_uvjet>; # zaglavlje
    <blok_naredbi> # tijelo
"""

a = 5

if a % 2 == 0:
    print("Broj je paran")
else:
    print("Broj je neparan")
    
# Ukoliko imamo više od dva uvjeta, korisitimo elif naredbu 
"""
if <logički_uvjet_1>:
    <blok_naredbi_1>
elif <logički_uvjet_2>:
    <blok_naredbi_2>
elif <logički_uvjet_3>:
    <blok_naredbi_3>
else: 
    <blok_naredbi_else>
"""

a = 5

if a % 2 == 0:
    print("Broj je paran")
elif a % 2 == 1:
    print("Broj je neparan")
else:
    print("Broj nije ni paran ni neparan")
    
# input() funkcija
a = int(input("Unesite broj: "))

if a % 2 == 0:
    print("Broj je paran")
elif a % 2 == 1:
    print("Broj je neparan")
else:
    print("Broj nije ni paran ni neparan")
    
tajni_broj = 42
broj = int(input("Pogodi broj! "))

if tajni_broj == broj:
    print("Bravo, pogodio si!")
else:
    if broj > tajni_broj:
        print("Manji je od tog broja!")
    else:
        print("Veći je od tog broja!")
print("Pokreni program ponovno za sljedeći pokušaj!")

# 4. ITERACIJE
# Iteracije se koriste za ponavljanje određenih dijelova koda. 
# for i while petlje

## WHILE PETLJA ##
"""
while <uvjetni_izraz>: # zaglavlje osnovnog stavka
    <naredbe> # tijelo osnovnog stavka
"""

#inicijaliziramo vrijednost broja koji ćemo kvadrirati
brojač = 1

# petlja se nastavlja sve dok je brojač manji od 11
while brojač < 11:
    print(brojač ** 2) # ispisujemo kvadrat broja
    brojač += 1 # povećamo brojač za 1
print("Gotovo!")

# FOR PETLJA 
for i in range(10):
    print(i)
    
# Ukoliko želimo ispisati brojeve od 1 do 10, možemo koristiti sljedeći kod
for i in range(1, 11):
    print(i)
    
# RANGE funkcija prima tri argumenta: početnu vrijednost, krajnju vrijednost i korak

# Primjer kako ispisati tablicu kvadrata brojeva od 1 do 10:
for x in range(1, 11):
    print(x ** 2)
    
# Primjer kako ispisati svako slovo u riječi cvrčak
for slovo in "cvrčak":
    print(slovo)
    
# Proslijedimo li konstruktoru raspona tri argumenta, tada će treći argument biti interpretiran kao prirast
# Stoga će sljedeće petlja ispisati kvadrate neparnih brojeva od 1 do 9:
for i in range(1, 10, 2):
    print(i ** 2)
    
# Ako želimo ispisati tablicu množenja brojeva od 1 do 10, to možemo jednostavno napraviti dvjema ugniježđenim petljama
for redak in range(1, 11):
    ispisRetka = ""
    for stupac in range(1, 11):
        umnozak = redak * stupac
        ispisRetka += f"{umnozak:4}"
    print(ispisRetka)
    
# U ovom primjeru koristimo f-stringove za formatiranje ispisa. f-string je moderna sintaksa za formatiranje znakovnih nizova u Pythonu
# Ugrađuje vrijednost varijabli u znakovni niz
# Ugrađivanje se vrši pomoću {} oznaka unutar znakovnog niza
# Ukoliko želimo dodatno formatirati vrijednost, možemo koristiti dvotočku i specifikator formata
# U ovom primjeru koristimo specifikator formata :4 kako bismo osigurali da svaki broj bude ispisivan na 4 mjesta 

# PRIMJER: kako ćemo ispisati brojeve od 1 do 10 s prefiksom "Broj":
for i in range(1, 11):
    print(f"Broj: {i}")
    
# 6. UGRAĐENE STRUKTURE PODATAKA

# 6.1. N-TORKE (ENG. TUPLE)
tuple = (1, 2, 3, 4, 5)
print(tuple) # (1, 2, 3, 4, 5)

# N-torke mogu sadržavati elemente različitih tipova
tuple = (1, "cvrčak", 3.14, True)
print(tuple) # (1, 'cvrčak', 3.14, True)

# Indeksi u Pythonu počinju od 0, stoga prvi element n-torke ima indeks 0, a drugi indeks 1 i tako dalje

sastojci = ("jaja", "mlijeko", "brašno", "šećer", "sol")

print(sastojci[0]) #jaja
print(sastojci[1]) # mlijeko
print(sastojci[-1]) # sol

# N-torke se mogu indeksirati i rezati na isti način kao i znakovni nizovi
sastojci = ("jaja", "mlijeko", "brašno", "šećer", "sol")

print(sastojci[1:3]) # ('mlijeko' , 'brašno') - dohvati elemente od indeksa 1 do 3 (ne uključujući indeks 3)
print(sastojci[:3]) # ('jaja', 'mlijeko', 'brašno') - dohvati elemente od početka do indeksa 3 (ne uključujući indeks 3)
print(sastojci[3:]) # ('šećer', 'sol') - dohvati elemente od indeksa 3 do kraja

# Kako se radi o slijednoj kolekciji, n-torke se mogu iterirati pomoću petlje for
sastojci = ("jaja", "mlijeko", "brašno", "šećer", "sol")

for sastojak in sastojci:
    print(sastojak)

# Veličinu n-torke možemo dobiti pomoću funkcije len()
sastojci = ("jaja", "mlijeko", "brašno", "šećer", "sol")

print(len(sastojci)) # 5

# 6.2. LISTA
lista = [1, 2, 3, 4, 5]

raznovrsna_lista = [1, "cvrčak", 3.14, True]
print(raznovrsna_lista) # [1, 'cvrčak', 3.14, True]

# Indeksiranje radimo na isti način kao i kod n-torki
sastojci = ["jaja", "mlijeko", "brašno", "šećer", "sol"]

print(sastojci[0]) # jaja
print(sastojci[1]) # mlijeko
print(sastojci[-2]) # šećer

# Možemo mijenjati sastojke
sastojci = ["jaja", "mlijeko", "brašno", "šećer", "sol"]
sastojci[0] = "kvasac"
print(sastojci) # ['kvasac', 'mlijeko', 'brašno', 'šećer', 'sol']

sastojci[-1] = "papar"
print(sastojci) # ['kvasac', 'mlijeko', 'brašno', 'šećer', 'papar']

# Liste mogu sadržavati i druge liste
matrica = [[1,2,3], [4,5,6], [7,8,9]]

print(matrica[0]) # [1, 2, 3]
print(matrica[1][1]) # 5

# Ali i n-torke
sastojci = [("jaja", 2) , ("mlijeko", 1), ("brašno", 3), ("šećer", 1), ("sol", 1)]

print(sastojci[0]) # ('jaja', 2)
print(sastojci[0][1]) # 2

# Operacije nad listama naječešće uključuju dodavanje i uklanjanje elemenata
# Dodavanje elemenata na kraj liste vršimo pomoću metode append():

sastojci = ["jaja", "mlijeko", "brašno", "šećer", "sol"]

sastojci.append("kvasac")
print(sastojci) # ['jaja', 'mlijeko', 'brašno', 'šećer', 'sol', 'kvasac']

# ili na određenu poziciju koristeći metodu insert()
sastojci.insert(2, "papar")
print(sastojci) # ['jaja', 'mlijeko', 'papar', 'brašno', 'šećer', 'sol', 'kvasac']

# Uklanjanje elemenata iz liste vršimo pomoću metode remove () - uklanja prvi element s određenom vrijednošću:
sastojci = ["jaja", "mlijeko", "brašno", "šećer", "sol"]

sastojci.remove("mlijeko")
print(sastojci) # ['jaja', 'brašno', 'šećer', 'sol']

# Ili metode pop() - uklanja element s određenim indeksom ili posljednji element ako indeks nije naveden
sastojci = ["jaja", "mlijeko", "brašno", "šećer", "sol"]

sastojci.pop() # uklanja posljednji element iz liste, jednako kao i sastojci.pop(-1)

print(sastojci) # ['jaja', 'mlijeko', 'brašno', 'šećer']
sastojci.pop(1)

print(sastojci) # ['jaja', 'brašno', 'šećer']

# Liste možemo jednistavno iterirati
sastojci = ["jaja", "mlijeko", "brašno", "šećer", "sol"]

for sastojak in sastojci:
    print(sastojak)

# ili koristeći enumerate() funkcije za ispisivanje indeksa
for indeks, sastojak in enumerate(sastojci):
    print(f"{indeks}: {sastojak}")
    
# Listama možemo promijeniti redoslijed elemenata koristeći metodu reverse() pa i sortirati ih koristeći metodu sort()
sastojci = ["jaja", "mlijeko", "brašno", "šećer", "sol"]

sastojci.reverse()
print(sastojci) # ['sol', 'šećer', 'brašno', 'mlijeko', 'jaja']

sastojci.sort()
print(sastojci) # ['brašno', 'jaja', 'mlijeko', 'sol', 'šećer']

# 7. RJEČNIK
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(rjecnik) # {'ime': 'Ivan', 'prezime': 'Ivić', 'dob': 25}

# Pojedinim elementima rječnika pristupamo pomoću ključa
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

print(rjecnik["ime"]) # Ivan
print(rjecnik["dob"]) # 25

# Ključevi rječnika moraju biti jedinstveni, ali vrijednosti ne moraju biti:
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25, "ime":"Marko"}

print(rjecnik) # {'ime': 'Marko', 'prezime': 'Ivić', 'dob': 25}

# U pravilu ne želimo mijenjati ključeve rječnika, ali možemo dodavati nove ključeve i mijenjati vrijednosti postojećih ključeva
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

rjecnik["adresa"] = "Zagreb"

print(rjecnik) # {'ime': 'Ivan', 'prezime': 'Ivić', 'dob': 25, 'adresa': 'Zagreb'}

rjecnik["dob"] = 26
print(rjecnik) # {'ime': 'Ivan', 'prezime': 'Ivić', 'dob': 26, 'adresa': 'Zagreb'}

# Rjecnike možemo iterirati pomoću petlje for
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

for kljuc in rjecnik:
    print(kljuc, rjecnik[kljuc]) # ime Ivan prezime Ivić dob 25
    
# Ključeve i vrijednosti rječnika možemo dohvatiti pomoću metoda keys() i values(), dok metodom items() možemo dohvatiti parove ključ-vrijednost:
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

print(rjecnik.keys()) # dict_keys(['ime', 'prezime', 'dob'])
print(rjecnik.values()) # dict_values(['Ivan', 'Ivić', 25])

# dohvaćanje ključeva i vrijednosti pomoću metode items()
for kljuc, vrijednost in rjecnik.items():
    print(kljuc, vrijednost) # ime Ivan prezime Ivić dob 25
    
# U pravilu, rječnike možemo, osim navođenjem izraza u vitičastim zagradama, stvarati i u pozivom konstruktora dict() nad pobrojivim argumentom koji sadrži parove ključ-vrijednost
tablica = dict([("rajčica", "povrće"), ("jabuka", "voće")])
print(tablica) # {'rajčica': 'povrće', 'jabuka': 'voće'}

# Literale malih rječnika je praktično stvarati navođenjem imenovanih argumenata konstruktoru dict()
cjenik = dict(ćevapi = 10, pivo = 15, kava = 7)
print(cjenik) # {'ćevapi': 10, 'pivo': 15, 'kava': 7}

# Uobičajeno je da rječnici sadrže i druge rječnike, ali i liste kao vrijednosti
namirnice = {"čokolada": ["smeđe", "ukusno", "zdravo"], "kelj":["zeleno", "gorko", "zdravo"],
             "luk": ["bijelo", "smrdljivo", "zdravo"], "špek": ["crveno", "slano", "nezdravo"]}

print(namirnice["čokolada"]) # ['smeđe', 'ukusno', 'zdravo']

print(type(namirnice)) # <class 'dict'>
#ali
print(type(namirnice["čokolada"])) # <class 'list'>

# Rekli smo da sve ključeve rječnika možemo dohvatiti pmooću metode keys()
namirnice = {"čokolada": ["smeđe", "ukusno", "zdravo"], "kelj":["zeleno", "gorko", "zdravo"],
             "luk": ["bijelo", "smrdljivo", "zdravo"], "špek": ["crveno", "slano", "nezdravo"]}

print(namirnice.keys()) # dict_keys(['čokolada', 'kelj', 'luk', 'špek'])

for kljuc in namirnice.keys():
    print(kljuc) # čokolada kelj luk špek
    
# Međutim, kako možemo dohvatiti samo zdrave namirnice ako nam je poznato da sadrže vrijednost "zdravo" unutar liste vrijednosti?
for kljuc, vrijednost in namirnice.items():
    if "zdravo" in vrijednost:
        print(kljuc) # čokolada kelj luk
        







