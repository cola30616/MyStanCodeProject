"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Pre_condition: Karel is on the (1,1),facing east.
    Post_condition:karel repair all the pillars,
    and stop on the (the end position of pillar,1),facing east.
    """
    turn_left()
    while front_is_clear():
        if facing_north():
            repair_the_pillar()
        else:
            down()
            go_to_next_pillar()

def turn_right():
    for i in range(3):
        turn_left()


def repair_the_pillar():
    """
Karen is repairing the pillar
It will check and fix the lost beepers of pillars.
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
    if not on_beeper():
        put_beeper()
    turn_around()

def down():
    """
    Karel returns to the first point of pillar.
    """
    while front_is_clear():
        move()
    turn_left()

def turn_around():
    """
    Karel turn left twice
    """
    turn_left()
    turn_left()


def go_to_next_pillar():
    """
    Karel move 4 steps to arrive next pillar.
    """
    if front_is_clear():
        for i in range(4):
            move()
        else:
            turn_left() #If this is the end of pillar,Karel will turn left and end up the loop.





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
