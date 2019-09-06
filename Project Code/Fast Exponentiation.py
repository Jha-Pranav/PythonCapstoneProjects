##################################################################
# This assignment is incomplete need to work  again
##################################################################
import math
import time
# from decimal import Decimal
start = time.time()


def exponentiation(a, b):
    """
    Exponentiation by using logarithm
    """
    result = a
    f, i = math.modf(math.log2(b))
    f = 2 ** f
    print(i, f)
    for n in range(int(i)):
        result **= 2
        print(result)
    return result ** f


# print(exponentiation(3, 999999))
my_method = start - time.time()
print('My method :', time.time() - start)
# # print(pow(34567, 99999))
# # print('In-built method :', time.time() - my_method)
# # print(math.factorial(2999) ** 0.1)
# # print('My method :', time.time() - start)

#
# def bits_of(m):
#     """
#     Binary digits of n, from the least significant bit.
#
#     >>> list(bits_of(11))
#     [1, 1, 0, 1]
#     """
#     n=int(m)
#     while n:
#         yield n & 1
#         n >>= 1
#
# def fast_exp(x,n):
#     """
#     Compute x^n, using the binary expansion of n.
#     """
#     result = 1
#     partial = x
#
#     for bit in bits_of(n):
#         if bit:
#             result *= partial
#         partial **= 2
# return result
