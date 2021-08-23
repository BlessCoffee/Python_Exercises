def polysum(n,s):
    """
    n = number of sides
    s = length of each side

    This function should sum the area and square of the
    perimeter of the regular polygon. The function returns the sum,
    rounded to 4 decimal places.
    """

    import math

    area = (0.25*n*s*s)/math.tan(math.pi/n)
    peri = n*s
    sum = round(area + peri**2, 4)
    return sum

x = polysum(10,12)
print(x)
