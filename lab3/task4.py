import random

sorting_dict = {0: 'ascending', 1: 'descending'}

def sorted_by_direction(current, sort_direction):
    should_be_reversed = bool(list(sorting_dict.keys())[list(sorting_dict.values()).index(sort_direction)])
    expected = sorted(current, reverse=should_be_reversed)
    return expected == current


if __name__ == '__main__':
    print("**** Task 4 - Check if sorted ***")
    N = 9
    size = N + 5
    values = [random.randint(0, 100) for i in range(size)]

    sort_key = input("Input sorted direction ({}) = ".format(", ".join(sorting_dict.values())))

    print("List  : {}".format(values))
    print("Does list sorted in the {} order: {}".format(sort_key, sorted_by_direction(values, sort_key)))
