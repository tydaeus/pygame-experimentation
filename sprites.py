import pygame, image_loader


class ViewSprite(pygame.sprite.Sprite):
    """
    Represents a rendering of the entity
    """

    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        self.rect = pygame.Rect(0, 0, 0, 0)

        self._image_identifier = None
        self.image = None
        self._pxsize = 100, 100

    def set_image_identifier(self, identifier):
        if self._image_identifier != identifier:
            self._image_identifier = identifier
            self.image = image_loader.load_image(identifier)
            self.rect.size = self.image.get_width(), self.image.get_height()
            self._scale_image()

    def _scale_image(self):
        if (self.image.get_width(), self.image.get_height()) != self._pxsize:
            self.image = pygame.transform.scale(self.image, self._pxsize)


class ModelSprite(pygame.sprite.Sprite):
    """
    Represents an entity's model.
    """

    def __init__(self, entity, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        self.entity = entity
        self.rect = pygame.Rect(0, 0, 0, 0)

    def update(self, *args, **kwargs):
        'Request that the entity handle updating the model.'
        self.entity.update(*args, **kwargs)
