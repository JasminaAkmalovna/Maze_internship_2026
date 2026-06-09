# main.py
from src.maze import Maze
from src.solver import Solver

def main():
    print("Welcome to the Procedural Labyrinth Generator!")
    print("---------------------------------------------")
    
    print("Choose your pathfinding algorithm:")
    print("1. DFS (Depth-First Search - fast, but messy paths)")
    print("2. BFS (Breadth-First Search - guarantees shortest path)")
    print("3. A* (A-Star - highly optimized shortest path)")
    
    choice = input("Enter 1, 2, or 3 (default is DFS): ")
    
    algo_map = {"1": "dfs", "2": "bfs", "3": "astar"}
    selected_algo = algo_map.get(choice, "dfs")

    # Generate a small maze so it's easy to read in the terminal
    print(f"\nGenerating a 5x5 maze and solving with {selected_algo.upper()}...")
    maze = Maze(5, 5)
    maze.generate()

    solver = Solver(maze, algorithm=selected_algo)
    path = solver.solve()

    print("\n--- GENERATED TERMINAL MAZE ---")
    print(maze.render())
    
    if path:
        print(f"\nSuccess! Path found taking {len(path)} steps.")
        print(f"Path coordinates: {path}")
    else:
        print("\nNo valid path found.")

if __name__ == "__main__":
    main()