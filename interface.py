import pygame

class Interface:
    def __init__(self, controller):
        self.controller = controller

    def draw_board(self):
        pygame.init()
        cell_size = self.controller.getCellSize()
        rows, cols = self.controller.getRows(), self.controller.getCols()
        score_height = 60  # Height for the score area
        width, height = cols * cell_size, rows * cell_size + score_height
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("6x7 Grid")

        # Fill background
        screen.fill((0, 0, 0))

        # Draw score area
        font = pygame.font.SysFont(None, 36)
        score1 = self.controller.getScore()["1"]
        score2 = self.controller.getScore()["2"]
        text1 = font.render(f"Joueur 1: {score1}", True, (255, 0, 0))
        text2 = font.render(f"Joueur 2: {score2}", True, (255, 255, 0))
        screen.blit(text1, (20, 10))
        screen.blit(text2, (width // 2, 10))

        # Draw grid
        for row in range(rows):
            for col in range(cols):
                rect = pygame.Rect(col * cell_size, row * cell_size + score_height, cell_size, cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect, 2)

        pygame.display.flip()

    def draw_coin(self, row, col):
        player = self.controller.getCurrentPlayer()
        cell_size = self.controller.getCellSize()
        color = (255, 0, 0) if player == 1 else (255, 255, 0)  # Rouge pour joueur 1, jaune sinon
        score_height = 60  # Same as in draw_board

        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2 + score_height

        pygame.draw.circle(pygame.display.get_surface(), color, (x, y), 25)
        pygame.display.flip()
