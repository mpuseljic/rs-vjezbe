# NAPIŠITE KORESPONDIRAJUĆE LAMBDA IZRAZE ZA SLJEDEĆE FUNKCIJE:

# 1. Kvadriranje broja:
def kvadriraj(x):
    return x ** 2

# print(kvadriraj(5))

# RJEŠENJE:
print((lambda x: x ** 2)(5))


# 2. Zbroji pa kvadriraj:
def zbroji_pa_kvadriraj(a, b):
    return (a + b) ** 2

# print(zbroji_pa_kvadriraj(2,2))

#RJEŠENJE:
print((lambda x, y: (x+y) ** 2)(2,2))

# 3. Kvadriraj duljinu niza:
def kvadriraj_duljinu(niz):
    return len(niz) ** 2

# print(kvadriraj_duljinu("Pozdrav"))

#RJEŠENJE:
print((lambda niz: len(niz) ** 2)("Pozdrav"))

# 4. Pomnoži vrijednost s 5 pa potenciraj na x:
def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x

# print(pomnozi_i_potenciraj(2,2))

#RJEŠENJE:
print((lambda x,y:(y * 5) ** x)(2,2))

# 5. Vrati True ako je broj paran, inače vrati None:
def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return None

#print(paran_broj(4))

# RJEŠENJE
paran_neparan = lambda x: True if x % 2 == 0 else None
print(paran_neparan(4)) 
print(paran_neparan(5)) 
