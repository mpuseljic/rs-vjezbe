import hashlib
import asyncio
from aiohttp import web

korisnici = [
    {"korisnicko_ime": "admin", "lozinka_hash": 
     "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"},  # lozinka = "lozinka123"
    {"korisnicko_ime": "markoMaric", "lozinka_hash": 
     "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"},  # lozinka = "markoKralj123"
    {"korisnicko_ime": "ivanHorvat", "lozinka_hash": 
     "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"},  # lozinka = "lllllllllllozinka_123"
    {"korisnicko_ime": "Nada000", "lozinka_hash": 
     "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"}  # lozinka = "blablabla"
]

def hash_data(data: str) -> str:
    """Hashira string pomoću SHA-256 algoritma"""
    return hashlib.sha256(data.encode()).hexdigest()

async def register(request):
    """Ruta za registraciju korisnika"""
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    if not korisnicko_ime or not lozinka:
        return web.json_response({"error": "Nedostaju korisničko ime ili lozinka"}, status=400)

    if any(k["korisnicko_ime"] == korisnicko_ime for k in korisnici):
        return web.json_response({"error": "Korisnik već postoji"}, status=400)

    lozinka_hash = hash_data(lozinka)
    korisnici.append({"korisnicko_ime": korisnicko_ime, "lozinka_hash": lozinka_hash})
    return web.json_response({"message": "Korisnik uspješno registriran"}, status=201)

async def login(request):
    """Ruta za prijavu korisnika"""
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")

    if not korisnicko_ime or not lozinka:
        return web.json_response({"error": "Nedostaju korisničko ime ili lozinka"}, status=400)

    korisnik = next((k for k in korisnici if k["korisnicko_ime"] == korisnicko_ime), None)
    if not korisnik:
        return web.json_response({"error": "Korisnik ne postoji"}, status=404)

    if korisnik["lozinka_hash"] != hash_data(lozinka):
        return web.json_response({"error": "Neispravna lozinka"}, status=401)

    return web.json_response({"message": "Prijava uspješna"}, status=200)

app = web.Application()
app.router.add_post("/register", register)
app.router.add_post("/login", login)

web.run_app(app, host="0.0.0.0", port=9000)
