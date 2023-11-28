import math


def compute_expression(x, a):
    if x <= -6 * a:
        return -(x + 3 * a) ** 2 - 2 * a
    else:
        return a * math.cos(x + 3 * a) - 3 * a


if __name__ == '__main__':
    print("**** Task 2 - Compute expression ***")
    print("Enter values (x, a): ")

    x = float(input("x = "))
    a = float(input("a = "))

    print("Result: {}".format(compute_expression(x, a)))
