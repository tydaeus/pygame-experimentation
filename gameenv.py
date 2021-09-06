"""
scalingfactor:
    Determines the view pixel to model coordinate multiplier, allowing separation between how an entity is modelled and
    how it is drawn.
    
    E.g. a scalingfactor of 0.1 indicates that 1 pixel in the view corresponds to 10 units in the model. If the entity
    moves 20 units as represented in the model, the image will be shifted by 2 pixels.
"""

scalingfactor = 0.1

def scalemodel(*args: int):
    """
    Returns a tuple of each arg converted from model scale to view scale.
    """
    return tuple(round(arg * scalingfactor) for arg in args)