def right_increase_triangle(n: int) -> None:
    for col in range(n):
        for row in range(0, n-col):
            if row >= col:
                print(" ", end='')
            else:
                print("*", end='')
        print()


right_increase_triangle(10)
