import math

def polysum(n, s):
    '''
    n: positive int; number of sides
    s: positive int; side length
    Returns: positive int; the sum of the area and the square of the perimeter rounded to 4 decimal places.
    '''
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    square_perimeter = (n * s) ** 2
    result = area + square_perimeter
    return round(result, 4)
