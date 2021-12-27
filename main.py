import os
import sys
import pygame
from PIL import Image, ImageDraw


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


def draw_tutorial(screen):
    font = pygame.font.Font(None, 80)
    text = font.render("Как играть?", True, (0, 255, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height * 0.1
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


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


def load_image_cube(name, colorkey=None):
    fullname = os.path.join('images/cube/', name)
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


def draw_cube(style_cube, color1, color2):
    width, height = 200, 200
    pic = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(pic)
    if style_cube == 1:
        drawer.rectangle(((width * 0.05, height * 0.05), (width * 0.95, int(height * 0.95))), color1)
        drawer.rectangle(((width * 0.225, height * 0.225), (width * 0.775, int(height * 0.775))), "black")

        drawer.rectangle(((width * 0.275, height * 0.275), (width * 0.725, int(height * 0.725))), (127, 127, 127))

        drawer.rectangle(((width * 0.375, height * 0.375), (width * 0.625, int(height * 0.625))), "black")
        drawer.rectangle(((width * 0.425, height * 0.425), (width * 0.575, int(height * 0.575))), color2)
    elif style_cube == 2:
        drawer.rectangle(((width * 0.05, height * 0.05), (width * 0.95, int(height * 0.95))), color1)
        drawer.rectangle(((width * 0.14, height * 0.19), (width * 0.36, int(height * 0.41))), "black")
        drawer.rectangle(((width * 0.175, height * 0.225), (width * 0.325, int(height * 0.375))), color2)

        drawer.rectangle(((width * 0.64, height * 0.19), (width * 0.86, int(height * 0.41))), "black")
        drawer.rectangle(((width * 0.675, height * 0.225), (width * 0.825, int(height * 0.375))), color2)

        drawer.rectangle(((width * 0.09, height * 0.69), (width * 0.91, int(height * 0.86))), "black")
        drawer.rectangle(((width * 0.125, height * 0.725), (width * 0.875, int(height * 0.825))), color2)
    elif style_cube == 3:
        drawer.rectangle(((width * 0.05, height * 0.05), (width * 0.95, int(height * 0.95))), color1)
        drawer.rectangle(((width * 0.24, height * 0.14), (width * 0.46, int(height * 0.36))), "black")
        drawer.rectangle(((width * 0.275, height * 0.175), (width * 0.425, int(height * 0.325))), color2)

        drawer.rectangle(((width * 0.54, height * 0.14), (width * 0.76, int(height * 0.36))), "black")
        drawer.rectangle(((width * 0.575, height * 0.175), (width * 0.725, int(height * 0.325))), color2)

        drawer.rectangle(((width * 0.14, height * 0.49), (width * 0.86, int(height * 0.71))), "black")
        drawer.rectangle(((width * 0.175, height * 0.525), (width * 0.825, int(height * 0.675))), color2)
    elif style_cube == 4:
        drawer.rectangle(((width * 0.05, height * 0.05), (width * 0.95, int(height * 0.95))), color1)
        drawer.rectangle(((width * 0.24, height * 0.14), (width * 0.46, int(height * 0.36))), "black")
        drawer.rectangle(((width * 0.275, height * 0.175), (width * 0.425, int(height * 0.325))), color2)

        drawer.rectangle(((width * 0.54, height * 0.14), (width * 0.76, int(height * 0.36))), "black")
        drawer.rectangle(((width * 0.575, height * 0.175), (width * 0.725, int(height * 0.325))), color2)
        drawer.line(((0, height * 0.67), (width, height * 0.67)), "black", width=10)

        drawer.rectangle(((width * 0.29, height * 0.49), (width * 0.47, height * 0.7)), "black")
        drawer.rectangle(((width * 0.53, height * 0.49), (width * 0.71, height * 0.7)), "black")

        drawer.rectangle(((width * 0.325, height * 0.525), (width * 0.435, height * 0.8)), "white")
        drawer.rectangle(((width * 0.565, height * 0.525), (width * 0.675, height * 0.8)), "white")

        drawer.rectangle(((0, height * 0.7), (width, height * 0.8)), "white")
        drawer.rectangle(((0, height * 0.8), (width, height * 0.85)), "black")
    text = ";".join([str(style_cube), str(color1), str(color2)])

    with open('color_cube.txt', encoding='utf8', mode="w") as f:
        f.write(text)

    pic.save("images\cube\cube.png")
    return pic


def troll_window(screen, size):
    troll_screen = screen
    width, height = size
    exit = Exit()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                settings_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                settings_sprites.update(event)
                if exit.rect.collidepoint(event.pos):
                    running = False

        screen.blit(load_image_buttons('../backgrounds/fon1.jpg'), (0, 0))
        image = load_image("no_internet.png", "white")
        image = pygame.transform.scale(image, (300, 300))
        screen.blit(image, (width // 2 - image.get_width() // 2, height * 0.3))
        troll_sprites.draw(troll_screen)
        draw_text(troll_screen)
        pygame.display.flip()


def tutorial_window(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                settings_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                settings_sprites.update(event)
                if exit.rect.collidepoint(event.pos):
                    running = False
        screen.blit(load_image_buttons('../backgrounds/fon1.jpg'), (0, 0))
        clock.tick(fps)
        draw_tutorial(screen)
        tutorial_sprites.draw(screen)
        pygame.display.flip()


def settings_window(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                settings_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                settings_sprites.update(event)
                if exit.rect.collidepoint(event.pos):
                    running = False
                if rate.rect.collidepoint(event.pos):
                    troll_window(screen, size)
                if tips.rect.collidepoint(event.pos):
                    tutorial_window(screen)

        screen.blit(load_image_buttons('../backgrounds/fon1.jpg'), (0, 0))
        clock.tick(fps)
        draw_settings(screen)
        settings_sprites.draw(screen)
        pygame.display.flip()


def custom_cube(screen, size):
    width, height = size
    style_cube, color1, color2 = None, None, None
    main_cube = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    styles = {"style1.png": (width * 0.17, height * 0.05), "style2.png": (width * 0.17, height * 0.225),
              "style3.png": (width * 0.17, height * 0.4), "style4.png": (width * 0.17, height * 0.575)}

    customize_screen = screen

    for name, coords in styles.items():
        style = Styles(name, coords)

    image = load_image_cube("colors.png", -1)
    for i in range(2):
        sprite = pygame.sprite.Sprite(all_sprites)
        sprite.image = image
        sprite.image = pygame.transform.scale(sprite.image, (200, 100))

        sprite.rect = sprite.image.get_rect()
        if i == 0:
            sprite.rect.x = 625
            sprite.rect.y = 40
        else:
            sprite.rect.x = 625
            sprite.rect.y = 180

    pygame.draw.rect(customize_screen, (87, 94, 83), (0, 0, width, height * 0.8))
    pygame.draw.rect(customize_screen, (10, 10, 10), (0, height * 0.8, width, height))
    pygame.draw.line(customize_screen, pygame.Color("white"), (width * 0.25, height * 0.82),
                     (width * 0.75, height * 0.82),
                     width=2)

    exit_button = Exit()

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cube_sprites.update(event)
                x, y = event.pos[0], event.pos[1]

                if 625 <= x <= 825 and 40 <= y <= 140:
                    c = customize_screen.get_at(event.pos)
                    color1 = c[0], c[1], c[2]
                if 625 <= x <= 825 and 180 <= y <= 280:
                    c = customize_screen.get_at(event.pos)
                    color2 = c[0], c[1], c[2]

                if width * 0.17 <= x <= width * 0.17 + 104 and 22 <= y <= 92:
                    style_cube = 1
                if width * 0.17 <= x <= width * 0.17 + 104 and 101 <= y <= 171:
                    style_cube = 2
                if width * 0.17 <= x <= width * 0.17 + 104 and 180 <= y <= 250:
                    style_cube = 3
                if width * 0.17 <= x <= width * 0.17 + 104 and 258 <= y <= 328:
                    style_cube = 4

            if event.type == pygame.MOUSEBUTTONUP:
                cube_sprites.update(event)
                if exit.rect.collidepoint(event.pos):
                    running = False

            sprite = pygame.sprite.Sprite(main_cube)

            with open('color_cube.txt', encoding='utf8', mode="r") as f:
                text = f.readline()

            text = text.split(";")
            style, c1, c2 = int(text[0]), text[1], text[2]
            c1 = c1[1:-1]
            c2 = c2[1:-1]

            c1 = tuple(int(item) for item in c1.split(', '))
            c2 = tuple(int(item) for item in c2.split(', '))

            if style_cube is not None:
                style = style_cube

            if color1 is not None:
                c1 = color1

            if color2 is not None:
                c2 = color2

            draw_cube(style, c1, c2)
            if style != 4:
                cube_image = load_image_cube("cube.png", None)
            else:
                cube_image = load_image_cube("cube.png", "white")

            sprite.image = cube_image
            sprite.image = pygame.transform.scale(sprite.image, (150, 150))

            sprite.rect = sprite.image.get_rect()
            sprite.rect.x, sprite.rect.y = 350, 240

            pygame.draw.rect(customize_screen, (87, 94, 83), (0, 0, width, height * 0.8))
            pygame.draw.rect(customize_screen, (10, 10, 10), (0, height * 0.8, width, height))
            pygame.draw.line(customize_screen, pygame.Color("white"), (width * 0.25, height * 0.82),
                             (width * 0.75, height * 0.82), width=2)
        main_cube.draw(customize_screen)
        main_cube = pygame.sprite.Group()
        cube_sprites.draw(customize_screen)
        all_sprites.draw(customize_screen)
        pygame.display.flip()


class Styles(pygame.sprite.Sprite):
    def __init__(self, name, coords):
        super().__init__(cube_sprites)
        self.flag_press = False
        if name != "style4.png":
            self.image = load_image_cube(name, None)
        else:
            self.image = load_image_cube(name, (255, 0, 0))
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.image_press = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = coords[0] + self.rect.width // 2, coords[1] + self.rect.height // 2
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) \
                and self.rect.collidepoint(event.pos):
            self.flag_press = True
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            self.flag_press = False


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
        self.flag_press = False
        self.image = load_image("rate.png", (127, 127, 127))
        self.image_press = pygame.transform.scale(self.image, (240, 100))
        self.rect = self.image.get_rect()
        self.rect.center = width * 0.15 + self.rect.width // 2, height * 0.3 + self.rect.height // 2
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) \
                and self.rect.collidepoint(event.pos):
            self.flag_press = True
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            self.flag_press = False


class Tips(Rate):
    def __init__(self):
        super().__init__()
        self.image = load_image("tips.png", (127, 127, 127))
        self.image_press = pygame.transform.scale(self.image, (240, 100))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = width * 0.6, height * 0.3
        self.mask = pygame.mask.from_surface(self.image)


class Exit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(troll_sprites, settings_sprites, cube_sprites, tutorial_sprites)
        self.flag_press = False
        self.image = pygame.transform.scale(load_image("cube\exit.png", "white"), (100, 60))
        self.image_press = pygame.transform.scale(load_image("cube\exit_pressed.png", "white"), (120, 80))
        self.rect = self.image.get_rect()
        self.rect.center = width * 0.025 + self.rect.width // 2, height * 0.06 + self.rect.height // 2
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and \
                self.rect.collidepoint(event.pos):
            self.flag_press = True
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            self.flag_press = False


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
    cube_sprites = pygame.sprite.Group()
    settings_sprites = pygame.sprite.Group()
    troll_sprites = pygame.sprite.Group()
    tutorial_sprites = pygame.sprite.Group()

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
