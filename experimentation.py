import sys, pygame

try:
    import numpy as np
    import pygame.surfarray as surfarray
except ImportError:
    raise ImportError("NumPy and Surfarray are required.")

pygame.init()

# setup
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

# TODO: setup background
black = 0, 0, 0
white = 255, 255, 255
screen.fill(white)

# TODO: setup sprite(s)

r = red = pygame.Color(255, 0, 0, 255)
c = clear = pygame.Color(0, 0, 0, 0)

squareArr = np.zeros((128, 128, 3), np.int32)
print("squareArr:")
print(squareArr)
squareSurface = surfarray.make_surface(squareArr)
screen.blit(squareSurface, squareSurface.get_rect())

testSymbolSurface = pygame.Surface((10, 10), flags=pygame.SRCALPHA)
testSymbolPxArray = pygame.PixelArray(testSymbolSurface)

# make the whole thing clear
testSymbolPxArray[:,:] = c

# first column red
testSymbolPxArray[0:1,:] = r
# last column red
testSymbolPxArray[9:,:] = r

#first row red
testSymbolPxArray[:,0:1] = r
# last row red
testSymbolPxArray[:,9:] = r
print("testSymbolPxArray:")
print(testSymbolPxArray)

# testSymbolArr = np.asarray([
#     [c, r, r, r, r, r, r, r, r, c],
#     [r, c, c, c, c, c, c, c, c, r],
#     [r, c, c, c, c, c, c, c, c, r],
#     [r, c, c, c, c, c, c, c, c, r],
#     [r, c, c, c, c, c, c, c, c, r],
#     [r, c, c, c, c, c, c, c, c, r],
#     [r, c, c, c, c, c, c, c, c, r],
#     [r, c, c, c, c, c, c, c, c, r],
#     [r, c, c, c, c, c, c, c, c, r],
#     [c, r, r, r, r, r, r, r, r, c]
# ])
# print("testSymbolArr:")
# print(testSymbolArr)
print("testSymbolPxArray:")
print(testSymbolPxArray)
# testSymbolSurface = surfarray.make_surface(testSymbolArr)
del testSymbolPxArray
screen.blit(testSymbolSurface, (120, 120))

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # update states

    pygame.display.flip()
    # Fix: delay between draws (otherwise too fast)
    clock.tick(60)