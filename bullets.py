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

# Створення класу для створення пуль
class Bullet(Area):
    def __init__(self, x, y):
        super().__init__(x, y, 5, 10, (255, 0, 0))
        self.speed = 10
    # функція, яка реалізує постійний рух пуль
    def move(self):
        self.rect.y -= self.speed
######################################

enemies = []
for e in range(11):
    x = random.randint(0, 450)
    y = 20
    enemy = Picture('name.png', x, y, 20, 20)
    enemies.append(enemy)

# Створення пустого списку для збереження пуль
bullets = []
######################################

move_r = False
move_l = False
game = True
ball = Picture('name.png',200,400,50,50)
clock = pygame.time.Clock()

while game:
    for e in enemies:
        e.fill()

    # Генерація пуль та виклик функції, яка робить постійний рух рух
    for bullet in bullets:
        bullet.fill()
        bullet.move()
        if bullet.rect.y < 0:
            bullets.remove(bullet)
    ######################################

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                move_r = True
            if e.key == pygame.K_a:
                move_l = True
            if e.key == pygame.K_r:
                x = ball.rect.x + ball.rect.width // 2 - 2
                y = ball.rect.y
                bullet = Bullet(x, y)
                bullets.append(bullet)

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_d:
                move_r = False
            if e.key == pygame.K_a:
                move_l = False

    if move_r:
        ball.rect.x += 10
    if move_l:
        ball.rect.x -= 10

    window.fill(back)
    ball.draw()
    for e in enemies:
        e.draw()

    # Відображення пуль на екрані
    for bullet in bullets:
        bullet.move()
        bullet.fill()
    ######################################

    # Перевірка зіткнення пуль з ворогами
    for enemy in enemies:
        for bullet in bullets:
            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
    ######################################

    pygame.display.update()
    clock.tick(50)

pygame.quit()
