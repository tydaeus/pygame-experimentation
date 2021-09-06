import sys, pygame, entities

try:
    import numpy as np
    import pygame.surfarray as surfarray
except ImportError:
    raise ImportError("NumPy and Surfarray are required.")

import sprites, input

pygame.init()

clock = pygame.time.Clock()

# setup window
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

# setup background
black = 0, 0, 0
white = 255, 255, 255

def draw_background():
    screen.fill(white)

    squareArr = np.zeros((128, 128, 3), np.int32)
    squareSurface = surfarray.make_surface(squareArr)
    screen.blit(squareSurface, squareSurface.get_rect())

draw_background()
sprites.init()
entities.init()
sprites.all_sprites.draw(screen)

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
            input.process_event(event)

    # update states
    input.update()
    sprites.all_sprites.update()

    draw_background()
    sprites.all_sprites.draw(screen)

    pygame.display.flip()
    # delay between draws / updates
    clock.tick(60)