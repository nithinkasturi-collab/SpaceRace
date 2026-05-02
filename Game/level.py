import pygame
import random
from gamesprite import GameSprite

class Level:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        try:
            spriteSheet = pygame.image.load("Game/bigbrownmeteorspritesheet.png").convert_alpha()
        except:
            spriteSheet = pygame.Surface((410, 160))
            spriteSheet.fill((100, 100, 100))

        self.meteors = []
        s_w = 102
        s_h = 80

        for row in range(2):
            for col in range(2):
                rect = pygame.Rect(col * s_w, row * s_h, s_w, s_h)
                image = pygame.Surface((s_w, s_h), pygame.SRCALPHA)
                image.blit(spriteSheet, (0, 0), rect)
 
                # don't add meteors that are just dust like pixels
                mask = pygame.mask.from_surface(image)
                if mask.count() > 500:  # Adjust this number based on your sprite size
                    self.meteors.append(image)

        self.meteorfield_list = pygame.sprite.Group()

        # 2. Generate meteors with spacing logic
        for i in range(15): 
            image = random.choice(self.meteors)
            new_meteor = GameSprite(image, s_w, s_h)
            new_meteor.radius = 40
            new_meteor.shrink_radius(0.85)

            # make the meteors like a field of meteors            
            new_meteor.rect.x = random.randint(0, (self.screen_width - s_w) // 10) * 10
            
            # Spread them far apart vertically
            # This makes ure they don't appear on top of each other
            new_meteor.rect.y = random.randint(-5000, -800)
            
            self.meteorfield_list.add(new_meteor)

    def shift_world(self, shift_x, shift_y):
        """
        Scrolls all meteors. 
        Positive shift_y moves them down (flying forward).
        Positive shift_x moves them right (player moving left).
        """
        for meteor in self.meteorfield_list:
            meteor.rect.y += shift_y
            meteor.rect.x += shift_x # Add horizontal movement

            if meteor.rect.top > self.screen_height:
                meteor.rect.y = random.randint(-1000, -100)
                meteor.rect.x = random.randint(0, self.screen_width - meteor.rect.width)
            
            elif meteor.rect.bottom < -1000:
                meteor.rect.y = self.screen_height


    def draw(self, screen):
        self.meteorfield_list.draw(screen)
