def compute_expression(a1, alim, t):
    current = a1
    items = []
    while current > alim:
        items.append(current)
        current *= t

    return sum(items)

if __name__ == '__main__':
    print("**** Task 3 - Geometric progression ***")
    print("Enter values (a(1), alim, t): ")

    a1 = float(input("a(1) = "))
    alim = float(input("alim = "))
    t = float(input("t = "))

    print("Result: {}".format(compute_expression(a1, alim, t)))
