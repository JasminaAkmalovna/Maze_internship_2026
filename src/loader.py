# src/loader.py
from src.maze import Maze

def load_maze_from_file(filename):
    """Reads a text map file and returns a fully configured Maze object.
    Robustly handles uneven line lengths or copy-paste spacing trims.
    """
    with open(filename, 'r') as f:
        # Read lines and strip out only newline characters
        raw_lines = [line.replace('\r', '').replace('\n', '') for line in f.readlines() if line.strip()]

    if not raw_lines:
        raise ValueError("The maze file is empty.")

    rows = len(raw_lines)
    # Determine the maximum width to protect against out-of-bounds errors
    cols = max(len(line) for line in raw_lines)
    
    # Pad any shorter lines with walls ('#') to make the matrix perfectly uniform
    lines = [line.ljust(cols, '#') for line in raw_lines]
    
    # Initialize a blank maze grid
    maze = Maze(rows, cols, generate=False)

    for r in range(rows):
        for c in range(cols):
            char = lines[r][c]
            current_cell = maze.grid[r][c]

            if char == 'S':
                maze.start = current_cell
            elif char == 'E':
                maze.end = current_cell

            # If it's a path space, knock down walls to adjacent connected paths
            if char != '#':
                if r > 0 and lines[r-1][c] != '#':
                    current_cell.north_wall = False
                    maze.grid[r-1][c].south_wall = False
                if r < rows - 1 and lines[r+1][c] != '#':
                    current_cell.south_wall = False
                    maze.grid[r+1][c].north_wall = False
                if c > 0 and lines[r][c-1] != '#':
                    current_cell.west_wall = False
                    maze.grid[r][c-1].east_wall = False
                if c < cols - 1 and lines[r][c+1] != '#':
                    current_cell.east_wall = False
                    maze.grid[r][c+1].west_wall = False
    
    # Fail-safe defaults if markers are missing
    if not maze.start: maze.start = maze.grid[0][0]
    if not maze.end: maze.end = maze.grid[rows-1][cols-1]
    
    return maze