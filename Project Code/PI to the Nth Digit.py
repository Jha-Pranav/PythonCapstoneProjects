# Monte Carlo estimation
from random import randint


def pi():
    """
    input : Takes the no of digit after decimal place.An integer.
    return : The estimated value of pi
    """
    try:
        precision = int(input('Enter the number of decimal places : '))
    except ValueError:
        print("The enter digit don't seems to be integer.")
        return 'The operation has been terminated'
    else:
        return f'The estimation value of pi by Monte Carlo method is : {_avg_val():.{precision}f}'


def _estimating_pi(loop):
    """
    :param loop: Total no. of points
    :return: The value of pi for one instance
    """

    radius = randint(500, 1000)
    total_point_inside_circle = 0
    # probability of point inside the circle equals pi/4 == point_inside_circle/total pint
    for i in range(loop):
        x = randint(-radius, radius)
        y = randint(-radius, radius)
        is_point_inside_circle = (x**2)+(y**2) <= radius**2
        if is_point_inside_circle:
            total_point_inside_circle += 1

    return 4 * (total_point_inside_circle/loop)


def _iterating(no_of_iteration):
    for i in range(no_of_iteration):
        yield _estimating_pi(randint(500, 10000))


def _avg_val():
    no_of_iteration = randint(10, 100)
    total_sum = sum(_iterating(no_of_iteration))
    return total_sum / no_of_iteration


print(pi())
