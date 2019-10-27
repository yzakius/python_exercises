"""
output: 31
"""


def simple_array_sum(ar):
    array_sum = 0
    for i in ar:
        array_sum += i
    return array_sum


if __name__ == '__main__':
    ar = [1, 2, 3, 4, 10, 11]
    print(simple_array_sum(ar))
