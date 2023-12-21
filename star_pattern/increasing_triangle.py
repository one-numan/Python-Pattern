def increasing_triangle(n: int) -> None:
    for col in range(n):
        for row in range(col):
            print('*', end='')
        print()


increasing_triangle(10)
