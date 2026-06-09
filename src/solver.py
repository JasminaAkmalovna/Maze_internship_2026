# src/solver.py
import heapq

class Solver:
    def __init__(self, maze, algorithm="dfs"):
        self.maze = maze
        self.algorithm = algorithm.lower()

    def solve(self):
        if self.algorithm == "bfs":
            return self._solve_bfs()
        elif self.algorithm == "astar":
            return self._solve_astar()
        else:
            return self._solve_dfs() # Default to DFS

    def _get_valid_neighbors(self, cell):
        """Helper method to clean up our algorithms"""
        neighbors = []
        r, c = cell.row, cell.col
        
        if not cell.north_wall and r > 0:
            neighbors.append(self.maze.grid[r - 1][c])
        if not cell.south_wall and r < self.maze.rows - 1:
            neighbors.append(self.maze.grid[r + 1][c])
        if not cell.east_wall and c < self.maze.cols - 1:
            neighbors.append(self.maze.grid[r][c + 1])
        if not cell.west_wall and c > 0:
            neighbors.append(self.maze.grid[r][c - 1])
            
        return neighbors

    def _solve_dfs(self):
        stack = [(self.maze.start, [(self.maze.start.row, self.maze.start.col)])]
        visited = set()

        while stack:
            current_cell, path = stack.pop() # Pop from end (Stack)

            if current_cell == self.maze.end:
                return path

            if current_cell in visited:
                continue
            visited.add(current_cell)

            for neighbor in self._get_valid_neighbors(current_cell):
                stack.append((neighbor, path + [(neighbor.row, neighbor.col)]))
        return []

    def _solve_bfs(self):
        queue = [(self.maze.start, [(self.maze.start.row, self.maze.start.col)])]
        visited = set()

        while queue:
            current_cell, path = queue.pop(0) # Pop from front (Queue)

            if current_cell == self.maze.end:
                return path

            if current_cell in visited:
                continue
            visited.add(current_cell)

            for neighbor in self._get_valid_neighbors(current_cell):
                queue.append((neighbor, path + [(neighbor.row, neighbor.col)]))
        return []

    def _solve_astar(self):
        # A* uses a priority queue based on: f_score = distance_traveled + estimated_distance_to_end
        def heuristic(cell):
            # Manhattan distance (rows away + cols away)
            return abs(cell.row - self.maze.end.row) + abs(cell.col - self.maze.end.col)

        count = 0 # Tie-breaker for the priority queue
        # Queue stores: (f_score, count, current_cell, path)
        queue = [(0, count, self.maze.start, [(self.maze.start.row, self.maze.start.col)])]
        visited = set()

        while queue:
            _, _, current_cell, path = heapq.heappop(queue)

            if current_cell == self.maze.end:
                return path

            if current_cell in visited:
                continue
            visited.add(current_cell)

            for neighbor in self._get_valid_neighbors(current_cell):
                g_score = len(path) # Distance traveled so far
                h_score = heuristic(neighbor) # Guess to the end
                f_score = g_score + h_score
                
                count += 1
                heapq.heappush(queue, (f_score, count, neighbor, path + [(neighbor.row, neighbor.col)]))
        return []