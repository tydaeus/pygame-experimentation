import pygame

def get_imagedef(imageid):
    if imageid in _images.keys():
        return _images[imageid]
    else:
        raise UserWarning(f"Image matching '{imageid}' not found.")

def _build_rotate_fn(degrees:int): 


    def _noop_fn(image:pygame.Surface):
        return image

    def _rotate_fn(image:pygame.Surface):
        return pygame.transform.rotate(image, -degrees)

    if degrees == 0:
        return _noop_fn
    else:
        return _rotate_fn

rotate0 = _build_rotate_fn(0)
rotate90 = _build_rotate_fn(90)
rotate180 = _build_rotate_fn(180)
rotate270 = _build_rotate_fn(270)

_images = {}

_images['test'] = {
    'base' :
"""
+-----------------------+
|  ███████████████████  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|  ██⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷██  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷█|
|█⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷█|
|█⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷█|
| ████⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷████ |
|  █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█  |
|  █⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷█  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷█ █⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|███████████ ███████████|
+-----------------------+
""",
    'headingS' : rotate0,
    'headingE' :
"""
+-----------------------+
|  ███████████████████  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|  ██⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷██  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷█|
| █⌷⌷⌷⌷⌷⌷⌷⌷███⌷⌷⌷⌷⌷⌷⌷⌷█ |
|  █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█  |
|  █⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷█  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷█ █⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|██████████   ██████████|
+-----------------------+
""",
    'headingW' :
"""
+-----------------------+
|  ███████████████████  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|  ██⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷██  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷█|
| █⌷⌷⌷⌷⌷⌷⌷⌷███⌷⌷⌷⌷⌷⌷⌷⌷█ |
|  █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█  |
|  █⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷█  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷█ █⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|██████████   ██████████|
+-----------------------+
""",
    'headingN' :
"""
+-----------------------+
|  ███████████████████  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|  ██⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷██  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷█|
|█⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷█|
|█⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷█|
| ████⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷████ |
|  █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█  |
|  █⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷█  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷█ █⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|███████████ ███████████|
+-----------------------+
"""
}

_images['test2'] = {
    'base' :
"""
+-----------------------+
|  ███████████████████  |
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷█|
|█⌷███████████████████⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
|█⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█|
| █⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷⌷█ |
|  ███████████████████  |
+-----------------------+
""",
    "headingE": rotate0,
    "headingS": rotate90,
    "headingW": rotate180,
    "headingN": rotate270
}

_images['block'] = """
+-----------------------+
|  ███████████████████  |
| █░░▓▓▓▓▓▓▓▓⌷⌷▓▓▓▓▓░▓█ |
|█▓▓░▓▓▓▓▓▓▓▓▓⌷▓▓▓▓░░▓▓█|
|█▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓█|
|█▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓▓▓▓▓█|
|█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░▓▓█|
|█▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓█|
|█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓█|
|█▓▓⌷▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⌷⌷⌷█|
|█▓▓▓⌷▓▓▓▓▓▓▓▓▓▓▓▓▓▓⌷⌷▓█|
|█▓▓⌷⌷▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█|
|█▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█|
|█▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█|
|█▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓▓▓░░█|
|█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░█|
|█▓▓▓▓⌷⌷▓▓▓▓▓▓▓▓▓▓▓▓▓░⌷█|
|█▓▓▓▓▓⌷⌷▓▓▓▓▓▓▓▓▓▓⌷⌷⌷▓█|
|█▓▓▓▓▓⌷⌷▓▓▓▓▓▓▓▓▓▓▓▓▓▓█|
|█▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓█|
|█▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓█|
|█▓▓▓▓▓▓▓▓⌷▓▓▓▓▓▓░░░▓▓▓█|
| █▓▓▓▓▓▓▓⌷⌷▓▓▓▓▓▓░░▓▓█ |
|  ███████████████████  |
+-----------------------+
"""
