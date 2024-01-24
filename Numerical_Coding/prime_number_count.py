n = int(input())


def check_prime(n: int):
    for i in range(2, n):
        if n % 2 == 0:
            return False
    return True


def main(n):
    sum = 1
    if n <= 0:
        # print(0)
        return 0
    elif n == 1:
        # print(1)
        return sum

    for i in range(2, n):
        if check_prime(i):
            sum += i
    return sum


print(main(n))
