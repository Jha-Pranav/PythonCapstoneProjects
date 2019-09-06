import math


def sieve_of_eratosthenes(n):
    dummy_list = []
    for i in range(n):
        dummy_list.append(True)
    dummy_list[0] = False
    dummy_list[1] = False

    for j in range(2, round(math.sqrt(n)+1)):
        pointer = 2*j

        while pointer < n:
            dummy_list[pointer] = False
            pointer += j
    return len([u for u, v in enumerate(dummy_list) if v])


print(sieve_of_eratosthenes(100000))