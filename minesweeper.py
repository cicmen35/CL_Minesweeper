"""Module contains minesweeper logic."""
import random
from typing import List, Tuple
from collections import namedtuple
# Importing namedtuple from collections for easier work with the coordinates of the grid.
Coordinate = namedtuple("Coordinate", "row column")


class Cell:
    """Represents a single grid cell."""

    def __init__(self, has_mine: bool, surrounding_mines_count: int, is_open: bool = False) -> None:
        """Initialize a single cell of the grid.

        :param has_mine: bool, following cell contains a mine,
        :param surrounding_mines_count: int, number of surrounding mines around cell[row][col],
        :param is_open: bool, following cell which has been opened.
        """
        self.has_mine = has_mine
        self.surrounding_mines_count = surrounding_mines_count
        self.is_open = is_open

    def open(self):
        """Mark the cell as opened."""
        self.is_open = True

    def unopened_non_mine(self) -> bool:
        """Check if the cell is unopened and not a mine.

        :return: bool, True if the cell is unopened and not a mine, False otherwise.
        """
        return self.is_open is False and self.has_mine is False

    def __str__(self) -> str:
        """Return the string representation of the cell.

        :return: str, "0" if the cell is open and has no surrounding mines,
                      otherwise the count of surrounding mines if open,
                      or a space (" ") if unopened.
        """
        if self.is_open:
            return str(self.surrounding_mines_count) if self.surrounding_mines_count != 0 else "0"
        else:
            return " "


