from fastapi import APIRouter, Query, HTTPException
import json
from models.filmovi import Film
from typing import Optional, Literal

router = APIRouter(prefix="/filmovi")

with open("film.json", "r") as f:
    films_data = json.load(f)

filmovi = [Film(**film) for film in films_data]

@router.get("/") 
def dohvati_sve_filmove(
    min_year: int = Query(1900, ge=1900),
    max_year: int = Query(2025, ge=1900),
    min_rating: float = Query(0.0, ge=0, le=10),
    max_rating: float = Query(10.0, ge=0, le=10),
    type: Optional[Literal["movie", "series"]] = None
):
    filtrirani_filmovi = filmovi

    if min_year:
        filtrirani_filmovi = [film for film in filtrirani_filmovi if film.Year >= min_year]
    if max_year:
        filtrirani_filmovi = [film for film in filtrirani_filmovi if film.Year <= max_year]

    if min_rating:
        filtrirani_filmovi = [
            film for film in filtrirani_filmovi
            if film.imdbRating is not None and film.imdbRating >= min_rating
        ]
    if max_rating:
        filtrirani_filmovi = [
            film for film in filtrirani_filmovi
            if film.imdbRating is not None and film.imdbRating <= max_rating
        ]

    if type:
        filtrirani_filmovi = [film for film in filtrirani_filmovi if film.Type == type]

    return filtrirani_filmovi


@router.get("/{imdbID}", response_model=Film)
def dohvati_film_po_imdbID(imdbID: str):
    for film in filmovi:
        if film.imdbID == imdbID:
            return film
    raise HTTPException(status_code=404, detail=f"Film s imdbID-om {imdbID} nije pronađen")

@router.get("/title/{title}", response_model=Film)
def dohvati_film_po_naslovu(title: str):
    for film in filmovi:
        if film.Title.lower() == title.lower():
            return film
    raise HTTPException(status_code=404, detail=f"Film s naslovom {title} nije pronađen")