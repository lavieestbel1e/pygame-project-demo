from load_image import load_image
import pygame
import random

class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = bomb_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 100)
        self.rect.y = random.randint(0, height - 100)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
                self.image = boom_image

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
bomb_image = load_image('bomb.png')
boom_image = load_image('boom.png')
all_sprites = pygame.sprite.Group()

for _ in range(20):
    bomb = Bomb(all_sprites)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)
    screen.fill('black')
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