class Grid:
    """Represents the Minesweeper game grid."""

    def __init__(self, width: int, height: int, difficulty: int) -> None:
        """Initialize the grid with the given width, height, and difficulty level.

        :param width: int, the number of columns in the grid,
        :param height: int, the number of rows in the grid,
        :param difficulty: int, game difficulty level (1: easy, 2: medium, 3: hard),
        """
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.cells = self._create_empty_cells()
        total_cells = self.width * self.height
        if difficulty == 1:
            self.mine_count = max(1, int(total_cells * 0.10))
        elif difficulty == 2:
            self.mine_count = max(2, int(total_cells * 0.15))
        elif difficulty == 3:
            self.mine_count = max(3, int(total_cells * 0.20))

        self._set_cell_mines_and_surrounding_counts()
        self.hinted_cells = set()

    def has_unopened_non_mines(self) -> bool:
        """Check if there are any unopened non-mine cells left.

        :return: bool, True if there are unopened non-mine cells, False otherwise.
        """
        for row in self.cells:
            for cell in row:
                if cell.unopened_non_mine():
                    return True
        return False

    def _create_empty_cells(self) -> List[List[Cell]]:
        """Create an empty grid of cells.

        :return: List of lists containing Cell objects, all initialized without mines.
        """
        return [[Cell(has_mine=False, surrounding_mines_count=0) for _ in range(self.width)] for _ in range(self.height)]

    def _set_cell_mines_and_surrounding_counts(self) -> None:
        """Set the mines and calculate the surrounding mine counts for each cell."""
        coordinate_positions = self._generate_grid_coordinate_positions()
        mine_positions = self._generate_mine_positions(coordinate_positions)
        self._place_mines(mine_positions)
        non_mine_positions = self._identify_non_mine_positions(coordinate_positions, mine_positions)
        self._set_surrounding_mine_count(non_mine_positions)

    def _generate_grid_coordinate_positions(self) -> List[Tuple[int, int]]:
        """Generate a list of all possible coordinate positions on the grid.

        :return: List of tuples representing each cell's coordinates (row, column).
        """
        return [(row, col) for row in range(self.height) for col in range(self.width)]

    def _generate_mine_positions(self, coordinate_positions: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """Randomly select mine positions from the grid.

        :param: coordinate_positions: List of all possible coordinates on the grid,
        :return: List of tuples representing the mine positions (row, column).
        """
        return random.sample(coordinate_positions, self.mine_count)

    def _identify_non_mine_positions(self, coordinate_positions: List[Tuple[int, int]],
                                     mine_positions: List[Tuple[int, int]]) -> set:
        """Identify the coordinates that do not contain mines.

        :param: coordinate_positions: List of all possible coordinates on the grid,
        :param: mine_positions: List of coordinates containing mines,
        :return: Set of coordinates that are non-mine positions.
        """
        return set(coordinate_positions) - set(mine_positions)

    def _place_mines(self, mine_positions: List[Tuple[int, int]]) -> List[List[Cell]]:
        """Place mines in the corresponding cell objects.

        :param: mine_positions: List of coordinates where mines will be placed,
        :return: List of lists representing the grid after mines are placed.
        """
        for row_index, column_index in mine_positions:
            self.cells[row_index][column_index].has_mine = True
        return self.cells

    def _is_valid_position(self, row_index: int, column_index: int) -> bool:
        """Check if the given position is valid within the grid.

        :param: row_index: int, row index to check,
        :param: column_index: int, column index to check,
        :return: bool, True if the position is valid, False otherwise.
        """
        return 0 <= row_index < self.height and 0 <= column_index < self.width

    def _set_surrounding_mine_count(self, non_mine_positions: set[Tuple[int, int]]) -> None:
        """Set the surrounding mine count for each non-mine cell.

        :param: non_mine_positions: Set of coordinates that do not contain mines,
        """
        for empty_row_index, empty_column_index in non_mine_positions:
            count = 0
            for row_index in range(empty_row_index - 1, empty_row_index + 2):
                for column_index in range(empty_column_index - 1, empty_column_index + 2):
                    if self._is_valid_position(row_index, column_index) and self.cells[row_index][column_index].has_mine:
                        count += 1
            self.cells[empty_row_index][empty_column_index].surrounding_mines_count = count

    def print(self) -> None:
        """Print the current state of the grid."""
        for row in self.cells:
            visible_row = [str(cell) for cell in row]
            print(visible_row)

    def is_cell_open(self, row_index: int, column_index: int) -> bool:
        """Check if a specific cell is open.

        :param: row_index: int, row index of the cell,
        :param: column_index: int, column index of the cell,
        :return: bool, True if the cell is open, False otherwise.
        """
        return self.cells[row_index][column_index].is_open

    def has_mine(self, coordinate: Coordinate) -> bool:
        """Check if the given coordinate contains a mine.

        :param: coordinate: Coordinate, representing the row and column of the cell,
        :return: bool, True if the cell contains a mine, False otherwise.
        """
        return self.cells[coordinate.row][coordinate.column].has_mine

    def hint(self):
        """
        Provides a hint using recursive backtracking.
        The search starts from a random unopened cell and recursively explores neighbors.
        """
        # Iterate over the entire grid, pick any unopened, non-mine cell as the starting point
        for row in range(self.height):
            for col in range(self.width):
                if (row, col) not in self.hinted_cells and not self.cells[row][col].is_open \
                        and not self.cells[row][col].has_mine:
                    # Perform the recursive search starting from this cell
                    result = self._recursive_backtrack_search(row, col, set())
                    if result:
                        self.hinted_cells.add(result)
                        return result

        # If no hint is found
        return None

    def _recursive_backtrack_search(self, row, col, visited):
        """
        Helper method to recursively search for a safe unopened cell.
        """
        # Mark this cell as visited
        visited.add((row, col))

        # If the current cell is unopened and safe, return it as a hint
        if (row, col) not in self.hinted_cells and not self.cells[row][col].is_open \
                and not self.cells[row][col].has_mine:
            if self.cells[row][col].surrounding_mines_count == 0:
                return row, col  # Found a completely safe cell

        # Recursively search the neighbors
        for neighbour_row, neighbour_col in self.get_neighbours(row, col):
            if (neighbour_row, neighbour_col) not in visited:
                result = self._recursive_backtrack_search(neighbour_row, neighbour_col, visited)
                if result:
                    return result  # If a safe cell is found, return it

        # If no safe cells are found in this path, backtrack
        return None

    def get_neighbours(self, row, col):
        """
        Returns the list of valid neighbors around a given cell (row, col).
        It considers all 8 possible neighbors in a 2D grid.
        """
        neighbours = []
        for r in range(max(0, row - 1), min(self.height, row + 2)):
            for c in range(max(0, col - 1), min(self.width, col + 2)):
                if (r, c) != (row, col):  # Exclude the current cell itself
                    neighbours.append((r, c))
        return neighbours


class Minesweeper:
    """Main class for the Minesweeper game."""

    def __init__(self, width: int, height: int, difficulty: int) -> None:
        """Initialize the Minesweeper game with a grid.

        :param: width: int, width of the game grid,
        :param: height: int, height of the game grid,
        :param: difficulty: int, difficulty level of the game (1: easy, 2: medium, 3: hard),
        """
        self.grid = Grid(width, height, difficulty)

    def _get_valid_coordinate(self, plane: str, max_index: int) -> int:
        """Get a valid coordinate input from the user.

        :param: plane: str, indicating whether the input is for the row or column,
        :param: max_index: int, the maximum allowed value for the coordinate,
        :return: int, a valid coordinate within the grid,
        """
        prompt_str = f"Enter {plane} coordinate between 0 and {max_index}: "
        prompt = prompt_str.format(plane=plane, max_index=max_index)
        while True:
            try:
                coordinate = int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            else:
                if 0 <= coordinate <= max_index:
                    return coordinate
                else:
                    print(f"Invalid input. Please enter a number between 0 and {max_index}.")

    def _get_user_guess(self) -> Coordinate:
        """Get a valid cell guess (row, column) from the user.

        :return: Coordinate, the user-selected cell's coordinates,
        """
        while True:
            max_row_index = self.grid.width - 1
            max_col_index = self.grid.height - 1
            column_index = self._get_valid_coordinate(plane="column", max_index=max_row_index)
            row_index = self._get_valid_coordinate(plane="row", max_index=max_col_index)

            if self.grid.is_cell_open(row_index=row_index, column_index=column_index):
                print("Invalid input. The cell is already opened. Please choose another cell.")
            else:
                return Coordinate(row_index, column_index)

    def _has_guessed_mine(self, user_coordinate_guess: Coordinate) -> bool:
        """Check if the user has guessed a mine.

        :param: user_coordinate_guess: Coordinate, the guessed cell's coordinates,
        :return: bool, True if the guessed cell contains a mine, False otherwise.
        """
        if self.grid.has_mine(user_coordinate_guess):
            self.grid.cells[user_coordinate_guess.row][user_coordinate_guess.column] = 'X'
            self.grid.print()
            print("You guessed a mine.")
            return True
        else:
            return False

    def request_hint(self):
        """
        Provides the user with a hint by suggesting a safe cell to open.
        """
        hint = self.grid.hint()
        if hint:
            row, col = hint
            print(f"Hint: Try opening the cell at ({row}, {col})")
        else:
            print("No safe cells available for a hint!")

    def play(self) -> None:
        """Main method to start and run the Minesweeper game."""
        # Continue the game while there are unopened non-mine cells
        while self.grid.has_unopened_non_mines():
            action = input("Enter 'play' to make a move, or 'hint' to get a hint: ").strip().lower()
            if action == 'play':
                self.grid.print()
                user_coordinate_guess = self._get_user_guess()
                if self._has_guessed_mine(user_coordinate_guess):
                    print("Game Over:(")
                    break
                else:
                    # Open the guessed cell if it is a valid non-mine guess
                    self.grid.cells[user_coordinate_guess.row][user_coordinate_guess.column].open()
                    self.grid.print()
            elif action == 'hint':
                self.request_hint()
            else:
                print("Invalid option. Please choose 'play' or 'hint'.")
        else:
            self.grid.print()
            print("Congratulations, you won!")
