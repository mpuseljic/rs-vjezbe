# 9. UKLANJANJE DUPLIKATA IZ LISTE

def ukloni_duplikate(lista):
    return list(set(lista))

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))
    