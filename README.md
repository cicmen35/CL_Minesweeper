# Command Line Minesweeper

A text-based implementation of the classic Minesweeper game in terminal.

## Overview

This project is a Python implementation of the classic Minesweeper game with a command-line interface.

## Features

- Customizable grid dimensions
- Three difficulty levels (Easy, Medium, Hard)
- Hint system to help find safe cells
- Text-based interface for terminal play

## How to Play

1. Run the game using `python play.py`
2. Enter the desired width and height for the grid (minimum 2x2)
3. Choose a difficulty level:
   - Easy (1): 10% of cells contain mines
   - Medium (2): 15% of cells contain mines
   - Hard (3): 20% of cells contain mines
4. When prompted, enter:
   - `play` to make a move, then enter row and column coordinates
   - `hint` to receive a suggestion for a safe cell

## Game Representation

- ` ` (space): Unopened cell
- `0`: Opened cell with no surrounding mines
- Numbers (`1`, `2`, etc.): Opened cell with that many mines in adjacent cells

## Project Structure

- `minesweeper.py`: Core game logic with Cell, Grid, and Minesweeper classes
- `play.py`: Entry point for the game with user interface
- `tech_doc.md`: Technical documentation of classes and methods
- `user_doc.md`: User guide with gameplay instructions
