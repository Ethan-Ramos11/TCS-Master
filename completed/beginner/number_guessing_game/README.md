# Number Guessing Game

A simple Python number guessing game where the player tries to guess a randomly generated number between 1 and 100.

## Project Overview

This game demonstrates basic Python concepts including:

- Random number generation
- User input handling
- Control flow (loops and conditionals)
- Function design
- Error handling
- Unit testing

## Project Structure

```
number_guessing_game/
├── number_guessing_game.py  # Main game implementation
└── tests/
    └── test_number_guessing_game.py  # Test suite
```

## Features

- Random number generation between 1 and 100
- Input validation for user guesses
- Clear feedback on whether guesses are too high or too low
- Option to play multiple rounds
- Comprehensive test suite

## Getting Started

1. Clone the repository
2. Navigate to the project directory
3. Run the game:
   ```bash
   python number_guessing_game.py
   ```

## How to Play

1. The computer generates a random number between 1 and 100
2. Enter your guess when prompted
3. You'll receive feedback if your guess is:
   - Too high
   - Too low
   - Correct
4. After guessing correctly, you can choose to play again

## Running Tests

To run the test suite:

```bash
python -m unittest tests/test_number_guessing_game.py
```

The test suite covers:

- Random number generation
- Input validation
- Guess checking
- Game flow
- Error handling

## Implementation Details

### Core Functions

1. `generate_secret_number()`

   - Generates a random number between 1 and 100
   - Returns an integer

2. `get_user_guess()`

   - Gets and validates user input
   - Handles invalid inputs and out-of-range numbers
   - Returns a valid integer guess

3. `check_guess(guess, secret_number)`

   - Compares guess with secret number
   - Provides feedback
   - Returns True if correct, False otherwise

4. `main()`
   - Controls game flow
   - Handles multiple rounds
   - Manages game state

## Error Handling

The game handles various error cases:

- Non-numeric input
- Numbers outside the valid range (1-100)
- Invalid play again responses

## Future Improvements

Potential enhancements:

1. Add difficulty levels
2. Track number of attempts
3. Keep high scores
4. Add hints system
5. Implement a GUI version

## Contributing

Feel free to submit issues and enhancement requests!
