import os
import sys
import pygame
from PIL import Image, ImageDraw


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

    pic.save("images/cube/cube.png")
    return pic


def create_level(n, point_cube):
    if point_cube is not None:
        x, y = point_cube
        board.board[y][x] = n
        # -----------------------
        if n == 1:
            Obstacle(1, 'game/thorn1.png', point_cube)
        elif n == 2:
            Obstacle(2, 'game/thorn2.png', point_cube)
        elif n == 3:
            Obstacle(3, 'game/square.png', point_cube)
        elif n == 4:
            finish = Finish(4, 'game/finish.png', point_cube)


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


def read_file(name='level1.txt'):
    level = open(f'levels/{name}', 'r', encoding='utf-8').readlines()
    for i in range(len(game_board.board)):
        for j in range(len(game_board.board[i])):
            try:
                game_board.board[i][j] = int(level[i][j])
                create_level(int(level[i][j]), [j, i])
            except Exception as ex:
                game_board.board[i][j] = 0


# -----------------"пишущие" функции---------------


def draw_text():
    font = pygame.font.SysFont("Calibri", 50)
    text = font.render("Невозможно подключиться к сети :(", True, (0, 255, 0))
    text_x = width * 0.09
    text_y = height * 0.1
    screen.blit(text, (text_x, text_y))


