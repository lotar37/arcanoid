import pygame
import sys
import pygame_template
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()