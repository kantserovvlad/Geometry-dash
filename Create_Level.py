import os
import sys
import pygame
from PyQt5.QtWidgets import QInputDialog, QWidget


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
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


def save_level():
    files = os.listdir('levels')
    n = 0
    while True:
        n += 1
        if f'level{n}.txt' not in files:
            file = open(f'levels/level{n}.txt', 'w')
            for i in board.board:
                file.write(''.join(str(j) for j in i))
                file.write('\n')
            return


def create_level(n):
    if point_cube is not None:
        x, y = point_cube
        board.board[y][x] = n
        # -----------------------
        if n == 1:
            thorn1 = Obstacle(1, 'game/thorn1.png', point_cube)
        elif n == 2:
            thorn2 = Obstacle(2, 'game/thorn2.png', point_cube)
        elif n == 3:
            square = Obstacle(3, 'game/square.png', point_cube)


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


class Button(pygame.sprite.Sprite):
    def __init__(self, point, image, image_press, action):
        super().__init__(all_sprites_front)
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

        if event.type == pygame.MOUSEMOTION and not self.rect.collidepoint(event.pos) and self.flag_press:
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y
            self.flag_press = False

        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos) and self.flag_press:
            exec(self.action)
            self.flag_press = False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 450
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    background = pygame.Surface(size)

    fps = 100
    v = 40
    clock = pygame.time.Clock()

    # Создаём группы спрайтов
    all_sprites = pygame.sprite.Group()
    all_sprites_front = pygame.sprite.Group()
    sprites_obstacles = pygame.sprite.Group()

    board = Board(840 // 30, 330 // 30)
    # ---------------------------------------
    # Теперь создаю кнопки
    pause = Button((width - 50, 50), 'buttons/pause.png', 'buttons/pause_press.png', '')
    delete = Button((77, height - 77), 'buttons/delete.png', 'buttons/delete.png',
                    'create_level(0)')
    clear = Button((77, height - 35), 'buttons/clear.png', 'buttons/clear.png', 'board.clear()')
    save = Button((width - 100, height - 77), 'buttons/save.png',
                  'buttons/save.png', "save_level()")
    add_square = Button((width // 2, height - 60), 'buttons/add_square.png',
                        'buttons/add_square-press.png', 'create_level(3)')
    add_thorn1 = Button((width // 2 - 100, height - 60), 'buttons/add_thorn1.png',
                        'buttons/add_thorn1-press.png', 'create_level(1)')
    add_thorn2 = Button((width // 2 + 100, height - 60), 'buttons/add_thorn2.png',
                        'buttons/add_thorn2-press.png', 'create_level(2)')
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
            if event.type == pygame.MOUSEMOTION:
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
