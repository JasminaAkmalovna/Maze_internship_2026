# src/solver.py

class Solver:
    def __init__(self, maze):
        self.maze = maze

    def solve(self):
        # Using a Stack for DFS. Holds tuples of (current_cell, path_taken_so_far)
        stack = [(self.maze.start, [(self.maze.start.row, self.maze.start.col)])]
        visited = set()

        while stack:
            # Notice we use .pop() here! This makes it a Stack (Last-In, First-Out)
            # This is what makes it a DFS instead of a BFS.
            current_cell, path = stack.pop()

            # If we reached the end, return the path!
            if current_cell == self.maze.end:
                return path

            if current_cell in visited:
                continue
                
            visited.add(current_cell)

            r = current_cell.row
            c = current_cell.col

            # Check North
            if not current_cell.north_wall and r > 0:
                neighbor = self.maze.grid[r - 1][c]
                stack.append((neighbor, path + [(neighbor.row, neighbor.col)]))
                
            # Check South
            if not current_cell.south_wall and r < self.maze.rows - 1:
                neighbor = self.maze.grid[r + 1][c]
                stack.append((neighbor, path + [(neighbor.row, neighbor.col)]))
                
            # Check East
            if not current_cell.east_wall and c < self.maze.cols - 1:
                neighbor = self.maze.grid[r][c + 1]
                stack.append((neighbor, path + [(neighbor.row, neighbor.col)]))
                
            # Check West
            if not current_cell.west_wall and c > 0:
                neighbor = self.maze.grid[r][c - 1]
                stack.append((neighbor, path + [(neighbor.row, neighbor.col)]))

        # If no path is found
        return []