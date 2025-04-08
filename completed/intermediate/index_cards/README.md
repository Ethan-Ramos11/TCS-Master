# Index Card System

A Python-based flash card system that allows users to create, manage, and study sets of index cards.

## Features

- Create and manage multiple card sets
- Add, remove, and update cards
- Display cards in a formatted way
- Save and load card sets to/from JSON files
- Interactive command-line interface

## Usage

1. Run the program:

```bash
python index_card.py
```

2. Choose from the following options:

   - Create a new card set
   - Load an existing card set
   - Exit the program

3. For each card set, you can:
   - Add new cards
   - Remove existing cards
   - Display all cards
   - Save the set to a file
   - Return to the main menu

## Card Set Management

- Each card has a name (front) and value (back)
- Cards are displayed in a formatted box
- You can flip cards to view their contents
- Card sets can be saved as JSON files for later use

## File Format

Card sets are saved in JSON format with the following structure:

```json
{
  "set_name": "Your Set Name",
  "cards": [
    {
      "name": "Card Front",
      "value": "Card Back"
    }
  ]
}
```

## Requirements

- Python 3.x
- No external dependencies required

## Testing

Run the test suite:

```bash
python test_index_card.py
```
