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


def tutorial_window():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                settings_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                settings_sprites.update(event)
                if exit_btn.rect.collidepoint(event.pos):
                    running = False
        screen.blit(load_image('backgrounds/fon1.jpg'), (0, 0))
        clock.tick(fps)
        draw_tutorial()
        all_sprites.draw(screen)
        pygame.display.flip()


def draw_text():
    font = pygame.font.Font(None, 50)
    text = font.render("Невозможно подключиться к сети :(", True, (0, 255, 0))
    text_x = width * 0.2
    text_y = height * 0.1
    screen.blit(text, (text_x, text_y))


def draw_settings():
    text = {"Настройки": [height * 0.1, 80], "Громкость": [height * 0.6, 50]}
    for k, v in text.items():
        font = pygame.font.Font(None, v[1])
        text = font.render(k, True, (0, 255, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = v[0]
        screen.blit(text, (text_x, text_y))


def draw_tutorial():
    text = {"Управление": [height * 0.1, 80], "Space (пробел) - прыжок": [height * 0.3, 50]}
    for k, v in text.items():
        font = pygame.font.Font(None, v[1])
        text = font.render(k, True, (0, 255, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = v[0]
        screen.blit(text, (text_x, text_y))


def troll_window():
    troll_screen = screen
    width, height = size
    exit = Exit()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                settings_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                settings_sprites.update(event)
                if exit.rect.collidepoint(event.pos):
                    running = False

        screen.blit(load_image('backgrounds/fon1.jpg'), (0, 0))
        image = load_image("no_internet.png", "white")
        image = pygame.transform.scale(image, (300, 300))
        screen.blit(image, (width // 2 - image.get_width() // 2, height * 0.3))
        all_sprites.draw(troll_screen)
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
                if exit_btn.rect.collidepoint(event.pos):
                    running = False
                if rate.rect.collidepoint(event.pos):
                    troll_window()
                if tips.rect.collidepoint(event.pos):
                    tutorial_window()

        screen.blit(load_image('backgrounds/fon1.jpg'), (0, 0))
        clock.tick(fps)
        draw_settings()
        settings_sprites.draw(screen)
        slider.draw()
        pygame.display.flip()


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
            print(self.circle_x)
            self.flag = True
            self.draw()
            self.update_volume(x)
            return self.volume


class Button(pygame.sprite.Sprite):
    def __init__(self, point, image, image_press, action):
        super().__init__(all_sprites)
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


class Exit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.flag_press = False
        self.image = load_image("cube/exit.png", "white")
        self.image_press = load_image("cube/exit_pressed.png", "white")
        self.rect = self.image.get_rect()
        self.rect.center = width * 0.025 + self.rect.width // 2, height * 0.06 + self.rect.height // 2
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and \
                self.rect.collidepoint(event.pos):
            self.flag_press = True
            x, y, = self.rect.center
            self.image, self.image_press = self.image_press, self.image
            self.rect = self.image.get_rect()
            self.rect.center = x, y

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            self.flag_press = False


class Rate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.flag_press = False
        self.image = load_image("buttons/rate.png", (127, 127, 127))
        self.image_press = pygame.transform.scale(self.image, (240, 100))
        self.rect = self.image.get_rect()
        self.rect.center = width * 0.15 + self.rect.width // 2, height * 0.3 + self.rect.height // 2
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


class Tips(Rate):
    def __init__(self):
        super().__init__()
        self.image = load_image("buttons/tips.png", (127, 127, 127))
        self.image_press = pygame.transform.scale(self.image, (240, 100))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = width * 0.6, height * 0.3
        self.mask = pygame.mask.from_surface(self.image)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 440
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))

    pygame.mixer.music.load('music/start.mp3')  # загружаем фоновую музыку
    pygame.mixer.music.play()

    # Создаём группы спрайтов
    all_sprites = pygame.sprite.Group()
    settings_sprites = pygame.sprite.Group()
    # -------------------------Создаём кнопки------------------------------------------------
    exit_btn = Exit()
    rate = Rate()
    tips = Tips()
    slider = Slider(width * 0.4, height * 0.7, 170, 10)
    # -----------------------Основные параметры-----------------------------------------------
    fps = 100
    clock = pygame.time.Clock()

    settings_window()
    pygame.mixer.music.stop()
    pygame.quit()
