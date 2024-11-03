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