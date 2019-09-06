# Calculating the value of Euler’s Number e :
# e = (1 + (1/n)) ** n
from random import randint


def e():
    """
    input : Takes the integer.
    return: Return the value of e.
    """
    total = 0
    no_of_iteration = randint(500, 1000)
    for i in range(no_of_iteration):
        n = randint(10000, 100000)
        total += (1 + (1/n)) ** n
    try:
        precision = int(input('Enter the no of decimal places : '))
    except ValueError:
        print("The entry don't seems to be integer.")
        return 'The operation has been terminated.'
    else:
        return f'The value of e is : {total/no_of_iteration:.{precision}f}'


print(e())
