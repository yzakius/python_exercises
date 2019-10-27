def a_very_big_sum(ar):
    big_sum = 0
    for i in ar:
        big_sum += i
    return big_sum


if __name__ == '__main__':
    ar_count = int(input(5))
    ar = list(map(int, input(ar_count).rstrip().split()))
    print(ar)
    print(a_very_big_sum(ar))
