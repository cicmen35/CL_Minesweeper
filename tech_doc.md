# **Technical Documentation**

## **Class Descriptions**

### **1. `Cell` Class**
Represents a single cell in the game grid.

**Main Methods**:
- `__init__(self, has_mine: bool, surrounding_mines_count: int, is_open: bool = False) -> None`: Initializes the cell.
- `open(self)`: Marks the cell as opened.
- `unopened_non_mine(self) -> bool`: Checks if the cell is unopened and not a mine.
- `__str__(self) -> str`: Returns the string representation of the cell.

### **2. `Grid` Class**
Represents the game grid and contains the core game logic.

**Main Methods**:
- `__init__(self, width: int, height: int, difficulty: int) -> None`: Initializes the grid with dimensions and difficulty from the user.
- `has_unopened_non_mines(self) -> bool`: Checks if there are any unopened non-mine cells.
- `print(self) -> None`: Prints the current state of the game grid in the terminal.
- `is_cell_open(self, row_index: int, column_index: int) -> bool`: Checks if a given cell is open.
- `has_mine(self, coordinate: Coordinate) -> bool`: Checks if the given coordinate contains a mine.
- `hint(self)`: Provides a hint to the user.
- `_create_empty_cells(self) -> List[List[Cell]]`: Creates an empty grid of cells.
- `_set_cell_mines_and_surrounding_counts(self) -> None`: Sets mines and calculates surrounding mine counts.
- `_generate_grid_coordinate_positions(self) -> List[Tuple[int, int]]`: Generates coordinates for the entire grid.
- `_generate_mine_positions(self, coordinate_positions: List[Tuple[int, int]]) -> List[Tuple[int, int]]`: Randomly selects positions for mines.
- `_identify_non_mine_positions(self, coordinate_positions: List[Tuple[int, int]], mine_positions: List[Tuple[int, int]]) -> set`: Identifies coordinates without mines.
- `_place_mines(self, mine_positions: List[Tuple[int, int]]) -> List[List[Cell]]`: Places mines in the grid.
- `_is_valid_position(self, row_index: int, column_index: int) -> bool`: Determines if a position is within the grid boundaries.
- `_set_surrounding_mine_count(self, non_mine_positions: set[Tuple[int, int]]) -> None`: Sets the number of surrounding mines for cells without mines.
- `_recursive_backtrack_search(self, row, col, visited)`: Recursive helper method for the hint functionality.

### **3. `Minesweeper` Class**
Main class for organizing the game flow.

**Main Methods**:
- `__init__(self, width: int, height: int, difficulty: int) -> None`: Initializes the complete game.
- `_get_valid_coordinate(self, plane: str, max_index: int) -> int`: Gets appropriate input from the user.
- `_get_user_guess(self) -> Coordinate`: Gets a valid guess from the user.
- `_has_guessed_mine(self, user_coordinate_guess: Coordinate) -> bool`: Checks if the user entered coordinates with a mine.
- `request_hint(self)`: Provides a hint to the user.
- `play(self) -> None`: Main game loop.

### **Algorithms**
- **Mine Placement**: Randomly selects mine positions based on the specified difficulty.
- **Hint Generation**: Uses recursive backtracking to find a safe cell.
