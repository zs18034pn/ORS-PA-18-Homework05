"""
===================   TASK 5   ====================
* Name: Average Value
*
* Write a function `averageval` that will take a
* integer list as an argument and return the 
* average value of the list elements.  
*
* Note: Please describe in details possible cases
* in which your solution might not work. It is not
* allowed to use built-in functions.
*
* Use main() function to test your solution.
===================================================
"""


def averageval(listt):

    summ = 0
    for el in listt:
        summ += int(el)
    lenght = 0
    for el in listt:
        lenght += 1
    return summ / lenght


def main():
    print(averageval([3, 4, 5]))


main()