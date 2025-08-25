import pygame

class Engine:
    def __init__(self, controller):
        self.running = True
        self.controller = controller
        self.currentPlayer = 1
        self.score = {"1" : 0, "2":0}
        self.board = [[0 for _ in range(self.controller.getRows())] for _ in range(self.controller.getCols())]

    def start(self):
        self.resetBoard()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    cell_size = self.controller.getCellSize()
                    col = x // cell_size
                    row = y // cell_size

                    print("Clique en ", row, col)

                    row = self.fillBoard(col)
                    if row != None:
                        self.controller.draw_coin(row, col)

                        if self.isWin():
                            print("Joueur a gagné", self.currentPlayer)
                            self.score[str(self.currentPlayer)] += 1
                            self.running = False
                        
                        if self.isDraw():
                            print("Égalité !")
                            self.running = False

                        self.nextPlayer()

        print("Score est ", self.score["1"], self.score["2"])

        pygame.quit()

        self.controller.start()

    def nextPlayer(self):
        # Toggle between player 1 and 2
        self.currentPlayer = 2 if self.currentPlayer == 1 else 1

    def fillBoard(self, col):
        # Find the lowest empty row in the given column and fill it with the current player's value
        for row in reversed(range(self.controller.getRows())):
            if self.board[col][row] == 0:
                self.board[col][row] = self.currentPlayer
                return row  # Return the row where the coin was placed
        print("Colonne pleine")
        return None  # Column is full

    def isWin(self):
        rows = self.controller.getRows()
        cols = self.controller.getCols()
        player = self.currentPlayer

        # Check horizontal
        for row in range(rows):
            count = 0
            for col in range(cols):
                if self.board[col][row] == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        # Check vertical
        for col in range(cols):
            count = 0
            for row in range(rows):
                if self.board[col][row] == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        # Check diagonal (bottom-left to top-right)
        for col in range(cols - 3):
            for row in range(rows - 3):
                if (self.board[col][row] == player and
                    self.board[col+1][row+1] == player and
                    self.board[col+2][row+2] == player and
                    self.board[col+3][row+3] == player):
                    return True

        # Check diagonal (top-left to bottom-right)
        for col in range(cols - 3):
            for row in range(3, rows):
                if (self.board[col][row] == player and
                    self.board[col+1][row-1] == player and
                    self.board[col+2][row-2] == player and
                    self.board[col+3][row-3] == player):
                    return True

        return False
    
    def isDraw(self):
        for col in self.board:
            if 0 in col:
                return False
        return True
    
    def resetBoard(self):
        self.board = [[0 for _ in range(self.controller.getRows())] for _ in range(self.controller.getCols())]

    def stop(self):
        self.state = "stopped"

    def get_state(self):
        return self.state

    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def getScore(self):
        return self.score

    