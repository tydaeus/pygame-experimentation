import pygame, pygame.surfarray as surfarray

r = red = pygame.Color(255, 0, 0, 255)
c = clear = pygame.Color(0, 0, 0, 0)
b = blue = pygame.Color(0, 0, 255, 255)

test_image_src = [
    [c, r, r, r, r, r, r, r, r, r, c],
    [r, c, c, c, c, c, c, c, c, c, r],
    [r, c, c, c, c, r, c, c, c, c, r],
    [r, c, c, c, c, c, r, c, c, c, r],
    [r, c, c, c, c, c, c, r, c, c, r],
    [r, c, r, r, r, r, r, r, r, c, r],
    [r, c, c, c, c, c, c, r, c, c, r],
    [r, c, c, c, c, c, r, c, c, c, r],
    [r, c, c, c, c, r, c, c, c, c, r],
    [r, c, c, c, c, c, c, c, c, c, r],
    [c, b, b, b, b, b, b, b, b, b, c]
]

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
    return convert_color_array_to_surface(test_image_src)