
# 🏛️ Terminal Maze Generator & Solver

A fun terminal app that builds random mazes and visualizes how different pathfinding algorithms solve them in real-time with smooth animations.

---

## 🚀 What it Does

* **Random Mazes:** Creates perfect, loop-free mazes instantly.
* **Live Animations:** Shows the solver step-by-step as it explores paths and backs out of dead ends.
* **Multiple Algorithms:** Let you compare different search methods side-by-side.
* **Speed Controls:** Let you slow down or speed up the live terminal animation.

---

## 📂 Folder Structure

Your project is organized into clean, dedicated folders for the game logic and automated testing:

```text
maze-solver-project/
├── maps/                   # Folder for maze text files
│   ├── maze_braided.txt
│   ├── maze_gauntlet.txt
│   ├── maze_spiral.txt
│   └── maze.txt
├── src/                    # Core logic folder
│   ├── __pycache__/        # Compiled Python files (ignored by git)
│   ├── __init__.py
│   ├── cell.py             # Individual grid cells and walls
│   ├── loader.py           # Text maze loading/parsing logic
│   ├── maze.py             # Random maze builder
│   ├── solver.py           # Pathfinding algorithms
│   └── ui.py               # Terminal rendering and animations
├── tests/                  # Automated unit tests
│   ├── __pycache__/        # Compiled Python files (ignored by git)
│   ├── __init__.py
│   ├── manual_mazes.py     # Static mazes used for debugging
│   ├── test_cell.py        # Tests for cell properties
│   ├── test_loader.py      # Tests for the file loader logic
│   ├── test_maze.py        # Tests for maze walls and sizes
│   └── test_solver.py      # Tests to ensure paths are correct
├── .gitignore              # Files git should ignore
├── main.py                 # Main file to launch the app
├── maze_corridor.txt       # Sample custom corridor maze file (root level)
└── README.md               # App documentation
```

---

## 🛠️ How to Setup and Run

### Prerequisites

* Make sure you have Python 3/ Python installed.

### Run the App

1. Clone this repository to your computer:
```bash
git clone https://github.com/JasminaAkmalovna/Maze_internship_2026.git
cd Maze_internship_2026

```


2. Start the program:
```bash
python3 main.py 

```
or

```bash
 python main.py
```



### Run the Tests

To verify all algorithms, configurations, and boundaries are working perfectly, run this test suite command:

```bash
python3 -m unittest discover tests

```

---

## 🕹️ Menu Settings

When you run the app, it will ask you to customize your run:

1. **Size:** Type the rows and columns you want (or just press Enter for a default 10x15 maze).
2. **Speed:** Choose `1` (Slow), `2` (Medium), or `3` (Fast) for the animation speed.
3. **Algorithm:** Pick which pathfinder you want to watch.

---

## 📊 Algorithms & Colors

| Algorithm | Menu Choice | How it Thinks |
| --- | --- | --- |
| **Depth-First Search (DFS)** | `1` or `dfs` | Explores as deep as possible down a path. Optimized to guess paths toward the exit first. |
| **Breadth-First Search (BFS)** | `2` or `bfs` | Scans evenly in all directions. Always finds the absolute shortest path. |
| **A* Search** | `3` or `astar` | Smart search using a scoring system based on distance traveled and distance left to go. |

> 💡 **Color Guide:**
> * `•` **Green dots:** The active path the solver is building toward the exit.
> * `•` **Red dots:** Explored paths that turned into dead ends (backtracked areas).
> 
> 

---

## 📂 Loading Custom Mazes from Text Files

The application includes a robust file parsing module that allows you to load custom hand-crafted maze environments from text files rather than relying solely on procedural generation.

### 📑 File Formatting Rules
When creating custom `.txt` maps inside the root directory, adhere to the following character mapping matrix:

| Character | Description |
| :---: | :--- |
| `#` | **Wall Element:** Represents an impassable structural block. |
| `S` | **Start Point:** The absolute origin cell where solvers begin calculation. |
| `E` | **End Point:** The target destination cell. |
| ` ` | **Open Path (Space):** Clean path tiles where agents can navigate. |

#### Example Layout Map (`maze.txt`):
```text
###########
#S    #   #
##### # # #
#   #   # #
# ####### #
#       #E#
###########

```

### 🚀 Running a Custom Layout

1. Open the suite terminal interface: `python3 main.py` or `python main.py`
2. Select option `2` (`Load Maze from a Text File`).
3. Provide the targeted filename when prompted (e.g., `maze_spiral.txt`).
4. Select your preferred search algorithm execution pipeline and watch the custom canvas animate!

```

