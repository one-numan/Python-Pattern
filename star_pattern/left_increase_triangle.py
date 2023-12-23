'''
*
**
***
****
***
**
*

'''


def left_increasing_triangle(n: int) -> None:
    for row in range(1, n//2+1):
        for col in range(row):
            print('*', end='')
        print()

    for row in range(n//2+1, 0, -1):
        for col in range(row, 0, -1):
            if (col <= row):
                print('*', end='')
            else:
                print(' ', end='')
        print()


left_increasing_triangle(10)
