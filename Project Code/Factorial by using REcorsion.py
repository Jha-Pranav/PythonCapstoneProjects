def factorial(n):
    """
    simple function to calculate factorial by using recursion technique.
    It has a limitation : it can calculate till some limit depending upon the version or hardware configuration
    for me it's 998.
    """
    fact = 1
    if n > 1:
        fact = n * factorial(n-1)
    return fact


try:
    print(factorial(999))
except RecursionError:
    print("Can't calculate factorial of large number by using this method")