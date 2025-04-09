# Password Generator Template

This template provides a starting point for creating a password generator in Python. The template includes the basic structure and documentation, with placeholders for implementing the core functionality.

## Features to Implement

1. `enough_chars(num_chars, modifiers)`: Check if the password length is sufficient for the selected character types
2. `get_input(modifier)`: Get and validate user input for character type inclusion
3. `generate_password(num_char, modifiers)`: Generate a random password based on requirements

## How to Use

1. Copy the template files to your project directory
2. Implement the TODO sections in each function
3. Test your implementation by running the program

## Implementation Hints

### enough_chars()

- Count how many character types are required (uppercase, numbers, special characters)
- Ensure the password length is at least the number of required types + 1

### get_input()

- Use a while loop to keep asking for input until valid
- Only accept 'y' or 'n' as valid inputs
- Convert input to lowercase for case-insensitive comparison

### generate_password()

1. Start with a list containing at least one lowercase character
2. Add required character types based on modifiers
3. Fill the remaining length with random characters from allowed sets
4. Shuffle the final password

## Testing

The template includes a test file (`test_password.py`) with placeholders for implementing unit tests. The tests are designed to verify:

1. `test_enough_chars()`: Validates password length requirements

   - Test different combinations of password lengths and character types
   - Verify both valid and invalid cases

2. `test_generate_password()`: Ensures password generation works correctly

   - Verify password length
   - Check for required character types
   - Ensure lowercase letters are always included

3. `test_get_input()`: Tests user input handling
   - Test valid and invalid inputs
   - Verify case sensitivity
   - Check input validation

To run the tests:

```bash
python -m unittest test_password.py -v
```

### Writing Tests

1. Start by implementing the test cases in `test_enough_chars()`
2. Move on to `test_generate_password()` once the length validation works
3. Finally, implement `test_get_input()` to test user input handling

Each test function includes TODO comments with hints and example test cases to help you get started.

## Example Usage

```python
# After implementation, the program should work like this:
Welcome to the Password Generator!
This program will help you create secure passwords.
--------------------------------------------------

Password Requirements:
Do you need to include uppercase letters? (y/n) y
Do you need to include numbers? (y/n) y
Do you need to include special characters? (y/n) n

How many characters should the password have? 12

Generated Password: aB3cD9eF2gH1
--------------------------------------------------
```

## Next Steps

After completing the basic implementation, consider adding:

1. Password strength evaluation
2. Save generated passwords to a file
3. Copy password to clipboard functionality
4. Predefined password templates
