'''

   *
  * *
 * * *
* * * *
'''


def star_trangle(n: int) -> None:
    for row in range(1, n+1):
        for col in range(0, n):
            if (col >= n-row):
                print("* ", end='')
            else:
                print(" ", end='')
        print()


star_trangle(5)


'''
* * * *
 * * *
  * *
   *
'''

'''
*****
 ***
  *
'''

'''
*
**
***
****
***
**
*

'''


