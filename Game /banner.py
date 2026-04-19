import pygame

from shape_transformations import Point, ShapeTransforms


class Banner(list):
    def __init__(self,screen_midpoint:Point):
        super().__init__()
        self.width=600
        self.height=200
        banner_v1 = Point(screen_midpoint.x-self.width//2,screen_midpoint.x-self.height//2)
        banner_v2 = ShapeTransforms.translate(banner_v1,deltaX=0,deltaY=-self.height)
        banner_v3 = ShapeTransforms.translate(banner_v2,deltaX=self.width,deltaY=0)
        banner_v4 = ShapeTransforms.translate(banner_v3,deltaX=0,deltaY=self.height)
        banner_image = [banner_v1, banner_v2,banner_v3,banner_v4,banner_v1]
        self.extend(banner_image)

    def draw(self, screen, text, bannerColor, textColor):
        my_font = pygame.font.SysFont('Arial', 80,True)
        text_surface = my_font.render(text, True, textColor)
        pygame.draw.polygon(screen,bannerColor,self)
        textX = ShapeTransforms.midPoint(self[0].x,self[3].x)
        textY = ShapeTransforms.midPoint(self[1].y,self[0].y)
        text_width = my_font.size(text)[0] // 2
        text_height = my_font.size(text)[1] // 2
        textPoint = Point(textX-text_width,textY-text_height)
        screen.blit(text_surface, textPoint)