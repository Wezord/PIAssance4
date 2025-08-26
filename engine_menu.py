import pygame

pygame.init()

class EngineMenu:
    def __init__(self, controller):
        self.controller = controller
        self.running = True

    def start(self):
        self.running = True
        # Définir les rectangles des boutons une seule fois
        # Doit correspondre à interface_menu.py
        width = 400
        btn_width, btn_height = 200, 50
        bouton1_rect = pygame.Rect(width // 2 - btn_width // 2, 120, btn_width, btn_height)
        bouton2_rect = pygame.Rect(width // 2 - btn_width // 2, 190, btn_width, btn_height)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if bouton1_rect.collidepoint(mouse_pos):
                        print("Bouton 1 cliqué")
                        self.controller.start_1_player()
                        self.running = False
                    elif bouton2_rect.collidepoint(mouse_pos):
                        print("Bouton 2 cliqué")
                        self.controller.start_2_player()
                        self.running = False
        pygame.quit()