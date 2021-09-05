import pygame, image_loader, input



class _TestSprite(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        self._image_identifier = None
        self.image = None
        self.rect = pygame.Rect(0, 0, 0, 0)
        self._pxsize = 100, 100
        self._current_message = 0
        self.update_strategy = None

    def update(self):
        if callable(self.update_strategy):
            self.update_strategy(self)

    def set_image_identifier(self, identifier):
        if self._image_identifier != identifier:
            self._image_identifier = identifier
            self.image = image_loader.load_image(identifier)
            self.rect.size = self.image.get_width(), self.image.get_height()
            self._scale_image()

    def _scale_image(self):
        if (self.image.get_width(), self.image.get_height()) != self._pxsize:
            self.image = pygame.transform.scale(self.image, self._pxsize)

    def input(self, message):
        self._current_message = message


def init():
    global all_sprites
    all_sprites = pygame.sprite.Group()

    # set up player
    playerSprite = _TestSprite(all_sprites)
    playerSprite.set_image_identifier('test')
    playerSprite.rect.topleft = 120, 120
    
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

    playerSprite.update_strategy = _playerupdate

    input.add_subscriber(lambda message: playerSprite.input(message))

    # set up block
    blockSprite = _TestSprite(all_sprites)
    blockSprite.set_image_identifier('block')
    blockSprite.rect.topleft = 500, 500