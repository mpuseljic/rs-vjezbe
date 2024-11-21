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
        
# 8. SKUP
skup = {1, 2, 3, 4, 5}

print(skup) # {1, 2, 3, 4, 5}

skup_2 = {"banana", "jabuka", "kruška"}
print(skup_2) # {'banana', 'kruška', 'jabuka'}

# Jednom kad smo skupove definirali, nije moguće mijenjati elemente, ali je moguće dodavati i uklanjati elemente
skup = {1, 2, 3, 4, 5}
skup.add(6) 
print(skup) # {1, 2, 3, 4, 5, 6}

skup.remove(3)
print(skup) # {1, 2, 4, 5, 6}
skup.add(1) # duplikar se neće dodati, skup ostaje nepromijenjen

# sve elemente željenog skupa možemo obići standardnom iteracijom na sljedeći način:
skup = {1, 2, 3, 4, 5}

for element in skup:
    print(element)
    
# jednako tako možemo i koristiti operator 'in' za ispitivanje vrijednosti
print(1 in skup)
print( 6 in skup)

# Metodama add() i remove() možemo dodavati i uklanjati elemente iz skupa. Metoda discard() također uklanja element iz skupa, ali neće baciti iznimku ako element ne postoji u skupu
skup = {1, 2, 3, 4, 5}
skup.discard(3)
print(skup) # {1, 2, 4, 5}

skup.discard(6) # neće baciti iznimku
print(skup) # {1, 2, 4, 5}

# Meotda union() vraća uniju dva skupa, metoda intersection() vraća presjek dva skupa, dok metoda difference() vraća razliku dva skupa:
voce = {"🍎", "🍌", "🍐", "🍊"}
povrce = {"🍅", "🥒", "🧅", "🥬"}

print(voce.union(povrce)) # {'🍊', '🍐', '🍎', '🧅', '🍌', '🍅', '🥬', '🥒'}

print(voce.intersection(povrce)) # set() prazan skup, jer voće i povrće nemaju zajedničkih elemenata

voce.add("🍅")

print(voce.intersection(povrce)) # {'🍅'}

print(voce.difference(povrce)) # {'🍎', '🍐', '🍌', '🍊'} - voće koje nije povrće
print(povrce.difference(voce)) # {'🧅', '🥬', '🥒'} -povrće koje nije voće

# 9. FUNKCIJE
def pozdrav():
    print("Hello World!")

pozdrav()

def zbroj(a,b):
    return a + b

print(zbroj(3, 5))

# Primjer funkcije koja ima podrazumijevane vrijednosti za argumente
def zbroj(a=0, b=0):
    return a+b

print(zbroj())
print(zbroj(3))
print(zbroj(3, 5))

# Primjer funkcije koja vraća više vrijednosti
def zbroj_razlika(a, b):
    zbroj = a + b
    razlika = a - b
    return zbroj, razlika

z, r = zbroj_razlika(5, 3)

# Primjer rekurzivne funkcije koja računa faktorijel broja 
def faktorijel(n):
    if n == 0:
        return 1
    else:
        return n*faktorijel(n-1)

print(faktorijel(5))

# Funkcija koja će nam izračunati točno vrijeme u lokalnoj vremenskoj zoni
import time

def točnoVrijeme():
    vrijeme = time.localtime()
    sati = vrijeme.tm_hour
    minute = vrijeme.tm_min
    sekunde = vrijeme.tm_sec
    return f"{sati}:{minute}:{sekunde}"

print(točnoVrijeme())

# Funkcije mogu primati sve tipove podataka kao argumente, uključujući i kolekcije. Idemo napisati funkciju
#koja će kao prvi argument primiti listu brojeva, a kao drugi argument broj koji će predstavljati faktor s kojim
#ćemo potencirati svaki broj iz liste.
def potenciranje_faktorom(lista, faktor):
    nova_lista = []
    for broj in lista:
        nova_lista.append(broj ** faktor)
    return nova_lista

print(potenciranje_faktorom([1, 2, 3, 4, 5], 2)) # [1, 4, 9, 16, 25]

# Funkcije mogu primati i druge funkcije kao argumente. Ovo je korisno kada želimo da funkcija izvrši neku
# operaciju nad drugom funkcijom. Primjer funkcije koja prima funkciju kao argument:
def pomnozi_s_dva(x):
    return x * 2

def primjeni_na_listu(funkcija, lista):
    nova_lista = []
    for element in lista:
        nova_lista.append(funkcija(element))
    return nova_lista

