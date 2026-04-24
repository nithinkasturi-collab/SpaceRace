import pygame

from shape_transformations import Point, ShapeTransforms


class StartButton(list):
    def __init__(self,screen_midpoint:Point):
        super().__init__()
        self.width=200
        self.height=60
        self.distance=100
        self.visible = False
        button_v1 = Point(screen_midpoint.x-self.width//2,screen_midpoint.y+ self.distance + self.height//2)
        button_v2 = ShapeTransforms.translate(button_v1,deltaX=0,deltaY=-self.height)
        button_v3 = ShapeTransforms.translate(button_v2,deltaX=self.width,deltaY=0)
        button_v4 = ShapeTransforms.translate(button_v3,deltaX=0,deltaY=self.height)
        button_image = [button_v1, button_v2,button_v3,button_v4,button_v1]
        self.extend(button_image)

    def draw(self, screen, text, bannerColor, textColor):
        my_font = pygame.font.SysFont('Arial', 20,True)
        text_surface = my_font.render(text, True, textColor)
        pygame.draw.polygon(screen,bannerColor,self)
        textX = ShapeTransforms.midPoint(self[0].x,self[3].x)
        textY = ShapeTransforms.midPoint(self[1].y,self[0].y)
        text_width = my_font.size(text)[0] // 2
        text_height = my_font.size(text)[1] // 2
        textPoint = Point(textX-text_width,textY-text_height)
        screen.blit(text_surface, textPoint)

        self.visible = True

    def isClicked(self, x,y):
        if not self.visible or x is None or y is None:
            return False
        bx = self[0][0]
        by = self[0][1]
        width = bx + self.width
        height = by - self.height
        print(x,y,bx,by,width,height)
        if x >= bx and x <= width and y <= by and y >= height: 
            return True
        return False
            