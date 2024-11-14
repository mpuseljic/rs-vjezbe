# 5. NAPIŠITE PROGRAM KOJI ĆE IZRAČUNATI FAKTORIJEL BROJA

# FOR PETLJA
a = int(input("Unesi broj: "))

faktorijel = 1

for i in range(a, 0, -1):
    faktorijel *= i

print("Faktorijel je: ", faktorijel)

# WHILE PETLJA
broj = int(input("Unesi broj: "))
fact = 1

while broj >= 1:
    fact *= broj
    broj -= 1
print("Faktorijel je: ", fact )