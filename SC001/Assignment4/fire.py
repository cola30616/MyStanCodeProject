"""
File: fire.py
Name:
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:  the picture from the document.
    :return: img, the fire will be marked by color red.
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.red < avg * HURDLE_FACTOR:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
        else:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
    return img


def main():
    """
    the picture will show where the fire happen, mark it by color red.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
