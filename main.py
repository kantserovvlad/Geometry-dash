import pygame


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

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pass
                # pygame.draw.rect(screen, pygame.Color(0, 0, 0), (x * self.cell_size + self.left,
                #                                                        y * self.cell_size + self.top,
                #                                                        self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)

    fps = 100
    running = True
    clock = pygame.time.Clock()

    board = Board(40, 25)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(board.get_cell(event.pos))
        screen.fill((0, 0, 0))
        board.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
