import pygame
import math
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
class Shape(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 50
        self.y = 50
        self.change_x = 5
        self.change_y = 5
        self.move_change = False
    def movelinear(self, x):
        m=1
        b=50
        y=m*x+b
        return y
    def movetrig(self,x):
        speed = 5
        waviness=50
        center=200
        y=math.sin(x*speed)*waviness+center
        return y
    def move(self):
        self.x += self.change_x;
 
        if (self.move_change):
            self.y = self.movetrig(self.x)
        else:
            self.y = self.movelinear(self.x) 
    
        edge = False
        if self.x > 649 or self.x < 0:
            self.change_x = self.change_x * -1
            edge = True
        if self.y > 449 or self.y < 0:
            self.change_x = self.change_x * -1
            edge = True
        
        if edge:
            self.move_change = not self.move_change

class Rect(Shape):
    def __init__(self):
        super().__init__()
        self.width=50
        self.height=50
    def draw (self, screen):
        pygame.draw.rect(screen,WHITE,(self.x,self.y,self.width,self.height))
 
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius=30
        self.x=130
    def draw (self, screen):
        pygame.draw.circle(screen,WHITE,(self.x,self.y),self.radius)   