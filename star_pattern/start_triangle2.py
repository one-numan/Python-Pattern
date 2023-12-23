'''
    *
   ***
  *****
 *******
*********
'''


def star_trangle2(n: int) -> None:
    space = 0
    for row in range(0, n):
        for col in range(1, n+row+1):
            if (col >= n-row):
                print('*', end='')
            else:
                print(' ', end='')

        print()


star_trangle2(5)


def start_triangle_draw(n, row) -> None:
    for col in range(1, n+row+1):
        if (col >= n-row):
            print('*', end='')
        else:
            print(' ', end='')


def multi_star_trangle2(n: int) -> None:
    space = 0
    for row in range(0, n):
        start_triangle_draw(n, row)
        space = n-row
        print(' '*space, end='')
        print(' '*10, end='')
        start_triangle_draw(n, row)
        print()


multi_star_trangle2(10)
