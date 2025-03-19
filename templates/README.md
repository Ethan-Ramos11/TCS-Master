# Tic Tac Toe Template

This is a template for building a command-line Tic Tac Toe game. Use this as a starting point for your project.

## Project Requirements

Create a Tic Tac Toe game that implements:

- Two-player gameplay
- Board display
- Move validation
- Win detection
- Game state management

### Basic Requirements

1. Create a 3x3 game board
2. Allow players to take turns placing their mark (X or O)
3. Validate moves to prevent:
   - Playing outside the board
   - Playing in an already filled position
4. Check for win conditions:
   - Three in a row horizontally
   - Three in a row vertically
   - Three in a row diagonally
5. Check for draw condition (board full)

### Advanced Requirements (Optional)

1. Add AI opponent
2. Implement GUI using tkinter
3. Add game statistics
4. Support for different board sizes
5. Network multiplayer

## Project Structure

```
tic-tac-toe/
├── README.md           # This file
├── tic_tac_toe.py      # Main game implementation
└── tests/
    └── test_tic_tac_toe.py  # Unit tests
```

## Getting Started

1. Copy this template to your work-in-progress directory
2. Implement the game logic in `tic_tac_toe.py`
3. Write tests in `test_tic_tac_toe.py`
4. Document your code and add comments
5. Test your implementation thoroughly

## Tips

- Start with the board representation
- Implement move validation early
- Write tests as you develop
- Keep your code clean and well-documented
- Test edge cases (invalid moves, full board, etc.)

## Example Usage

```python
# Example of how the game should work
game = TicTacToe()
game.make_move(0, 0, 'X')  # Place X in top-left corner
game.make_move(1, 1, 'O')  # Place O in center
game.display_board()       # Show current board state
```

## Submission

When you're done:

1. Ensure all tests pass
2. Update this README with your implementation details
3. Move the project to the completed directory
4. Create a pull request for review
