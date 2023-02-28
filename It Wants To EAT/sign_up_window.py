import pygame
import random
import time
from load_image import load_image
from random import shuffle

pygame.init()
pygame.display.set_caption('It Wants To EAT')
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
passive_confirm_btn = load_image('pixil-frame-0 (18).png')
active_confirm_btn = load_image('pixil-frame-0 (19).png')
passive_gen_pass_btn = load_image('pixil-frame-0 (22).png')
active_gen_pass_btn = load_image('pixil-frame-0 (20).png')

class SignUpWindow:
    def __init__(self, screen):
        self.screen = screen

    def background_image(self):
        image = pygame.image.load('data\image.png').convert_alpha()
        image = pygame.transform.scale(image, (width, height))
        rect = image.get_rect()
        self.screen.blit(image, rect)

    def draw_title(self):
        self.font = pygame.font.Font('data/Sonic 1 Title Screen Filled.ttf', 28)
        title = self.font.render('Sign Up', True, 'red')
        pos = title.get_rect(center=(300, 150))
        self.screen.blit(title, pos)
        pygame.display.update()

class InputBox:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.rect = pygame.Rect(self.x, self.y, 250, 50)
        self.input_surf = pygame.Surface((250, 50))
        self.passive_color = pygame.Color('#9F0000')
        self.active_color = pygame.Color('#FF0000')
        self.color = self.passive_color
        self.font = pygame.font.Font('data/Sonic 1 Title Screen Filled.ttf', 16)
        self.text = text
        self.symbol = self.font.render(self.text, True, self.color)
        self.all_symbols = []
        self.active = False
        self.flag = True

    def generate_password(self):
        length = []
        abc = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
        for letter in abc:
            length.append(letter)
        shuffle(length)
        self.shuffled_password = ''.join(length[:10])
        self.flag = False

    def generate(self, event):
        screen.blit(self.input_surf, self.rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.text = ''
                self.active = not self.active
            else:
                self.active = False
            self.color = self.active_color if self.active else self.passive_color
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.symbol)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE and len(self.all_symbols) > 0:
                    self.text = self.text[:-1]
                    self.all_symbols.remove(self.all_symbols[-1])
                elif len(self.all_symbols) < 16:
                    self.text += event.unicode
                    self.all_symbols.append(self.text)
                self.symbol = self.font.render(self.text, True, self.color)
        pygame.draw.rect(screen, self.color, self.rect, 3)
        screen.blit(self.symbol, (self.rect.x + 5, self.rect.y + 10))


class Button(pygame.sprite.Sprite):
    def __init__(self, group, x, y, btn_passive, btn_active, on_click):
        super().__init__(group)
        self.btn_passive, self.btn_active = btn_passive, btn_active
        self.image = btn_passive
        self.on_click = on_click
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(args[0].pos):
                self.image = self.btn_active
            else:
                self.image = self.btn_passive
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
             self.on_click()


pelmen_image = pygame.image.load('data/pelmen.png')
hero_image = pygame.image.load('data/shlepa_in_the_basket.png')
all_sprites = pygame.sprite.Group()



ib = InputBox(175, 225, 'user name')
ib_2 = InputBox(175, 275, 'password')
running = True


def closeall():
    global running
    running = False


button = Button(all_sprites, 225, 400, passive_confirm_btn, active_confirm_btn, closeall)
button_2 = Button(all_sprites, 375, 400, passive_gen_pass_btn, active_gen_pass_btn, ib_2.generate_password)
sign = SignUpWindow(screen)
sign.draw_title()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ib.generate(event)
        ib_2.generate(event)
        all_sprites.update(event)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()