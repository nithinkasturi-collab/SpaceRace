import pygame
from banner import Banner
from shape_transformations import Point,ShapeTransforms

#
 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE= (255, 165, 0) 
 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    pygame.init()
    pygame.display.set_caption("Space Race")

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    screen.fill(ORANGE)
    screen_midpoint = Point(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    banner = Banner(screen_midpoint)
    banner.draw(screen, "Space Race", RED, WHITE)

    

    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
        clock.tick(60) 
        pygame.display.flip()
    
    pygame.quit()
 
if __name__ == "__main__":
    main()
 
 
 