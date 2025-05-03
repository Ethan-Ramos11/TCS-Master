from math_quiz import (
    pick_numbers,
    pick_operation,
    valid_division,
    create_question,
    display_question,
    check_answer,
    get_right_answer
)
import unittest
from unittest.mock import patch
import random
import sys
import os

# Add the parent directory to the path so we can import the math_quiz module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMathQuiz(unittest.TestCase):
    def test_pick_numbers(self):
        """Test that pick_numbers returns two numbers between 1 and 100"""
        for _ in range(100):  # Test multiple times due to randomness
            num_one, num_two = pick_numbers()
            self.assertGreaterEqual(num_one, 1)
            self.assertLessEqual(num_one, 100)
            self.assertGreaterEqual(num_two, 1)
            self.assertLessEqual(num_two, 100)

    def test_pick_operation(self):
        """Test that pick_operation returns a valid operation"""
        valid_operations = ['+', '-', '*', '/']
        for _ in range(100):  # Test multiple times due to randomness
            operation = pick_operation()
            self.assertIn(operation, valid_operations)

    def test_valid_division(self):
        """Test the valid_division function"""
        # Test valid division cases
        self.assertTrue(valid_division(10, 2))
        self.assertTrue(valid_division(100, 10))
        self.assertTrue(valid_division(1, 1))

        # Test invalid division cases
        self.assertFalse(valid_division(10, 3))
        self.assertFalse(valid_division(7, 2))
        self.assertFalse(valid_division(1, 2))

    def test_create_question(self):
        """Test that create_question returns valid question components"""
        for _ in range(100):  # Test multiple times due to randomness
            question = create_question()
            self.assertEqual(len(question), 3)
            num_one, num_two, operation = question

            # Check number ranges
            self.assertGreaterEqual(num_one, 1)
            self.assertLessEqual(num_one, 100)
            self.assertGreaterEqual(num_two, 1)
            self.assertLessEqual(num_two, 100)

            # Check operation validity
            self.assertIn(operation, ['+', '-', '*', '/'])

            # If operation is division, check if it's valid
            if operation == '/':
                self.assertTrue(valid_division(num_one, num_two))

    def test_display_question(self):
        """Test the display_question function"""
        test_cases = [
            ([5, 3, '+'], '5 + 3 = ?'),
            ([10, 2, '-'], '10 - 2 = ?'),
            ([4, 6, '*'], '4 * 6 = ?'),
            ([20, 5, '/'], '20 / 5 = ?')
        ]

        for question_info, expected in test_cases:
            self.assertEqual(display_question(question_info), expected)

    def test_check_answer(self):
        """Test the check_answer function"""
        self.assertTrue(check_answer(5, 5))
        self.assertTrue(check_answer(0, 0))
        self.assertTrue(check_answer(-5, -5))
        self.assertFalse(check_answer(5, 4))
        self.assertFalse(check_answer(0, 1))
        self.assertFalse(check_answer(-5, 5))

    def test_get_right_answer(self):
        """Test the get_right_answer function"""
        test_cases = [
            ([5, 3, '+'], 8),
            ([10, 2, '-'], 8),
            ([4, 6, '*'], 24),
            ([20, 5, '/'], 4)
        ]

        for question_info, expected in test_cases:
            self.assertEqual(get_right_answer(question_info), expected)


if __name__ == '__main__':
    unittest.main()
