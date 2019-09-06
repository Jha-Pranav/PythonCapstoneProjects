import time
from math import sqrt
start = time.time()


def prime_number(n):
    """
    :param n: prime number between 0 to n; both inclusive
    :return: return list of all prime number till upper limit n.
    """
    yield 2
    for i in range(2, n+1):
        if i % 2 != 0:
            for j in range(2, round(sqrt(i)+1)):
                if i % j == 0:
                    break
            else:
                yield i


def prime_factorial(m):
    """
    :param m: Prime factor of number m.
    :return: return unique prime factor of m as a list.
    """

    prime = tuple(prime_number(m))
    if m in prime:
        return f'{m} is a prime number'
    factor_list = []
    d = m
    for factor in prime:
        while d % factor == 0:
            factor_list.append(factor)
            d = int(d / factor)
    return factor_list


print(prime_factorial(9007))
print('Time taken', time.time() - start)
