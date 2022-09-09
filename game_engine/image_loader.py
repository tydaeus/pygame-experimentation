"""
Takes care of finding and loading images needed for the game.
"""
import logging, pygame
from . import imagedef, textimage_loader

_logger = logging.getLogger(__name__)

def load_image(view):
    """
    Attempts to find an image matching the provided specifying object.
    """

    # FUTURE: cache previously loaded images
    # FUTURE: provide a standardized definition of what the view will be examined for
    _logger.debug("Loading image '%s'", view.imageid)
    imageentry = imagedef.get_imagedef(view.imageid)
    # FUTURE: allow multi-frame or otherwise more complex images
    if type(imageentry) == dict:
        textimage = imageentry['base']
    else:
        textimage = imageentry

    baseimage = textimage_loader._convert_text_image_to_surface(textimage)
    resultimage = baseimage

    # FUTURE: simplify, extract
    if view.heading:
        compassdir = view.heading.compass_direction
        headingkey = f"heading{compassdir}"
        if headingkey in imageentry.keys():
            headingval = imageentry[headingkey]
                resultimage = textimage_loader._convert_text_image_to_surface(headingval)
        else:
            raise UserWarning("heading specified, but not allowed")
            

    if tuple(resultimage.get_size()) != tuple(view.size):
        resultimage = pygame.transform.scale(resultimage, view.size)
    
    return resultimage



