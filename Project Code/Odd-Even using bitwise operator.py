import time
start = time.time()
def odd_even(n):
    if n % 2 != 0:
        return f'The number {n} is odd number.'
    else:
        return f'The number {n} is even number.'


for i in range(10000000):
    odd_even(i)
print(time.time()-start)