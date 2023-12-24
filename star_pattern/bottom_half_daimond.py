'''
*****
 ***
  *

'''


def bottom_half_daimond(n: int):
    space = 0
    star = n*2 - 1
    for row in range(1, n+1):
        print(' '*space, end='')
        print('*'*star, end='')

        print()
        space += 1
        star -= 2


def bottom_half_daimond2(n: int):
    space = 0
    for row in range(1, n*2, 2):
        print(' '*space, end='')

        print('*'*(n*2-row), end='')

        print()
        space += 1


bottom_half_daimond2(3)
