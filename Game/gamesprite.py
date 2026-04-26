import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 1. Load image and keep transparency channel
        sprite = pygame.image.load("Game/spaceship.png").convert_alpha() 
        first_color = sprite.get_at((0, 0))
        # 2. Set the colorkey
        sprite.set_colorkey(first_color)

        # 3. Create target surface with transparent alpha
        self.image = pygame.Surface([80,80], pygame.SRCALPHA) 
        self.image.blit(sprite, [0, 0])
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
    def draw(self, screen, x,y):
        screen.blit(self.image, [x,y])