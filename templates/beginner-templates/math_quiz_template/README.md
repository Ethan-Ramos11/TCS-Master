# Math Quiz Template

A template for creating a command-line math quiz application that tests basic arithmetic skills.

## Learning Objectives

By completing this project, you will learn:

- How to work with random numbers in Python
- How to handle user input and validation
- How to implement basic arithmetic operations
- How to structure a program with multiple functions
- How to handle edge cases (like division by zero)
- How to create a simple game loop

## Project Structure

The project consists of several functions that work together to create a math quiz:

1. `pick_numbers()`: Generates random numbers
2. `pick_operation()`: Selects a random operation
3. `valid_division()`: Ensures division problems have whole number answers
4. `create_question()`: Creates a valid math question
5. `display_question()`: Formats the question for display
6. `check_answer()`: Compares user's answer with correct answer
7. `get_user_input()`: Handles user input and validation
8. `get_right_answer()`: Calculates the correct answer
9. `main()`: Implements the game loop

## Requirements

- Python 3.x
- Basic understanding of Python functions and control flow
- Familiarity with arithmetic operations

## Getting Started

1. Clone or download this template
2. Open `math_quiz.py` in your favorite code editor
3. Implement each function following the docstrings and TODO comments
4. Test your implementation by running the program

## Implementation Tips

1. Start with the basic functions first (`pick_numbers`, `pick_operation`)
2. Test each function as you implement it
3. Pay special attention to the division validation
4. Make sure to handle invalid user input gracefully
5. Test edge cases (like division by zero)

## Example Output

```
Welcome to the Math Quiz!
You will be asked 10 math questions to solve

Question 1:
What is 45 + 67 = ? 112
Correct!

Question 2:
What is 89 - 34 = ? 55
Correct!

...

Quiz complete! Your score: 8/10
```

## Testing

The project includes a test suite to verify your implementation. Run the tests using:

```bash
python -m unittest discover tests
```

## Next Steps

After completing the basic implementation, consider adding these features:

- Difficulty levels
- Time limit for each question
- High score tracking
- Different types of math problems
- Customizable number of questions
