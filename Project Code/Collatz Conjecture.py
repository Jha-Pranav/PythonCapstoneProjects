def affinity_for_one():
    """
    This algorithm is applicable only for number greater then 1.
    """
    try:
        n = int(input('Enter the number : '))
        if n < 1:
            return 'Please input number greater then 1'
        step_count = 0
        while n != 1:
            if n % 2 == 0:
                step_count += 1
                n = n / 2
            else:
                step_count += 1
                n = n*3 + 1
        return step_count
    except (ValueError, TypeError):
        return 'Seems you have entered non-int value'


print(affinity_for_one())
