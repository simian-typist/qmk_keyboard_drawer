import math
import numpy as np
from PIL import Image, ImageDraw


def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return np.round(qx), np.round(qy)


def get_corners(centre, width, width_scale):
    width = 0.5*width
    horiz_rot = 2*math.atan(width_scale)
    vert_rot = math.pi - horiz_rot

    top_left = (centre[0]-width_scale*width, centre[1]-width)
    top_right = rotate(centre, top_left, horiz_rot)
    bottom_left = rotate(centre, top_left, -vert_rot)
    bottom_right = rotate(centre, top_left, horiz_rot+vert_rot)
    return top_left, top_right, bottom_left, bottom_right


def get_smaller_rectangle(centre, top_left, width_scale, small_scale):
    h_rot = 2*math.atan(width_scale)
    v_rot = math.pi - h_rot
    small_top_left =  ((centre[0]-top_left[0])*small_scale+centre[0], (centre[1]-top_left[1])*small_scale + centre[1])
    small_top_right = rotate(centre, small_top_left, h_rot)
    small_bottom_left = rotate(centre, small_top_left, -v_rot)
    small_bottom_right = rotate(centre, small_top_left, h_rot+v_rot)
    return small_top_left, small_top_right, small_bottom_left, small_bottom_right


def draw_key(image, centre, width, width_scale):
    top_left, top_right, bottom_left, bottom_right = get_corners(centre, width, width_scale)
    s_tl, s_tr, s_bl, s_br = get_smaller_rectangle(centre, top_left, width_scale, 0.8)

    left = (top_left, bottom_left)
    right = (top_right, bottom_right)
    top = (top_left, top_right)
    bottom = (bottom_left, bottom_right)

    s_left = (s_tl, s_bl)
    s_right = (s_tr, s_br)
    s_top = (s_tl, s_tr)
    s_bottom = (s_bl, s_br)

    draw = ImageDraw.Draw(image)
    draw.line(s_left, fill=0)
    draw.line(s_right, fill=0)
    draw.line(s_top, fill=0)
    draw.line(s_bottom, fill=0)

    draw.line(left, fill=0)
    draw.line(right, fill=0)
    draw.line(top, fill=0)
    draw.line(bottom, fill=0)


def main():
    im = Image.new('RGBA', (400, 400), (255, 255, 255, 0))
    draw_key(im, (200, 200), 100, 1.5)
    im.show()


if __name__ == "__main__":
    main()
