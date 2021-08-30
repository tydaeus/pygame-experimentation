import sys, pygame

try:
    import numpy as np
    import pygame.surfarray as surfarray
except ImportError:
    raise ImportError("NumPy and Surfarray are required.")

import sprites

pygame.init()

# setup
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

# TODO: setup background
black = 0, 0, 0
white = 255, 255, 255
screen.fill(white)

squareArr = np.zeros((128, 128, 3), np.int32)
print("squareArr:")
print(squareArr)
squareSurface = surfarray.make_surface(squareArr)
screen.blit(squareSurface, squareSurface.get_rect())

screen.blit(sprites.get_test_surface(), (120, 120))

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # update states

    pygame.display.flip()
    # delay between draws
    clock.tick(60)