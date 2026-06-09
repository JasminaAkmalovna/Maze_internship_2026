# src/solver.py
import heapq

class Solver:
    def __init__(self, maze, algorithm="dfs"):
        self.maze = maze
        self.algorithm = algorithm.lower()

    def solve(self, return_history=False):
        if self.algorithm == "bfs":
            return self._solve_bfs(return_history)
        elif self.algorithm == "astar":
            return self._solve_astar(return_history)
        else:
            return self._solve_dfs(return_history)

    def _get_valid_neighbors(self, cell):
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

    def _solve_dfs(self, return_history):
        stack = [(self.maze.start, [(self.maze.start.row, self.maze.start.col)])]
        visited = set()
        history = []

        # Manhattan distance heuristic helper to pull the search toward the exit
        def distance_to_end(cell):
            return abs(cell.row - self.maze.end.row) + abs(cell.col - self.maze.end.col)

        while stack:
            current_cell, path = stack.pop()

            if current_cell in visited:
                continue
            visited.add(current_cell)

            if return_history:
                history.append(({(c.row, c.col) for c in visited}, list(path)))

            if current_cell == self.maze.end:
                return (path, history) if return_history else path

            # OPTIMIZATION: Fetch neighbors and sort them by distance to the end.
            # Since stack is Last-In, First-Out (LIFO), reversing the sort puts the 
            # neighbor CLOSEST to the exit on TOP of the stack to be processed first.
            neighbors = self._get_valid_neighbors(current_cell)
            neighbors.sort(key=distance_to_end, reverse=True)

            for neighbor in neighbors:
                stack.append((neighbor, path + [(neighbor.row, neighbor.col)]))
        return ([], history) if return_history else []

    def _solve_bfs(self, return_history):
        queue = [(self.maze.start, [(self.maze.start.row, self.maze.start.col)])]
        visited = set()
        history = []

        while queue:
            current_cell, path = queue.pop(0)

            if current_cell in visited:
                continue
            visited.add(current_cell)

            if return_history:
                history.append(({(c.row, c.col) for c in visited}, list(path)))

            if current_cell == self.maze.end:
                return (path, history) if return_history else path

            for neighbor in self._get_valid_neighbors(current_cell):
                queue.append((neighbor, path + [(neighbor.row, neighbor.col)]))
        return ([], history) if return_history else []

    def _solve_astar(self, return_history):
        def heuristic(cell):
            return abs(cell.row - self.maze.end.row) + abs(cell.col - self.maze.end.col)

        count = 0
        queue = [(0, count, self.maze.start, [(self.maze.start.row, self.maze.start.col)])]
        visited = set()
        history = []

        while queue:
            _, _, current_cell, path = heapq.heappop(queue)

            if current_cell in visited:
                continue
            visited.add(current_cell)

            if return_history:
                history.append(({(c.row, c.col) for c in visited}, list(path)))

            if current_cell == self.maze.end:
                return (path, history) if return_history else path

            for neighbor in self._get_valid_neighbors(current_cell):
                g_score = len(path)
                h_score = heuristic(neighbor)
                f_score = g_score + h_score
                count += 1
                heapq.heappush(queue, (f_score, count, neighbor, path + [(neighbor.row, neighbor.col)]))
        return ([], history) if return_history else []