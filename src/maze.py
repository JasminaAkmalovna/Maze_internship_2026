import random
from src.cell import Cell

class Maze:
    def __init__(self, rows=10, cols=15, generate=True):  # 👈 Add 'generate=True' here
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.start = None
        self.end = None

        # 👈 Wrap your generation initializer inside this if statement:
        if generate:
            self.start = self.grid[0][0]
            self.end = self.grid[rows - 1][cols - 1]
            self._generate_maze()
        self.start = self.grid[0][0]
        self.end = self.grid[self.rows - 1][self.cols - 1]
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
        
        # Open outer walls for start and end points
        self.start.west_wall = False
        self.end.east_wall = False
    
    def _dfs_generate(self, cell):
        cell.visited = True
        
        while True:
            unvisited = self.get_unvisited_neighbors(cell)
            if not unvisited:
                break
            
            neighbor = random.choice(unvisited)
            self.remove_wall_between(cell, neighbor)
            self._dfs_generate(neighbor)

    def render(self):
        output = ""
        # Render top outer ceiling border
        output += "┏" + "━━━┳" * (self.cols - 1) + "━━━┓\n"

        for r in range(self.rows):
            row = self.grid[r]
            # Left outer entry wall marker (respects start room path)
            top = " " if not row[0].west_wall else "┃"
            
            # Bottom intersection line starts with a left junction or corner
            if r == self.rows - 1:
                bottom = "┗"
            else:
                bottom = "┣"

            for c in range(self.cols):
                cell = row[c]
                
                # 1. Build out the path body cavity space and East walls
                if cell.east_wall:
                    # End cell right-hand exit point check
                    if r == self.rows - 1 and c == self.cols - 1:
                        top += "    "
                    else:
                        top += "   ┃"
                else:
                    top += "    "

                # 2. Build out floor dividers and intersection cross segments
                if r == self.rows - 1:
                    # Last row bottom floor caps
                    bottom += "━━━┛" if c == self.cols - 1 else "━━━┻"
                else:
                    # Intermediate rows use structural cross elements
                    if cell.south_wall:
                        bottom += "━━━┫" if c == self.cols - 1 else "━━━╋"
                    else:
                        bottom += "   ┫" if c == self.cols - 1 else "   ╋"

            output += top + "\n"
            if r < self.rows - 1 or any(cell.south_wall for cell in row):
                output += bottom + "\n"
                
        return output
    def reset_visited(self):
        for row in self.grid:
            for cell in row:
                cell.visited = False

    