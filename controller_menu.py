import interface_menu
import engine_menu
import controller

class ControllerMenu:
    def __init__(self):
        self.interface_menu = interface_menu.InterfaceMenu(self)
        self.engine_menu = engine_menu.EngineMenu(self)
        self.start_menu()

    def start_menu(self):
        self.interface_menu.draw_menu()
        self.engine_menu.start()
    
    def start_1_player(self):
        game = controller.Controller(6, 7, 80)

    def start_2_player(self):
        game = controller.Controller(6, 7, 80)
        game.start_2_player()
