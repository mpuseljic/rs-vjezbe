from pydantic import BaseModel, Field, HttpUrl, validator
from typing import List, Optional, Literal


class Actor(BaseModel):
    name: str
    surname: str


class Writer(BaseModel):
    name: str
    surname: str

"""
odajte provjere za sljedeće atribute filma unutar Pydantic modela za film:
Images mora biti lista stringova (javnih poveznica na slike)
type mora biti odabir između "movie" i "series"
Obavezni atributi su: Title, Year, Rated, Runtime, Genre, Language, Country, Actors,
Plot, Writer
Ostali atributi su neobavezni, a ako nisu navedeni, postavite im zadanu vrijednost
Dodajte validacije za Year i Runtime atribut (godina mora biti veća od 1900, a trajanje filma mora
biti veće od 0)
Dodajte validacije za imdbRating i imdbVotes (ocjena mora biti između 0 i 10, a broj glasova
mora biti veći od 0)

"""

class Film(BaseModel):
    Title: str
    Year: int = Field(..., ge=1900, description="godina mora biti veća od 1900")
    Rated: str
    Released: str
    Runtime: Optional[int] = Field(None, gt=0, description="trajanje filma mora biti veće od 0")
    Genre: str
    Director: Optional[str]
    Writer: List[str]  
    Actors: List[str]  
    Plot: str
    Language: str
    Country: str
    Awards: Optional[str]
    Poster: Optional[HttpUrl]
    Metascore: Optional[str]
    imdbRating: Optional[float] = Field(None, ge=0, le=10, description="ocjena mora biti između 0 i 10")
    imdbVotes: Optional[int] = Field(None, gt=0, description="broj glasova mora biti veći od 0")
    imdbID: str
    Type: Literal["movie", "series"]
    Response: Optional[str]
    Images: List[HttpUrl]

    @validator("Year", pre=True)
    def validacija_godine(cls, value):
        if isinstance(value, str):
            parsed = "".join(filter(str.isdigit, value.split("–")[0]))
            if parsed.isdigit():
                return int(parsed)
        raise ValueError(f"Neispravan format godine: {value}")

    @validator("Runtime", pre=True, always=True)
    def validacija_runtime(cls, value):
        if isinstance(value, str) and value != "N/A":
            return int(value.split(" ")[0])
        return None  

    @validator("imdbRating", pre=True, always=True)
    def validacija_rating(cls, value):
        if isinstance(value, str) and value != "N/A":
            return float(value)
        return None  

    @validator("imdbVotes", pre=True, always=True)
    def validacija_votes(cls, value):
        if isinstance(value, str) and value != "N/A":
            return int(value.replace(",", ""))
        return None  

    @validator("Actors", pre=True)
    def validacija_actors(cls, value):
        return [actor.strip() for actor in value.split(",")]

    @validator("Writer", pre=True)
    def validacija_writers(cls, value):
        return [writer.strip() for writer in value.split(",")]
