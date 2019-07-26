import math
import numpy as np
from PIL import Image, ImageDraw
from utils import rotate_point


def get_corners(centre, width_scale, start_point):
    horiz_rot = 2*math.atan(width_scale)
    vert_rot = math.pi - horiz_rot

    points = np.vstack((start_point, rotate_point(centre, start_point, horiz_rot)))
    points = np.vstack((points, rotate_point(centre, points[0, :], horiz_rot+vert_rot)))
    points = np.vstack((points, rotate_point(centre, points[0, :], -vert_rot)))
    return points


def draw_borders(points, draw, fill, outline=None):
    draw.polygon(list(points.flatten()), fill=fill, outline=outline)
    # for i in range(-1, points.shape[0] - 1):
    #     draw.line((tuple(points[i, :]), tuple(points[i + 1, :])), fill=0)


def draw_key(image, centre, width, width_scale, small_scale):
    width = 0.5*width

    main_top_left = np.array([centre[0] - width_scale * width, centre[1] - width])
    main_points = get_corners(centre, width_scale, main_top_left)
    small_top_left =  np.array([
        (centre[0]-main_points[0, 0])*small_scale+centre[0],
        (centre[1]-main_points[0, 1])*small_scale + centre[1]
    ])
    small_points = get_corners(centre, width_scale, small_top_left)
    offset = width*small_scale*0.12
    small_points[:, 1] -= offset

    print(small_points)
    print(small_points.shape)

    draw = ImageDraw.Draw(image)
    draw_borders(main_points, draw, (200, 200, 200), outline=(50, 50, 50))
    draw_borders(small_points, draw, (250, 250, 250), outline=(180, 180, 180))


def main():
    im = Image.new('RGBA', (400, 400), (255, 255, 255, 0))
    draw_key(im, (200, 200), 110, width_scale=1.0, small_scale=0.75)
    im.save("test_img.bmp")
    im.show()


if __name__ == "__main__":
    main()
