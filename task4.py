"""
===================   TASK 4   ====================
* Name: Can String Be Float
*
* Write a script that will take integer number as
* user input and return the product of digits. 
* The script should be able to handle incorrect
* input, as well as the negative integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def main():
    int_num = input("Please enter a number: ")

    allowed_chr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for ch in int_num:
        if ch not in allowed_chr:
            print("Your input is not valid!")
            quit()

    product_of_dig = 1
    for dg in int_num:
        product_of_dig *= int(dg)
    print(product_of_dig)


main()


