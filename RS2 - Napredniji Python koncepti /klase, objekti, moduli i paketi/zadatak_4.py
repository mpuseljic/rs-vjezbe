# ZADATAK 4: KLASE I OBJEKTI
"""
1. Definirajte klasu Automobil s atributima marka, model, godina_proizvodnje i kilometraža.
Dodajte metodu ispis koja će ispisivati sve atribute automobila.
- Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis.
- Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
godine dohvatite pomoću datetime modula.
"""
import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizovdnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizovdnje
        self.kilometraza = kilometraza
        
    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraza: {self.kilometraza}")
        
    def starost(self):
        trenutna_godina = datetime.datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost} godina.")
        
automobil = Automobil("Marka1", "Model1", 2020, 30000)

automobil.ispis()

automobil.starost()
        
"""
2. Definirajte klasu Kalkulator s atributima a i b. Dodajte metode zbroj, oduzimanje, mnozenje,
dijeljenje, potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
b.
"""
import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        return self.a / self.b
    
    def potenciranje(self):
        return self.a ** self.b
        
    def korijen(self):
        return math.sqrt(self.a)
    
kalkulator = Kalkulator(2, 2)

print("Zbroj:", kalkulator.zbroj())          
print("Oduzimanje:", kalkulator.oduzimanje())  
print("Množenje:", kalkulator.mnozenje())     
print("Dijeljenje:", kalkulator.dijeljenje())  
print("Potenciranje:", kalkulator.potenciranje())  
print("Korijen:", kalkulator.korijen()) 
    

"""
3. Definirajte klasu Student s atributima ime, prezime, godine i ocjene.
Iterirajte kroz sljedeću listu studenata i za svakog studenta stvorite objekt klase Student i dodajte ga u
novu listu studenti_objekti:
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
- Dodajte metodu prosjek koja će računati prosječnu ocjenu studenta.
- U varijablu najbolji_student pohranite studenta s najvećim prosjekom ocjena iz liste
    studenti_objekti. Implementirajte u jednoj liniji koda.
"""

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    
    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
    
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [
    Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti
]

najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())

print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime}, Prosjek: {najbolji_student.prosjek()}")

"""
4. Definirajte klasu Krug s atributom r. Dodajte metode opseg i povrsina koje će računati opseg i
površinu kruga.
Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.
"""


class Krug:
    def __init__(self, r):
        self.r = r
        
    def opseg(self):
        return 2 * math.pi * self.r
    
    def povrsina(self):
        return math.pi * self.r ** 2
    
krug = Krug(2)

print(f"Površina: {krug.povrsina()}")
print(f"Opseg: {krug.opseg()}")

"""
5. Definirajte klasu Radnik s atributima ime, pozicija, placa. Dodajte metodu work koja će ispisivati
"Radim na poziciji {pozicija}".
-Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department. Dodajte
    metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
- U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
    povećava plaću radnika ( Radnik) za iznos povecanje.
- Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i
    give_raise.
"""
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
        
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")
        
class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
        
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
        
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Povećana plaća u iznosu od {povecanje} radniku {radnik.ime}")
        
radnik = Radnik("Ivan", "Web developer", 1000)

manager = Manager("Marko", "Menadžer", 5000, "IT")

radnik.work()
manager.work()
manager.give_raise(radnik, 500)

        


        