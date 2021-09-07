import pygame, sprites, input, gameenv, math

class Entity:
    """
    Represents an in-game entity.

    Graphical representation is managed in _viewsprite (view).
    Functional representation is managed in _modelsprite (model).
    """

    def __init__(self):
        self._viewsprite = None
        self._modelsprite = None

    def update(self):
        self._viewsprite.rect.center = gameenv.scalemodel(*self.center)


    @property
    def center(self):
        'The center of the model rect.'
        return self._modelsprite.rect.center

    @center.setter
    def center(self, centerxy):
        self._modelsprite.rect.center = centerxy


    @property
    def x(self):
        'X-coordinate of model center.'
        return self._modelsprite.rect.centerx
    
    @x.setter
    def x(self, value):
        self._modelsprite.rect.centerx = value


    @property
    def y(self):
        'Y-coordinate of model center.'
        return self._modelsprite.rect.centery
    
    @y.setter
    def y(self, value):
        self._modelsprite.rect.centery = value



    @property
    def size(self):
        'Width and length of model.'
        return self._modelsprite.rect.size

    @size.setter
    def size(self, value):
        self._modelsprite.rect.size = value


    @property
    def width(self):
        'Width of model.'
        return self._modelsprite.rect.width

    @width.setter
    def width(self, value):
        self._modelsprite.rect.width = value
    
    
    @property
    def height(self):
        'height of model.'
        return self._modelsprite.rect.height

    @height.setter
    def height(self, value):
        self._modelsprite.rect.height = value




def init():
    global entitymodels, entityviews
    
    entitymodels = pygame.sprite.Group()
    entityviews = pygame.sprite.Group()


    # set up player
    playerentity = Entity()

    playerentity._viewsprite = sprites.TestSprite(entityviews)
    playerentity._viewsprite.set_image_identifier('test')

    playerentity._modelsprite = sprites.TestSprite(entitymodels)
    playerentity.center = (1200, 1200)
    playerentity._modelsprite.entity = playerentity

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

    playerentity._modelsprite.update_strategy = _playerupdate

    input.add_subscriber(lambda message: playerentity._modelsprite.input(message))

    # set up block
    blockentity = Entity()
    blockentity._viewsprite = sprites.TestSprite(entityviews)
    blockentity._viewsprite.set_image_identifier('block')
    blockentity._viewsprite.rect.topleft = 500, 500