from fastapi import FastAPI
from models import FilmResponse

app = FastAPI()

filmovi = [
{
"id": 1,
"naziv": "Titanic",
"genre": "drama",
"godina": 1997
},
{
"id": 2,
"naziv": "Inception",
"genre": "akcija",
"godina": 2010
}
]

@app.get("/filmovi", response_model=list[FilmResponse]) # povratna vrijednost je lista rječnika, sada konkretno validirana lista modela FilmResponse
def get_filmovi():
    return filmovi