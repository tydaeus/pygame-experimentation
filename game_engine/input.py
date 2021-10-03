import pygame, math

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

    def __init__(self, heading, magnitude):
        self.heading = Heading(heading)
        self.magnitude = magnitude


# pre-calculate coordinate distance for a 45 degree diagonal, to reduce calculations needed
_DIAG_DIST = math.sin((45 * math.pi) / 180)

class Heading:
    def __init__(self, degrees):
        self.heading = degrees % 360

    @property
    def heading(self):
        'Directional heading, in degrees, where 0 is up, 90 is right, etc.'
        return self._degrees

    @heading.setter
    def heading(self, value):
        self._degrees = value % 360

    @property
    def compass_direction(self):
        """
        Directional heading as a 4-way compass reading ('N', 'E', 'S', or 'W')
        """
        if self._degrees > 315  or self._degrees <= 45:
            return 'N'
        elif self._degrees > 45 and self._degrees <= 135:
            return 'E'
        elif self._degrees > 135 and self._degrees <= 225:
            return 'S'
        elif self._degrees > 225 and self._degrees <= 315:
            return 'W'
        else:
            raise ValueError(f"Invalid heading:{self._degrees}")

    @property
    def coordinate_direction_precise(self):
        """
        Directional heading in terms of where a 1-unit move in that direction would end up.
        """

        angle = (self._degrees * math.pi) / 180

        return math.cos(angle), math.sin(angle)

    @property
    def coordinate_direction(self):
        """
        Directional heading in terms of where a 1-unit move in that direction would end up, supporting only 8-way
        movement.
        """

        xcoord = ycoord = 0

        # moving north
        if self._degrees > 337 or self._degrees <= 22:
            ycoord = -1
        # northeast
        elif self._degrees > 22 and self._degrees <= 67:
            ycoord = -_DIAG_DIST
            xcoord = _DIAG_DIST
        # east
        elif self._degrees > 67 and self._degrees <= 112:
            xcoord = 1
        # southeast
        elif self._degrees > 112 and self._degrees <= 157:
            xcoord = ycoord = _DIAG_DIST
        # south
        elif self._degrees > 157 and self._degrees <= 202:
            ycoord = 1
        # southwest
        elif self._degrees > 202 and self._degrees <= 247:
            ycoord = _DIAG_DIST
            xcoord = -_DIAG_DIST
        # west
        elif self._degrees > 247 and self._degrees <= 292:
            xcoord = -1
        # northwest
        elif self._degrees > 292 and self._degrees <= 337:
            xcoord = ycoord = -_DIAG_DIST
        # impossible
        else:
            raise ValueError(f"Invalid heading:{self._degrees}")

        return xcoord, ycoord

    def __repr__(self):
        return f"degrees: {self._degrees}"

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

    # working from keyboard input, we'll always have magnitude 1 if valid move input present
    magnitude = 1

    if inputs & _MOVE_NORTH:
        # northeast
        if inputs & _MOVE_EAST:
            heading = 45
        # northwest
        elif inputs & _MOVE_WEST:
            heading = 315
        # north
        else:
            heading = 0
    elif inputs & _MOVE_SOUTH:
        # southeast
        if inputs & _MOVE_EAST:
            heading = 135
        # southwest
        elif inputs &_MOVE_WEST:
            heading = 225
        # south
        else:
            heading = 180
    # east
    elif inputs & _MOVE_EAST:
        heading = 90
    # west
    elif inputs & _MOVE_WEST:
        heading = 270
    # something went wrong
    else:
        # make it obvious if we got something unexpected by this point
        raise ValueError(f"Unable to parse input: {inputs:04b}")
    
    return InputMessage(heading, magnitude)


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