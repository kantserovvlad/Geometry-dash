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


class Button(pygame.sprite.Sprite):
    def __init__(self, point, image, image_press, action):
        super().__init__(all_sprites)
        self.action = action
        self.flag_press = False
        self.image = load_image(image)
        self.image_press = load_image(image_press)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = point

    def update(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and \
                self.rect.collidepoint(event.pos):
            self.flag_press = True
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y

        if event.type == pygame.MOUSEMOTION and self.flag_press:
            if not self.rect.collidepoint(event.pos):
                self.flag_press = False
                x, y, = self.rect.center
                self.image, self.image_press = self.image_press, self.image
                self.rect = self.image.get_rect()
                self.rect.center = x, y

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            exec(self.action)
            self.flag_press = False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 440
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))

    pygame.mixer.music.load('music/start.mp3')  # загружаем фоновую музыку
    pygame.mixer.music.play()

    # Создаём группы спрайтов
    all_sprites = pygame.sprite.Group()

    # -------------------------Создаём кнопки------------------------------------------------
    Button((screen.get_width() // 2, screen.get_height() // 2),
           'buttons/play.png', 'buttons/play-press.png', '')
    Button((screen.get_width() // 2 - 120, screen.get_height() // 2),
           'buttons/change_cube.png', 'buttons/change_cube-press.png', '')
    Button((screen.get_width() // 2, screen.get_height() * 0.7),
           'buttons/settings-a.png', 'buttons/settings-a.png', '')
    Button((screen.get_width() // 2 + 120, screen.get_height() // 2),
           'buttons/editor_level.png', 'buttons/editor_level-press.png', '')
    # -----------------------Основные параметры-----------------------------------------------
    fps = 100
    clock = pygame.time.Clock()

    running = True
    point_cube = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                all_sprites.update(event)
            if event.type == pygame.MOUSEMOTION:
                all_sprites.update(event)
        screen.blit(load_image('backgrounds/fon1.jpg'), (0, 0))
        screen.blit(load_image("Name_game.png"), (width // 2 - 200, 100))
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.quit()
