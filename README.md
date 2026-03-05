# Conway's Game of Life

A minimalist, from-scratch implementation of Conway's Game of Life. 

This project was built entirely using pure Python logic for the cellular automaton engine and Tkinter for the graphical user interface. It avoids external game development libraries to provide a foundational look into algorithm design and graphical rendering in standard Python.

## Features

- **Pure Python Logic**: The core simulation is implemented without third-party mathematical or matrix libraries.
- **Tkinter GUI**: An interactive, lightweight graphical interface built using Python's standard `tkinter` library.
- **Interactive Grid**: Click to toggle the state of individual cells to create custom initial configurations.
- **Simulation Controls**: Start, stop, reset, or step through the simulation round-by-round.
- **Adjustable Speed**: Real-time slider to control the execution speed of the simulation.
- **Command-Line Interface**: An optional CLI mode to initialize grids and stream the simulation directly inside the terminal.

## How to Run

### Requirements
- Python 3.x (Tkinter is included in standard Python distributions)

### Running the GUI
To start the graphical version of the Game of Life:

```bash
python tk_window.py
```

### Running the CLI
To run the command-line interface version of the simulation:

```bash
python game_of_life.py
```
Follow the interactive prompts in the terminal to configure the board size, round delay, round count, and the initial active cells.

## Architecture

- `game_of_life.py`: Contains the `Grid` data structure and the standalone `GameOfLife` engine that calculates state transitions based on Conway's rules. Also provides the terminal application logic.
- `tk_window.py`: Contains the `Window` class, integrating the engine with a Tkinter canvas to render cell states and handle mouse/button event callbacks.

## AI Usage

The code in this project was authored entirely by a human developer in **2023**. It was written from scratch without the involvement of any GenAI coding assistants or automated generation tools, reflecting an authentic exercise in algorithmic problem-solving and standard library UI integration.
