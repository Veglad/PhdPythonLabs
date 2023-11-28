import  random

if __name__ == '__main__':
    print("**** Task 3 - Swap 1st and last elements ***")
    LIST_SIZE = 19
    print("List size = {}", LIST_SIZE )

    lst = [random.randint(-100, 100) for _ in range(LIST_SIZE)]

    print("List before: {}".format(lst))
    lst[0], lst[-1] = lst[-1], lst[0]
    print("List after: {}".format(lst))
