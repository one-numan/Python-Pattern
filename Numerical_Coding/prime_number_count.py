# n = int(input())


def check_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main(n):
    count_prime = 0
    if n <= 1:
        # print(0)
        return 0

    for i in range(2, n):
        if check_prime(i):
            # print(F"Prime Number {i}")
            count_prime += 1
    return count_prime


for i in range(100):
    print(i, main(i))
