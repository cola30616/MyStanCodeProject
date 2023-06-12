"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre_condition: Karel is at the (3,4)
    post_condition: karel pick the letter and return to (3,4)
    """
    move_to_the_newspaper()
    bring_the_newspaper_back_to_read()

def move_to_the_newspaper():
    """
    Karel moves to the door to take the newspaper.
    """
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()
    pick_beeper()


def bring_the_newspaper_back_to_read():
    """
    Karel takes the newspaper and return to (3,4)
    """
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    """
    Karel turn left 3 times.
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Karel turn left twice.
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
