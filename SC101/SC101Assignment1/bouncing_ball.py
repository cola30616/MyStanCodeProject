"""
File:  bouncing_ball.py
Name: Clement Lin 林子謙
-------------------------
This file is about to simulate the situation of bouncing ball.
Users clicked the window and play the animation.
While playing the animation, it won't effect by the click from user.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
# const
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
# global variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(width=SIZE, height=SIZE, x=START_X, y=START_Y)  # the ball at the START_X, START
click = True
counter = 0 # count how many times it run


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bouncing_ball)


def bouncing_ball(e):  # e is not used
    """
    1. If counter is equal to three times, user cannot click and start the animation
    2. My way to avoid the repeat click problem.
        (1) click = True.  and run the True scope
        (2) while the animation running, counter+1, click = False, it runs in the false scope, nothing gonna happen
        (3) while the animation end up , click = True , run the True scope , user can click again
    """
    global click
    global counter

    if counter < 3:  # the ball jump out of the window three times and cannot run
        if click:  # avoid the repeat click event
            window.remove(ball)  # remove the ball(global variable)
            bouncing()  # run the animation


def bouncing():  # animation
    global click
    global counter

    vy = 0  # vertical velocity of new_ball
    counter += 1  # count how many times it runs
    click = False  # let click = True , it won't effect by the  user click
    new_ball = GOval(width=SIZE, height=SIZE, x=START_X, y=START_Y)  # create a new ball to run the animation
    new_ball.filled = True
    window.add(new_ball)

    while True:
        if new_ball.x <= window.width:  # falling condition of new_ball
            # the ball falling, VX is the same , vy + the value of GRAVITY
            new_ball.move(VX, vy)
            vy += GRAVITY
            pause(DELAY)
        if new_ball.y + new_ball.height >= window.height:  # the condition of hitting the ground
            # when the ball hit the ground, it will change the direction and multiply REDUCE
            vy = -vy * REDUCE
        if new_ball.x > window.width:  # the ball out of the window
            window.add(ball)
            window.remove(new_ball)
            click = True  # the animation is end. Open the switch and user can click again to stat the animation.
            break


if __name__ == "__main__":
    main()
