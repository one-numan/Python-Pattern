'''

*********
********
*******
******
*****
****
***
**
*


'''


def right_increase_triangle(n: int) -> None:
    for row in range(1, n):
        for col in range(1, n+1):
            if (col <= n-row):
                print('*', end='')
            else:
                print(" ", end='')
        print()


print("Start")
right_increase_triangle(10)
