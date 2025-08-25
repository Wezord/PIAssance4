import engine
import interface

class Controller:
    def __init__(self, row, col, cellSize):
        self.row = row
        self.col = col
        self.cellSize = cellSize
        self.interface = interface.Interface(self)
        self.engine = engine.Engine(self)

    def start(self):
        self.interface.draw_board()
        self.engine.start()

    def draw_coin(self, row, col):
        self.interface.draw_coin(row, col)

    def getCurrentPlayer(self):
        return self.engine.getCurrentPlayer()

    def getRows(self):
        return self.row

    def getCols(self):
        return self.col

    def getCellSize(self):
        return self.cellSize

    def getScore(self):
        return self.engine.getScore()

    