import math

if __name__ == '__main__':
    print("**** arithmetic expression calculation ***")
    print("Enter values: ")

    a = float(input("a = "))
    x = float(input("x = "))
    beta = float(input("β = "))

    result = (math.sin(math.pi - beta / 2) + math.log10(2 * x + a * a) + x * x + abs(x - a ** 3) ** (1 / 4)) / \
             (math.e ** (x + a) + x ** 3 + 5.4 * 10 ** (-4) + math.tan(x * x + 0.5 * (10 ** 2.1)))

    print("Result is: {}".format(result))
