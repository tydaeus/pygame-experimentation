import sprites, input

class Entity:
    """
    Represents an in-game entity.

    Graphical representation is managed in viewsprite (view).
    Functional representation is managed in modelsprite (model).
    """

    def __init__(self):
        self.viewsprite = None
        self.modelsprite = None

def init():
    # set up player
    playerentity = Entity()
    playerentity.viewsprite = sprites.TestSprite(sprites.all_sprites)
    playerentity.viewsprite.set_image_identifier('test')
    playerentity.viewsprite.rect.topleft = 120, 120

    def _playerupdate(self):
        vector = [0, 0]

        if self._current_message.move_north:
            vector[1] += -1
        if self._current_message.move_east:
            vector[0] += 1
        if self._current_message.move_south:
            vector[1] += 1
        if self._current_message.move_west:
            vector[0] += -1

        if vector != [0, 0]:
            self.rect.move_ip(vector[0], vector[1])

    playerentity.viewsprite.update_strategy = _playerupdate

    input.add_subscriber(lambda message: playerentity.viewsprite.input(message))

    # set up block
    blockentity = Entity()
    blockentity.viewsprite = sprites.TestSprite(sprites.all_sprites)
    blockentity.viewsprite.set_image_identifier('block')
    blockentity.viewsprite.rect.topleft = 500, 500