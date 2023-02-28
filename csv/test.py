import pygame



pygame.init()
pygame.display.set_caption('Buttons')
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill('white')
button_surface = pygame.Surface((150, 25))
button_rect = pygame.Rect(300, 300, 150, 25)
font = pygame.font.Font('data/Sonic 1 Title Screen Filled.ttf', 16)
button_font = font.render('Bойти', True, 'red')
screen.blit(button_surface, button_rect)
screen.blit(button_font, button_rect)
colors = {
    'normal': 'black',
    'hover': 'blue',
    'pressed': 'grey',
}
mouse = pygame.mouse.get_pos()
pygame.draw.rect(button_surface, colors['normal'], button_rect, 0)
if button_rect.collidepoint(mouse):
    pygame.draw.rect(button_surface, colors['hover'], button_rect, 0)
    if pygame.mouse.get_pressed():
        pygame.draw.rect(button_surface, colors['clicked'], button_rect, 0)
pygame.display.update()

class Landing():
    pygame.draw.rect(button_surface, colors['normal'], button_rect, 0)

    def __init__(self, pos):
        self.button_surface = pygame.Surface((150, 25))
        self.button_rect = pygame.Rect(300, 300, 150, 25)
        self.button = pygame.draw.rect(button_surface, colors['normal'], button_rect, 0)
        self.mask = pygame.mask.from_surface(self.button_rect)
        self.button_rect.x = pos[0]
        self.button_rect.y = pos[1]

    def update(self):
        pygame.draw.rect(button_surface, colors['pressed'], button_rect, 0)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()