"""
===================   TASK 6   ====================
* Name: Typewriter
*
* Write a script that will take file name as user
* input. Then the script should take file content
* as user input as well until user hits `Enter`.
* At the end, the script should store the content
* into the file with given name. If the file already
* exists the script should append the new content
* at the end.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def main():
    file_name = input("Please enter the name of a file: ")
    infile = open(file_name, "w")
    infile.write(input("Enter the content of a file: "))
    infile.close()


main()
