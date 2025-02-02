from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
import aiohttp
import asyncio

app = FastAPI()

objave = []

class KorisnikLogin(BaseModel):
    korisnicko_ime: str
    lozinka: str

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

@app.post("/korisnici/objave", response_model=List[Objava])
async def dohvati_objave_korisnika(cred: KorisnikLogin):
    
    async with aiohttp.ClientSession() as session:
        async with session.post("http://authAPI:5000/login", json=cred.dict()) as response:
            if response.status == 200:
                return [objava for objava in objave if objava.korisnik == cred.korisnicko_ime]
    
    raise HTTPException(status_code=401, detail="Neispravni korisnički podaci")
