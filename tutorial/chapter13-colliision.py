import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.change_x = 5
    def  move(self):
        self.rect.topleft = (self.rect.left+self.change_x,self.rect.top)

# Create Sprites
rect1 = Rectangle(0, 150, 50, 50,RED)
rect2 = Rectangle(650, 150, 50, 50,GREEN)
rect2.change_x = -rect2.change_x;

all_sprites = pygame.sprite.Group()
all_sprites.add(rect1)
all_sprites.add(rect2)

rect_group = pygame.sprite.Group()
rect_group.add(rect2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect1.move();
    rect2.move();
    all_sprites.update();

    hits = pygame.sprite.spritecollide(rect1, rect_group, True)
    
    if hits:
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render("Crashed!", True,BLUE)
        screen.blit(text_surface, (0, 0))
        pygame.display.flip()
        break

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.time.wait(2000)
pygame.quit()
sys.exit()