# **User Documentation**

## **Introduction**
This version of 'Minesweeper' is a text-based version of the game. The goal is to clear the field by opening all cells that do not contain mines, without triggering any hidden mines. You can also request a hint that will help you find safe cells.

## **Game Settings**
1. **Board Dimensions**:
   - The user enters the dimensions of the playing field (width and height). The board must be at least 2x2.
   
2. **Difficulty**:
   - After determining the board dimensions, the user selects a difficulty level:
     - **Easy (1)**: 10% of the board will contain mines.
     - **Medium (2)**: 15% of the board will contain mines.
     - **Hard (3)**: 20% of the board will contain mines.

## **Gameplay**
1. **Game Objective**:
   - Open all cells that don't have mines.
   - The game ends when a cell with a mine is opened.

2. **Board Representation**:
   - The board is displayed with cells represented as follows:
     - `" "`: Unopened cell.
     - `"0"`: Opened cell with no surrounding mines.
     - Number (`"1"`, `"2"`, etc.): Indicates the number of mines surrounding the opened cell.

3. **Steps**:
   - **Play**: The user enters a guess, based on which a cell is revealed.
   - **Hint**: The game provides a hint with coordinates that definitely do not contain mines.
   - When the user selects the `play` option, they choose a cell by entering its coordinates.

## **Hints**
- You can request a hint by typing `hint` when prompted. The game will guide you to a safe cell.
