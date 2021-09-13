import pygame

_MOVE_NORTH =   0b1000
_MOVE_EAST  =   0b0100
_MOVE_SOUTH =   0b0010
_MOVE_WEST  =   0b0001


_key_mapping = {
    pygame.K_UP     : _MOVE_NORTH,
    pygame.K_RIGHT  : _MOVE_EAST,
    pygame.K_DOWN   : _MOVE_SOUTH,
    pygame.K_LEFT   : _MOVE_WEST
}

class InputMessage:
    """
    Represents user input targeted to a specific player character
    """

    """
    Direction the move was made in, where 0 is up, 90 is right, etc.
    """
    heading = 0

    """
    How forcefully the move was made, 0 to 1 (float).
    """
    magnitude = 0

_subscribers = []

def add_subscriber(subscriber):
    _subscribers.append(subscriber)

_engaged_keys = set()

def process_event(event):
    if event.type == pygame.KEYDOWN:
        _engaged_keys.add(event.key)
    if event.type == pygame.KEYUP:
        _engaged_keys.remove(event.key)

def _read_heading(inputs):
    "Convert input keys into a heading and magnitude"

    # no move if contradictory movements or no movements
    if inputs == 0:
        return None
    elif inputs & _MOVE_NORTH and inputs & _MOVE_SOUTH:
        return None
    elif inputs & _MOVE_EAST and inputs & _MOVE_WEST:
        return None

    event_message = InputMessage()

    # working from keyboard input, we'll always have magnitude 1 if valid move input present
    event_message.magnitude = 1

    if inputs & _MOVE_NORTH:
        # northeast
        if inputs & _MOVE_EAST:
            event_message.heading = 45
        # northwest
        elif inputs & _MOVE_WEST:
            event_message.heading = 315
        # north
        else:
            event_message.heading = 0
    elif inputs & _MOVE_SOUTH:
        # southeast
        if inputs & _MOVE_EAST:
            event_message.heading = 135
        # southwest
        elif inputs &_MOVE_WEST:
            event_message.heading = 225
        # south
        else:
            event_message.heading = 180
    # east
    elif inputs & _MOVE_EAST:
        event_message.heading = 90
    # west
    elif inputs & _MOVE_WEST:
        event_message.heading = 270
    # something went wrong
    else:
        # make it obvious if we got something unexpected by this point
        raise ValueError(f"Unable to parse input: {inputs:04b}")
    
    return event_message


def update():
    inputs = 0b0000

    # convert keys currently down into inputs
    for engaged_key in _engaged_keys:
        if engaged_key in _key_mapping.keys():
            inputs |= _key_mapping[engaged_key]
    
    event_message = _read_heading(inputs)

    if event_message:
        for subscriber in _subscribers:
            subscriber(event_message)