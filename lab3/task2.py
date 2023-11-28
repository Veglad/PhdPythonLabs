from functools import reduce


def compute_expression(a1, t, q):
    progression_list = list(range(a1, a1 + t * q, t))
    return reduce(lambda x, y: x * y, progression_list)


if __name__ == '__main__':
    print("**** Task 2 - Arithmetic progression multiplication ***")
    print("Enter values (a(1), t, q): ")

    a1 = int(input("a(1) = "))
    t = int(input("t = "))
    q = int(input("q = "))

    print("Result: {}".format(compute_expression(a1, t, q)))
