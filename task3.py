"""
===================   TASK 3   ====================
* Name: Convert to Octal
*
* Write a function `dec2oct` that will convert
* positive integer number passed as argument into
* the octal based number. 
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""


def dec2oct(num):
    remainder = ""
    while num > 0:
        rem = num % 8
        remainder += str(rem)
        num = num // 8
    return remainder[-1 :: -1]


def main():
    oct_num = dec2oct(500)
    print("Octal result is: ", oct_num)


main()
