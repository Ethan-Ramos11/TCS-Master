# Rock Paper Scissors Game Template

A template for implementing a command-line Rock Paper Scissors game in Python.

## Project Requirements

### Basic Requirements

- Two-player gameplay (player vs computer)
- Input validation for player choices
- Computer opponent that makes random choices
- Score tracking for wins, losses, and draws
- Clear game feedback and statistics
- Option to play multiple rounds

### Advanced Requirements (Optional)

- Support for full word inputs (rock/paper/scissors)
- Difficulty levels for computer opponent
- Player statistics persistence
- Graphical user interface
- Multiplayer support

## Project Structure

```
rps/
├── rps.py           # Main game implementation
└── tests/
    └── test_rps.py  # Test suite
```

## Getting Started

1. Review the function stubs in `rps.py`
2. Implement each function according to its docstring
3. Run the test suite to verify your implementation
4. Test the game manually to ensure proper functionality

## Tips for Development

1. Start with the core game logic:

   - Implement `get_player_choice()`
   - Implement `get_computer_choice()`
   - Implement `determine_winner()`

2. Add game state management:

   - Implement `update_stats()`
   - Implement `display_stats()`

3. Finally, implement the main game loop in `main()`

## Example Usage

```python
# Example game flow
player_choice = get_player_choice()  # Returns 'r', 'p', or 's'
computer_choice = get_computer_choice()  # Returns 'r', 'p', or 's'
result = determine_winner(player_choice, computer_choice)  # Returns 'player', 'computer', or 'tie'
update_stats(stats, result)  # Updates the game statistics
display_stats(stats)  # Shows current game statistics
```

## Testing

The test suite in `test_rps.py` provides comprehensive test cases for:

- Input validation
- Computer choice generation
- Winner determination
- Statistics tracking
- Display formatting

Run the tests:

```bash
python3 -m unittest tests/test_rps.py -v
```

## Submission Guidelines

1. Ensure all tests pass
2. Follow PEP 8 style guidelines
3. Include docstrings for all functions
4. Handle edge cases and invalid inputs
5. Provide clear user feedback
6. Include a README with setup and usage instructions

## Resources

- [Python Random Module Documentation](https://docs.python.org/3/library/random.html)
- [Python Input/Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python Testing with unittest](https://docs.python.org/3/library/unittest.html)
