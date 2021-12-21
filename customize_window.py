import pygame

from draw_cube import draw_cube
from load_image import load_image


def custom_window():
    size = width, height = 850, 450
    style_cube, color1, color2 = None, None, None
    main_cube = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    styles = {"style1.png": (width * 0.15, height * 0.05), "style2.png": (width * 0.15, height * 0.225),
              "style3.png": (width * 0.15, height * 0.4), "style4.png": (width * 0.15, height * 0.575)}

    pygame.init()
    customize_screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Customize cube")

    for name, coords in styles.items():
        sprite = pygame.sprite.Sprite(all_sprites)
        if name != "style4.png":
            sprite.image = load_image(name, None)
        else:
            sprite.image = load_image(name, (255, 0, 0))
        sprite.image = pygame.transform.scale(sprite.image, (70, 70))
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x, sprite.rect.y = styles[name]

    image = load_image("colors.png", -1)
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

    pygame.draw.rect(customize_screen, (87, 94, 83), (0, 0, width, height * 0.8))
    pygame.draw.rect(customize_screen, (10, 10, 10), (0, height * 0.8, width, height))
    pygame.draw.line(customize_screen, pygame.Color("white"), (width * 0.25, height * 0.82),
                     (width * 0.75, height * 0.82),
                     width=2)
    pygame.draw.polygon(customize_screen, (245, 50, 255), ((width * 0.02, height * 0.1),
                                                           (width * 0.07, height * 0.05),
                                                           (width * 0.07, height * 0.15)))

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = event.pos[0], event.pos[1]
                if 625 <= x <= 825 and 40 <= y <= 140:
                    c = customize_screen.get_at(event.pos)
                    color1 = c[0], c[1], c[2]
                if 625 <= x <= 825 and 180 <= y <= 280:
                    c = customize_screen.get_at(event.pos)
                    color2 = c[0], c[1], c[2]

                if 127 <= x <= 197 and 22 <= y <= 92:
                    style_cube = 1
                if 127 <= x <= 197 and 101 <= y <= 171:
                    style_cube = 2
                if 127 <= x <= 197 and 180 <= y <= 250:
                    style_cube = 3
                if 127 <= x <= 197 and 258 <= y <= 328:
                    style_cube = 4

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
                cube_image = load_image("cube.png", None)
            else:
                cube_image = load_image("cube.png", "white")

            sprite.image = cube_image
            sprite.image = pygame.transform.scale(sprite.image, (150, 150))

            sprite.rect = sprite.image.get_rect()
            sprite.rect.x, sprite.rect.y = 350, 240

            pygame.draw.rect(customize_screen, (87, 94, 83), (0, 0, width, height * 0.8))
            pygame.draw.rect(customize_screen, (10, 10, 10), (0, height * 0.8, width, height))
            pygame.draw.line(customize_screen, pygame.Color("white"), (width * 0.25, height * 0.82),
                             (width * 0.75, height * 0.82), width=2)
            pygame.draw.polygon(customize_screen, (245, 50, 255), ((width * 0.02, height * 0.1),
                                                                   (width * 0.07, height * 0.05),
                                                                   (width * 0.07, height * 0.15)))

        main_cube.draw(customize_screen)
        main_cube = pygame.sprite.Group()
        all_sprites.draw(customize_screen)
        pygame.display.flip()
    pygame.quit()


custom_window()
