import unittest
from src.maze import Maze
from src.cell import Cell
class TestMaze(unittest.TestCase):

    def test_maze_has_rows_and_cols(self):
        maze = Maze(3, 4)

        self.assertEqual(maze.rows, 3)
        self.assertEqual(maze.cols, 4)
    def test_maze_creates_grid(self):
        maze = Maze(2, 3)

        self.assertEqual(len(maze.grid), 2)
        self.assertEqual(len(maze.grid[0]), 3)
   
    def test_grid_contains_cells(self):
        maze = Maze(2, 3)

        self.assertIsInstance(maze.grid[0][0], Cell)
    def test_top_left_cell_has_two_neighbors(self):
        maze = Maze(3, 3)

        neighbors = maze.get_neighbors(0, 0)

        self.assertEqual(len(neighbors), 2)
    def test_remove_wall_between_horizontal_neighbors(self):
        maze = Maze(1, 2)

        left = maze.grid[0][0]
        right = maze.grid[0][1]

        maze.remove_wall_between(left, right)

        self.assertFalse(left.east_wall)
        self.assertFalse(right.west_wall)

    def test_remove_wall_between_vertical_neighbors(self):
        maze = Maze(2, 1)

        top = maze.grid[0][0]
        bottom = maze.grid[1][0]

        maze.remove_wall_between(top, bottom)

        self.assertFalse(top.south_wall)
        self.assertFalse(bottom.north_wall)
        
    def test_get_unvisited_neighbors(self):
        maze = Maze(2, 2)

        cell = maze.grid[0][0]

        neighbors = maze.get_unvisited_neighbors(cell)

        self.assertEqual(len(neighbors), 2)
if __name__ == "__main__":
    unittest.main()