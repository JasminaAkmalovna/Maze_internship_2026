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
if __name__ == "__main__":
    unittest.main()