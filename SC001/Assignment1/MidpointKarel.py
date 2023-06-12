"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre_condition: Karel is at the(1,1)
    Post_condtion: karel put the beepers at the middle of the street.beeper is under the karel,
                    in the odd world facing north,in the even world facing south.
    """
    if facing_east():       #to solve the problem at the world 1x1
         if not front_is_clear():   #if facing north or south, the loop will stop.
            turn_left()
    put_both_end()
    while facing_east() or facing_west():
            pick_and_move()




def put_both_end():
    """
    put the beeper at the both end of the street
    """
    if front_is_clear():
        put_beeper()
    while front_is_clear():
        move()
    if not front_is_clear():
        put_beeper()


def pick_and_move():
    """
    Karel pick up a beeper and put it on the front block.
    Finally,Karel will find the middle one and stop the loop
    beeper is under the Karel.
    """
    if on_beeper():
        turn_around()
        pick_beeper()
        move()
    if not on_beeper():
        put_beeper()
        move()
    else:
        turn_left() #turn left to stop at the middle,facing south or north to stop the loop.
    while not on_beeper():
        move()



def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()




# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
