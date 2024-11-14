from shop.proizvodi import dodaj_proizvod, proizvodi as lista_proizvoda, Proizvod
from shop.narudzbe import napravi_narudzbu

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in proizvodi:
    dodaj_proizvod(Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"]))

print("PROIZVODI:")
for proizvod in lista_proizvoda:
    proizvod.ispis()


naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 1},  
]

narudzba = napravi_narudzbu(naruceni_proizvodi)
narudzba.ispis_narudzbe()

#for proizvod in lista_proizvoda:
#    proizvod.ispis()