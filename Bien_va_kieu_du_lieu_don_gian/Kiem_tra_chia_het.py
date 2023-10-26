def sieve_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

primes = sieve_eratosthenes(50)

while True:
    s = input()
    if s == '-1':
        break
    l, r = map(int, s.split())
    n = int(input())
    res = 0
    for i in range(l, r + 1, 2):
        is_prime = True
        for prime in primes:
            if prime > n:
                break
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            res += 1
    print(res)
