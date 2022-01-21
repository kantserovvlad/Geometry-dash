import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('images/', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.is_jump = False
        self.up = False
        self.down = False
        self.angle = 0
        self.image = load_image("cube/cube.png", "white")
        self.orig_image = self.rot_image = self.image = pygame.transform.scale(self.image, (40, 40))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = 150 + self.image.get_width(), height - (self.image.get_height() // 2)

    def jump(self):
        self.angle = 0
        x, y = self.rect.center
        y -= 10
        self.rect.center = x, y
        self.is_jump = True
        self.up = True

    def cjump(self):
        global flag
        x, y = self.rect.center
        if self.is_jump:
            self.angle -= 5
            self.rot_image = pygame.transform.rotate(self.orig_image, self.angle % 360)
            print(self.rot_image.get_rect(), "rotate:", self.angle)
            self.image = self.rot_image
            if y > 230 and self.up:
                y -= 10
                if y <= 230:
                    self.down = True
                    self.up = False
            if y < height - (self.image.get_height() // 2) and self.down:
                y += 10
                if y >= height - (self.image.get_height() // 2):
                    self.down = False
                    self.up = False
                    self.is_jump = False
                    flag = True
                    self.orig_image = self.image
                    print("Alles")
            self.rect.center = x, y


pygame.init()
size = width, height = 840, 440
screen = pygame.display.set_mode(size)

flag = True
all_sprites = pygame.sprite.Group()
player = Cube()
running = True

while running:
    pygame.time.delay(30)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if flag:
                    player.jump()
                    flag = False
    player.cjump()
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
