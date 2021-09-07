import pygame

_key_mapping = {
    pygame.K_UP     : 'move_north',
    pygame.K_RIGHT  : 'move_east',
    pygame.K_DOWN   : 'move_south',
    pygame.K_LEFT   : 'move_west'
}

class InputMessage:
    move_north = False
    move_east  = False
    move_south = False
    move_west  = False

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
    event_message = InputMessage()

    for engaged_key in _engaged_keys:
        if engaged_key in _key_mapping.keys():
            setattr(event_message, _key_mapping[engaged_key], True)

    if len(_engaged_keys) > 0:
        for subscriber in _subscribers:
            subscriber(event_message)