import os
import sys
import pygame
from custom_cube import custom_cube


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
            if event.type == pygame.MOUSEBUTTONDOWN and exit.rect.collidepoint(event.pos):
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                settings_sprites.update(event)
        screen.blit(load_image_buttons('../backgrounds/fon1.jpg'), (0, 0))
        clock.tick(fps)
        draw_settings(screen)
        settings_sprites.draw(screen)
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
    text = font.render("Настройки", True, (0, 255, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height * 0.1
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


def load_image_buttons(name, colorkey=None):
    fullname = os.path.join('images/buttons', name)
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


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 20

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y


class Play(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image_buttons("play.png")
        self.image_press = load_image_buttons('play-press.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    def update(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and \
                self.rect.collidepoint(event.pos):
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y


class CubeStyle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.flag_press = False
        self.image = load_image_buttons("change_cube.png")
        self.image_press = load_image_buttons('change_cube-press.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (screen.get_width() // 2 - 120, screen.get_height() // 2)

    def update(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and \
                self.rect.collidepoint(event.pos):
            self.flag_press = True
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            custom_cube(screen, size)
            self.flag_press = False


class EditorLevel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.flag_press = False
        self.image = load_image_buttons("editor_level.png")
        self.image_press = load_image_buttons('editor_level-press.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (screen.get_width() // 2 + 120, screen.get_height() // 2)

    def update(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and \
                self.rect.collidepoint(event.pos):
            self.flag_press = True
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            settings_window(screen)
            self.flag_press = False


class Rate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(settings_sprites)
        self.image = load_image("rate.png", (127, 127, 127))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = width * 0.15, height * 0.3
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            print(self.mask)
            troll_window(screen, size)


class Tips(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(settings_sprites)
        self.image = load_image("tips.png", (127, 127, 127))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = width * 0.6, height * 0.3
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            pass


class Exit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(troll_sprites, settings_sprites)
        self.flag_press = False
        self.image = load_image("exit.png", "white")
        self.image_press = load_image("exit_pressed.png", "white")
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = width * 0.025, height * 0.07
        self.mask = pygame.mask.from_surface(self.image)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 850, 450
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images\icon.png"))

    fps = 100
    v = 40
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    settings_sprites = pygame.sprite.Group()
    troll_sprites = pygame.sprite.Group()
    exit = Exit()
    rate = Rate()
    tips = Tips()

    board = Board(40, 25)
    play = Play()
    cube_style = CubeStyle()
    editor_level = EditorLevel()

    pygame.mixer.music.load('music\start.mp3')
    pygame.mixer.music.play()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                all_sprites.update(event)
        screen.blit(load_image_buttons('../backgrounds/fon1.jpg'), (0, 0))
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.quit()
