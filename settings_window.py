import pygame
import os
import sys
from main import load_image_buttons


def troll_window(screen, size):
    troll_screen = screen
    width, height = size
    exit = Exit()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and exit.rect.collidepoint(event.pos):
                running = False

        screen.blit(load_image_buttons('../backgrounds/fon1.jpg'), (0, 0))
        image = load_image("no_internet.png", "white")
        image = pygame.transform.scale(image, (300, 300))
        screen.blit(image, (width // 2 - image.get_width() // 2, height * 0.3))
        troll_sprites.draw(troll_screen)
        draw_text(troll_screen)
        pygame.display.flip()


def settings_window(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        screen.blit(load_image_buttons('../backgrounds/fon1.jpg'), (0, 0))
        clock.tick(fps)
        draw_settings(screen)
        all_sprites.draw(screen)
        pygame.display.flip()


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


def draw_text(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Невозможно подключиться к сети :(", True, (0, 255, 0))
    text_x = width * 0.2
    text_y = height * 0.1
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


def draw_settings(screen):
    font = pygame.font.Font(None, 80)
    text = font.render("Settings", True, (0, 255, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height * 0.1
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


class Rate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image("rate.png", (127, 127, 127))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = width * 0.15, height * 0.3
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            print(self.mask)
            troll_window(screen, size)


class Exit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(troll_sprites)
        self.image = load_image("exit.png", "white")
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = width * 0.025, height * 0.07
        self.mask = pygame.mask.from_surface(self.image)


pygame.init()
pygame.display.set_caption("Geometry dash")
size = width, height = 850, 450
screen = pygame.display.set_mode(size)

all_sprites = pygame.sprite.Group()
troll_sprites = pygame.sprite.Group()
rate = Rate()
buttons = {"tips.png": (width * 0.6, height * 0.3)}

for name, coords in buttons.items():
    sprite = pygame.sprite.Sprite(all_sprites)
    sprite.image = load_image(name, (127, 127, 127))
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x, sprite.rect.y = buttons[name]

fps = 100
clock = pygame.time.Clock()
settings_window(screen)

pygame.quit()
