import pygame, sprites, input, gameenv, math

class Entity:
    """
    Represents an in-game entity.

    Graphical representation is managed in viewsprite (view).
    Functional representation is managed in modelsprite (model).
    """

    def __init__(self):
        self.viewsprite = None
        self.modelsprite = None

    def update(self):
        self.viewsprite.rect.center = round(self.modelsprite.rect.centerx * gameenv.scalingfactor), round(self.modelsprite.rect.centery * gameenv.scalingfactor)



def init():
    global entitymodels, entityviews
    
    entitymodels = pygame.sprite.Group()
    entityviews = pygame.sprite.Group()


    # set up player
    playerentity = Entity()

    playerentity.viewsprite = sprites.TestSprite(entityviews)
    playerentity.viewsprite.set_image_identifier('test')
    playerentity.viewsprite.rect.topleft = 120, 120

    playerentity.modelsprite = sprites.TestSprite(entitymodels)
    playerentity.modelsprite.rect.topleft = 1200, 1200
    playerentity.modelsprite.entity = playerentity

    def _playerupdate(self):
        vector = [0, 0]

        if self._current_message.move_north:
            vector[1] += -10
        if self._current_message.move_east:
            vector[0] += 10
        if self._current_message.move_south:
            vector[1] += 10
        if self._current_message.move_west:
            vector[0] += -10

        if vector != [0, 0]:
            self.rect.move_ip(vector[0], vector[1])
            self.entity.update()

    playerentity.modelsprite.update_strategy = _playerupdate

    input.add_subscriber(lambda message: playerentity.modelsprite.input(message))

    # set up block
    blockentity = Entity()
    blockentity.viewsprite = sprites.TestSprite(entityviews)
    blockentity.viewsprite.set_image_identifier('block')
    blockentity.viewsprite.rect.topleft = 500, 500