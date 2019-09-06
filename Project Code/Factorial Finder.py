# Factorial by using loop
def factorial(n):
    """
    simple function function to calculate factorial of a number by using loop
    """
    if n < 0:
        print("This function don't support factorial of negative number. Google Gama function for more details")
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    print(fact)


factorial(999)