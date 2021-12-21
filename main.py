import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('Images', name)
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
        self.image = load_image("play.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.image = load_image("play-press.png")
            self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        else:
            self.image = load_image("play.png")
            self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')

    fps = 100
    v = 40
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    board = Board(40, 25)
    play = Play()

    pygame.mixer.music.load('music\start.mp3')
    pygame.mixer.music.play()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        screen.blit(load_image('fon1.jpg'), (0, 0))
        all_sprites.draw(screen)
        all_sprites.update(event)
        clock.tick(fps)
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.quit()
