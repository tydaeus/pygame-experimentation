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

testSymbolPxArray[:,0:1] = [c, r, r, r, r, r, r, r, r, c]
testSymbolPxArray[:,1:2] = [r, c, c, c, c, c, c, c, c, r]
testSymbolPxArray[:,2:3] = [r, c, c, c, c, c, c, c, c, r]
testSymbolPxArray[:,3:4] = [r, c, c, c, c, c, c, c, c, r]
testSymbolPxArray[:,4:5] = [r, c, c, c, c, c, c, c, c, r]
testSymbolPxArray[:,5:6] = [r, c, c, c, c, c, c, c, c, r]
testSymbolPxArray[:,6:7] = [r, c, c, c, c, c, c, c, c, r]
testSymbolPxArray[:,7:8] = [r, c, c, c, c, c, c, c, c, r]
testSymbolPxArray[:,8:9] = [r, c, c, c, c, c, c, c, c, r]
testSymbolPxArray[:,9:10] = [c, r, r, r, r, r, r, r, r, c]

print("testSymbolPxArray:")
print(testSymbolPxArray)
del testSymbolPxArray
screen.blit(testSymbolSurface, (120, 120))

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # update states

    pygame.display.flip()
    # delay between draws
    clock.tick(60)