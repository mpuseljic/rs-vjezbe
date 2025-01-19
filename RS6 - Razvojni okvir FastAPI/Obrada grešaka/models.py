from pydantic import BaseModel

# 1. zadatak i 2. zadatak
class Automobil(BaseModel):
     id: int
     marka: str 
     model: str
     godina_proizvodnje: int
     cijena: float
     boja: str

# 3. zadatak
class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str

class CarRequest(BaseCar):
    pass

class CarResponse(BaseCar):
    id: int
    cijena_pdv: float