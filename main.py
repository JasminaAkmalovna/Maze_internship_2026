# main.py
import os
import time
from src.maze import Maze
from src.solver import Solver

def animate_search_process(maze, history, speed_delay):
    """
    Animates the full procedural search process frame-by-frame with dynamic speed.
    """
    base_render = maze.render()
    GREEN_DOT = "\033[92m•\033[0m"
    RED_DOT   = "\033[91m•\033[0m"

    for visited_coords, active_path in history:
        lines = base_render.split('\n')
        active_set = set(active_path)

        for line_idx in range(len(lines)):
            if line_idx % 2 == 1:
                r = (line_idx - 1) // 2
                line_list = list(lines[line_idx])
                
                for c in range(maze.cols):
                    char_idx = 2 + 4 * c
                    if (r, c) in active_set:
                        line_list[char_idx] = GREEN_DOT
                    elif (r, c) in visited_coords:
                        line_list[char_idx] = RED_DOT
                        
                lines[line_idx] = "".join(line_list)

        os.system('clear' if os.name != 'nt' else 'cls')
        print("Welcome to the Procedural Labyrinth Generator!")
        print("---------------------------------------------")
        print(f"VISUALIZATION KEY: {GREEN_DOT} Active Path  {RED_DOT} Visited/Dead End")
        print("\n" + "\n".join(lines))
        time.sleep(speed_delay)

def main():
    print("Welcome to the Procedural Labyrinth Generator!")
    print("---------------------------------------------")
    
    try:
        height = int(input("Enter maze height/rows (e.g., 10): ") or 10)
        width = int(input("Enter maze width/columns (e.g., 15): ") or 15)
    except ValueError:
        print("Invalid number entered. Defaulting to 10x15.")
        height, width = 10, 15

    # Ask user for preferred speed
    print("\nChoose Animation Speed:")
    print("1. Slow")
    print("2. Medium")
    print("3. Fast")
    speed_choice = input("Enter 1, 2, or 3 [Default: 2]: ")
    speed_map = {"1": 0.3, "2": 0.12, "3": 0.04}
    speed_delay = speed_map.get(speed_choice, 0.12)

    print("\nChoose your pathfinding algorithm:")
    print("1. DFS (Depth-First Search)")
    print("2. BFS (Breadth-First Search)")
    print("3. A* (A-Star)")
    
    choice = input("Enter 1, 2, or 3 (default is DFS): ")
    algo_map = {"1": "dfs", "2": "bfs", "3": "astar"}
    selected_algo = algo_map.get(choice, "dfs")

    print(f"\nGenerating a {height}x{width} maze layout...")
    maze = Maze(height, width)
    maze.generate()

    solver = Solver(maze, algorithm=selected_algo)
    path, history = solver.solve(return_history=True)
    
    if history:
        animate_search_process(maze, history, speed_delay)
        print(f"\nTarget path secured using {selected_algo.upper()} in {len(path)} active steps.")
    else:
        print("\n--- GENERATED TERMINAL MAZE ---")
        print(maze.render())
        print("\nNo structural path resolved.")

if __name__ == "__main__":
    main()