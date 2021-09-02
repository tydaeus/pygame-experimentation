import pygame, image_loader



class TestSprite(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self, *args)

        self.image = image_loader.load_image('test')
        self.rect = pygame.Rect(120, 120, self.image.get_width(), self.image.get_height())

    def update(self):
        # placeholder
        pass

def init():
    global all_sprites
    all_sprites = pygame.sprite.Group()
    TestSprite(all_sprites)