# tests/test_loader.py
import unittest
import os
from src.loader import load_maze_from_file

class TestLoader(unittest.TestCase):
    def setUp(self):
        """Create a temporary maze text file before each test runs."""
        self.test_filename = "test_map_temp.txt"
        with open(self.test_filename, "w") as f:
            f.write("#####\n")
            f.write("#S E#\n")
            f.write("#####\n")

    def tearDown(self):
        """Clean up and delete the temporary file after each test finishes."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_load_maze_dimensions_and_markers(self):
        """Test that the loader correctly parses dimensions and finds S and E."""
        maze = load_maze_from_file(self.test_filename)
        
        # 1. Check if dimensions match our 3x5 layout
        self.assertEqual(maze.rows, 3)
        self.assertEqual(maze.cols, 5)
        
        # 2. Check if Start and End cells were auto-detected correctly
        self.assertIsNotNone(maze.start, "Start cell (S) was not detected!")
        self.assertIsNotNone(maze.end, "End cell (E) was not detected!")
        
        # 3. Check specific coordinate mappings
        self.assertEqual((maze.start.row, maze.start.col), (1, 1))
        self.assertEqual((maze.end.row, maze.end.col), (1, 3))