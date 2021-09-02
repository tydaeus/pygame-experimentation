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

class _TextImageParser:
    """
    Provides state machine processing for parsing images defined as text in an ascii-image style format.
    
    Expects the image to be bordered, with '+' for corners, '-' for horizontal edges, and '|' for vertical edges.
    Ignores characters outside the borders (including newlines); considers all characters inside the borders as part
    of the image. 
    """

    def __init__(self):
        self._parse_done = 'DONE'

    def parse(self, text_image, text_palette):
        """
        Converts text_image to a 2d list of Colors, using text_palette to look up character to color mapping.
        """
        self.width = self.row = self.index = 0
        self.output = []
        self.state = self._parse_prelim

        while self.state != self._parse_done and self.index < len(text_image):
            self.state(text_image[self.index], text_palette)
            self.index += 1

        if self.state != self._parse_done:
            raise UserWarning("Malformed text image - parsing incomplete")

        return self.output

    # parsing states (state machine pattern)
    def _parse_prelim(self, c, text_palette):
        "discard characters until we hit the start of the image frame ('+')"
        if c == '+':
            self.state = self._parse_frametop

    def _parse_frametop(self, c, text_palette):
        "read in the top frame ('-' to '+')"
        if c == '-':
            self.width += 1
        elif c == '+':
            self.state = self._parse_framestartedge
        else:
            raise UserWarning(f"Illegal frame char: {c}")

    def _parse_framestartedge(self, c, text_palette):
        "discard characters until we hit the left edge of the image frame ('|' or '+')"
        if c == '|':
            self.state = self._parse_picturechar
            self.output.append([])
        elif c == '+':
            self.state = self._parse_framebottom

    def _parse_picturechar(self, c, text_palette):
        "convert the characters of the picture until we hit the right edge of the image frame ('|')"
        if c == '|':
            self.state = self._parse_framestartedge
            if len(self.output[self.row]) != self.width:
                raise UserWarning(f"Text image row of length {len(self.output[self.row])} mismatch with width: {self.width}")
            self.row += 1
        else:
            self.output[self.row].append(text_palette[c])
    
    def _parse_framebottom(self, c, text_palette):
        "read in the bottom frame ('-')"
        if c == '-':
            pass
        elif c == '+':
            self.state = self._parse_done
        else:
            raise UserWarning(f"Illegal frame char: {c}")
        # note: currently no width check on bottom frame


_textImageParser = _TextImageParser()

def convert_text_image_to_colorarray(text_image, text_palette=_default_text_palette):
    return _textImageParser.parse(text_image, text_palette)



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