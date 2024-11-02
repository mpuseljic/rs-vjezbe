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


