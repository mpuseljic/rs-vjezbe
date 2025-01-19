from pydantic import BaseModel
from typing import Optional, List, Literal, TypedDict
from datetime import datetime


class FilmResponse(BaseModel):
    id: int
    naziv: str
    genre: str
    godina: int
    

# 1. zadatak
class Izdavac(BaseModel):
    naziv: str
    adresa: str
    
class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: Optional[int] = datetime.now().year
    broj_stranica: int
    izdavac: Izdavac
    
# 2.zadatak
class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: List[Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]] = []
    
# 3. zadatak
class Jelo(BaseModel):
    identifikator: int
    naziv:str
    cijena: float
    
class StolInfo(TypedDict):
    broj: int
    lokacija: str
    
class RestaurantOrder(BaseModel):
    identifikator: int
    ime_kupca: str
    stol_info: StolInfo
    lista_jela: List[Jelo]
    ukupna_cijena: float

#4. zadatak
class CCTV_frame(BaseModel):
    identifikator: int
    vrijeme_snimanja: datetime
    koordinate: Optional[tuple[float, float]] = (0.0, 0.0)