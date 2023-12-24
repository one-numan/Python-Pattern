'''
   *
  ***
 *****
*******
 *****
  ***
   *

'''


def daimond_triangle(n: int) -> None:
    space = n//2
    star = 0

    for row in range(1, n//2+1):
        star = row*2-1
        print(" "*space, end='')
        print('*'*star, end='')
        print()

        space -= 1
    print('*'*n)
    # print(space, star)
    space = +1
    for row in range(n//2+1, 1, -1):
        print(" "*space, end='')
        print("*"*star, end='')
        space += 1
        star -= 2
        print()
        # print(space, star)


def half_daimond_triangle2(n):
    for row in range(1, n//2):
        space = n//2-row
        star = row * 2-1
        print(' '*space, end='')
        print('*'*star)


daimond_triangle(9)
