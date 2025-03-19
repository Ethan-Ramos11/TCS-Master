# Tic Tac Toe

A command-line implementation of the classic Tic Tac Toe game.

## Features

- Two-player gameplay
- Board display
- Move validation
- Win detection
- Game state management

## Learning Objectives

This project helps students learn:

- 2D array/list manipulation
- Game logic implementation
- Input validation
- State management
- Object-oriented programming concepts

## Project Structure

```
tic-tac-toe/
├── README.md           # This file
├── tic_tac_toe.py      # Main game implementation
└── tests/
    └── test_tic_tac_toe.py  # Unit tests
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Usage

1. Run the game:

   ```bash
   python tic_tac_toe.py
   ```

2. Run the tests:
   ```bash
   python -m unittest tests/test_tic_tac_toe.py
   ```

## Game Rules

1. Players take turns placing their mark (X or O) on the board
2. First player to get 3 in a row (horizontally, vertically, or diagonally) wins
3. If all squares are filled and no player has won, the game is a draw

## Implementation Details

The game is implemented with the following key features:

- Board representation using a 2D list
- Move validation to prevent invalid moves
- Win condition checking
- Clear board display
- Turn management

## Testing

The project includes unit tests that verify:

- Board initialization
- Move validation
- Win condition detection
- Draw condition detection
- Invalid move handling

## Future Improvements

Possible enhancements:

1. Add AI opponent
2. Implement GUI using tkinter
3. Add game statistics
4. Support for different board sizes
5. Network multiplayer
