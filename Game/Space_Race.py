import pygame
from banner import Banner
from shape_transformations import Point,ShapeTransforms
from start_button import StartButton
from gamesprite import GameSprite
from level import Level

import time


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE= (255, 165, 0) 
 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def main():
    pygame.init()
    pygame.display.set_caption("Space Race")

    crash_sound = pygame.mixer.Sound("Game/crash.wav")
    bkgd_sound = pygame.mixer.Sound("Game/Trouble-On-Mercury.mp3")
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    screen.fill(ORANGE)
    screen_midpoint = Point(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    banner = Banner(screen_midpoint)
    banner.draw(screen, "Space Race", RED, WHITE)

    startButton = StartButton(screen_midpoint)
    startButton.draw(screen, "Start", BLUE, WHITE) 
    player = GameSprite("Game/spaceship.png",80,80)
    player.shrink_radius(0.7)

    level = Level(SCREEN_WIDTH,SCREEN_HEIGHT)
    level.shift_world(0, 0)

    clock = pygame.time.Clock()
    done = False

    speed = 5

    start_time = time.perf_counter()
    elapsed_time = 0
    
    def reset_game():
        nonlocal level, player, startButton, speed, elapsed, start_time
        level = Level(SCREEN_WIDTH, SCREEN_HEIGHT)
        player = GameSprite("Game/spaceship.png", 80, 80)
        player.shrink_radius(0.7)
        speed = 5
        bkgd_sound.play()
        start_time = time.perf_counter()
        elapsed_time = 0

    while not done:
        mouse_x=mouse_y = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif  event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Fixed typo and logic
                    if (speed + 1 < 11):
                        speed += 1
                        pygame.mixer.music.load("Game/speedup.mp3")
                        # play(loops, start_time_in_seconds)
                        pygame.mixer.music.play(0, 1) #  # play piece of the file
                elif event.key == pygame.K_DOWN:
                    if (speed - 1 > 4):
                        speed -= 1
                        pygame.mixer.music.load("Game/speeddn.ogg")
                        pygame.mixer.music.play(0, 0.51) # play piece of the file
 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            level.shift_world(speed, 0)
        if keys[pygame.K_RIGHT]:
            level.shift_world(-speed, 0)


        if not startButton.visible:
            level.shift_world(0, speed)
            hits = pygame.sprite.spritecollide(player, level.meteorfield_list, False,pygame.sprite.collide_circle)
        
            if hits and len(hits) > 0:
                font = pygame.font.SysFont("Arial", 36)
                crashedText = "Crashed!"
                text_surface = font.render(crashedText, True,RED)
                bkgd_sound.stop()
                crash_sound.play()
                f_w, f_h = font.size(crashedText)
                screen.blit(text_surface, (screen_midpoint.x - f_w//2,screen_midpoint.y-f_h//2))
                pygame.display.flip()
                startButton.visible
                pygame.time.delay(2000)
                crash_sound.stop()
                reset_game()

            screen.blit(background_image, [0, 0])
            player.rect.x = screen_midpoint.x-player.width//2
            player.rect.y = screen_midpoint.y+100
            player.draw(screen,player.rect.x,player.rect.y)
            level.draw(screen)

            font = pygame.font.SysFont("Arial", 36)
            speedText = f"Speed: {speed}"
            text_surface = font.render(speedText, True,BLUE)
            f_w, f_h = font.size(speedText)
            screen.blit(text_surface, (screen_midpoint.x + f_w//4,SCREEN_HEIGHT-(f_h+5)))

            end_time = time.perf_counter()
            elapsed = int(end_time - start_time )
            timeText = f"Time: {elapsed:05}"
            text_surface = font.render(timeText, True,GREEN)
            f_w, f_h = font.size(timeText)
            screen.blit(text_surface, (10,SCREEN_HEIGHT-(f_h+5)))

            # #debug collision circles
            # #Draw player collision circle
            # pygame.draw.circle(screen, (255, 0, 0), player.rect.center, player.radius, 2)

            # # Draw meteor collision circles
            # for meteor in level.meteorfield_list:
            #     pygame.draw.circle(screen, (255, 0, 0), meteor.rect.center, meteor.radius, 2)


 
        if startButton.isClicked(mouse_x,mouse_y):
            background_image = pygame.image.load("Game//spacebackdrop.jpg").convert()
            startButton.visible=False 
            bkgd_sound.play()



        clock.tick(60) 
        pygame.display.flip()
    
    wait_for_key()
    pygame.quit()

if __name__ == "__main__":
    main()
 
 
 