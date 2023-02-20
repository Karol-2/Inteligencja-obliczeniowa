def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def select_primes(x):
    wynik = []
    for i in x:
        if prime(i):
            wynik.append(i)
    return wynik


print("zadanie 1a")

print(prime(3))
print(prime(4))
print(prime(49))

print("zadanie 1b")
print(select_primes([3, 6, 11, 25, 19]))
