"""
File: draw_line.py
Name: Clement Lin 林子謙
-------------------------
This File is about to click twice and create a line.
first, click and appear a circle
second, click and the circle disappear, create a new line where users clicked.

"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
# constants
window = GWindow(width=400, height=400)
SIZE = 8
# global variable
check = False
temp2 = GOval(width=0, height=0)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(e):  # e = event
    global check
    global temp2
    circle = GOval(width=SIZE, height=SIZE, x=e.x-SIZE/2, y=e.y-SIZE/2)  # the first circle users clicked
    circle.color = 'black'  # make the hollow circle
    window.add(circle)  # add into the window
    temp1 = circle  # temp1 = temporary position of the first circle

    if temp1 != temp2:  # only run in the False condition.  # temp2 = temporary position of the second circle
        if check:  # the second time click run this scope(第二個圓執行這個區塊)
            line = GLine(temp1.x, temp1.y, temp2.x, temp2.y)
            window.remove(temp1)
            window.remove(temp2)
            window.add(line)
            check = False  # switch to another scope
        else:  # the first time click run this scope (第一個圓執行這個區塊)
            temp2 = temp1  # record the first circle that was clicked
            check = True  # switch to another scope


if __name__ == "__main__":
    main()
