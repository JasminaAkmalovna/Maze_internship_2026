# main.py
import os
import time
from src.maze import Maze
from src.solver import Solver

def animate_path(maze, path):
    """
    Takes the standard maze render string and progressively injects 
    a path marker '•' step-by-step to create a live animation.
    """
    base_render = maze.render()
    current_path = []
    
    for coordinate in path:
        current_path.append(coordinate)
        lines = base_render.split('\n')
        
        # Inject the path markers for all coordinates visited so far
        for r, c in current_path:
            # Mathematical mapping to your terminal maze grid characters
            line_idx = 2 * r + 1
            char_idx = 2 + 4 * c
            
            if line_idx < len(lines) and char_idx < len(lines[line_idx]):
                line_list = list(lines[line_idx])
                line_list[char_idx] = '•'  # Drawing our path tracking dot
                lines[line_idx] = "".join(line_list)
        
        # Clear the terminal screen completely before drawing the next frame
        os.system('clear' if os.name != 'nt' else 'cls')
        
        print("Welcome to the Procedural Labyrinth Generator!")
        print("---------------------------------------------")
        print("\n--- ANIMATING PATHFINDING ROUTE ---")
        print("\n".join(lines))
        
        # Speed of the animation (0.15 seconds per step)
        time.sleep(0.15)

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

    # Let's upscale to a slightly larger maze (10x10) to make the animation look cooler!
    print(f"\nGenerating a 10x10 maze and solving...")
    maze = Maze(10, 10)
    maze.generate()

    solver = Solver(maze, algorithm=selected_algo)
    path = solver.solve()
    
    if path:
        # Launch the live visual tracker animation loop
        animate_path(maze, path)
        print(f"\nSuccess! Destination reached using {selected_algo.upper()} in {len(path)} steps.")
    else:
        print("\n--- GENERATED TERMINAL MAZE ---")
        print(maze.render())
        print("\nNo valid path found.")

if __name__ == "__main__":
    main()