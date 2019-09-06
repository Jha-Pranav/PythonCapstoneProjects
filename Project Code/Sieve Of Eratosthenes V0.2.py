def sieve_of_eratosthenes(limit):
    a = [True] * (limit+1)
    a[0] = a[1] = False
    for i, v in enumerate(a):
        if v:
            yield i
            for n in range(i*i, limit+1, i):
                a[n] = False


print(len(list(sieve_of_eratosthenes(100000))))
