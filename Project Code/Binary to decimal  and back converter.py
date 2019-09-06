def binary_to_decimal(num):
    """
    simply convert binary to decimal
    """
    try:
        return f'Binary : {num}, Decimal : {int(num, 2)}'
    except TypeError:
        return "integer can't be converted as non-string with explicit base"
    except ValueError:
        return "This is not a valid binary"


def decimal_to_binary(num):
    """
    simply convert decimal to binary
    """
    try:
        return f'Number : {num}, Binary : {bin(int(num))}'
    except TypeError:
        return "string cannot be interpreted as an integer"


print(decimal_to_binary(8990999))
print(binary_to_decimal('0b100010010011000100010111'))

