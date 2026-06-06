from src.cell import Cell

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = [
            [Cell(r, c) for c in range(cols)]
            for r in range(rows)
        ]