"""
mechanisms to load a textimage from file (currently imagedef.py)
"""

import logging, pygame, re
from . import imagedef

_logger = logging.getLogger(__name__)

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
            raise UserWarning(f"Malformed text image - parsing incomplete at {self.index} / {len(text_image)}")

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

_red = pygame.Color(255, 0, 0, 255)
_green = pygame.Color(0, 255, 0, 255)
_blue = pygame.Color(0, 0, 255, 255)
_clear = pygame.Color(0, 0, 0, 0)
_black = pygame.Color(0, 0, 0, 255)
_white = pygame.Color(255, 255, 255, 255)
_gray = pygame.Color(128, 128, 128, 255)
_lightgray = pygame.Color(200, 200, 200, 255)
_darkgray = pygame.Color(100, 100, 100, 255)

_default_text_palette = {
    ' ': _clear,
    '░': _lightgray,
    '▒': _gray,
    '▓': _darkgray,
    '█': _black,
    '⌷': _white 
}

def _convert_text_image_to_colorarray(text_image, text_palette=_default_text_palette):
    return _textImageParser.parse(text_image, text_palette)



def _convert_color_array_to_surface(color_array):
    height = len(color_array)
    width = len(color_array[0])

    surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    pxarr = pygame.PixelArray(surface)

    for y in range(height):
        if len(color_array[y]) != width:
            raise UserWarning(
                f"Image array inconsistent row width; row 0: {width}px, row {y}: {len(color_array[y])}"
            )
        for x in range(width):
            pxarr[x,y] = color_array[y][x]

    del pxarr
    return surface

def _convert_text_image_to_surface(text_image, text_palette=_default_text_palette):
    return _convert_color_array_to_surface(_convert_text_image_to_colorarray(text_image, text_palette))

def _read_text_image_file(filepath):
    """
    Reads a text file containing one or more text images.
    Returns a list of strings, one for each text image.
    """

    with open(filepath, encoding='utf8') as fp:
        rawcontents = fp.readlines()

    output = []
    curimage = ''
    reading = False
    re_textframe = re.compile(r'^\+-+\+$')

    for line in rawcontents:
        if re_textframe.match(line):
            # frame edges are always part of the image
            curimage += line

            # bottom of frame
            if reading:
                output.append(curimage)
                curimage = ''
                reading = False
            # top of frame
            else:
                reading = True
        elif reading:
                curimage += line
    
    return output
# TODO: parse output