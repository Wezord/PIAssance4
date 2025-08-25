import pygame

class Interface:
    def __init__(self, controller):
        self.controller = controller

    def draw_board(self):
        pygame.init()
        cell_size = self.controller.getCellSize()
        rows, cols = self.controller.getRows(), self.controller.getCols()
        width, height = cols * cell_size, rows * cell_size
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("6x7 Grid")

        screen.fill((0, 0, 0))
        for row in range(rows):
            for col in range(cols):
                rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect, 2)

        pygame.display.flip()

    def draw_coin(self, row, col):
        player = self.controller.getCurrentPlayer()
        cell_size = self.controller.getCellSize()
        color = (255, 0, 0) if player == 1 else (255, 255, 0)  # Rouge pour joueur 1, jaune sinon

        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2

        pygame.draw.circle(pygame.display.get_surface(), color, (x, y), 25)
        pygame.display.flip()
