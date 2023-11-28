def sum_of_ones_from_binary_representation(n):
    binary_string = bin(n)
    return len(list(filter(lambda char: char == '1', list(binary_string))))

if __name__ == '__main__':
    print("**** Task 1 - Calculate sum of ones for a binary number ***")
    N = 9
    print("Initial number N = {}".format(N))
    print("Result - {}".format(sum_of_ones_from_binary_representation(N)))

