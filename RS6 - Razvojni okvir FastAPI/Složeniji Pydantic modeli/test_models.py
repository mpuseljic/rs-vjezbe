from models import Izdavac, Knjiga, Admin, RestaurantOrder, CCTV_frame
from datetime import datetime

# 1. zadatak
izdavac = Izdavac(naziv="Školska knjiga", adresa="Ulica 1")
knjiga = Knjiga(
    naslov="Knjiga Test",
    ime_autora="Ivo",
    prezime_autora="Ivić",
    broj_stranica=300,
    izdavac=izdavac
)
print(knjiga)


# 2.zadatak
admin = Admin(
    ime="Marko",
    prezime="Marić",
    korisnicko_ime="mmaric",
    email="marko.maric@gmail.com",
    ovlasti=["dodavanje", "brisanje"]
)
print(admin)

# 3.zadatak
narudzba = RestaurantOrder(
    identifikator=1,
    ime_kupca="Ivan Ivić",
    stol_info={"broj": 5, "lokacija": "restoran"},
    lista_jela=[
        {"identifikator": 1, "naziv": "Hamburger", "cijena": 9.0},
        {"identifikator": 2, "naziv": "Pizza", "cijena": 10.0}
    ],
    ukupna_cijena=19.0
)
print(narudzba)

# 4. zadatak
frame = CCTV_frame(
    identifikator=1,
    vrijeme_snimanja=datetime.now(),
    koordinate=(25.6753, 15.9819)
)
print(frame)