# main.py
import os
from src.maze import Maze
from src.solver import Solver
from src.ui import generate_smooth_frames, animate_search_process
from src.loader import load_maze_from_file

def main():
    print("---------------------------------------------")
    print("Welcome to the Procedural Labyrinth Suite!")
    print("---------------------------------------------")
    print("1. Generate a Random Maze")
    print("2. Load Maze from a Text File")
    mode = input("Select an option (1-2) [Default: 1]: ").strip()

    # main.py (Updated Loading Block)
    if mode == "2":
        filename = input("Enter maze filename (e.g., maze_spiral.txt) [Default: maze.txt]: ").strip() or "maze.txt"
        
        if not os.path.exists(filename):
            print(f"❌ '{filename}' not found! Falling back to random generation.")
            mode = "1"
        else:
            try:
                print(f"📂 Loading '{filename}' layout...")
                maze = load_maze_from_file(filename)
            except Exception as e:
                # Catch empty files or completely unreadable formatting safely
                print(f"❌ Failed to parse '{filename}': {e}")
                print("Falling back to random maze generation.")
                mode = "1"
    if mode != "2":
        try:
            height = int(input("Enter maze height/rows (e.g., 10): ") or 10)
            width = int(input("Enter maze width/columns (e.g., 15): ") or 15)
        except ValueError:
            print("Invalid number entered. Defaulting to 10x15.")
            height, width = 10, 15

        print(f"\nGenerating a {height}x{width} maze layout...")
        maze = Maze(height, width)
        maze.generate()

    print("\nChoose Animation Speed:")
    print("1. Slow")
    print("2. Medium")
    print("3. Fast")
    speed_choice = input("Enter 1, 2, or 3 [Default: 2]: ")
    
    speed_map = {"1": (0.3, "SLOW"), "2": (0.12, "MED"), "3": (0.04, "FAST")}
    speed_delay, speed_name = speed_map.get(speed_choice, (0.12, "MED"))

    print("\nChoose your pathfinding algorithm:")
    print("1. DFS (Depth-First Search)")
    print("2. BFS (Breadth-First Search)")
    print("3. A* (A-Star)")
    
    choice = input("Enter 1, 2, or 3 (default is DFS): ")
    algo_map = {"1": "dfs", "2": "bfs", "3": "astar"}
    selected_algo = algo_map.get(choice, "dfs")

    solver = Solver(maze, algorithm=selected_algo)
    path, history = solver.solve(return_history=True)
    
    if history:
        print("Calculating smooth backtracking trajectory frames...")
        smooth_frames = generate_smooth_frames(history)
        animate_search_process(maze, smooth_frames, speed_delay, speed_name)
        print(f"\nTarget path secured using {selected_algo.upper()} in {len(path)} active steps.")
    else:
        print("\n--- GENERATED TERMINAL MAZE ---")
        print(maze.render())
        print("\nNo structural path resolved.")

if __name__ == "__main__":
    main()