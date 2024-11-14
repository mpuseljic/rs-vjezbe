# 8. FILTRIRANJE PARNIH IZ LISTE 

def filtriraj_parne(lista):
    nova_lista = []
    for element in lista:
        if element % 2 == 0:
            nova_lista.append(element)
    return nova_lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista))
            