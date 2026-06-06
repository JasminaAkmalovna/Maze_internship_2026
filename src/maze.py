from src.cell import Cell

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.grid = [
            [Cell(r, c) for c in range(cols)]
            for r in range(rows)
        ]
    def get_neighbors(self, row, col):
        neighbors = []

        if row > 0:
            neighbors.append(self.grid[row - 1][col])

        if row < self.rows - 1:
            neighbors.append(self.grid[row + 1][col])

        if col > 0:
            neighbors.append(self.grid[row][col - 1])

        if col < self.cols - 1:
            neighbors.append(self.grid[row][col + 1])

        return neighbors