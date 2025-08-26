import pygame

class InterfaceMenu:
    def __init__(self, controller):
        self.controller = controller

    def draw_menu(self):
        pygame.init()
        pygame.font.init()
        width, height = 400, 300
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Menu")

        # Fill background
        screen.fill((30, 30, 30))

        font = pygame.font.SysFont(None, 48)
        title = font.render("Choisissez le mode", True, (255, 255, 255))
        screen.blit(title, (width // 2 - title.get_width() // 2, 40))

        button_font = pygame.font.SysFont(None, 36)
        btn1_text = button_font.render("1 Joueur", True, (0, 0, 0))
        btn2_text = button_font.render("2 Joueurs", True, (0, 0, 0))

        btn_width, btn_height = 200, 50
        btn1_rect = pygame.Rect(width // 2 - btn_width // 2, 120, btn_width, btn_height)
        btn2_rect = pygame.Rect(width // 2 - btn_width // 2, 190, btn_width, btn_height)

        pygame.draw.rect(screen, (200, 200, 200), btn1_rect)
        pygame.draw.rect(screen, (200, 200, 200), btn2_rect)

        screen.blit(btn1_text, (btn1_rect.x + (btn_width - btn1_text.get_width()) // 2, btn1_rect.y + (btn_height - btn1_text.get_height()) // 2))
        screen.blit(btn2_text, (btn2_rect.x + (btn_width - btn2_text.get_width()) // 2, btn2_rect.y + (btn_height - btn2_text.get_height()) // 2))

        pygame.display.flip()