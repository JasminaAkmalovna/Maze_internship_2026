class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False

        self.north_wall = True
        self.south_wall = True
        self.east_wall = True
        self.west_wall = True