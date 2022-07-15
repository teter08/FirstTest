class Cell:
    def __init__(self, around_mines: int, mine: bool):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.pole = []

    def init(self):
        pass

    def show(self):
        pass
