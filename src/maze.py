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
    def remove_wall_between(self, cell1, cell2):
        if cell1.row == cell2.row:
            if cell1.col < cell2.col:
                cell1.east_wall = False
                cell2.west_wall = False
            else:
                cell1.west_wall = False
                cell2.east_wall = False
        elif cell1.col == cell2.col:
            if cell1.row < cell2.row:
                cell1.south_wall = False
                cell2.north_wall = False
            else:
                cell1.north_wall = False
                cell2.south_wall = False
    def get_unvisited_neighbors(self, cell):
        neighbors = self.get_neighbors(cell.row, cell.col)

        return [n for n in neighbors if not n.visited]
    def generate(self):
        start = self.grid[0][0]
        self._dfs_generate(start)
    
    def _dfs_generate(self, cell):
        cell.visited = True

        neighbors = self.get_unvisited_neighbors(cell)

        for neighbor in neighbors:
            self.remove_wall_between(cell, neighbor)
            self._dfs_generate(neighbor)
    def render(self):
        output = ""

        # top border
        output += "+" + "---+" * self.cols + "\n"

        for row in self.grid:
            top = "|"
            bottom = "+"

            for cell in row:
                top += "   " if not cell.east_wall else "   |"

                bottom += "---+" if cell.south_wall else "   +"

            output += top + "\n"
            output += bottom + "\n"

        return output
        