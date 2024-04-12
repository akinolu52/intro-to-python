"""
    A program to print prime numbers between a range of numbers.
"""


def is_prime(val):
    if val < 2:
        return False
    else:
        for i in range(2, int(val ** 0.5) + 1):
            if val % i == 0:
                return False
        return True


def get_prime(start_index, end_index):
    for i in range(start_index, end_index):
        if is_prime(i):
            print(i)


if __name__ == '__main__':
    start = 1
    end = 30

    get_prime(start, end)
