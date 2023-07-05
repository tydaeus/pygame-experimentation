'''
Display an image in a window until closed
'''
import sys, pygame, logging
from pygame import image as image

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('{asctime}.{msecs:3.0f}[{name}]{levelname}: {message}', datefmt='%H.%M.%S', style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

pygame.init()

clock = pygame.time.Clock()


white = 255, 255, 255

imagepath = sys.argv[1]
img = image.load_extended(imagepath)

logger.info(f"image size: {img.get_rect().size}")

# size window based on image
screen = pygame.display.set_mode(img.get_rect().size)
displayInfo = pygame.display.Info()
logger.info(f"display dimensions: {displayInfo.current_w} x {displayInfo.current_h}")

screen.fill(white)
screen.blit(img, img.get_rect())

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # sleep/wait between draws / updates
    clock.tick(60)
