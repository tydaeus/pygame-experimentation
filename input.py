import pygame


MOVE_NORTH = 0b1000
MOVE_EAST  = 0b0100
MOVE_SOUTH = 0b0010
MOVE_WEST  = 0b0001

_key_mapping = {
    pygame.K_UP     : MOVE_NORTH,
    pygame.K_RIGHT  : MOVE_EAST,
    pygame.K_DOWN   : MOVE_SOUTH,
    pygame.K_LEFT   : MOVE_WEST
}

_subscribers = []

def add_subscriber(subscriber):
    _subscribers.append(subscriber)

_engaged_keys = set()

def process_event(event):
    if event.type == pygame.KEYDOWN:
        _engaged_keys.add(event.key)
    if event.type == pygame.KEYUP:
        _engaged_keys.remove(event.key)

def update():
    event_message = 0b0000

    for engaged_key in _engaged_keys:
        if engaged_key in _key_mapping.keys():
            event_message = event_message | _key_mapping[engaged_key]

    for subscriber in _subscribers:
        subscriber(event_message)