print(primjeni_na_listu(pomnozi_s_dva, [1, 2, 3, 4, 5])) # [2, 4, 6, 8, 10]

# Idemo napisati i jednu matematičku funkciju koja će računati vrijednosti trigonometrijskih funkcija za zadani
# kut izrađen u radijanima. Za to ćemo koristiti modul math.

import math

def trigonometrija(kut):
    radijani = math.radians(kut)
    sinus = math.sin(radijani)
    kosinus = math.cos(radijani)
    tangens = math.tan(radijani)
    
    return sinus, kosinus, tangens

kut = 45
sinus, kosinus, tangens = trigonometrija(kut)
print(f"Sinus: {sinus}, Kosinus: {kosinus}, Tangens: {tangens}")

###### RS-02 - LAMBDA FUNKCIJE 
# Lambda funkcije su anonimne funkcije koje se u pravilu koriste za jednokratne, male operacije. 
# Funkcije su anonimne jer se ne dodjeljuju imen kao što je to slučaj kod običnih funkcija.
# Lambda funkcije mogu primiti proizvoljan broj argumenata, ali mogu sadržavati samo jedan izraz

"""
SINSTAKSA LAMBDA FUNKCIJE JE SLJEDEĆA:

lambda arguments : expression 
"""

# NPR. KLASIČNA FUNKCIJA ZA KVADRIRANJE BROJA MOŽEMO NAPISATI OVAKO
def kvadriraj(x):
    return x ** 2

print(kvadriraj(5)) # 25

# KOD LAMBDA FUNKCIJE POTREBNO JE IZBACITI KLJUČNU RIJEČ DEF I IME FUNKCIJE, A UMJESTO TOGA KORISTIMO KLJUČNU RIJEČ LAMBDA
lambda x: x ** 2

print((lambda x: x ** 2)(5)) # 25

kvadriraj = lambda x: x ** 2

print(kvadriraj(5))

# LAMBDA FUNKCIJE MOGU PRIMITI VIŠE ARGUMENATA:
zbroji = lambda x, y: x + y

print(zbroj(5, 3))

zbroji_kvadrate = lambda x, y: x ** 2 + y ** 2
print(zbroji_kvadrate(3, 4))

"""
Ali i ne moraju primiti niti jedan argument:
Sljedeći primjer nema puno smisla jer je moguće samo pohraniti vrijednost "Pozdrav!" u varijablu i
ispisati je, ali je koristan za demonstraciju:
"""

pozdrav = lambda: "Pozdrav!"

print(pozdrav())

# U lambda funkcijama, kao i običnim, možemo postaviti zadane vrijednosti za argumente:
pozdrav = lambda ime = "Ivan": f"Pozdrav, {ime}!" # koristimo f-string za formatiranje stringa

print(pozdrav())
print(pozdrav("Marko"))

# pa i više njih
circle_area = lambda r=1, pi=3.14: pi * r ** 2

print(circle_area())
print(circle_area(2))

# Ako lambda funkcija ima više argumenata, argumente s zadanim vrijednostima postavljamo na kraj.
multiplier = lambda x, factor = 2: x * factor

print(multiplier(5))
print(multiplier(5, 3))

"""
Naravno, kao i obične funkcije, lambda funkcije je moguće koristiti sa svim tipovima podataka, uključujući i
strukture podataka:
"""
tekst = "Ovo je neki tekst"

print((lambda x: x.upper())(tekst))

######### Lambda funkcije kao argumenti drugim funkcijama ####
"""
Primjerice: Želimo napisati funkciju koja će primati listu brojeva i funkciju koja će se primijeniti na svaki
element liste. To možemo napraviti ovako:
"""

def primijeni_na_sve(lista, funkcija):
    rezultat = []
    for element in lista:
        rezultat.append(funkcija(element)) # u novu listu dodajemo rezultate funkcije primijenjene na svaki element
        
    return rezultat

"""
Što je ovdje funkcija ? Što god želimo i definiramo kao funkciju. Primjer, želimo kvadrirati svaki element
liste, za to možemo definirait malo anonimnu lambda funkciju:
"""

lambda x: x ** 2 # za svaki element x vraća x na kvadrat

# i proslijedimo je kao argument funkciji primijeni_na_sve
print(primijeni_na_sve([1, 2, 3, 4], lambda x: x ** 2))

# ili želimo primijeniti funkciju koja potencira vrijednost na 3.potenciju
print(primijeni_na_sve([1, 2, 3, 4], lambda x: x ** 3))

