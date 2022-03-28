import pygame
import sys
import polygon

FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 800
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
GREEN = (100, 255, 100)


clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))

# радиус будущего круга
r = 30
# координаты круга
# скрываем за левой границей
x = 0 - r
# выравнивание по центру по вертикали
y = WIN_HEIGHT // 2

xR = 40
yR = 40
stepR = 5

p = polygons(x, y, r, GREEN, sc)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # заливаем фон
    sc.fill(WHITE)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,
                       (x, y), r)
    # рисуем квадарат
    p.draw()
    # pygame.draw.rect(sc, GREEN, (xR, yR, r, r))
    # обновляем окно
    pygame.display.update()

    # Если круг полностью скрылся
    # за правой границей,
    if x >= WIN_WIDTH + r:
        # перемещаем его за левую
        x = 0 - r
    else:  # Если еще нет,
        # на следующей итерации цикла
        # круг отобразится немного правее
        x += 2
    if xR + r >= WIN_WIDTH or xR <= 0:
        stepR = -stepR
    xR += stepR

    clock.tick(FPS)