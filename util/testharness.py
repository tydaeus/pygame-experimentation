'''
This script is intended to provide a minimalist scratch area for testing fresh scripting attempts.
'''
import sys, pygame

pygame.init()

clock = pygame.time.Clock()

# setup window
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)

white = 255, 255, 255

def draw_background():
    screen.fill(white)

draw_background()
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
