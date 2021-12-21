import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)

    fps = 100
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