def draw_settings_tutorial(text):
    for k, v in text.items():
        font = pygame.font.SysFont("Calibri", v[1])
        text = font.render(k, True, (0, 255, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = v[0]
        screen.blit(text, (text_x, text_y))


def draw_tutorial(screen):
    text = {"Управление": [height * 0.1, 80], "Space (пробел) - прыжок": [height * 0.3, 50]}
    for k, v in text.items():
        font = pygame.font.Font(None, v[1])
        text = font.render(k, True, (0, 255, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = v[0]
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))


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


# -----------------функции окон---------------


def tutorial_window():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                tutorial_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                tutorial_sprites.update(event)
                if exit_btn.rect.collidepoint(event.pos):
                    running = False
        screen.fill((54, 85, 110))
        clock.tick(fps)
        draw_settings_tutorial(text={"Управление": [height * 0.1, 80], "Space (пробел) - прыжок": [height * 0.3, 50]})
        tutorial_sprites.draw(screen)
        pygame.display.flip()


def troll_window():
    width, height = size
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                troll_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                troll_sprites.update(event)
                if exit_btn.rect.collidepoint(event.pos):
                    running = False

        screen.fill((54, 85, 110))
        image = load_image("no_internet.png", "white")
        image = pygame.transform.scale(image, (300, 300))
        screen.blit(image, (width // 2 - image.get_width() // 2, height * 0.25))
        troll_sprites.draw(screen)
        draw_text()
        pygame.display.flip()


def settings_window():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                volume = slider.handle_event(event.pos[0], event.pos[1])
                if volume:
                    pygame.mixer.music.set_volume(volume / 100)
                settings_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                settings_sprites.update(event)
                if rate.rect.collidepoint(event.pos):
                    troll_window()
                if tips.rect.collidepoint(event.pos):
                    tutorial_window()
                if exit_btn.rect.collidepoint(event.pos):
                    running = False

        screen.fill((54, 85, 110))
        clock.tick(fps)
        draw_settings_tutorial(text={"Настройки": [height * 0.1, 80], "Громкость": [height * 0.6, 50]})
        settings_sprites.draw(screen)
        slider.draw()
        pygame.display.flip()


def custom_cube_window():
    global size
    width, height = size
    style_cube, color1, color2 = None, None, None
    main_cube = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    styles = {"style1.png": (width * 0.17, height * 0.05), "style2.png": (width * 0.17, height * 0.225),
              "style3.png": (width * 0.17, height * 0.4), "style4.png": (width * 0.17, height * 0.575)}

    for name, coords in styles.items():
        style = Styles(name, coords)

    image = load_image("cube/colors.png", -1)
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

    pygame.draw.rect(screen, (87, 94, 83), [0, 0, width, height * 0.8])
    pygame.draw.rect(screen, (10, 10, 10), [0, height * 0.8, width, height])
    pygame.draw.line(screen, pygame.Color("white"), (width * 0.25, height * 0.82),
                     (width * 0.75, height * 0.82),
                     width=2)
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
                    c = screen.get_at(event.pos)
                    color1 = c[0], c[1], c[2]
                if 625 <= x <= 825 and 180 <= y <= 280:
                    c = screen.get_at(event.pos)
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
                if exit_btn.rect.collidepoint(event.pos):
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
                cube_image = load_image("cube/cube.png", None)
            else:
                cube_image = load_image("cube/cube.png", "white")

            sprite.image = cube_image
            sprite.image = pygame.transform.scale(sprite.image, (150, 150))

            sprite.rect = sprite.image.get_rect()
            sprite.rect.x, sprite.rect.y = 350, 240

            pygame.draw.rect(screen, (87, 94, 83), [0, 0, width, height * 0.8])
            pygame.draw.rect(screen, (10, 10, 10), [0, height * 0.8, width, height])
            pygame.draw.line(screen, pygame.Color("white"), (width * 0.25, height * 0.82),
                             (width * 0.75, height * 0.82), width=2)
        main_cube.draw(screen)
        main_cube = pygame.sprite.Group()
        cube_sprites.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()


def create_level_window():
    background = pygame.Surface(size)
    running = True
    global point_cube  # Какой пользователь выбрал место
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites_front.update(event)
                # Проверки нажатия на квадратик
                if point_cube == board.get_cell(event.pos):
                    point_cube = None
                elif board.get_cell(event.pos) is None:
                    pass
                elif point_cube is None:
                    point_cube = board.get_cell(event.pos)
                else:
                    point_cube = board.get_cell(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                all_sprites_front.update(event)
                if exit_btn.rect.collidepoint(event.pos):
                    running = False
        # -------------------------------------
        # Проходим по каждому объекту-препятствию
        for item in sprites_obstacles:
            # Если не совпдает номер приепятсвия и номер в поле, то удаляем это препятсвие
            if board.board[item.point[1]][item.point[0]] != item.n:
                item.kill()
                sprites_obstacles.clear(screen, background)
                sprites_obstacles.draw(screen)
        # --------------------------------------
        screen.blit(load_image('backgrounds/fon1.jpg'), (0, 0))  # Создаём фон
        pygame.draw.rect(screen, '#1B233D', (0, 330, width, height))  # Дополнительнй прямоугольник
        sprites_obstacles.draw(screen)  # Отрисовываем препятсвия
        board.render(screen, point_cube)  # Рисуем клеточное поле
        all_sprites_front.draw(screen)  # Отрисовываем те спрайты, которые должны быть впереди поля
        # -----------------------------
        clock.tick(fps)
        pygame.display.flip()


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
                    game_window()

        load_level_sprites.draw(screen)
        draw_name_level(num_level)
        pygame.display.flip()


def game_window():
    # -----------------------------------------
    read_file()
    global flag
    global music_name
    pygame.mixer.music.load(music_name)
    pygame.mixer.music.play(10)
    running = True
    while running:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if flag:
                        player.jump()
                        flag = False

        # -------------------------------------
        screen.blit(load_image('backgrounds/fon1.jpg'), (0, 0))  # Создаём фон
        pygame.draw.rect(screen, '#1B233D', (0, 330, width, height))  # Дополнительнй прямоугольник
        game_sprites_obstacles.draw(screen)  # Отрисовываем препятсвия
        game_sprites_obstacles.update()
        finish_sprites.draw(screen)
        finish_sprites.update()
        player.cjump()
        player.update()
        game_cube_sprites.draw(screen)
        # -----------------------------
        clock.tick(fps)
        pygame.display.flip()
    pygame.mixer.music.stop()


# -----------------классы---------------


class Finish(pygame.sprite.Sprite):
    def __init__(self, n, image, point):
        super().__init__(finish_sprites)
        self.n = n
        self.point = point
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (point[0] * 30 + 15, point[1] * 30 + 15)

    def update(self):
        self.rect.x -= int(v / fps)


class Slider:
    def __init__(self, x, y, w, h):
        self.full_x = self.circle_x = x
        self.volume = 100
        self.sliderRect = pygame.Rect(x, y, w, h)
        self.flag = False

    def draw(self):
        if not self.flag:
            pygame.draw.rect(screen, (0, 255, 0), self.sliderRect)
            pygame.draw.circle(screen, (255, 240, 255),
                               (self.circle_x + self.sliderRect.w, (self.sliderRect.h / 2 + self.sliderRect.y)),
                               self.sliderRect.h * 1.5)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.circle_x + self.sliderRect.w, (self.sliderRect.h / 2 + self.sliderRect.y)),
                               self.sliderRect.h * 1.5, width=1)
        else:
            pygame.draw.rect(screen, (0, 255, 0), self.sliderRect)
            pygame.draw.rect(screen, (127, 127, 127), (self.circle_x, self.sliderRect[1],
                                                       self.sliderRect[0] + self.sliderRect[2] - self.circle_x,
                                                       self.sliderRect[3]))
            pygame.draw.circle(screen, (255, 240, 255), (self.circle_x, (self.sliderRect.h / 2 + self.sliderRect.y)),
                               self.sliderRect.h * 1.5)
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.circle_x, (self.sliderRect.h / 2 + self.sliderRect.y)),
                               self.sliderRect.h * 1.5, width=1)

    def get_volume(self):
        return self.volume

    def set_volume(self, num):
        self.volume = num

    def update_volume(self, x):
        if x < self.sliderRect.x:
            self.volume = 0
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.volume = 100
        else:
            self.volume = int((x - self.sliderRect.x) / float(self.sliderRect.w) * 100)

    def on_slider(self, x, y):
        if self.on_slider_hold(x, y) or self.sliderRect.x <= x <= self.sliderRect.x + self.sliderRect.w and \
                self.sliderRect.y <= y <= self.sliderRect.y + self.sliderRect.h:
            return True
        else:
            return False

    def on_slider_hold(self, x, y):
        if ((x - self.circle_x) * (x - self.circle_x) + (y - (self.sliderRect.y + self.sliderRect.h / 2)) * (
                y - (self.sliderRect.y + self.sliderRect.h / 2))) \
                <= (self.sliderRect.h * 1.5) * (self.sliderRect.h * 1.5):
            return True
        else:
            return False

    def handle_event(self, x, y):
        if self.sliderRect[0] <= x <= self.sliderRect[0] + self.sliderRect[2] and \
                self.sliderRect[1] <= y <= self.sliderRect[1] + self.sliderRect[3]:
            if x < self.sliderRect.x:
                self.circle_x = self.sliderRect.x
            elif x > self.sliderRect.x + self.sliderRect.w:
                self.circle_x = self.sliderRect.x + self.sliderRect.w
            else:
                self.circle_x = x
            self.flag = True
            self.draw()
            self.update_volume(x)
            return self.volume


class Styles(pygame.sprite.Sprite):
    def __init__(self, name, coords):
        super().__init__(cube_sprites)
        self.flag_press = False
        if name != "style4.png":
            self.image = load_image('cube/' + name, None)
        else:
            self.image = load_image('cube/' + name, (255, 0, 0))
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


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, n, image, point):
        super().__init__(game_sprites_obstacles, sprites_obstacles)
        self.n = n
        self.point = point
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (point[0] * 30 + 15, point[1] * 30 + 15)

    def update(self):
        self.rect.x -= int(v / fps)


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


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, select=None):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(0, 0, 0), (x * self.cell_size + self.left,
                                                                 y * self.cell_size + self.top,
                                                                 self.cell_size, self.cell_size), 1)
        if select is not None:
            self.select_cube(select)

    def update(self):
        self.left -= int(v / fps)
        self.render(screen)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def select_cube(self, point):
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (point[0] * self.cell_size + self.left,
                                                               point[1] * self.cell_size + self.top,
                                                               self.cell_size, self.cell_size), 1)

    def clear(self):
        self.board = [[0] * self.width for _ in range(self.height)]
        self.render(screen)

    def save(self):
        with open("level_test.txt", mode="w") as f:
            for row in self.board:
                row = list(map(str, row))
                row = "".join(row)
                f.write(row)
                f.write("\n")


