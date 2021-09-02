import pygame, pygame.surfarray as surfarray

r = red = pygame.Color(255, 0, 0, 255)
g = green = pygame.Color(0, 255, 0, 255)
b = blue = pygame.Color(0, 0, 255, 255)
c = clear = pygame.Color(0, 0, 0, 0)
k = black = pygame.Color(0, 0, 0, 255)
w = white = pygame.Color(255, 255, 255, 255)
g = gray = pygame.Color(128, 128, 128, 255)

test_txt_image = """
+-----------+
| ######### |
|#.........#|
|#....#....#|
|#.....#...#|
|#......#..#|
|#.#######.#|
|#......#..#|
|#.....#...#|
|#....#....#|
|#.........#|
| ========= |
+-----------+
"""

_default_text_palette = {
    '#': blue,
    '=': green,
    ' ': clear,
    '.': gray
}

def convert_text_image_to_colorarray(text_image, text_palette=_default_text_palette):
    width = row = index = 0
    output = []

    # _parse* functions 
    def _parse_prelim(c):
        "discard characters until we hit the start of the image frame ('+')"
        nonlocal parser
        if c == '+':
            parser = _parse_frametop

    def _parse_frametop(c):
        "read in the top frame ('-' to '+')"
        nonlocal width, parser
        if c == '-':
            width += 1
        elif c == '+':
            parser = _parse_framestartedge
        else:
            raise UserWarning(f"Illegal frame char: {c}")

    def _parse_framestartedge(c):
        "discard characters until we hit the left edge of the image frame ('|' or '+')"
        nonlocal parser
        if c == '|':
            parser = _parse_picturechar
            output.append([])
        elif c == '+':
            parser = _parse_framebottom

    def _parse_picturechar(c):
        "convert the characters of the picture until we hit the right edge of the image frame ('|')"
        nonlocal parser, output, row
        if c == '|':
            parser = _parse_framestartedge
            if len(output[row]) != width:
                raise UserWarning(f"Text image row of length {len(output[row])} mismatch with width: {width}")
            row += 1
        else:
            output[row].append(text_palette[c])
    
    def _parse_framebottom(c):
        "read in the bottom frame ('-')"
        nonlocal parser
        if c == '-':
            pass
        elif c == '+':
            parser = _parse_done
        else:
            raise UserWarning(f"Illegal frame char: {c}")
        # note: currently no width check on bottom frame

    _parse_done = 'DONE'

    parser = _parse_prelim

    while parser != _parse_done and index < len(text_image):
        parser(text_image[index])
        index += 1

    if parser != _parse_done:
        raise UserWarning("Malformed text image - parsing incomplete")

    return output



def convert_color_array_to_surface(color_array):
    height = len(color_array)
    width = len(color_array[0])

    test_surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    test_pxarr = pygame.PixelArray(test_surface)

    for y in range(height):
        if len(color_array[y]) != width:
            raise UserWarning(
                f"Image array inconsistent row width; row 0: {width}px, row {y}: {len(color_array[y])}"
            )
        for x in range(width):
            test_pxarr[x,y] = color_array[y][x]

    del test_pxarr
    return test_surface

def get_test_surface():
    return convert_color_array_to_surface(convert_text_image_to_colorarray(test_txt_image))
    # return convert_color_array_to_surface(test_image_src)