# funkciju je moguće pohraniti i u varijablu te potom proslijediti
uvecaj_za_5 = lambda broj: broj + 5

print(primijeni_na_sve([1, 2, 3, 4], uvecaj_za_5))

# AKO ŽELIMO MOŽEMO DEFINIRATI I UVJETE UNUTAR LAMBDA FUNKCIJE
# lambda arguments: expression if condition else expression

# Primjer: Želimo kvadrirati broj samo ako je paran
kvadriraj_parne = lambda x: x ** 2 if x % 2 == 0 else x

# ili želimo vratiti duljinu znakovnog niza ako je duljina veća od 5, inače vraćamo sam znakovni niz:
dulji_od_5 = lambda niz: len(niz) if len(niz) > 5 else niz

# ili želimo vratiti "paran" ako je broj paran, inače "neparan":
paran_neparan = lambda x: "paran" if x % 2 == 0 else "neparan"


#### FUNKCIJE VIŠEG REDA ####
"""
Funkcije višeg reda (eng. Higher-order functions) su funkcije koje primaju druge funkcije kao argumente
ILI vraćaju druge funkcije kao rezultat.

Funkcije višeg reda su korisne jer omogućuju pisanje modularnog koda, tj. koda koji je podijeljen u manje,
samostalne dijelove koji obavljaju specifične zadatke.
Ono što ćemo vjerojatno najčešće raditi, je koristiti lambda funkcije kao argumente ugrađenim
funkcijama višeg reda, kao što su map , filter , reduce , sort itd.

"""

### FUNKCIJA MAP
"""
Funkcija map prima funkciju i iterabilni objekt (npr. listu) i primjenjuje tu funkciju na svaki element tog
objekta. Povratna vrijednost je map objekt koji se može pretvoriti u listu, tuple ili neki drugi iterabilni
objekt.
"""

# SINTAKSA: map(function, iterables)

# Primjerice: Želimo kvadrirati svaki element liste:

lista = [1, 2, 3, 4]

kvadriraj = lambda x: x ** 2
kvadrirana_lista = list(map(kvadriraj, lista)) # map vraća map objekt, zato koristimo list () za pretvaranje u listu

# ili kraće
kvadrirana_lista = list(map(lambda x: x ** 2, lista))

"""
Primjer: Imamo listu studenata s imenom, prezimenom i JMBAG-om. Želimo izvući samo JMBAG-ove:
Kako bismo ovo učinili "ručno"? Bez lambda funkcija i funkcija višeg reda (map)?
"""

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889"},
    {"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878"},
    {"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777"}
]

jmbagovi = []

for student in studenti:
    jmbagovi.append(student["jmbag"])
    
print(jmbagovi)

# Kako bismo to učinili koristeći map i lambda funkciju?
jmbagovi = list(map(lambda student: student["jmbag"], studenti))

print(jmbagovi)

#### FUNKCIJA FILTER ####
"""
Funkcija filter prima funkciju koja vraća True ili False i iterabilni objekt. Vraća filter objekt koji se
može pretvoriti u listu, tuple ili neki drugi iterabilni objekt.
Ova funkcija će filtrirati elemente iterabilnog objekta prema rezultatu funkcije (predikata) koja vraća True
ili False .
"""

# SINTAKSA: filter(function, iterables)

# Primjerice: Želimo filtrirati samo parne brojeve iz liste:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

parni = []

for broj in lista:
    if broj % 2 == 0:
        parni.append(broj)

print(parni)

# ili koristeći filter i lambda funkciju
parni = list(filter(lambda x: x % 2 == 0, lista))

# Naravno možemo kombinirati i različite strukture podataka:
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889", "godina_rodenja" : 2000},
{"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878", "godina_rodenja" : 1999},
{"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777", "godina_rodenja" : 2003},
{"ime": "Petra", "prezime": "Petrić", "jmbag": "0303088777", "godina_rodenja" : 2001}
]

rodeni_prije_2000 = list(filter(lambda student: student["godina_rodenja"] < 2000, studenti))

# ručno
rodeni_prije_2000 = []
for student in studenti:
    if student["godina_rodenja"] < 2000:
        rodeni_prije_2000.append(student)
        
print(rodeni_prije_2000)

#### FUNKCIJE ANY I ALL
"""
Funkcije any i all su također funkcije višeg reda koje primaju iterabilni objekt i vraćaju True ili False.
any vraća True ako je bilo koji (barem jedan) element iterabilnog objekta istinit, inače vraća False.
all vraća True ako su svi elementi iterabilnog objekta istiniti, inače vraća False.
"""

