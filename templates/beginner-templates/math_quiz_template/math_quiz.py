import random


def get_num_range(difficulty):
    """Get the number range based on difficulty level.

    Args:
        difficulty (str): The difficulty level ('easy', 'medium', or 'hard')

    Returns:
        tuple: A tuple containing (lower_bound, upper_bound) for the number range
    """
    # TODO: Return appropriate number ranges based on difficulty
    # Easy: 0-20
    # Medium: 0-50
    # Hard: 0-1000
    pass


def pick_numbers(lower_num, upper_num):
    """Generate two random numbers between the specified range.

    Args:
        lower_num (int): The lower bound for random numbers
        upper_num (int): The upper bound for random numbers

    Returns:
        tuple: A tuple containing two random integers between lower_num and upper_num
    """
    # TODO: Generate and return two random numbers between lower_num and upper_num
    pass


def pick_operation():
    """Randomly select one of the four basic arithmetic operations.

    Returns:
        str: One of the following operations: '+', '-', '*', '/'
    """
    # TODO: Randomly select and return one of the four operations
    pass


def valid_division(num_one, num_two):
    """Check if division of two numbers results in a whole number.

    Args:
        num_one (int): The dividend
        num_two (int): The divisor

    Returns:
        bool: True if num_one is divisible by num_two, False otherwise
    """
    # TODO: Check if num_one is divisible by num_two
    pass


def create_question():
    """Generate a valid math question with random numbers and operation.

    For division questions, ensures the result will be a whole number.

    Returns:
        list: A list containing [num_one, num_two, operation]
    """
    # TODO: Generate a valid question with random numbers and operation
    # For division, ensure the result is a whole number
    pass


def display_question(question_info):
    """Format the question information into a readable string.

    Args:
        question_info (list): A list containing [num_one, num_two, operation]

    Returns:
        str: A formatted question string (e.g., "5 + 3 = ?")
    """
    # TODO: Format the question into a readable string
    pass


def check_answer(user_answer, correct_answer):
    """Compare the user's answer with the correct answer.

    Args:
        user_answer (int): The answer provided by the user
        correct_answer (int): The correct answer to the question

    Returns:
        bool: True if the answers match, False otherwise
    """
    # TODO: Compare the user's answer with the correct answer
    pass


def get_user_input(question):
    """Prompt the user for input and validate it as an integer.

    Args:
        question (str): The question to display to the user

    Returns:
        int: The validated integer input from the user

    Note:
        This function will continue to prompt the user until a valid integer is provided.
    """
    # TODO: Get and validate user input
    pass


def get_right_answer(question_info):
    """Calculate the correct answer for a given question.

    Args:
        question_info (list): A list containing [num_one, num_two, operation]

    Returns:
        int: The correct answer to the question
    """
    # TODO: Calculate the correct answer based on the operation
    pass


def main():
    """Run the math quiz game.

    The game will:
    1. Ask for difficulty level
    2. Present 10 random math questions
    3. Accept and validate user input
    4. Check answers and keep score
    5. Display the final score
    """
    # TODO: Implement the main game loop
    # 1. Ask user to choose difficulty (easy, medium, hard)
    # 2. Get the number range based on difficulty
    # 3. Generate and present questions using the appropriate number range
    # 4. Keep track of score
    # 5. Display final score
    pass


if __name__ == "__main__":
    main()
