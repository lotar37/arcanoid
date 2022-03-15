# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    # Цикл игры
    running = True
    count = 0
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        count += 1
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        if count % FPS == 0:
            pygame.display.set_caption("cекунда " + str(count // FPS))

    pygame.quit()

if __name__ == "__main__":
    main()
else:
    print("подключен модуль pygame_template")
