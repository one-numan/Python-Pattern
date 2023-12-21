""" ******
    ******
    ******
    ******
    ******
Full Star Pattern
"""


def full_star(n: int) -> None:
    """ 
    ******
    ******
    ******
    ******
    ******
    Full Star Pattern
    """
    pass
    for col in range(n):
        for row in range(n):
            print("*", end='')
        print()


full_star(int(input("Enter the Length :")))
