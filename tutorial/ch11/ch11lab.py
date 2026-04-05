import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK,[96+x,83+y,10,10],0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [100+x,100+y], [105+x,110+y], 2)
    pygame.draw.line(screen, BLACK, [100+x,100+y], [95+x,110+y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [100+x,100+y], [100+x,90+y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [100+x,90+y], [104+x,100+y], 2)
    pygame.draw.line(screen, RED, [100+x,90+y], [96+x,100+y], 2)

def main():
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Move Stick Figure")
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    done = False
    x = y = 50
    pygame.mouse.set_visible(0)
    background_image = pygame.image.load("tutorial/ch11/backdrop.jpeg").convert()
    player_image = pygame.image.load("tutorial/ch11/player.png").convert()
    player_image.set_colorkey(WHITE)
    walk_sound = pygame.mixer.Sound("tutorial/ch11/walk.ogg")
    while not done:
        # --- Main event loop 
        for event in pygame.event.get():

            prevx = x
            prevy = y
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 3
                elif event.key == pygame.K_RIGHT:
                    x += 3
                elif event.key == pygame.K_UP:
                     y -= 3
                elif event.key == pygame.K_DOWN:
                     y += 3
                walk_sound.play()
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                walk_sound.play()
                
        screen.blit(background_image, [0, 0])
    
        screen.blit(player_image, [x,y])
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()