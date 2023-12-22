def right_increase_triangle(n):
    '''
**********
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
    for row in range(n):
        for col in range(n):
            if row < col+1:
                print("*", end='')
            else:
                print(" ", end='')
        print()


right_increase_triangle(10)
