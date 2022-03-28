import pygame

class polygons:
    stepX = 5
    stepY = 5
    def __init__(self,x,y,R,color,sc):
        self.x = x
        self.y = y
        self.R = R
        self.color = color
        self.screen = sc

    def draw(self):
        if self.x + self.R >= WIN_WIDTH or self.x <= 0:
            self.stepX = -self.stepX
        self.x += self.stepX

        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.R, self.R))

