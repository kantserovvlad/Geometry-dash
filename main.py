import pygame
from load_image import load_image


def draw_settings(screen):
    font = pygame.font.Font(None, 80)
    text = font.render("Settings", True, (0, 255, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height * 0.1
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Geometry dash")
    size = width, height = 850, 450
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    buttons = {"rate.png": (width * 0.15, height * 0.3),
               "tips.png": (width * 0.6, height * 0.3)}

    for name, coords in buttons.items():
        sprite = pygame.sprite.Sprite(all_sprites)
        sprite.image = load_image(name, (127, 127, 127))
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x, sprite.rect.y = buttons[name]

    fps = 100
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(load_image('fon1.jpg'), (0, 0))
        clock.tick(fps)
        draw_settings(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
