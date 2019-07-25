import numpy as np
from PIL import Image, ImageDraw
import math
def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return np.round(qx), np.round(qy)

def draw_key(image, centre, width, width_scale):
    width = 0.5*width
    horiz_rot = 2*math.atan(width_scale)
    vert_rot = math.pi - horiz_rot


    top_left = (centre[0]-width_scale*width, centre[1]-width)
    top_right = rotate(centre, top_left, horiz_rot)
    bottom_left = rotate(centre, top_left, -vert_rot)
    bottom_right = rotate(centre, top_left, horiz_rot+vert_rot)

    left = (top_left, bottom_left)
    right = (top_right, bottom_right)
    top = (top_left, top_right)
    bottom = (bottom_left, bottom_right)

    draw = ImageDraw.Draw(image)
    draw.line(left, fill=0)
    draw.line(right, fill=0)
    draw.line(top, fill=0)
    draw.line(bottom, fill=0)


def main():
    im = Image.new('RGBA', (400, 400), (255, 255, 255, 0))
    draw_key(im, (200, 200), 100, 2.0)
    im.show()


if __name__ == "__main__":
    main()
