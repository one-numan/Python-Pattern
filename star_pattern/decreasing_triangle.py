def decreasing_triangle(n: int) -> None:
    for col in range(n):
        for row in range(n-col, 0, -1):
            print("*", end='')
        print()


decreasing_triangle(10)
