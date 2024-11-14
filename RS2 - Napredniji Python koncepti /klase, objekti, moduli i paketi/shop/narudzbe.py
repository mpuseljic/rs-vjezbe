from shop.proizvodi import Proizvod, proizvodi  

class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena
    
    def ispis_narudzbe(self):
        svi_proizvodi = ", ".join([f"{p['naziv']} x {p['kolicina']}" for p in self.proizvodi])
        print(f"Naručeni proizvodi: {svi_proizvodi}, Ukupna cijena: {self.ukupna_cijena} EUR")

def napravi_narudzbu(proizvodi_lista):
    if len(proizvodi_lista) == 0:
        print("Lista ne smije biti prazna!")
        return None

    for proizvod in proizvodi_lista:
        if not("naziv" in proizvod and "cijena" in proizvod and "kolicina" in proizvod):
            print("Svaki rječnik mora sadržavati ključeve: naziv, cijena i kolicina.")
            return None

    ukupna_cijena = 0
    narudzbe = []

    for proizvod in proizvodi_lista:
        dostupan_proizvod = None
        for p in proizvodi:
            if p.naziv == proizvod['naziv']: 
                dostupan_proizvod = p
                break

        if dostupan_proizvod is None:
            print(f"Proizvod {proizvod['naziv']} nije dostupan!")
            return None 

        dostupan_proizvod.kolicina -= proizvod['kolicina']
        
        narudzbe.append(proizvod)
        ukupna_cijena += proizvod["cijena"] * proizvod["kolicina"]

    return Narudzba(narudzbe, ukupna_cijena)
