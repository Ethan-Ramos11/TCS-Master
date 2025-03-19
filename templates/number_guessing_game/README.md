# Number Guessing Game

A Python project template for implementing a number guessing game where the player tries to guess a randomly generated number.

## Project Overview

In this project, you'll create a number guessing game where:

1. The computer generates a random number between 1 and 100
2. The player tries to guess the number
3. The game provides feedback on whether the guess is too high or too low
4. The game continues until the player guesses correctly

## Project Structure

```
number_guessing_game/
├── number_guessing_game.py  # Main game implementation
└── tests/
    └── test_number_guessing_game.py  # Test suite
```

## Implementation Tasks

### Core Functions

1. `generate_secret_number()`

   - Generate a random number between 1 and 100
   - Return the number as an integer

2. `get_user_guess()`

   - Get input from the user
   - Validate the input is a number between 1 and 100
   - Return the validated guess as an integer

3. `check_guess(guess, secret_number)`

   - Compare the guess with the secret number
   - Provide feedback (too high, too low, correct)
   - Return True if guess is correct, False otherwise

4. `main()`
   - Display welcome message
   - Generate secret number
   - Handle game loop
   - Ask to play again

### Advanced Features (Optional)

1. Add difficulty levels:

   - Easy: 1-50
   - Medium: 1-100
   - Hard: 1-200

2. Add a scoring system:

   - Track number of attempts
   - Award points based on attempts
   - Keep high scores

3. Add hints:
   - Provide hints after certain number of attempts
   - Show if the number is even/odd
   - Show if the number is prime

## Testing

The project includes a test suite in `tests/test_number_guessing_game.py`. You should:

1. Implement the tests marked with TODO comments
2. Test edge cases and invalid inputs
3. Use mocking for user input and random number generation
4. Ensure all tests pass before submitting

## Learning Objectives

- Random number generation
- Input validation
- Control flow (loops and conditionals)
- Function design and implementation
- Unit testing with unittest
- Mocking in tests

## Development Steps

1. Review the function signatures and docstrings
2. Implement each function one at a time
3. Test your implementation using the test suite
4. Add error handling and input validation
5. Implement optional features if desired

## Resources

- [Python random module](https://docs.python.org/3/library/random.html)
- [Python unittest](https://docs.python.org/3/library/unittest.html)
- [Python input/output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python control flow](https://docs.python.org/3/tutorial/controlflow.html)
