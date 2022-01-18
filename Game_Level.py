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


def read_file(name='level1.txt'):
    level = open(f'levels/{name}', 'r', encoding='utf-8').readlines()
    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            try:
                board.board[i][j] = int(level[i][j])
                create_level(int(level[i][j]), [j, i])
            except Exception as ex:
                board.board[i][j] = 0


def create_level(n, point_cube):
    if n == 1:
        thorn1 = Obstacle(1, 'game/thorn1.png', point_cube)
    elif n == 2:
        thorn2 = Obstacle(2, 'game/thorn2.png', point_cube)
    elif n == 3:
        square = Obstacle(3, 'game/square.png', point_cube)
    else:
        pass


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
        self.rect.x -= int(v / fps)


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

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(0, 0, 0), (x * self.cell_size + self.left,
                                                                 y * self.cell_size + self.top,
                                                                 self.cell_size, self.cell_size), 1)

    def update(self):
        self.left -= int(v / fps)
        self.render(screen)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def clear(self):
        self.board = [[0] * self.width for _ in range(self.height)]


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 450
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    background = pygame.Surface(size)

    fps = 100
    v = 1000
    clock = pygame.time.Clock()

    # Создаём группы спрайтов
    all_sprites_front = pygame.sprite.Group()
    sprites_obstacles = pygame.sprite.Group()

    board = Board(28 * 5, 11)
    # -----------------------------------------
    pygame.mixer.music.load('music/start.mp3')
    pygame.mixer.music.play(10)
    read_file()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # -------------------------------------
        screen.blit(load_image('backgrounds/fon1.jpg'), (0, 0))  # Создаём фон
        pygame.draw.rect(screen, '#1B233D', (0, 330, width, height))  # Дополнительнй прямоугольник
        sprites_obstacles.draw(screen)  # Отрисовываем препятсвия
        sprites_obstacles.update(event)
        all_sprites_front.draw(screen)  # Отрисовываем те спрайты, которые должны быть впереди поля
        # -----------------------------
        clock.tick(fps)
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.quit()
