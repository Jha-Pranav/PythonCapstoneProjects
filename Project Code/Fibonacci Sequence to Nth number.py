def fibonacci_sequence(n):
    """
    :param n: Takes integer value.
    :return: iterable series of fibonacci sequence
    """
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a+b


try:
    r = int(input('Enter the limit of fibonacci sequence : '))
except ValueError:
    print("This limit can't be non-integer.")
else:
    sequence_list = []
    for num in fibonacci_sequence(r):
        sequence_list.append(num)
finally:
    try:
        print(sequence_list)
    except NameError:
        print('The program has been terminated.')


