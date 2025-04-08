# Index Card System Template

This is a template for building an index card/flash card system. Use this as a starting point for your project.

## Project Requirements

Create an index card system that implements:

- Card creation and management
- Card set organization
- File I/O for persistence
- User-friendly interface

### Basic Requirements

1. Create an `Index_Card` class with:

   - Name and value attributes
   - Display functionality
   - Update methods
   - Proper comparison methods

2. Create an `Index_Card_Set` class with:

   - Set name attribute
   - Card management (add/remove)
   - Display functionality
   - File I/O operations

3. Implement main program with:
   - Card set creation/loading
   - User interface
   - Error handling

### Advanced Requirements (Optional)

1. Add card categories/tags
2. Implement card review mode
3. Add card statistics
4. Support multiple file formats
5. Add card set merging
6. Implement search functionality

## Project Structure

```
index_cards/
├── README.md           # This file
├── index_card.py       # Main implementation
└── tests/
    └── test_index_card.py  # Unit tests
```

## Getting Started

1. Copy this template to your work-in-progress directory
2. Implement the `Index_Card` class
3. Implement the `Index_Card_Set` class
4. Create the main program flow
5. Add error handling
6. Test your implementation

## Tips

- Start with the basic card structure
- Implement file I/O early
- Write tests as you develop
- Keep your code clean and well-documented
- Handle edge cases (empty sets, invalid input, etc.)

## Example Usage

```python
# Example of how the system should work
card_set = Index_Card_Set("My Cards")
card_set.add_card("Python", "A programming language")
card_set.display_cards()
card_set.upload_to_file("my_cards.json")
```

## Submission

When you're done:

1. Ensure all tests pass
2. Update this README with your implementation details
3. Move the project to the completed directory
4. Create a pull request for review
