def happy_number(n):
    visited = []
    while n not in visited:
        visited.append(n)
        n = square_sum(n)
        if n == 1:
            return True
            break
    else:
        return False


def square_sum(m):
    total = 0
    while m > 0:
        div = m % 10
        total += div ** 2
        m = m//10
    return total


x = map(happy_number, range(100))
happy = []
for i, n in enumerate(x):
    if n:
        happy.append(i)
print(happy)
