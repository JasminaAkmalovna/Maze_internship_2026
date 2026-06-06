import unittest
from src.cell import Cell

class TestCell(unittest.TestCase):

    def test_cell_has_row_and_col(self):
        cell = Cell(2, 3)

        self.assertEqual(cell.row, 2)
        self.assertEqual(cell.col, 3)
    def test_cell_is_unvisited_by_default(self):
        cell = Cell(0, 0)
        self.assertFalse(cell.visited)
    def test_cell_has_four_walls_by_default(self):
        cell = Cell(0, 0)

        self.assertTrue(cell.north_wall)
        self.assertTrue(cell.south_wall)
        self.assertTrue(cell.east_wall)
        self.assertTrue(cell.west_wall)
    def test_can_remove_north_wall(self):

        cell = Cell(0, 0)

        cell.north_wall = False

        self.assertFalse(cell.north_wall)
if __name__ == "__main__":
    unittest.main()