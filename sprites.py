import pygame, image_loader, input



class _TestSprite(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        self._image_identifier = None
        self.image = None
        self.rect = pygame.Rect(0, 0, 0, 0)
        self._pxsize = 100, 100
        self._current_message = 0

    def update(self):
        vector = [0, 0]

        if self._current_message & input.MOVE_NORTH:
            print('NORTH')
            vector[1] += -1
        if self._current_message & input.MOVE_EAST:
            print('EAST')
            vector[0] += 1
        if self._current_message & input.MOVE_SOUTH:
            print('SOUTH')
            vector[1] += 1
        if self._current_message & input.MOVE_WEST:
            print('WEST')
            vector[0] += -1

        if vector != [0, 0]:
            self.rect.move_ip(vector[0], vector[1])

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

    testSprite = _TestSprite(all_sprites)
    testSprite.set_image_identifier('test')
    testSprite.rect.topleft = 120, 120

    input.add_subscriber(testSprite.input)