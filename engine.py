import pygame

class Engine:
    def __init__(self, controller):
        self.running = True
        self.controller = controller
        self.board = [[0 for _ in range(self.controller.getRows())] for _ in range(self.controller.getCols())]

    def start(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        pygame.quit()

    def stop(self):
        self.state = "stopped"

    def get_state(self):
        return self.state


    