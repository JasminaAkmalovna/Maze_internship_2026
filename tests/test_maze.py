import unittest
from src.maze import Maze

class TestMaze(unittest.TestCase):

    def test_maze_has_rows_and_cols(self):
        maze = Maze(3, 4)

        self.assertEqual(maze.rows, 3)
        self.assertEqual(maze.cols, 4)
    def test_maze_creates_grid(self):
        maze = Maze(2, 3)

        self.assertEqual(len(maze.grid), 2)
        self.assertEqual(len(maze.grid[0]), 3)
if __name__ == "__main__":
    unittest.main()