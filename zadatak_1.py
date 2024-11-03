# 1. JEDNOSTAVNI KALKULATOR
a = float(input("Unesi prvi broj: "))
b = float(input("Unesi drugi broj: "))

operator = input("Unesi operator (+, -, *, /)")

if operator == '+':
    print("Rezultat operacije ",a, "+", b , " je ", a +b )
elif operator == '-':
    print("Rezultat operacije ", a, "-", b, " je ", a - b)
elif operator == '*':
    print("Rezultat operacije ", a, "*", b, " je ", a * b)
elif operator == '/':
    if b == 0:
        print("Dijeljenje s nulom nije dopušteno!")
    else:
        print("Rezultat operacije ", a, "/", b, " je ", a / b)
else:
    print("Nepodržani operator!")
    
    