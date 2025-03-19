# Calculator Project Template

This is a template for building a basic calculator application. Use this as a starting point for your project.

## Project Requirements

Create a calculator that can perform the following operations:

- Addition
- Subtraction
- Multiplication
- Division

### Basic Requirements

1. Accept user input for two numbers
2. Allow user to choose an operation
3. Display the result
4. Handle basic error cases (division by zero)

### Advanced Requirements (Optional)

1. Add support for more operations (power, square root, etc.)
2. Implement a continuous calculation mode
3. Add input validation
4. Support decimal numbers

## Project Structure

```
calculator/
├── README.md
├── calculator.py
└── tests/
    └── test_calculator.py
```

## Getting Started

1. Copy this template to your work-in-progress directory
2. Implement the calculator functionality in `calculator.py`
3. Write tests in `test_calculator.py`
4. Document your code and add comments
5. Test your implementation thoroughly

## Tips

- Start with basic arithmetic operations
- Add error handling early
- Write tests as you develop
- Keep your code clean and well-documented

## Example Usage

```python
# Example of how the calculator should work
result = calculate(5, 3, '+')  # Should return 8
result = calculate(10, 2, '/')  # Should return 5
```

## Submission

When you're done:

1. Ensure all tests pass
2. Update this README with your implementation details
3. Move the project to the completed directory
4. Create a pull request for review
