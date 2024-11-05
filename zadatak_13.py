# 13. FUNKCIJA KOJA VRAĆA N-TORKU S PRVIM I ZADNJIM ELEMENTOM LISTE U JEDNOJ LINIJI KODA

def prvi_i_zadnji(lista):
    return (lista[0],lista[-1])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prvi_i_zadnji(lista)) 

# Funkcija koja n-torku s maksimalnim i minimalnim elementom liste, bez korištenja ugrađenih funkcija max() i min().
def maks_i_min(lista):
    return (max(lista), min(lista))

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))

# Funkcija presjek koja prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa.

def presjek(skup_1, skup_2):
    return skup_1.intersection(skup_2)

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2)) # {4, 5}

