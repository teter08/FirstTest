class Cell:
    def __init__(self, around_mines: int, mine: bool):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
