"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: photo from the document
    :return: the blurred photo
    """
    # Todo: create a new blank img that is as big as the original one

    # Loop over the picture
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            total = r = g = b = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            r += pixel.red
                            g += pixel.green
                            b += pixel.blue
                            total += 1
            new_pixel = new_img.get_pixel(x,y)
            new_pixel.red = r/total
            new_pixel.blue = b/total
            new_pixel.green = g/total
    return new_img
    #         if x == 0 and y == 0:
    #             # Get pixel at the top-left corner of the image.
    #             new_img_p.red = img_p.red
    #             new_img_p.blue = img_p.blue
    #             new_img_p.green = img_p.green
    #         elif x == img.width-1 and y == 0:
    #             # Get pixel at the top-right corner of the image.
    #             new_img_p.red = img_p.red
    #             new_img_p.blue = img_p.blue
    #             new_img_p.green = img_p.green
    #         elif x == 0 and y == img.height-1:
    #             # Get pixel at the bottom-left corner of the image
    #             new_img_p.red = img_p.red
    #             new_img_p.blue = img_p.blue
    #             new_img_p.green = img_p.green
    #
    #         elif x == img.width-1 and y == img.height-1:
    #             # Get pixel at the bottom-right corner of the image
    #             new_img_p.red = img_p.red
    #             new_img_p.blue = img_p.blue
    #             new_img_p.green = img_p.green
    #
    #         elif 0 < x < img.width-1 and y == 0:
    #             # Get top edge's pixels (without two corners)
    #             new_img_p.red = img_p.red
    #             new_img_p.blue = img_p.blue
    #             new_img_p.green = img_p.green
    #
    #         elif 0 < x < img.width-1 and y == img.height-1:
    #             # Get bottom edge's pixels (without two corners)
    #             new_img_p.red = img_p.red
    #             new_img_p.blue = img_p.blue
    #             new_img_p.green = img_p.green
    #
    #         elif x == 0 and 0 < y < img.height-1:
    #             # Get left edge's pixels (without two corners)
    #             new_img_p.red = img_p.red
    #             new_img_p.blue = img_p.blue
    #             new_img_p.green = img_p.green
    #
    #         elif x == img.width-1 and 0 < y < img.height-1:
    #             # Get right edge's pixels (without two corners)
    #             new_img_p.red = img_p.red
    #             new_img_p.blue = img_p.blue
    #             new_img_p.green = img_p.green
    #
    #         else:
    #             # Inner pixels.
    #             new_img_p.red = (img_p.red**2)/9
    #             new_img_p.blue = (img_p.blue**2)/9
    #             new_img_p.green = (img_p.green**2)/9
    #
    # return new_img


def main():
    """
    put a photo in it, it will show a blurred one.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
