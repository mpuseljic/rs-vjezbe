# 3. POGAĐANJE BROJA SVE DOK NIJE POGOĐEN

tajni_broj = 28
broj_je_pogoden = False
brojač = 0

while not broj_je_pogoden:
    broj = int(input("Pogodi broj u rasponu od 1 do 100: "))
    brojač += 1
    
    if broj < tajni_broj:
        print("Tvoj broj je manji od zamišljenog broja.")
    elif broj > tajni_broj:
        print("Tvoj broj je veći od zamišljenog broja.")
    else:
        broj_je_pogoden = True
        print("Bravo, pogodio si u ", brojač, "pokušaja.")
     
    
