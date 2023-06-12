"""
File: CheckerboardKarel.py
Name: Clement Lin
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *

def main():
    put_beeper()
    if not front_is_clear():    # to solve the direction problem in karel's world 8X1
        check()
    while front_is_clear():
        if on_beeper():     # if on beeper, Karel fill the odd line.
            fill_a_line()
            go_back()
        else:
            fill_a_line()
            go_back1()


def fill_a_line():
    """
Karel put one beeper and move two steps.
    """
    while front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
        else:
            move()


def go_back():
    """
    Karel move back on the odd street.
    """
    if not front_is_clear():
        turn_around()
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_right()
    if front_is_clear():
        if facing_north():
            move()
            turn_right()


def go_back1():
    """
    Karel move back on the even street.
    """
    if not front_is_clear():
        turn_around()
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_right()
    if front_is_clear():
        if facing_north():
            move()
            turn_right()
            put_beeper()


def check():
    """
    Karel will check if front is clear.
    If not, it will go to the right direction.
    """
    while not front_is_clear():
        if facing_east():
            turn_left()
        if facing_west():
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