class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(game_cube_sprites)
        self.is_jump = False
        self.up = False
        self.down = False

        self.bottom = 330
        self.k = 0
        self.sopr = None

        self.angle = 0
        self.speed = 10
        self.image = load_image("cube/cube.png", "white")
        self.orig_image = self.rot_image = self.image = pygame.transform.scale(self.image, (30, 30))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = 150 + self.image.get_width(), 330 - (self.image.get_height() // 2)

    def jump(self):
        self.angle = 0
        x, y = self.rect.center
        y -= self.speed
        self.rect.center = x, y
        self.is_jump = True
        self.up = True

    def cjump(self):
        global flag
        x, y = self.rect.center

        if self.is_jump:
            self.angle -= 10
            self.k += 1
            self.rot_image = pygame.transform.rotate(self.orig_image, self.angle % 360)
            self.image = self.rot_image
            if y > self.bottom - 110 and self.up:
                y -= self.speed
                if y <= self.bottom - 110:
                    self.down = True
                    self.up = False
            if y < self.bottom - (self.orig_image.get_height() // 2) and self.down:
                y += self.speed
                if y >= self.bottom - (self.orig_image.get_height() // 2):
                    self.down = False
                    self.up = False
                    self.is_jump = False
                    flag = True
                    self.k = 0
                    self.orig_image = self.image
            self.rect.center = x, y
        else:
            self.rect.y = self.bottom - (self.orig_image.get_height())
            self.down = False
            self.up = False
            self.is_jump = False
            flag = True
            self.k = 0
            self.orig_image = self.image

    def update(self):
        for f in finish_sprites:
            self.sopr = False
            if self.rect.collidepoint(f.rect.x, f.rect.y):
                pygame.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 440
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))

    pygame.mixer.music.load('music/start.mp3')  # загружаем фоновую музыку
    pygame.mixer.music.play()

    dict_of_levels = {1: ["Level Test", "level_test.txt", "music\Bossfight-Vextron.mp3"],
                      2: ["Level Test - 2", "level_test_2.txt", "music\Bossfight-Vextron.mp3"],
                      3: ["Level Test - 3", "level_test_3.txt", "music\Bossfight-Vextron.mp3"]
                      }

    num_level = 1
    num = None
    music_name = ""

    # Создаём группы спрайтов
    all_sprites = pygame.sprite.Group()
    all_sprites_front = pygame.sprite.Group()
    sprites_obstacles = pygame.sprite.Group()
    load_level_sprites = pygame.sprite.Group()

    settings_sprites = pygame.sprite.Group()  # группа спайтов основного окна настроек
    troll_sprites = pygame.sprite.Group()  # группа спайтов окна "Без Интернета"
    tutorial_sprites = pygame.sprite.Group()  # группа спайтов окна управления/обучения
    cube_sprites = pygame.sprite.Group()

    game_sprites_obstacles = pygame.sprite.Group()
    game_cube_sprites = pygame.sprite.Group()
    finish_sprites = pygame.sprite.Group()

    # -------------------------Создаём кнопки------------------------------------------------
    Button((screen.get_width() // 2, screen.get_height() // 2), 'buttons/play.png', 'buttons/play-press.png', None,
           'load_level_window()',
           all_sprites)
    Button((screen.get_width() // 2 - 120, screen.get_height() // 2),
           'buttons/change_cube.png', 'buttons/change_cube-press.png', None, 'custom_cube_window()', all_sprites)
    Button((screen.get_width() // 2, screen.get_height() * 0.7),
           'buttons/settings.png', 'buttons/settings-pressed.png', "black", 'settings_window()', all_sprites)
    Button((screen.get_width() // 2 + 120, screen.get_height() // 2),
           'buttons/editor_level.png', 'buttons/editor_level-press.png', None, 'create_level_window()', all_sprites)

    board = Board(28 * 5, 11)
    # ---------------------------------------
    # Теперь создаю кнопки
    Button((77, height - 77), 'buttons/delete.png', 'buttons/delete.png', None, 'create_level(0, point_cube)',
           all_sprites_front)
    Button((77, height - 35), 'buttons/clear.png', 'buttons/clear.png', None, 'board.clear()', all_sprites_front)
    Button((width - 100, height - 77), 'buttons/save.png', 'buttons/save.png', None, 'board.save()', all_sprites_front)
    Button((width // 2, height - 60), 'buttons/add_square.png', 'buttons/add_square-press.png', None,
           'create_level(3, point_cube)',
           all_sprites_front)
    Button((width // 2 - 100, height - 60), 'buttons/add_thorn1.png', 'buttons/add_thorn1-press.png', None,
           'create_level(1, point_cube)', all_sprites_front)
    Button((width // 2 + 100, height - 60), 'buttons/add_thorn2.png', 'buttons/add_thorn2-press.png', None,
           'create_level(2, point_cube)', all_sprites_front)

    exit_btn = Button((width * 0.025 + 31, height * 0.06 + 29),
                      "cube/exit.png", "cube/exit_pressed.png", "white", '', settings_sprites, troll_sprites,
                      tutorial_sprites, all_sprites_front, cube_sprites)
    rate = Button((width * 0.15 + 105, height * 0.3 + 40),
                  "buttons/rate.png", "buttons/rate_pressed.png", "white", 'troll_window()', settings_sprites)
    tips = Button((width * 0.6 + 105, height * 0.3 + 40),
                  "buttons/tips.png", "buttons/tips_pressed.png", "white", 'tutorial_window()', settings_sprites)
    slider = Slider(width * 0.4, height * 0.75, 170, 10)

    edge_top = Button((width // 2, 28), 'load_level/edge_top.png', 'load_level/edge_top.png', 'white', '',
                      load_level_sprites)
    edge_left = Button((60, height - 118 // 2 + 1), 'load_level/edge_left.png', 'load_level/edge_left.png',
                       'white', '', load_level_sprites)
    edge_right = Button((width - 60, height - 118 // 2 + 1), 'load_level/edge_right.png',
                        'load_level/edge_right.png',
                        'white', '', load_level_sprites)

    goto_left = Button((42, 220), 'load_level/goto_left.png', 'load_level/goto_left_press.png', 'red',
                       'func(-1)', load_level_sprites)
    goto_right = Button((width - 42, 220), 'load_level/goto_right.png', 'load_level/goto_right_press.png',
                        'red', 'func(1)', load_level_sprites)

    exit2 = Button((40, 49), 'load_level/exit2.png', 'load_level/exit2_press.png', 'white', '', load_level_sprites)
    back = Button((width // 2, 153), 'load_level/back.png', 'load_level/back_press.png', 'black',
                  'draw_name_level(num_level)', load_level_sprites)

    coin1 = Button((508, 199), 'load_level/silver_coin.png', 'load_level/silver_coin.png', 'black', '',
                   load_level_sprites)
    coin2 = Button((543, 199), 'load_level/silver_coin.png', 'load_level/silver_coin.png', 'black', '',
                   load_level_sprites)
    coin3 = Button((578, 199), 'load_level/silver_coin.png', 'load_level/silver_coin.png', 'black', '',
                   load_level_sprites)

    difficulty = Button((273, 156), 'difficulty/easy.png', 'difficulty/easy.png', 'red', '', load_level_sprites)

    game_board = Board(28 * 5, 11)
    player = Cube()

    # -----------------------Основные параметры-----------------------------------------------
    fps = 5000
    v = 50000
    clock = pygame.time.Clock()

    point_cube = None

    running = True
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
