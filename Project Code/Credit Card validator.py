def card_validator():
    card_no = str(input('Enter card number : '))
    no_list = []
    for i, n in enumerate(card_no):
        if i % 2 == 0:
            x = int(n) * 2
            if x > 9:
                x = __sum_of_digit(x)
            no_list.append(x)
        else:
            no_list.append(int(n))
    if sum(no_list) % 10 == 0 :
        print('validation completed.')
    else:
        print('Invalid card number.')


def __sum_of_digit(n):
    total = 0
    while n > 0:
        div = n % 10
        total += div
        n = n // 10
    return total


card_validator()

