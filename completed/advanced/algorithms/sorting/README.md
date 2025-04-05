# Sorting Algorithms

This directory contains implementations of various sorting algorithms. Each implementation includes detailed documentation, complexity analysis, and example usage.

## Available Algorithms

- [Selection Sort](selection.py) - O(n²) time complexity, O(1) space complexity - INCOMPLETE
- [Bubble Sort](bubble.py) - O(n²) time complexity, O(1) space complexity
- [Insertion Sort](insertion_sort.py) - O(n²) time complexity, O(1) space complexity - INCOMPLETE
- [Merge Sort](merge_sort.py) - O(n log n) time complexity, O(n) space complexit - INCOMPLETEy
- [Quick Sort](quick_sort.py) - O(n log n) average time complexity, O(n²) worst case, O(log n) space complexity - INCOMPLETE

## Complexity Comparison

| Algorithm      | Best Case  | Average Case | Worst Case | Space Complexity | Stable |
| -------------- | ---------- | ------------ | ---------- | ---------------- | ------ |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)             | No     |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes    |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)             | Yes    |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)             | Yes    |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n)         | No     |

## Usage

Each sorting algorithm is implemented as a function that takes a list of numbers and returns the sorted list. Example:

```python
from selection import selection_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

## Implementation Details

Each sorting algorithm implementation includes:

- Clear function documentation
- Time and space complexity analysis
- Example usage
- Test cases

## Contributing

When adding new sorting algorithms:

1. Create a new Python file with the algorithm name
2. Include comprehensive documentation
3. Add test cases
4. Update this README with the new algorithm's details
5. Follow the existing code style and documentation standards
