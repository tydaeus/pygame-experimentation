import sys, pygame

try:
    import numpy as np
    import pygame.surfarray as surfarray
except ImportError:
    raise ImportError("NumPy and Surfarray are required.")

import sprites, input

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
squareSurface = surfarray.make_surface(squareArr)
screen.blit(squareSurface, squareSurface.get_rect())

sprites.init()
sprites.all_sprites.draw(screen)

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
            input.process_event(event)

    # update states

    pygame.display.flip()
    # delay between draws
    clock.tick(60)