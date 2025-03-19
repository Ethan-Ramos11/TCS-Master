# Calculator Project

A simple command-line calculator that demonstrates basic arithmetic operations and error handling in Python.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Input validation
- Error handling for division by zero
- Clean, user-friendly interface
- Comprehensive test suite

## Learning Objectives

This project helps students learn:

- Basic Python syntax
- Function definitions and calls
- User input handling
- Error handling with try/except
- Unit testing
- Code documentation

## Project Structure

```
calculator/
├── README.md           # This file
├── calculator.py       # Main calculator implementation
└── tests/
    └── test_calculator.py  # Unit tests
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Usage

1. Run the calculator:

   ```bash
   python calculator.py
   ```

2. Follow the prompts to:

   - Enter the first number
   - Choose an operation (+, -, \*, /)
   - Enter the second number
   - View the result

3. Run the tests:
   ```bash
   python -m unittest tests/test_calculator.py
   ```

## Example Output

```
Welcome to the Calculator!
Enter first number: 10
Choose operation (+, -, *, /): +
Enter second number: 5
Result: 15
```

## Implementation Details

The calculator is implemented with the following key features:

- Input validation to ensure numbers are valid
- Error handling for division by zero
- Clear separation of concerns between calculation and user interface
- Comprehensive test coverage
- Detailed code documentation

## Testing

The project includes unit tests that verify:

- All basic arithmetic operations
- Error handling for invalid inputs
- Edge cases (zero, negative numbers)
- Invalid operations

## Future Improvements

Possible enhancements for students to implement:

1. Support for more operations (power, square root)
2. Memory functions (store, recall)
3. Support for decimal numbers
4. History of calculations
5. GUI interface using tkinter
