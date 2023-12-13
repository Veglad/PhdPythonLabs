import itertools

if __name__ == '__main__':
    a = [(1, 'a'), (2, 'a'), (3, 'b'), (4, 'b'), (5, 'c')]
    b = itertools.groupby(a, lambda it: it[1])
    for key, value in b:
        print(key, list(value))

