import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,file,width,height,sheetLoc=None):
        super().__init__()
        sprite=None
        self.radius = width // 2
        self.file = file
        if isinstance(file, (str)):
            sprite = pygame.image.load(file).convert_alpha() 
        elif isinstance(file,(pygame.Surface)):
            sprite = file

        first_color = sprite.get_at((0, 0))
        # 2. Set the colorkey
        
        sprite.set_colorkey(first_color)

        # 3. Create target surface with transparent alpha
        self.image = pygame.Surface([width,height], pygame.SRCALPHA)
        if sheetLoc is None:
            self.image.blit(sprite, [0, 0])
        else:
            self.image.blit(sprite, (0,0),sheetLoc)
        
        self.image.set_colorkey(first_color)
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        
    def shrink_radius(self, percent):
        self.radius = self.radius * percent

    def draw(self, screen, x,y):
        screen.blit(self.image, [x,y])