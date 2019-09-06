import time
from math import sqrt
start = time.time()


def prime_number(n):
    """
    :param n: prime number next to n
    :return: return next prime number
    """
    n = n+1
    while True:
        for j in range(2, round(sqrt(n)+1)):
            if n % j == 0:
                n +=1
                break
        else:
            return n


print(prime_number(9007199254740991))
print('Time taken', time.time() - start)
