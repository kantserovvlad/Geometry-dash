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
    for i in range(len(game_board.board)):
        for j in range(len(game_board.board[i])):
            try:
                game_board.board[i][j] = int(level[i][j])
                create_level(int(level[i][j]), [j, i])
            except Exception as ex:
                game_board.board[i][j] = 0


def create_level(n, point_cube):
    if n == 1:
        thorn1 = Thorn1(1, 'game/thorn1.png', point_cube)
    elif n == 2:
        thorn2 = Thorn2(2, 'game/thorn2.png', point_cube)
    elif n == 3:
        square = Square(3, 'game/square.png', point_cube)
    else:
        pass


class Thorn1(pygame.sprite.Sprite):
    def __init__(self, n, image, point):
        super().__init__(thorn1_sprites)
        self.n = n
        self.point = point
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (point[0] * 30 + 15, point[1] * 30 + 15)

    def update(self):
        self.rect.x -= int(v / fps)


class Thorn2(pygame.sprite.Sprite):
    def __init__(self, n, image, point):
        super().__init__(thorn2_sprites)
        self.n = n
        self.point = point
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (point[0] * 30 + 15, point[1] * 30 + 15)

    def update(self):
        self.rect.x -= int(v / fps)


class Square(pygame.sprite.Sprite):
    def __init__(self, n, image, point):
        super().__init__(square_sprites)
        self.n = n
        self.point = point
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (point[0] * 30 + 15, point[1] * 30 + 15)

    def update(self):
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


class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(cube_sprites)
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
            self.angle -= 0
            self.k += 1
            print(self.k)
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
            print(self.is_jump, y, self.bottom, self.bottom - (self.orig_image.get_height() // 2))
        else:
            self.rect.y = self.bottom - (self.orig_image.get_height())
            self.down = False
            self.up = False
            self.is_jump = False
            flag = True
            self.k = 0
            self.orig_image = self.image

    def update(self):
        for s in square_sprites:
            self.sopr = False
            if self.rect.collidepoint(s.rect.x, s.rect.y):
                if self.rect.y < s.rect.y:
                    self.bottom = s.rect.y + 30
                    self.image = self.orig_image
                    player.cjump()
                    self.is_jump = False
                else:
                    print("restart")
                self.sopr = True
            if not self.sopr:
                self.bottom = 330



        """for t1 in thorn1_sprites:
            if self.rect.collidepoint(t1.rect.x, t1.rect.y):
                print("thorn1")
        for t2 in thorn2_sprites:
            if self.rect.collidepoint(t2.rect.x, t2.rect.y):
                print("thorn2")"""


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 440
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))
    background = pygame.Surface(size)

    fps = 5000
    v = 50000
    clock = pygame.time.Clock()

    # Создаём группы спрайтов
    cube_sprites = pygame.sprite.Group()

    thorn1_sprites = pygame.sprite.Group()
    thorn2_sprites = pygame.sprite.Group()
    square_sprites = pygame.sprite.Group()

    game_board = Board(28 * 5, 11)
    player = Cube()
    # -----------------------------------------
    """pygame.mixer.music.load('music/start.mp3')
    pygame.mixer.music.play(10)"""
    read_file()
    flag = True
    running = True
    while running:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if flag:
                        player.jump()
                        flag = False
                        
        # -------------------------------------
        screen.blit(load_image('backgrounds/fon1.jpg'), (0, 0))  # Создаём фон
        pygame.draw.rect(screen, '#1B233D', (0, 330, width, height))  # Дополнительнй прямоугольник

        thorn1_sprites.draw(screen)  # Отрисовываем препятсвия
        thorn1_sprites.update()
        thorn2_sprites.draw(screen)  # Отрисовываем препятсвия
        thorn2_sprites.update()
        square_sprites.draw(screen)  # Отрисовываем препятсвия
        square_sprites.update()
        player.cjump()
        player.update()
        cube_sprites.draw(screen)
        # -----------------------------
        clock.tick(fps)
        pygame.display.flip()
    "pygame.mixer.music.stop()"
    pygame.quit()
