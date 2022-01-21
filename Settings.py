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


def draw_text():
    font = pygame.font.SysFont("Calibri", 50)
    text = font.render("Невозможно подключиться к сети :(", True, (0, 255, 0))
    text_x = width * 0.09
    text_y = height * 0.1
    screen.blit(text, (text_x, text_y))


def draw_settings_tutorial(text):
    for k, v in text.items():
        font = pygame.font.SysFont("Calibri", v[1])
        text = font.render(k, True, (0, 255, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = v[0]
        screen.blit(text, (text_x, text_y))


def tutorial_window():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                tutorial_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                tutorial_sprites.update(event)
                if exit_btn.rect.collidepoint(event.pos):
                    running = False
        screen.fill((54, 85, 110))
        clock.tick(fps)
        draw_settings_tutorial(text={"Управление": [height * 0.1, 80], "Space (пробел) - прыжок": [height * 0.3, 50]})
        tutorial_sprites.draw(screen)
        pygame.display.flip()


def troll_window():
    width, height = size
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                troll_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                troll_sprites.update(event)
                if exit_btn.rect.collidepoint(event.pos):
                    running = False

        screen.fill((54, 85, 110))
        image = load_image("no_internet.png", "white")
        image = pygame.transform.scale(image, (300, 300))
        screen.blit(image, (width // 2 - image.get_width() // 2, height * 0.25))
        troll_sprites.draw(screen)
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
                if rate.rect.collidepoint(event.pos):
                    troll_window()
                if tips.rect.collidepoint(event.pos):
                    tutorial_window()

        screen.fill((54, 85, 110))
        clock.tick(fps)
        draw_settings_tutorial(text={"Настройки": [height * 0.1, 80], "Громкость": [height * 0.6, 50]})
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
            self.flag = True
            self.draw()
            self.update_volume(x)
            return self.volume


class Button(pygame.sprite.Sprite):
    def __init__(self, point, image, image_press, fon, action, *sprite_groups):
        super().__init__(*sprite_groups)
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

        if event.type == pygame.MOUSEBUTTONUP and self.flag_press:
            exec(self.action)
            self.flag_press = False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 840, 440
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Geometry dash')
    pygame.display.set_icon(pygame.image.load("images/icon.png"))

    """pygame.mixer.music.load('music/start.mp3')  # загружаем фоновую музыку
    pygame.mixer.music.play()"""

    # Создаём группы спрайтов
    settings_sprites = pygame.sprite.Group()  # группа спайтов основного окна настроек
    troll_sprites = pygame.sprite.Group()  # группа спайтов окна "Без Интернета"
    tutorial_sprites = pygame.sprite.Group()  # группа спайтов окна управления/обучения
    # -------------------------Создаём кнопки------------------------------------------------
    exit_btn = Button((width * 0.025 + 31, height * 0.06 + 29),
                      "cube/exit.png", "cube/exit_pressed.png", "white", '', troll_sprites, tutorial_sprites)
    rate = Button((width * 0.15 + 105, height * 0.3 + 40),
                  "buttons/rate.png", "buttons/rate_pressed.png", "white", '', settings_sprites)
    tips = Button((width * 0.6 + 105, height * 0.3 + 40),
                  "buttons/tips.png", "buttons/tips_pressed.png", "white", '', settings_sprites)
    slider = Slider(width * 0.4, height * 0.75, 170, 10)
    # -----------------------Основные параметры-----------------------------------------------
    fps = 100
    clock = pygame.time.Clock()

    settings_window()
    """pygame.mixer.music.stop()"""
    pygame.quit()
