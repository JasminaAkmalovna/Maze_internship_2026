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
if __name__ == "__main__":
    unittest.main()