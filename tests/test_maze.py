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
    def test_generate_marks_start_cell_visited(self):
        maze = Maze(2, 2)

        maze.generate()

        self.assertTrue(maze.grid[0][0].visited)

    def test_generation_visits_more_than_one_cell(self):
        maze = Maze(2, 2)

        maze.generate()

        visited_count = 0

        for row in maze.grid:
            for cell in row:
                if cell.visited:
                    visited_count += 1

        self.assertGreater(visited_count, 1)
    
    def test_generation_removes_a_wall(self):
        maze = Maze(2, 2)

        maze.generate()

        start = maze.grid[0][0]

        wall_removed = (
            not start.north_wall or
            not start.south_wall or
            not start.east_wall or
            not start.west_wall
        )

        self.assertTrue(wall_removed)
    def test_generation_visits_all_cells(self):
        maze = Maze(3, 3)

        maze.generate()

        for row in maze.grid:
            for cell in row:
                self.assertTrue(cell.visited)

    def test_maze_can_render_as_string(self):
        maze = Maze(2, 2)
        maze.generate()

        output = maze.render()

        self.assertIsInstance(output, str)
        self.assertTrue(len(output) > 0)
    
    def test_maze_has_start_and_end(self):
        maze = Maze(3, 3)

        self.assertIsNotNone(maze.start)
        self.assertIsNotNone(maze.end)
        
    def test_maze_can_reset_visited(self):
        maze = Maze(2, 2)
        maze.generate()

        maze.reset_visited()

        for row in maze.grid:
            for cell in row:
                self.assertFalse(cell.visited)
if __name__ == "__main__":
    unittest.main()