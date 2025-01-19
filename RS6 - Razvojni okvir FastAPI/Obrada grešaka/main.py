from fastapi import FastAPI, HTTPException, Query
from models import Automobil, CarRequest, CarResponse


app = FastAPI()

automobili = [
    {"id": 1, "marka": "Marka 1", "model": "Model 1", "godina_proizvodnje": 2020, "cijena": 30000, "boja": "crvena"},
    {"id": 2, "marka": "Marka 2", "model": "Model 2", "godina_proizvodnje": 2021, "cijena": 50000, "boja": "plava"},
]

# 1. zadatak
@app.get("/automobili/{id}", response_model=Automobil)
def dohvati_automobil(id: int):
    for auto in automobili:
        if auto["id"] == id:
            return auto
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")

# 2. zadatak
@app.get("/automobili", response_model=list[Automobil])
def dohvati_automobile(
    min_cijena: float = Query(0, ge=1), 
    max_cijena: float = Query(1_000_000, ge=1), 
    min_godina: int = Query(1960, ge=1960), 
    max_godina: int = Query(2025, ge=1960)
):
    if min_cijena > max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena mora biti manja od maksimalne cijene")
    if min_godina > max_godina:
        raise HTTPException(status_code=400, detail="Minimalna godina mora biti manja od maksimalne godine")
    
    filtrirani_automobili = [
        auto for auto in automobili
        if min_cijena <= auto["cijena"] <= max_cijena and min_godina <= auto["godina_proizvodnje"] <= max_godina
    ]
    return filtrirani_automobili

# 3. zadatak
@app.post("/automobili", response_model=CarResponse)
def dodaj_automobil(automobil: CarRequest):
    for auto in automobili:
        if auto["marka"] == automobil.marka and auto["model"] == automobil.model:
            raise HTTPException(status_code=400, detail="Automobil već postoji")

    novi_id = automobili[-1]["id"] + 1 if automobili else 1
    cijena_pdv = automobil.cijena * 1.25

    novi_auto = CarResponse(
        id=novi_id,
        cijena_pdv=cijena_pdv,
        **automobil.dict()
    )
    automobili.append(novi_auto.dict())
    return novi_auto