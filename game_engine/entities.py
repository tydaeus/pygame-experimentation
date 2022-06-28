import pygame
from . import sprites, input

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
        self.imageid = None
        self.heading = None
        # track whether updates have occurred
        self._lastcenter = (0,0)
        self._lastsize = (0,0)
        self._speed = 10
        self._lastimageid = None

    def update(self, *args, **kwargs):

        if callable(self._updatestrategy):
            for message in self._messages:
                self._updatestrategy(self, message)

        if tuple(self.center) != self._lastcenter or \
            tuple(self.size) != tuple(self._lastsize) or \
            self.imageid != self._lastimageid:

            self._viewsprite.update(self)

        self._messages = []

        self._lastcenter = self.center
        self._lastsize = self.size


    def input(self, message):
        self._messages.append(message)

    def move(self, xshift, yshift):
        """
        Moves the model by the specified amount. Use how_traversible and/or can_move first to check whether the move is
        legal.
        """
        self._modelsprite.rect.move_ip(xshift, yshift)

    def how_traversible(self, xshift, yshift):
        """
        Returns how much of the desired move can be performed, including by sliding.
        """

        result_x = result_y = 0
        # incrementers
        ix = iy = 0

        if xshift < 0: ix = -1
        elif xshift > 0: ix = 1

        if yshift < 0: iy = -1
        elif yshift > 0: iy = 1

        while abs(xshift) > 0 or abs(yshift) > 0:
            attemptx = ix if xshift else 0
            attempty = iy if yshift else 0

            # always decrement
            xshift -= ix
            yshift -= iy

            # try moving diagonally (if applicable) first
            if self.can_move(result_x + attemptx, result_y + attempty):
                result_x += attemptx
                result_y += attempty
            # fallback to orthogonal movement
            else:
                if attemptx and self.can_move(result_x + attemptx, 0):
                    result_x += attemptx
                elif attempty and self.can_move(0, result_y + attempty):
                    result_y += attempty
                else:
                    break
        
        return result_x, result_y


    def can_move(self, xshift, yshift):
            """
            Returns whether the proposed move can be performed.
            """

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
    def heading(self):
        return self._heading
    
    @heading.setter
    def heading(self,value):
        self._heading = value


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
        return self._imageid

    @imageid.setter
    def imageid(self, value):
        self._imageid = value




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

        if message.heading:
            self.heading = message.heading

        if message.magnitude <= 0:
            return

        magnitude_speed = message.magnitude * self._speed

        xshift, yshift = message.heading.coordinate_direction
        xshift = int(xshift * magnitude_speed)
        yshift = int(yshift * magnitude_speed)

        if xshift or yshift:
            xactual, yactual = self.how_traversible(xshift, yshift)
            if xactual or yactual:
                self.move(xactual, yactual)

    playerentity._updatestrategy = _playerupdate

    input.add_subscriber(lambda message: playerentity.input(message))

    # set up block
    blockentity = Entity()
    blockentity.imageid = 'block'
    blockentity.center = 2500, 2500
    blockentity.size = 1000, 1000
