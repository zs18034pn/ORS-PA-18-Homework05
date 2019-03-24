"""
===================   TASK 1   ====================
* Name: Power to the Number
*
* Write a function `numpower()` that will for the
* passed based number `num` and exponent `expo`
* return the value of the number `num` raised to
* the power of `expo`.
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in operators and functions
* for this task.
*
* Use main() function to test your solution.
===================================================
"""


def num_power(num, expo):
    powered = num
    if expo == 0:
        return 1
    if expo == 1:
        return num
    if expo != 1:
        powered = (num * num_power(num, expo-1))
        return powered


def main():
    num_on_expo = num_power(1, 3)
    print("Number on the exponent is: ", num_on_expo)

main()

#This function will not work if passed "expo" value is a fraction or less than 0.