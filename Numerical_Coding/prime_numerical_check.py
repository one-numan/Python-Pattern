def check_prime(n: int):
    if n == 0:
        return False
    if n in [1, 2]:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# for i in range(100):
    # print(i, check_prime(i))


n = int(input('Enter The Number : '))
if check_prime(n):
    print(f"Its Prime Number : {n}")
else:
    print(f'Its Not A Prime Number : {n}')
