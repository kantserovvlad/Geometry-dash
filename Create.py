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


def create_level(n):
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


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, n, image, point):
        super().__init__(sprites_obstacles)
        self.n = n
        self.point = point
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (point[0] * 30 + 15, point[1] * 30 + 15)

    def update(self, event):
        self.rect.center = self.rect.center


class Button(pygame.sprite.Sprite):
    def __init__(self, point, image, image_press, action, fon=None):
        super().__init__(all_sprites_front)
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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 440
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    background = pygame.Surface(size)

    pygame.mixer.music.load('music/start.mp3')  # загружаем фоновую музыку
    pygame.mixer.music.play()

    # Создаём группы спрайтов
    all_sprites = pygame.sprite.Group()
    all_sprites_front = pygame.sprite.Group()
    sprites_obstacles = pygame.sprite.Group()
    # -----------------------Основные параметры-----------------------------------------------
    fps = 100
    v = 50
    clock = pygame.time.Clock()

    board = Board(28 * 5, 11)
    # ---------------------------------------
    # Теперь создаю кнопки
    Button((30, 30), 'cube/exit.png', 'cube/exit_pressed.png', 'running = False', fon='white')
    Button((77, height - 77), 'buttons/delete.png', 'buttons/delete.png', 'create_level(0)')
    Button((77, height - 35), 'buttons/clear.png', 'buttons/clear.png', 'board.clear()')
    Button((width - 100, height - 77), 'buttons/save.png', 'buttons/save.png', 'board.save()')
    Button((width // 2, height - 60), 'buttons/add_square.png', 'buttons/add_square-press.png',
           'create_level(3)')
    Button((width // 2 - 100, height - 60), 'buttons/add_thorn1.png', 'buttons/add_thorn1-press.png',
           'create_level(1)')
    Button((width // 2 + 100, height - 60), 'buttons/add_thorn2.png', 'buttons/add_thorn2-press.png',
           'create_level(2)')
    # -----------------------------------------
    pygame.mixer.music.load('music/start.mp3')
    pygame.mixer.music.play(10)
    running = True
    point_cube = None  # Какой пользователь выбрал место
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
        all_sprites.draw(screen)
        board.render(screen, point_cube)  # Рисуем клеточное поле
        all_sprites_front.draw(screen)  # Отрисовываем те спрайты, которые должны быть впереди поля
        # -----------------------------
        clock.tick(fps)
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.quit()
