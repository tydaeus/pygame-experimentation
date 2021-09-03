import pygame, image_loader



class _TestSprite(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        self._image_identifier = None
        self.image = None
        self.rect = pygame.Rect(0, 0, 0, 0)
        self._pxsize = 100, 100

    def update(self):
        # placeholder
        pass

    def set_image_identifier(self, identifier):
        if self._image_identifier != identifier:
            self._image_identifier = identifier
            self.image = image_loader.load_image(identifier)
            self.rect.size = self.image.get_width(), self.image.get_height()
            self._scale_image()

    def _scale_image(self):
        if (self.image.get_width(), self.image.get_height()) != self._pxsize:
            self.image = pygame.transform.scale(self.image, self._pxsize)
    


def init():
    global all_sprites
    all_sprites = pygame.sprite.Group()

    testSprite = _TestSprite(all_sprites)
    testSprite.set_image_identifier('test')
    testSprite.rect.topleft = 120, 120