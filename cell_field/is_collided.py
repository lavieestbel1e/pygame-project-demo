import pygame


class Board:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.board = [[0] * width for _ in range(height)]
        self.top, self.left, self.cell = 0, 0, 30

    def get_click(self, mouse_pos):
        cell_coords = self.get_cell(mouse_pos)
        if cell_coords:
            self.on_click(cell_coords)

    def on_click(self, cell_coords):
        row, col = cell_coords
        self.board[row][col] = 1 - self.board[row][col]

    def set_view(self, left, top, cell):
        self.left, self.top, self.cell = left, top, cell

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        col = (x - self.left) // self.cell
        row = (y - self.top) // self.cell
        if 0 <= col < self.width and 0 <= row < self.height:
            return row, col
        return None

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + j * self.cell, self.top + i * self.cell,
                                                           self.cell, self.cell), 1)


if __name__ == '__main__':
    board = Board(5, 7)
    board.set_view(100, 100, 30)
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()