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
        self._messages = []
        self._updatestrategy = None

    def update(self):
        if callable(self._updatestrategy):
            for message in self._messages:
                self._updatestrategy(self, message)
        
        self._messages = []
        self._viewsprite.rect.center = gameenv.scalemodel(*self.center)

    def input(self, message):
        self._messages.append(message)

    def move(self, xshift, yshift):
        self._modelsprite.rect.move_ip(xshift, yshift)

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
    playerentity._modelsprite.update_strategy = lambda self: self.entity.update()

    def _playerupdate(self, message):
        xshift = yshift = 0

        if message.move_north:
            yshift += -10
        if message.move_east:
            xshift += 10
        if message.move_south:
            yshift += 10
        if message.move_west:
            xshift += -10

        if xshift or yshift:
            self.move(xshift, yshift)

    playerentity._updatestrategy = _playerupdate

    input.add_subscriber(lambda message: playerentity.input(message))

    # set up block
    blockentity = Entity()
    blockentity._viewsprite = sprites.TestSprite(entityviews)
    blockentity._viewsprite.set_image_identifier('block')
    blockentity._viewsprite.rect.topleft = 500, 500