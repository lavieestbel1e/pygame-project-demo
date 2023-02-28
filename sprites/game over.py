from main import load_image
import pygame


def move(image):
    rect = image.get_rect()
    while rect.top != 0 and rect.bottom != 600:
        rect = image.get_rect()
        rect.top += 0.00000000000000000000000000000000001
        rect.bottom += 0.00000000000000000000000000000000001



pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
gameover_image = load_image('gameover.png')
pygame.display.set_caption('Game Over')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        image = gameover_image
        move(image)
    screen.fill('blue')
    pygame.display.flip()
pygame.quit()