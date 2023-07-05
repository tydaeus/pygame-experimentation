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


"""
Planning
Need to separate concerns a bit further

Loader (rename?)
should take care of reading the files and providing easy access to the different images necessary to render
needs a way to consistently describe the different images
- heading for each image variant
- state (running, idle, etc.) for each image variant
    - frames applicable to state
- modifiers?
- component images?

Entity model
tracks entity's current state
- heading
- state
    - agnostic to current frame
    - knows how long has been in current state
        - maximum length of tracking followed by rollover, or transition to another state
            - likely not useful to track indefinitely, at least not here, but could technically do so
        - conventions? e.g. rollover, or transition between states may need divisibility to prevent stutter
            - 60 ticks or 1s could be reasonable, maybe not if engine allows adjustable clock freq
- modifiers

Translator (rename? ImageProvider, ImageSelector)
reads Entity's current state and available options from loader to determine what should actually get rendered

ImageSource - defines where to pull one or more associated images from
ImageDef - groups one or more related ImageSources together to gather all (or just multiple?) images for a given entity
ImageLoader - used to convert images defined by ImageDef into pygame surfaces - where to cache? store in imageDef or imageProvider, or as part of loading? likely should cache initial surface load

who controls frame rate (ticks/frame)?
- entity should know how long a given state lasts (or if it is indefinite/player controlled, and whether interruptable)
- Loader should know how many frames there are for a given state
- who knows whether a given sequence should loop indefinitely vs. get padded?

"""

