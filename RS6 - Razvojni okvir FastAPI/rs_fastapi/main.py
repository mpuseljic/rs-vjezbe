from fastapi import FastAPI
from models import Film, CreateFilm

app = FastAPI()

filmovi = [
{"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
{"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
{"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
{"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]


# 1. zadatak
@app.get("/filmovi")
def get_filmovi(): 
    return filmovi

# 2. zadatak
@app.get("/filmovi")
def get_filmovi():
    return [Film(**film).model_dump() for film in filmovi]

# 3. zadatak
@app.get("/filmovi/{id}")
def get_film_by_id(id: int):
    film = next((film for film in filmovi if film["id"] == id), None)
    if film:
        return Film(**film).model_dump()
 
# 4. zadatak
@app.post("/filmovi")
def add_film(film: CreateFilm):
    new_id = len(filmovi) + 1 
    film_s_id = Film(id=new_id, naziv=film.naziv, genre=film.genre, godina=film.godina) 
    return film_s_id

# 5. zadatak
@app.get("/filmovi") 
def get_filmovi_by_query(genre: str = None, min_godina: int = 2000):
    pronadeni_filmovi = [
        film for film in filmovi
        if (genre is None or film["genre"] == genre) and film["godina"] >= min_godina
    ]
    return pronadeni_filmovi




