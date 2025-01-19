from fastapi import FastAPI
from routers.filmovi import router as filmovi_router

app = FastAPI()

app.include_router(filmovi_router)

@app.get("/")
def home():
    return {"poruka": "Dobrodošli na FastAPI poslužitelj"}