# src/ui.py
import os
import time

def generate_smooth_frames(history):
    """
    Calculates step-by-step backtracking frames between solver states
    so the cursor physically walks backward out of dead ends.
    """
    smooth_history = []
    all_visited = set()
    current_path = []

    for _, active_path in history:
        common_len = 0
        for i in range(min(len(current_path), len(active_path))):
            if current_path[i] == active_path[i]:
                common_len += 1
            else:
                break
        
        while len(current_path) > common_len:
            popped = current_path.pop()
            all_visited.add(popped)
            smooth_history.append((set(all_visited), list(current_path)))
        
        for i in range(common_len, len(active_path)):
            current_path.append(active_path[i])
            all_visited.add(active_path[i])
            smooth_history.append((set(all_visited), list(current_path)))
            
    return smooth_history

def animate_search_process(maze, smooth_history, speed_delay, speed_name):
    """
    Renders the maze search animation along with a real-time live stats dashboard.
    """
    base_render = maze.render()
    GREEN_DOT = "\033[92m•\033[0m"
    RED_DOT   = "\033[91m•\033[0m"

    dead_ends_hit = 0
    was_backtracking = False
    prev_path_len = 0

    for visited_coords, active_path in smooth_history:
        lines = base_render.split('\n')
        active_set = set(active_path)
        current_path_len = len(active_path)

        if current_path_len < prev_path_len:
            if not was_backtracking:
                dead_ends_hit += 1
                was_backtracking = True
        else:
            was_backtracking = False
        prev_path_len = current_path_len

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

        cells_explored = len(visited_coords)
        efficiency = (current_path_len / cells_explored * 100) if cells_explored > 0 else 0.0

        os.system('clear' if os.name != 'nt' else 'cls')
        print("Welcome to the Procedural Labyrinth Generator!")
        print("---------------------------------------------")
        print(f"VISUALIZATION KEY: {GREEN_DOT} Active Path  {RED_DOT} Visited/Dead End")
        print("\n" + "\n".join(lines))
        
        print("\n┌────────────────────────────────────────────────────────┐")
        print("│                LIVE SEARCH ENGINE STATS                │")
        print("├────────────────────────────────────────────────────────┤")
        print(f"│  Cells Explored:  {cells_explored:<6} │  Active Path Length: {current_path_len:<5} │")
        print(f"│  Dead Ends Hit:   {dead_ends_hit:<6} │  Refresh Setting:    {speed_name:<5} │")
        print(f"│  Current Search Efficiency Rating: {efficiency:>5.1f}%             │")
        print("└────────────────────────────────────────────────────────┘")
        
        time.sleep(speed_delay)