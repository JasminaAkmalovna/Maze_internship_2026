from src.maze import Maze

def main():
    # Initialize a 15-row by 20-column layout matching your image ratio
    print("Generating your procedural labyrinth...")
    maze = Maze(15, 20)
    maze.generate()

    print("\n--- GENERATED TERMINAL MAZE ---")
    print(maze.render())

if __name__ == "__main__":
    main()