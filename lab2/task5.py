import math

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

if __name__ == '__main__':
    print("**** Task 5 - Factorial of 14 ***")
    print("Factorial of 14 = {}".format(factorial(14)))
    print("Factorial of 14 = {} [System function]".format(math.factorial(14)))
