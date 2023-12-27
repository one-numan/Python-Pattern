'''
*
**
***
****
*****
******
*******
********
'''


def increasing_triangle(n: int) -> None:
    for col in range(1, n+1):
        for row in range(col):
            print('*', end='')
        print()


increasing_triangle(10)