# Primjer korištenja funkcije any
print(any([False, False, True])) # True (jer je barem jedan element True)
print(any([False, False, False])) # False (jer niti jedan element nije True)

# Primjer korištenja funkcije all
print(all([True, True, True])) # True (jer su svi elementi True)
print(all([True, False, True])) # False (jer nisu svi elementi True)

"""
Kako koristiti ove funkcije s lambda funkcijama?
Recimo da želimo provjeriti jesu li svi brojevi u listi parni. Idemo prvo ručno:
"""
def svi_parni(lista):
    for broj in lista:
        if broj % 2 != 0:
            return False
    return True
print(svi_parni([2, 4, 6, 8])) # True
print(svi_parni([2, 4, 6, 7])) # False

# ili koristeći all, map i lambda funkciju:

print(all(map(lambda x: x % 2 == 0, [2, 4, 6, 8]))) # True
print(all(map(lambda x: x % 2 == 0, [2, 4, 6, 7]))) # False

# Pogledajmo još jedan primjer, gdje želimo provjeriti jesu li svi putnici uplatili aranžman:
putnici = [
{"ime": "Ivan", "prezime": "Ivić" , "uplata": True},
{"ime": "Marko", "prezime": "Marković", "uplata": True},
{"ime": "Ana", "prezime": "Anić", "uplata": False}
]

print(all(map(lambda putnik: putnik["uplata"], putnici)))

# ili ručno
def svi_uplatili(putnici):
    for putnik in putnici:
        if not putnik["uplata"]:
            return False
    return True

print(svi_uplatili(putnici))

### IZGRADNJA STRUKTURA KROZ COMPREHENSION SINTAKSU

"""
Postoje 4 vrste comprehension sintakse:
1. List comprehension (izgradnja liste)
2. Dictionary comprehension (izgradnja rječnika)
3. Set comprehension (izgradnja skupa)
4. Generator comprehension (izgradnja generatora)
"""

### LIST COMPREHENSION
# KLASIČAN NAČIN
kvadrati = []
for i in range(1, 11):
    kvadrati.append(i ** 2)
    
print(kvadrati) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Rekli smo da ovo možemo skratiti i korištenjem map funkcije višeg reda:
kvadrati = list(map(lambda x: x ** 2, range(1, 11)))

print(kvadrati) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Ali i korištenjem list comprehension sintakse:
kvadrati = [x ** 2 for x in range(1, 11)]

print(kvadrati) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""
Osnovna sintaksa list comprehensiona je sljedeća:
[expression for element in iterable]

