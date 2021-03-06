#素因数分解
a = []
def prime_factorize(n):
    global a
    while n % 2 == 0:
        a.append(2)
        n //= 2
    
    f = 3
    while f*f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    
    if n != 1:
        a.append(n)
    
    return n

N = int(input())
print(prime_factorize(N))
