
def provjera_lozinke(lozinka):
    if (len(lozinka) < 8 or len(lozinka) > 15):
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return
    
    veliko_slovo = False
    broj = False
    for znak in lozinka:
        if znak.isupper():
            veliko_slovo = True
        if znak.isdigit():
            broj = True
        
    if not veliko_slovo or not broj:
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return
    elif "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return

    print("Lozinka je jaka")

lozinka = input("Unesi lozinku: ")
provjera_lozinke(lozinka)