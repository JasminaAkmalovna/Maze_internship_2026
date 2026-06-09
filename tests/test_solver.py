# tests/test_solver.py
import unittest
from src.maze import Maze
from src.solver import Solver
from tests.manual_mazes import get_simple_2x2_maze, get_unsolvable_2x2_maze

class TestSolver(unittest.TestCase):
    
    def test_solver_initializes_with_maze(self):
        maze = get_simple_2x2_maze()
        solver = Solver(maze)
        
        self.assertEqual(solver.maze, maze)

    def test_algorithms_find_correct_path(self):
        maze = get_simple_2x2_maze()
        
        # Test DFS
        dfs_solver = Solver(maze, algorithm="dfs")
        self.assertEqual(dfs_solver.solve(), [(0, 0), (0, 1), (1, 1)])

        # Test BFS
        bfs_solver = Solver(maze, algorithm="bfs")
        self.assertEqual(bfs_solver.solve(), [(0, 0), (0, 1), (1, 1)])
        
        # Test A*
        astar_solver = Solver(maze, algorithm="astar")
        self.assertEqual(astar_solver.solve(), [(0, 0), (0, 1), (1, 1)])
    
    
    def test_solver_returns_empty_list_when_unsolvable(self):
        maze = get_unsolvable_2x2_maze()
        solver = Solver(maze)
        
        path = solver.solve()
        
        # If there is no path, it should return an empty list
        self.assertEqual(path, [])
    def test_solver_handles_start_being_the_end(self):
        # A 1x1 maze means the start (0,0) is also the end (0,0)
        maze = Maze(1, 1)
        solver = Solver(maze)
        
        path = solver.solve()
        
        expected_path = [(0, 0)]
        self.assertEqual(path, expected_path)
    
    

if __name__ == "__main__":
    unittest.main()