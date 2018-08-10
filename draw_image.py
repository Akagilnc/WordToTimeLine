from PIL import Image, ImageDraw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


if __name__ == '__main__':

    width, height = 800, 600
    image = Image.new('RGB', size=(width, height), color=WHITE)
    draw = ImageDraw.Draw(image)

    # timeline
    p0 = 0, height / 2
    p1 = width, height / 2
    draw.line(xy=[p0, p1], fill=BLACK, width=1)

    # events
    n = 5
    for i in range(n):
        radius = 4
        origin = (width / (n + 1)) * (i + 1), height / 2
        topleft = origin[0] - radius, origin[1] - radius
        bottomright = origin[0] + radius, origin[1] + radius
        draw.ellipse(xy=(topleft, bottomright), fill=None, outline=BLACK)

    image.show()