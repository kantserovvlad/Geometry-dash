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


def draw_name_level(num):
    if num is not None:
        global music_name
        info = dict_of_levels[num]
        music_name = info[2]

        font = pygame.font.Font(None, 60)
        text = font.render(info[0], True, (255, 255, 255))
        text_x = width // 2 - text.get_width() // 2 + 20
        text_y = height // 2 - 2 * text.get_height()
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))


def func(doing):
    global num_level
    if doing == 1:
        if num_level < len(dict_of_levels.keys()):
            num_level += 1
        else:
            num_level = 1
    else:
        if num_level > 1:
            num_level -= 1
        else:
            num_level = len(dict_of_levels.keys())


def load_level_window():
    global num_level
    running = True
    while running:
        screen.fill((45, 58, 175))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                load_level_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                load_level_sprites.update(event)
                if exit2.rect.collidepoint(event.pos):
                    running = False
                if back.rect.collidepoint(event.pos):
                    """game_window(screen)"""

        load_level_sprites.draw(screen)
        draw_name_level(num_level)
        pygame.display.flip()


class Button(pygame.sprite.Sprite):
    def __init__(self, point, image, image_press, fon, action, *sprite_groups):
        super().__init__(*sprite_groups)
        self.action = action
        self.flag_press = False
        self.image = load_image(image, fon)
        self.image_press = load_image(image_press, fon)
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

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            exec(self.action)
            self.flag_press = False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 440
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))

    num_level = 1
    num = None
    music_name = ""

    load_level_sprites = pygame.sprite.Group()

    dict_of_levels = {1: ["Level Test", "level_test.txt", "music\Bossfight-Vextron.mp3"],
                      2: ["Level Test - 2", "level_test_2.txt", "music\Bossfight-Vextron.mp3"],
                      3: ["Level Test - 3", "level_test_3.txt", "music\Bossfight-Vextron.mp3"]
                      }

    edge_top = Button((width // 2, 28), 'load_level/edge_top.png', 'load_level/edge_top.png', 'white', '', load_level_sprites)
    edge_left = Button((60, height - 118 // 2 + 1), 'load_level/edge_left.png', 'load_level/edge_left.png',
                                 'white', '', load_level_sprites)
    edge_right = Button((width - 60, height - 118 // 2 + 1), 'load_level/edge_right.png',
                                  'load_level/edge_right.png',
                                  'white', '', load_level_sprites)

    goto_left = Button((42, 220), 'load_level/goto_left.png', 'load_level/goto_left_press.png', 'red',
                                 'func(-1)', load_level_sprites)
    goto_right = Button((width - 42, 220), 'load_level/goto_right.png', 'load_level/goto_right_press.png',
                                  'red', 'func(1)', load_level_sprites)

    exit2 = Button((40, 49), 'load_level/exit2.png', 'load_level/exit2_press.png', 'white', '')
    back = Button((width // 2, 153), 'load_level/back.png', 'load_level/back_press.png', 'black',
                            'draw_name_level(num_level)', load_level_sprites)

    coin1 = Button((508, 199), 'load_level/silver_coin.png', 'load_level/silver_coin.png', 'black', '', load_level_sprites)
    coin2 = Button((543, 199), 'load_level/silver_coin.png', 'load_level/silver_coin.png', 'black', '', load_level_sprites)
    coin3 = Button((578, 199), 'load_level/silver_coin.png', 'load_level/silver_coin.png', 'black', '', load_level_sprites)

    difficulty = Button((273, 156), 'difficulty/easy.png', 'difficulty/easy.png', 'red', '', load_level_sprites)

    load_level_window()
    pygame.quit()
