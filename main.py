# main.py
import os
import time
from src.maze import Maze
from src.solver import Solver

def animate_search_process(maze, history):
    """
    Animates the full procedural search process frame-by-frame.
    Green = Current path being explored.
    Red   = Backtracked dead-ends/visited paths.
    """
    base_render = maze.render()
    
    # ANSI Escape codes for high-visibility terminal text formatting
    GREEN_DOT = "\033[92m•\033[0m"
    RED_DOT   = "\033[91m•\033[0m"

    for visited_coords, active_path in history:
        lines = base_render.split('\n')
        active_set = set(active_path)

        for line_idx in range(len(lines)):
            # Row index calculations matching terminal layout mapping
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

        # Draw frame
        os.system('clear' if os.name != 'nt' else 'cls')
        print("Welcome to the Procedural Labyrinth Generator!")
        print("---------------------------------------------")
        print(f"VISUALIZATION KEY: {GREEN_DOT} Active Path  {RED_DOT} Visited/Dead End")
        print("\n" + "\n".join(lines))
        
        # Frame delay speed adjustment (0.08 seconds per evaluation step)
        time.sleep(0.08)

def main():
    print("Welcome to the Procedural Labyrinth Generator!")
    print("---------------------------------------------")
    print("Choose your pathfinding algorithm:")
    print("1. DFS (Depth-First Search - deep backtracking visual)")
    print("2. BFS (Breadth-First Search - wide expanding wave visual)")
    print("3. A* (A-Star - intelligent target-seeking visual)")
    
    choice = input("Enter 1, 2, or 3 (default is DFS): ")
    algo_map = {"1": "dfs", "2": "bfs", "3": "astar"}
    selected_algo = algo_map.get(choice, "dfs")

    print(f"\nGenerating maze layout and initializing search matrix...")
    maze = Maze(10, 12)
    maze.generate()

    solver = Solver(maze, algorithm=selected_algo)
    # Requesting full tracking data matrix execution
    path, history = solver.solve(return_history=True)
    
    if history:
        animate_search_process(maze, history)
        print(f"\nTarget path secured using {selected_algo.upper()} in {len(path)} active steps.")
    else:
        print("\n--- GENERATED TERMINAL MAZE ---")
        print(maze.render())
        print("\nNo structural path resolved.")

if __name__ == "__main__":
    main()