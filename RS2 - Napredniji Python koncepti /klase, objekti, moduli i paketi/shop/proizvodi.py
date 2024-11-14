class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina    
    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Kolicina: {self.kolicina}")
        
proizvodi = []
proizvodi.append(Proizvod("Mlijeko", 2, 5))
proizvodi.append(Proizvod("Kruh", 1.50, 2))

def dodaj_proizvod(novi):
    proizvodi.append(novi)