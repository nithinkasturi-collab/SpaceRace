import pygame
from banner import Banner
from shape_transformations import Point,ShapeTransforms
from start_button import StartButton
from gamesprite import GameSprite
from level import Level

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

    startButton = StartButton(screen_midpoint)
    startButton.draw(screen, "Start", BLUE, WHITE) 
    player = GameSprite("Game/spaceship.png",80,80)

    level = Level(SCREEN_WIDTH,SCREEN_HEIGHT)

    clock = pygame.time.Clock()
    done = False
    while not done:
        mouse_x=mouse_y = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif  event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
 
        level.shift_world(0, 5)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            level.shift_world(5, 0)
        if keys[pygame.K_RIGHT]:
            level.shift_world(-5, 0)
                
        if not startButton.visible:
            screen.blit(background_image, [0, 0])
            player.draw(screen,screen_midpoint.x-player.width//2,screen_midpoint.y+100)
            level.draw(screen)

 
        if startButton.isClicked(mouse_x,mouse_y):
            background_image = pygame.image.load("Game//spacebackdrop.jpg").convert()
            startButton.visible=False 


        
        














        clock.tick(60) 
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
 
 
 