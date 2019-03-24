"""
===================   TASK 2   ====================
* Name: Most Frequent Letter
*
* Write a script that takes the stirng as user
* input and displays which letter has the most
* occurences and how many. If two or more letters
* have the same number of occurences print any.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
===================================================
"""
string = input("Please enter a word or a sentence: ")
maximum = 0
for i in string:
    if string.count(i) > maximum:
        maximum = string.count(i)
        print(i, ":", maximum)


