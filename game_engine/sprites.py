import pygame
from . import image_loader, gameenv


class ViewSprite(pygame.sprite.Sprite):
    """
    Represents a rendering of the entity
    """

    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        self.rect = pygame.Rect(0, 0, 0, 0)

        self._image_identifier = None
        self._changed = False
        self._heading = None
        self.image = None
        self.originalimage = None

    def update(self, entity, *args):
        self.imageid = entity.imageid
        self.center = gameenv.scalemodel(*entity.center)
        self.size = gameenv.scalemodel(*entity.size)
        self.heading = entity.heading

        if self._changed:
            self.reload_image()
            self._changed = False

    def reload_image(self):
        originalcenter = self.center
        self.originalimage = image_loader.load_image(self)
        self.image = self.originalimage
        self.center = originalcenter

    @property
    def imageid(self):
        'Identifier used to load and render the view.'
        return self._image_identifier

    @imageid.setter
    def imageid(self, value):
        if self._image_identifier != value:
            self._changed = True
            self._image_identifier = value


    @property
    def center(self):
        return self.rect.center

    @center.setter
    def center(self, centerxy):
        self.rect.center = centerxy

    @property
    def size(self):
        return self.rect.size

    @size.setter
    def size(self, value):
        if tuple(self.rect.size) != tuple(value):
            # preserve original center, otherwise a change in size moves away from it
            originalcenter = self.rect.center
            self.rect.size = value
            self.rect.center = originalcenter

            self._changed = True

    
    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        if self._heading != value:
            self._heading = value
            self._changed = True


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
