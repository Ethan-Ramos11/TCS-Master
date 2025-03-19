# Tic Tac Toe Game

A Python implementation of the classic Tic Tac Toe game with a command-line interface.

## Features

- Two-player gameplay
- Move validation (1-9 grid positions)
- Win detection (horizontal, vertical, diagonal)
- Tie game detection
- Game statistics tracking
- Option to play multiple games
- Clean exit with 'q' command
- Comprehensive test suite

## Project Structure

```
tic-tac-toe/
├── __init__.py
├── tic_tac_toe.py      # Main game implementation
└── tests/
    ├── __init__.py
    └── test_tic_tac_toe.py  # Unit tests
```

## Requirements

- Python 3.x

## Usage

1. Run the game:

```bash
python3 tic_tac_toe.py
```

2. Make moves by entering numbers 1-9:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

3. Game Controls:
   - Enter numbers 1-9 to make a move
   - Enter 'q' to quit the game
   - Enter 'y' to play again after a game ends

## Testing

Run the test suite:

```bash
python3 -m unittest tests/test_tic_tac_toe.py
```

Test coverage includes:

- Initial board state
- Valid and invalid moves
- Win conditions (horizontal, vertical, diagonal)
- Board full condition
- No winner condition
- Board reset functionality

## Implementation Details

- Board representation: List of 9 elements
- Player marks: 'X' and 'O'
- Move validation: Checks for range (1-9) and occupied positions
- Win detection: Checks all possible winning combinations
- Statistics tracking: Keeps count of wins and ties

## Future Improvements

- Add AI opponent
- Implement GUI
- Add difficulty levels
- Save game statistics to file
- Add multiplayer support
