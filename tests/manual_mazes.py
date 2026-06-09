# tests/manual_mazes.py
from src.maze import Maze

def get_simple_2x2_maze():
    """
    Creates this solvable 2x2 maze:
    Start -> [ ][ ]
             [-][ ] -> End
    """
    maze = Maze(2, 2)
    # Manually knock down walls to create a known path: (0,0) -> (0,1) -> (1,1)
    maze.remove_wall_between(maze.grid[0][0], maze.grid[0][1])
    maze.remove_wall_between(maze.grid[0][1], maze.grid[1][1])
    # Open entrance and exit
    maze.start.west_wall = False
    maze.end.east_wall = False
    return maze
def get_unsolvable_2x2_maze():
        """
        Creates a 2x2 maze where all internal walls are intact.
        Start -> [|][ ]
                [-][ ] -> End
        """
        maze = Maze(2, 2)
        
        # We DO NOT remove any internal walls. It is completely blocked.
        
        # Open entrance and exit
        maze.start.west_wall = False
        maze.end.east_wall = False
        
        return maze