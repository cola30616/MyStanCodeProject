"""
File:  my_drawing.py
Name: Clement Lin 林子謙
----------------------
This file is to create a photo by using the Package of Campy.
I use GOval, GPolygon, GArc, GLine, GRect, GLabel in this file.
"""

from campy.graphics.gobjects import GOval, GPolygon, GArc, GLine, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    你已被好運鯊魚造訪
    分享這張圖並回覆
    '不管你吸了什麼，都給我來一點鯊鯊'
    """
    window = GWindow(width=800, height=400)
    bgc = GRect(800, 400)  # background color
    bgc.filled = True
    bgc.fill_color = 'lightyellow'

    body = GOval(200, 350, x=250, y=150)
    body.filled = True
    body.fill_color = 'skyblue'

    belly = GOval(140, 350, x=280, y=200)
    belly.filled = True
    belly.fill_color = 'snow'

    left_eye = GOval(20, 20, x=283, y=200)
    left_eye.filled = True

    right_eye = GOval(20, 20, x=390, y=198)
    right_eye.filled = True

    left_pupil = GOval(10, 10, x=293, y=205)
    left_pupil.filled = True
    left_pupil.fill_color = 'white'

    right_pupil = GOval(10, 10, x=390, y=203)
    right_pupil.filled = True
    right_pupil.fill_color = 'white'

    mouth = GArc(90, 70, 0, -180)
    mouth.filled = True
    mouth.fill_color = 'salmon'

    tooth1 = GPolygon()
    tooth1.add_vertex((314, 238))
    tooth1.add_vertex((324, 238))
    tooth1.add_vertex((319, 248))
    tooth1.filled = True
    tooth1.fill_color = 'white'

    tooth2 = GPolygon()
    tooth2.add_vertex((374, 238))
    tooth2.add_vertex((384, 238))
    tooth2.add_vertex((379, 248))
    tooth2.filled = True
    tooth2.fill_color = 'white'

    fish_gill_left1 = GLine(270, 240, 290, 260)
    fish_gill_left2 = GLine(268, 250, 288, 270)
    fish_gill_left3 = GLine(265, 260, 285, 280)
    fish_gill_right1 = GLine(430, 240, 410, 260)
    fish_gill_right2 = GLine(435, 250, 415, 270)
    fish_gill_right3 = GLine(440, 260, 420, 280)

    fish_fin_right = GArc(130, 75, 20, -200)
    fish_fin_right.filled = True
    fish_fin_right.fill_color = 'skyblue'

    fish_fin_left = GArc(135, 75, 10, 195)
    fish_fin_left.filled = True
    fish_fin_left.fill_color = 'skyblue'

    title = GLabel('不管你吸了什麼，都給我來一點鯊鯊')
    title.font = '-40'
    title.color = 'skyblue'

    window.add(bgc)
    window.add(body)
    window.add(belly)
    window.add(left_eye)
    window.add(right_eye)
    window.add(right_pupil)
    window.add(left_pupil)
    window.add(mouth, x=304, y=220)
    window.add(fish_gill_left1)
    window.add(fish_gill_left2)
    window.add(fish_gill_left3)
    window.add(fish_gill_right1)
    window.add(fish_gill_right2)
    window.add(fish_gill_right3)
    window.add(tooth1)
    window.add(tooth2)
    window.add(fish_fin_right, x=133, y=240)
    window.add(fish_fin_left, x=438, y=240)
    window.add(title, x=0, y=title.height+20)


if __name__ == '__main__':
    main()