Gdje je:
expression izraz koji se izvršava za svaki element
element varijabla koja predstavlja trenutni element
iterable iterabilni objekt (npr. lista, skup, rječnik, generator), u ovom slučaju je lista brojeva od 1 do 10
"""

# Recimo da imamo listu znakovnih nizova gdje želimo izgraditi listu duljina tih nizova:
# Klasičan način:
nizovi = ["jabuka", "kruška", "banana", "naranča"]
duljine = []

for niz in nizovi:
    duljine.append(len(niz))
    
print(duljine) # [6, 6, 6, 7]

# List comprehension:
duljine = [len(niz) for niz in nizovi]

print(duljine)

# Kako izgraditi listu kvadrata brojeva od 1 do 10, ali samo za neparne brojeve:
# Klasičan način:
kvadrati_neparnih = []
for i in range(1, 11):
    if i % 2 != 0:
        kvadrati_neparnih.append(i ** 2)
        
print(kvadrati_neparnih) # [1, 9, 25, 49, 81]

# List comprehension:
kvadrati_neparnih = [x ** 2 for x in range(1, 11) if x % 2 != 0]

"""
Sintaksa s if uvjetom:
[expression for element in iterable if condition]
"""

"""
Kako ovo koristiti sa strukturama? Imamo listu rječnika gdje želimo izgraditi listu imena studenata koji su
rođeni prije 1999. godine:
"""
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godina_rodenja": 2000},
{"ime": "Marko", "prezime": "Marković", "godina_rodenja": 1990},
{"ime": "Ana", "prezime": "Anić", "godina_rodenja": 2003},
{"ime": "Petra", "prezime": "Petrić", "godina_rodenja": 2001}
]

# KLASIČAN NAČIN
rodeni_prije_1999 = []

for student in studenti:
    if student["godina_rodenja"] < 1999:
        rodeni_prije_1999.append(student["ime"])
        
print(rodeni_prije_1999) # ['Marko']

# LIST COMPREHENSION:

rodeni_prije_1999 = [student["ime"] for student in studenti if student["godina_rodenja"] < 1999]

# MOGUĆE JE DODATI I ELSE IZRAZ
"""
Primjer: Želimo izgraditi listu kvadrata brojeva od 1 do 10, ali za neparne brojeve kvadrat, a za parne
brojeve sam broj:
"""
# KLASIČAN NAČIN
kvadrati_neparnih_a_parne_brojevi= []

for i in range(1, 11):
    if i % 2 != 0:
        kvadrati_neparnih_a_parne_brojevi.append(i ** 2)
    else:
        kvadrati_neparnih_a_parne_brojevi.append(i)
        
print(kvadrati_neparnih_a_parne_brojevi) # [1, 2, 9, 4, 25, 6, 49, 8, 81, 10]

# List comprehension:
kvadrati_neparnih_a_parne_brojevi = [x ** 2 if x % 2 != 0 else x for x in range(1, 11)] #
[1, 2, 9, 4, 25, 6, 49, 8, 81, 10]

# Želimo izgraditi listu voća, ali samo prva tri slova svakog voća:
# KLASIČAN NAČIN
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

prva_tri_slova = []

for fruit in fruits:
    prva_tri_slova.append(fruit[:3])
    
print(prva_tri_slova) # ['app', 'ban', 'che', 'kiw', 'man']

# List comprehension:
prva_tri_slova = [fruit[:3] for fruit in fruits]

# Ili želimo izgraditi novu listu voća, npr. koja sadrži samo ono voće koje sadrži slovo a:
#Klasičan način:
sa_slovom_a = []

for fruit in fruits:
    if "a" in fruit:
        sa_slovom_a.append(fruit)
        
print(sa_slovom_a) # ['apple', 'banana', 'mango']

# List comprehension:
sa_slovom_a = [fruit for fruit in fruits if "a" in fruit]



##### Dictionary comprehension ####
"""
Dictionary comprehension je vrlo sličan list comprehensionu, ali umjesto liste, gradimo rječnik kroz
comprehension sintaksu.
Sintaksa dictionary comprehensiona je sljedeća:
{key_expression: value_expression for item in iterable if condition}

