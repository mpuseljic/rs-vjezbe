from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

app = FastAPI()

objave = []

class NovaObjava(BaseModel):
    korisnik: str = Field(..., max_length=20, title="Korisničko ime autora objave")
    tekst: str = Field(..., max_length=280, title="Tekst objave")

class Objava(NovaObjava):
    id: int
    vrijeme: datetime

@app.post("/objava", response_model=Objava)
def dodaj_objavu(nova_objava: NovaObjava):
    id_nove_objave = len(objave) + 1  
    nova = Objava(id=id_nove_objave, korisnik=nova_objava.korisnik, tekst=nova_objava.tekst, vrijeme=datetime.now())
    objave.append(nova)
    return nova

@app.get("/objava/{id}", response_model=Objava)
def dohvati_objavu(id: int):
    for objava in objave:
        if objava.id == id:
            return objava
    raise HTTPException(status_code=404, detail="Objava nije pronađena")

@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
def dohvati_objave_korisnika(korisnik: str):
    korisnikove_objave = [objava for objava in objave if objava.korisnik == korisnik]
    if not korisnikove_objave:
        raise HTTPException(status_code=404, detail="Korisnik nema objava")
    return korisnikove_objave
