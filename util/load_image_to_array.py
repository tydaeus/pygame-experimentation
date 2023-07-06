'''
Load an image and convert it to an array for subsequent transformation
'''
import sys, pygame, logging
from pygame import image, surfarray

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('{asctime}.{msecs:3.0f}[{name}]{levelname}: {message}', datefmt='%H.%M.%S', style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

pygame.init()

def load_image_to_array(imagepath):
    img = image.load_extended(imagepath)
    # img = img.convert_alpha()

    rawsurfarray = surfarray.array2d(img)
    processedsurfarray = []

    # TODO: figure out how to properly copy 2d array to lists (or array)
    for i in range(len(rawsurfarray)):
        processedsurfarray[i].append([])
        for j in range(len(rawsurfarray[i])):
            processedsurfarray[i][j] = img.unmap_rgb(rawsurfarray[i][j])

    return processedsurfarray