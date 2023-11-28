import math


def triangle_with_sides_exists(a, b, c):
    return a + b > c and a + c > b and b + c > a


def calculate_triangle_space(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


if __name__ == '__main__':
    print("**** Triangle space calculation ***")
    print("Enter the values of the sides of the triangle")

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if triangle_with_sides_exists(a, b, c):
        space = calculate_triangle_space(a, b, c)
        print("The space of triangle with sizes a = {}, b = {}, c = {} equals to {}".format(a, b, c, space))
    else:
        print("Triangle with the provided sides does not exist.")
