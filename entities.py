import pygame, sprites, input, gameenv

class Entity:
    """
    Represents an in-game entity.

    Graphical representation is managed in _viewsprite (view).
    Functional representation is managed in _modelsprite (model).
    """

    def __init__(self):
        # Future: support multiple views
        self._viewsprite = sprites.ViewSprite(entityviews)
        self._modelsprite = sprites.ModelSprite(self, entitymodels)
        self._messages = []
        self._updatestrategy = None
        # track whether updates have occurred
        self._lastcenter = (0,0)
        self._lastsize = (0,0)
        self._speed = 10

    def update(self, *args, **kwargs):

        if callable(self._updatestrategy):
            for message in self._messages:
                self._updatestrategy(self, message)

        if tuple(self.center) != self._lastcenter:
            self._viewsprite.center = gameenv.scalemodel(*self.center)

        if tuple(self.size) != self._lastsize:
            self._viewsprite.size = gameenv.scalemodel(*self.size)

        self._messages = []

        self._lastcenter = self.center
        self._lastsize = self.size


    def input(self, message):
        self._messages.append(message)

    def move(self, xshift, yshift):
        self._modelsprite.rect.move_ip(xshift, yshift)

    def can_move(self, xshift, yshift):
            """
            Returns whether the proposed move can be performed.
            """
            # Future: handle cases where a partial move can be performed

            # do a bit of swapping so that we can check the destination without forcing a move
            target_position = self._modelsprite.rect.move(xshift, yshift)
            original_position = self._modelsprite.rect
            self._modelsprite.rect = target_position

            collisions = pygame.sprite.spritecollide(self._modelsprite, entitymodels, False)

            movable = True
            
            for collision in collisions:
                if collision == self._modelsprite:
                    pass
                else:
                    movable = False
                    break
            
            self._modelsprite.rect = original_position

            return movable


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
        originalcenter = self._modelsprite.rect.center
        self._modelsprite.rect.size = value
        self._modelsprite.rect.center = originalcenter


    @property
    def width(self):
        'Width of model.'
        return self._modelsprite.rect.width

    @width.setter
    def width(self, value):
        centerx = self._modelsprite.rect.centerx
        self._modelsprite.rect.width = value
        self._modelsprite.rect.centerx = centerx
    

    @property
    def height(self):
        'height of model.'
        return self._modelsprite.rect.height

    @height.setter
    def height(self, value):
        centery = self._modelsprite.rect.centery
        self._modelsprite.rect.height = value
        self._modelsprite.rect.centery = centery


    @property
    def imageid(self):
        'Determines image(set) used to render the view.'
        return self._viewsprite._image_identifier

    @imageid.setter
    def imageid(self, value):
        self._viewsprite.imageid = value




def init():
    global entitymodels, entityviews
    
    entitymodels = pygame.sprite.Group()
    entityviews = pygame.sprite.Group()


    # set up player
    playerentity = Entity()
    playerentity.imageid = 'test'
    playerentity.size = 1000, 1000
    playerentity.center = 1200, 1200

    def _playerupdate(self, message):
        xshift = yshift = 0

        if message.move_north:
            yshift += -self._speed
        if message.move_east:
            xshift += self._speed
        if message.move_south:
            yshift += self._speed
        if message.move_west:
            xshift += -self._speed

        if xshift or yshift:
            if self.can_move(xshift, yshift):
                self.move(xshift, yshift)

    playerentity._updatestrategy = _playerupdate

    input.add_subscriber(lambda message: playerentity.input(message))

    # set up block
    blockentity = Entity()
    blockentity.imageid = 'block'
    blockentity.center = 5000, 5000
    blockentity.size = 1000, 1000
