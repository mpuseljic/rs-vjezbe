
def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    broj_samoglasnika = 0
    broj_sulasnika = 0
    
    for slovo in tekst:
        if slovo in vowels:
            broj_samoglasnika += 1
        elif slovo in consonants:
            broj_sulasnika += 1
    return {'vowels:':broj_samoglasnika,"consonants":broj_sulasnika}

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))