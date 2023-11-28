import random
from lab3.task4 import sorted_by_direction

sorting_dict = {0: 'ascending', 1: 'descending'}

def update_if_sorted(current, sort_direction):
    if sorted_by_direction(current, sort_direction):
        return [i + current[i] for i in range(len(current))]
    else:
        return current


if __name__ == '__main__':
    print("**** Task 5 ***")
    N = 9
    size = N + 5
    values = [random.randint(0, 100) for i in range(size)]

    sort_key = input("Input sorted direction ({}) = ".format(", ".join(sorting_dict.values())))

    print("List  : {}".format(values))
    print("Does list sorted in the {} order: {}".format(sort_key, sorted_by_direction(values, sort_key)))
    print("Final list result: {}".format(update_if_sorted(values, sort_key)))
