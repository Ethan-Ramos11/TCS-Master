# Rock Paper Scissors Game

A simple command-line implementation of the classic Rock Paper Scissors game in Python.

## Features

- Two-player gameplay (player vs computer)
- Simple input system using single letters (r/p/s)
- Score tracking for wins, losses, and draws
- Clear game feedback and statistics
- Option to play multiple rounds
- Final game summary

## How to Play

1. Run the game:

   ```bash
   python3 rps.py
   ```

2. Enter your choice:

   - `r` for Rock
   - `p` for Paper
   - `s` for Scissors

3. The computer will make its choice and the winner will be determined:

   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock

4. After each round:

   - The current score will be displayed
   - You can choose to play again (y/n)

5. When you're done:
   - A final summary will show your total games and results
   - The game will exit

## Project Structure

```
rps/
├── rps.py           # Main game implementation
└── tests/
    └── test_rps.py  # Test suite
```

## Testing

Run the test suite:

```bash
python3 -m unittest tests/test_rps.py -v
```

The test suite covers:

- Valid and invalid player inputs
- Computer choice generation
- Winner determination
- Statistics tracking
- Display formatting

## Implementation Details

- Uses Python's built-in `random` module for computer choices
- Implements a simple state machine for game flow
- Maintains a dictionary for tracking game statistics
- Uses f-strings for formatted output

## Future Improvements

- Add support for full word inputs (rock/paper/scissors)
- Implement difficulty levels for computer opponent
- Add a graphical user interface
- Include player statistics persistence
- Add multiplayer support
