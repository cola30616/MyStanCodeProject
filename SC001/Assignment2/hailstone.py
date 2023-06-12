"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    pre_condition: users input the number in this programme.
    post_condition: user will get the answers of the hailstone sequence, and how many steps to reach 1.
    """
    print('This program computes Hailstone sequence.')
    n = int(input('Enter a number: '))
    count = 0
    while n != 1:  # if n = 1 , the loop will end.
        if n % 2 == 1:  # if n is odd, it will make 3n+1.
            print(str(n)+' is odd, so I make 3n+1: ' + str(int(3 * n + 1)))
            n = int((3 * n + 1))
            count += 1  # it will count once  while making 3n+1
        if n % 2 == 0:  # if n is even, it will take half.
            print(str(n)+' is even, so I take half: ' + str(int(n / 2)))
            n = int(n / 2)
            count += 1  # it will count once  while taking half
    print('It took ' + str(count) + ' steps to reach 1.')  # it will print how many steps to reach 1.


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
