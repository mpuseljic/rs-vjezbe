
def isPrime(broj):
    if broj <= 1:
        return False
    for i in range(2, (broj // 2)+1):
        if broj % i == 0:
            return False
    return True
    
print(isPrime(7)) 
print(isPrime(10)) 

def primes_in_range(start, end):
    prosti = []
    for i in range(start, end + 1):
        if isPrime(i):
            prosti.append(i)
    return prosti

print(primes_in_range(1, 10)) 