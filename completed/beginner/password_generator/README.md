# Password Generator

A Python program that generates secure, customizable passwords based on user requirements.

## Features

- Generate passwords of custom length
- Include/exclude different character types:
  - Uppercase letters
  - Numbers
  - Special characters
- Input validation
- Minimum length requirements
- Guaranteed inclusion of selected character types

## Usage

1. Run the program:

   ```bash
   python password.py
   ```

2. Follow the prompts to:
   - Choose which character types to include
   - Specify password length
   - Generate additional passwords if desired

## Requirements

- Python 3
- No external dependencies required

## Example

```
Welcome to the Password Generator!
This program will help you create secure passwords.
--------------------------------------------------

Password Requirements:
Do you need to include uppercase letters? (y/n) y
Do you need to include numbers? (y/n) y
Do you need to include special characters? (y/n) y

How many characters should the password have? 12

Generated Password: aB3$kL9#mN2@
--------------------------------------------------

Generate another password? (y/n): n

Thank you for using the Password Generator!
```

## Implementation Details

The program consists of several key functions:

- `get_input()`: Handles user input for character type selection
- `enough_chars()`: Validates password length requirements
- `generate_password()`: Creates the password based on requirements
- `main()`: Orchestrates the program flow

## Security Notes

- The program uses Python's `random` module for password generation
- Passwords are generated with at least one of each selected character type
- Minimum length requirements ensure password strength

## Contributing

Feel free to submit issues and enhancement requests!
