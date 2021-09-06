import pygame, image_loader, input



class TestSprite(pygame.sprite.Sprite):
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

