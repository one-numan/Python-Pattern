'''
    *
   **
  ***
 **** 
*****
 ****
  ***
   **
    *

'''


def check_odd(n):
    if n % 2 == 0:
        print("Even")
        return
    return right_triangle(n)


def right_triangle(n):

    top_space = n//2
    bottom_space = 1
    for row in range(1, n+1):
        if (row < n//2+2):
            print(' '*top_space, end='')
            print('*'*row, end='')
            top_space -= 1
        elif (row > n//2+1):
            print(' '*bottom_space, end='')
            print("*"*(n+1-row), end='')
            bottom_space += 1
        else:
            print(' ', end='')
        print()
    print(n//2+1)


check_odd(11)
