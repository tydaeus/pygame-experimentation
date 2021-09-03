import pygame, image_loader



class TestSprite(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self, *args)
        self.image_identifier = None
        self.image = None
        self.rect = pygame.Rect(0, 0, 0, 0)

    def update(self):
        # placeholder
        pass

    def set_image_identifier(self, identifier):
        if self.image_identifier != identifier:
            self.image_identifier = identifier
            self.image = image_loader.load_image(identifier)
            self.rect.size = self.image.get_width(), self.image.get_height()
    


def init():
    global all_sprites
    all_sprites = pygame.sprite.Group()

    testSprite = TestSprite(all_sprites)
    testSprite.set_image_identifier('test')
    testSprite.rect.topleft = 120, 120