Gdje je:
key_expression izraz koji se izvršava za ključeve
value_expression izraz koji se izvršava za vrijednosti
item varijabla koja predstavlja trenutni element
iterable iterabilni objekt (npr. lista, skup, rječnik, generator)
condition uvjet koji se može dodati (nije obavezan)
"""

#Recimo da imamo listu voća fruits i želimo izgraditi rječnik gdje su ključevi voća, a vrijednosti duljina
# tih voća:
# Klasičan način:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
duljine_voca = {}

for fruit in fruits:
    duljine_voca[fruit] = len(fruit)
    
print(duljine_voca) # {'apple': 5, 'banana': 6, 'cherry': 6, 'kiwi': 4, 'mango': 5}


#Dictionary comprehension:
duljine_voca = {fruit: len(fruit) for fruit in fruits}

print(duljine_voca) # {'apple': 5, 'banana': 6, 'cherry': 6, 'kiwi': 4, 'mango': 5}

# Ključevi neka budu brojevi od 1 do 5, a vrijednosti kvadrati tih brojeva:
# Klasičan način:
kvadrati_brojeva = {}

for i in range(1, 6):
    kvadrati_brojeva[i] = i ** 2
    
print(kvadrati_brojeva) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary comprehension:
kvadrati_brojeva = {i: i ** 2 for i in range(1, 6)}
print(kvadrati_brojeva) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Primjer: Želimo izgraditi rječnik gdje su ključevi brojevi, a vrijednosti kvadrati tih brojeva, ali samo za parne
# brojeve od 1 do 10:
#Klasičan način:
kvadrati_parnih = {}

for i in range(1, 11):
    if i % 2 == 0:
        kvadrati_parnih[i] = i ** 2
        
print(kvadrati_parnih) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

#Dictionary comprehension:
kvadrati_parnih = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}
print(kvadrati_parnih) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Primjer: Izradit ćemo rječnik gdje ćemo za svaki broj kao ključ postaviti taj broj, a vrijednost će biti "paran"
# ako je broj paran, inače "neparan":
# Klasičan način:
paran_neparan = {}

for i in range(1, 11):
    if i % 2 == 0:
        paran_neparan[i] = "paran"
    else:
        paran_neparan[i] = "neparan"
        
print(paran_neparan) # {1: 'neparan', 2: 'paran', 3: 'neparan', 4: 'paran', 5: 'neparan', 6: 'paran', 7: 'neparan', 8: 'paran', 9: 'neparan', 10: 'paran'}

# Dictionary comprehension:
paran_neparan = {i: "paran" if i % 2 == 0 else "neparan" for i in range(1, 11)}
print(paran_neparan) # {1: 'neparan', 2: 'paran', 3: 'neparan', 4: 'paran', 5: 'neparan', 6: 'paran', 7: 'neparan', 8: 'paran', 9: 'neparan', 10: 'paran'}


#### KLASE I OBJEKTI
"""
Klase (eng. Class) i objekti (eng. Object) su temeljna paradigma u objektno orijentiranom programiranju.
Klase su šablonski opisi objekata, dok su objekti instance klasa. Izradom nove klase, automatski se
stvara novi tip podataka.
Slično kao i u JavaScriptu, u Pythonu je gotovo su gotovo svi programski konstrukti objekti koji sadrže
atribute (eng. attribute) i metode (eng. method).
Dakle klase možemo zamisliti kao šablone (eng. blueprint) za definiranje atributa i metoda objekata.
Klasu definiramo ključnom riječju class, a objekt klase stvaramo pozivom klase kao funkcije. Ne
koristimo new ključnu riječ kao u nekim drugim jezicima.
"""
# Atribute možemo definirati prilikom definicije, navodeći ih kao varijable unutar klase:
class Osoba:
    ime = "Ivan"
    prezime = "Ivić"
    godine = 25
    
osoba = Osoba()

print(osoba.ime) # Ivan
print(osoba.prezime) # Ivić
print(osoba.godine) # 25

#### KONSTRUKTOR KLASE
"""
Primjer iznad nije dobar način definiranja klase jer svi objekti klase Osoba dijele iste atribute.
Konstruktor (eng. Constructor) je posebna metoda koja se koristi za inicijalizaciju objekta klase.
Iz tog razloga možemo definirati konstruktor klase koji se definira metodom __init__. Ova metoda
poziva se svaki put prilikom inicijalizacije objekta klase.
"""

# Primjer: Nadogradnja klase Osoba s konstruktorom:
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        
osoba = Osoba("Ivan", "Ivić", 25)

print(osoba.ime) # Ivan
print(osoba.prezime) # Ivić
print(osoba.godine) # 25

osoba2 = Osoba("Marko", "Marković", 30)

print(osoba2.ime) # Marko
print(osoba2.prezime) # Marković
print(osoba2.godine) # 30

#### METODE KLASE
"""
Metode klase su funkcije koje se definiraju unutar klase i koriste se za izvršavanje određenih operacija nad
objektima klase.
Kada definiramo metode, možemo pristupati vrijednostima atributa objekta pomoću self reference.
"""

# Primjer metode pozdrav:
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        
    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime} i imam {self.godine} godina."

# Poziv metode:
osoba = Osoba("Snješka", "Snježanić", 25)

print(osoba.pozdrav()) # Pozdrav, ja sam Snješka Snježanić i imam 25 godina.

#### NASLJEĐIVANJE
"""
Nasljeđivanje (eng. Inheritance) je ključna paradigma u objektno orijentiranom programiranju. Omogućuje
nam definiranje novih klasa koje nasljeđuju atribute i metode od postojećih klasa.
Klasa koja nasljeđuje zove se podklasa (eng. subclass), a klasa koja se nasljeđuje zove se nadklasa (eng.
superclass).
Prilikom definiranja podklase, navodimo nadklasu u zagradama, a koristeći super() funkciju možemo
nasljediti sve atribute i metode nadklase.
"""

# Primjer nasljeđivanja
class Korisnik:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        self.username = f"{ime.lower()}_{prezime.lower()}"
        
    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime}, moj username je {self.username}."

class Admin(Korisnik):
    def __init__(self, ime, prezime, privilegije):
        super().__init__(ime, prezime) # nasljeđujemo atribute od nadklase
        self.privilegije = privilegije
        
    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime}, moj username je {self.username} i imam ukupno {len(self.privilegije)} privilegije: {','.join(self.privilegije)}."

# Instaciramo objekt klase Admin:
root = ["dodavanje_korisnika", "brisanje_korisnika", "dodavanje_postova", "brisanje_postova"]
admin = Admin("Ivan", "Ivić", root)
print(admin.pozdrav()) #Pozdrav, ja sam Ivan Ivić, moj username je ivan_ivić i imam ukupno 4 privilegije: dodavanje_korisnika, brisanje_korisnika, dodavanje_postova, brisanje_postova.



###### RS3 - Asinkroni Python - Osnove asyncio biblioteke ###########
### KORUTINE
"""
Ključne riječi async i await koriste se za:
1. definiranje asinkronih ( async) funkcija (koje vraćaju coroutine objekte) te za
2. čekanje na rezultat izvršavanja asinkronih funkcija ( await).
Kako bismo simulirali asinkrono izvršavanje, iskoristit ćemo funkciju asyncio.sleep() koja simulira
čekanje određenog vremena zadanog u sekundama.
Sintaksa:
asyncio.sleep(delay)
delay - broj sekundi koliko želimo čekati - odgoditi izvršavanje koda
"""

import asyncio
async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
    
asyncio.run(main())

### Konkurentno izvršavanje više korutina
async def fetch_data():
    print("Dohvaćam podatke...")
    data = {"iznos": "3000", "stanje":"uspješno"}
    await asyncio.sleep(2)
    print("Podaci dohvaćeni.")
    return data

async def main():
    data = await fetch_data()
    print(f"Podaci: {data}")
    
asyncio.run(main())


async def fetch_api_1():
    print("Dohvaćam podatke s API-ja 1...")
    await asyncio.sleep(2)
    print("Podaci s API-ja 1 dohvaćeni.")
    return {"api_1": "uspješno"}

async def fetch_api_2():
    print("Dohvaćam podatke s API-ja 2...")
    await asyncio.sleep(4)
    print("Podaci s API-ja 2 dohvaćeni.")
    return {"api_2": "uspješno"}

async def main():
    podaci_1 = await fetch_api_1()
    podaci_2 = await fetch_api_2()
    
    print(f"Podaci s API-ja 1: {podaci_1}")
    print(f"Podaci s API-ja 2: {podaci_2}")
    
asyncio.run(main())


async def main():
    podaci_1, podaci_2 = await asyncio.gather(fetch_api_1(), fetch_api_2())
    
    print(f"Podaci s API-ja 1: {podaci_1}")
    print(f"Podaci s API-ja 2: {podaci_2}")
    
    
"""
Primjer: Definirat ćemo korutinu timer() koja će simulirati otkucaje timera svake sekunde. Korutina prima
2 argumenta: naziv timera i broj sekundi koliko će trajati, a zatim svake sekunde ispisuje preostale vrijeme.
"""

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f"{name}: {i} sekundi preostalo...")
        await asyncio.sleep(1)
        print(f"{name}: Vrijeme je isteklo!")
        
async def main():
    await asyncio.gather(
        timer("Timer 1", 3),
        timer("Timer 2", 5)
    )
    
asyncio.run(main())



#### ASYNCIO TASKS
"""
Radni zadatak, odnosno task u asyncio su temeljni gradivni blokovi asinkronog programiranja u Pythonu.
Task predstavlja izvršnu jedinicu, odnosno asinkronu operaciju, koja se zakazuje (eng. schedules) za
izvršavanje u event loop-u.
asyncio.create_task() je funkcija koja stvara novi Task objekt koji izvršava asinkronu funkciju. Ova
funkcija je korisna kada želimo definirati korutinu koju ćemo zakazati za konkurentno izvršavanje kasnije u
programu.
Sintaksa:
asyncio.create_task(coroutine)
coroutine - asinkrona funkcija koju želimo zakazati za konkurentno izvršavanje
vraća Task objekt ( <class '_asyncio.Task'>)
"""

async def fetch_api_1():
    print("Dohvaćam podatke s API-ja 1...")
    await asyncio.sleep(2)
    print("Podaci s API-ja 1 dohvaćeni.")
    return {"api_1": "uspješno"}

async def fetch_api_2():
    print('Dohvaćam podatke s API-ja 2...')
    await asyncio.sleep(4)
    print('Podaci s API-ja 2 dohvaćeni.')
    return {'api_2': 'uspješno'}


async def main():
    taks_1 = asyncio.create_task(fetch_api_1())
    task_2 = asyncio.create_task(fetch_api_2())
    
    podaci_1 = await taks_1
    podaci_2 = await task_2
    
    print(f"Podaci s API-ja: {podaci_1}")
    print(f"Podaci s API-ja 2: {podaci_2}")
    
asyncio.run(main())

#### Konkurentno izvođenje kroz asyncio.gather() i asyncio.create_task()

"""
Želimo definirati jednu korutinu korutina(n) koja će čekati jednu sekundu, a zatim vratiti poruku o
završetku izvođenja.
"""
async def korutina(n):
    await asyncio.sleep(1)
    return f"Korutina {n} je završila."

"""
U main() funkciji ćemo pohraniti 5 korutina u liste tasks. Drugim riječima, želimo pohraniti 5 Task
objekata koji će izvršavati korutine korutina(n), za n od 1 do 5.
"""

async def main():
    tasks = []
    
    for i in range(1,6):
        task = asyncio.create_task(korutina(i))
        tasks.append(task)
        
    print(tasks)
    
# asyncio.run(main())

# Kako ovo možemo napraviti elegantnije? list comprehension nam može pomoći.
async def main():
    tasks = [asyncio.create_task(korutina(i)) for i in range(1, 6)]
    print(tasks)
    
asyncio.run(main())

"""
Za pokretanje svih korutina konkurentno, ne želimo pisati await task za svaki Task objekt.
Dakle, sljedeće nije najbolje rješenje:
"""

async def main():
    tasks = [asyncio.create_task(korutina(i)) for i in range(1, 6)]
    
    for task in tasks:
        await task
    
    print("Sve korutine su završile.")

asyncio.run(main())


"""
Zašto? Nigdje ne pohranjujemo rezultate korutina, već samo čekamo na njihov završetak.
Stvari možemo riješiti ovako:
"""

async def main():
    tasks = [asyncio.create_task(korutina(i)) for i in range(1, 6)]
    
    results = []
    
    for task in tasks:
        results.append(await task)
    
    print(results)

asyncio.run(main())

"""
Međutim, puno bolje rješenje je koristiti asyncio.gather().
asyncio.gather() osim može korutina može primiti i Task objekte
možemo proslijediti jedan ili više Task objekata na isti način kao i korutine: await
asyncio.gather(task_1, task_2, task_3)
međutim, možemo proslijediti i listu korutina ili Task objekata s operatorom *: await
asyncio.gather(*tasks)
"""
async def main():
    tasks = [asyncio.create_task(korutina(i)) for i in range(1,6)]
    results = await asyncio.gather(*tasks)
    print(results)
    
asyncio.run(main())

"""
Pogledat ćemo još nekoliko jednostavnih primjera i mjeriti vrijeme izvođenja programa koristeći time
modul.
"""

# Definirat ćemo korutinu koja će nakon određenog vremena ispisati poruku.
import time 

async def kaži_nakon(delay, poruka):
    await asyncio.sleep(delay)
    print(poruka)
    
async def main():
    print(f"Početak: {time.strftime('%X')}")
    
    await kaži_nakon(1, "Pozdraaav!")
    await kaži_nakon(2, "Kako si?")
    
    print(f"Kraj: {time.strftime('%X')}")
    
asyncio.run(main())

# Isto možemo pretočiti u Task objekte:
async def main():
    print(f"Početak: {time.strftime('%X')}")
    
    task1 = asyncio.create_task(kaži_nakon(1, "Pozdraaav!"))
    task2 = asyncio.create_task(kaži_nakon(2, "Kako si?"))
    
    await task1
    await task2
    
    print(f"Kraj: {time.strftime('%X')}")
    
asyncio.run(main())

# ili koristeći asyncio.gather()
async def main():
    print(f"Početak: {time.strftime('%X')}")
    
    task1 = asyncio.create_task(kaži_nakon(1, "Pozdraaav!"))
    task2 = asyncio.create_task(kaži_nakon(2, "Kako si?"))
    
    await asyncio.gather(task1, task2)
    
    print(f"Kraj: {time.strftime('%X')}")
    
asyncio.run(main())

"""
Primjer: Idemo vidjeti kako možemo na isti način koristiti asyncio.gather() za pozivanje prethodne
korutine Timer(name, delay) koja simulira otkucaje timera svake sekunde. Korutinu želimo pokrenuti 3
puta s različitim vremenima trajanja. Potrebno je definirati Task objekte i pohraniti ih u listu tasks, a zatim
koristiti asyncio.gather() za pokretanje svih korutina konkurentno.
"""

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f"{name}: {i} sekundi preostalo...")
        await asyncio.sleep(1)
    print(f"{name}: Vrijeme je isteklo!")
    
async def main():
    timers = [
        asyncio.create_task(timer("Timer 1", 3)),
        asyncio.create_task(timer("Timer 2", 5)),
        asyncio.create_task(timer("Timer 3", 7))
    ]
    
    await asyncio.gather(*timers)
    
asyncio.run(main())