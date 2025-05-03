# Math Quiz

A simple command-line math quiz application that tests your basic arithmetic skills.

## Description

This Python program generates a series of 10 random math questions involving addition, subtraction, multiplication, and division. The questions are designed to be challenging yet solvable, with division problems ensuring whole number answers.

## Features

- Generates random math problems with numbers between 1 and 100
- Supports four basic operations: addition (+), subtraction (-), multiplication (\*), and division (/)
- Ensures division problems result in whole numbers
- Tracks and displays your score at the end
- Handles invalid input gracefully

## Requirements

- Python 3.x

## Usage

1. Run the program:

   ```bash
   python math_quiz.py
   ```

2. You will be presented with 10 random math questions
3. Enter your answer for each question
4. The program will tell you if your answer is correct or incorrect
5. At the end, you'll see your total score out of 10

## Example

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

## Error Handling

- The program will prompt you to enter a valid number if you provide:
  - Empty input
  - Non-numeric input
  - Decimal numbers (only whole numbers are accepted)
