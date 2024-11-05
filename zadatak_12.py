# 12. OBRNUTI RJEČNIK

def obrni_rjecnik(rjecnik):
    obrnuti_rjecnik = {}
    
    for ključ, vrijednost in rjecnik.items():
        obrnuti_rjecnik[vrijednost] = ključ
    return obrnuti_rjecnik

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
print(obrni_rjecnik(rjecnik))