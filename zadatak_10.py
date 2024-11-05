# 10. BROJANJE RIJEČI U TEKSTU

def brojanje_riječi(tekst):
    broj_riječi = dict()
    
    riječi = tekst.split()
    
    for riječ in riječi:
        if riječ in broj_riječi:
            broj_riječi[riječ] += 1
        else:
            broj_riječi[riječ] = 1
    return broj_riječi

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(brojanje_riječi(tekst))