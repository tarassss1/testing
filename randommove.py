import pygame
import random

pygame.init()

back = (255, 255, 255)
window = pygame.display.set_mode((500, 500))
window.fill(back)
pygame.display.update()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

enemies = []
for e in range(11):
    x = random.randint(0, 500)
    y = 20
    enemy = Picture('name.png', x, y, 20, 20)
    # Випадкова швидкість для кожного ворога
    enemy.speed = random.randint(1, 5)  
    ########################################
    enemies.append(enemy)

move_r = False
move_l = False
ball = Picture('name.png', 200, 400, 50, 50)

clock = pygame.time.Clock()
game = True

while game:
    ball.fill()
    for e in enemies:
        e.fill()

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                move_r = True
            if e.key == pygame.K_a:
                move_l = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_d:
                move_r = False
            if e.key == pygame.K_a:
                move_l = False

    if move_r:
        ball.rect.x += 10
    if move_l:
        ball.rect.x -= 10

    # Рух персонажів від початку до кінця
    for enemy in enemies:
        enemy.rect.x += enemy.speed

        # Перевірка, чи ворог дійшов до кінця вікна
        if enemy.rect.x < 0:
            enemy.rect.x = 0
            enemy.speed = -enemy.speed  # Зміна напрямку руху
        if enemy.rect.x > 500 - enemy.rect.width:
            enemy.rect.x = 500 - enemy.rect.width
            enemy.speed = -enemy.speed  # Зміна напрямку руху
    ##############################################################

    window.fill(back)
    ball.draw()
    for enemy in enemies:
        enemy.draw()

    pygame.display.update()
    clock.tick(50)

pygame.quit()
