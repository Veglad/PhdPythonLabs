from dataclasses import dataclass


def test():
    print("before 1")
    yield 1
    print("after 1")
    yield 2

if __name__ == '__main__':
    for res in test():
        print("printing res: ", res)

