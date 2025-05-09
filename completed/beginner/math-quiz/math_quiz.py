import random


def get_num_range(difficulty):
    if difficulty == 'easy':
        return 0, 20
    elif difficulty == 'medium':
        return 0, 50
    elif difficulty == 'hard':
        return 0, 1000
    else:
        return -1


def pick_numbers():
    """Generate two random numbers between 1 and 100.

    Returns:
        tuple: A tuple containing two random integers between 1 and 100.
    """
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    return num_one, num_two


def pick_operation():
    """Randomly select one of the four basic arithmetic operations.

    Returns:
        str: One of the following operations: '+', '-', '*', '/'
    """
    OPERATIONS = ['+', '-', '*', '/']
    operation = random.choice(OPERATIONS)
    return operation


def valid_division(num_one, num_two):
    """Check if division of two numbers results in a whole number.

    Args:
        num_one (int): The dividend
        num_two (int): The divisor

    Returns:
        bool: True if num_one is divisible by num_two, False otherwise
    """
    return num_one % num_two == 0


def create_question():
    """Generate a valid math question with random numbers and operation.

    For division questions, ensures the result will be a whole number.

    Returns:
        list: A list containing [num_one, num_two, operation]
    """
    operation = pick_operation()
    num_one, num_two = pick_numbers()

    if operation == '/':
        while not valid_division(num_one, num_two):
            num_one, num_two = pick_numbers()
    return [num_one, num_two, operation]


def display_question(question_info):
    """Format the question information into a readable string.

    Args:
        question_info (list): A list containing [num_one, num_two, operation]

    Returns:
        str: A formatted question string (e.g., "5 + 3 = ?")
    """
    question_string = f'{question_info[0]} {question_info[2]} {question_info[1]} = ?'
    return question_string


def check_answer(user_answer, correct_answer):
    """Compare the user's answer with the correct answer.

    Args:
        user_answer (int): The answer provided by the user
        correct_answer (int): The correct answer to the question

    Returns:
        bool: True if the answers match, False otherwise
    """
    return user_answer == correct_answer


def get_user_input(question):
    """Prompt the user for input and validate it as an integer.

    Args:
        question (str): The question to display to the user

    Returns:
        int: The validated integer input from the user

    Note:
        This function will continue to prompt the user until a valid integer is provided.
    """
    while True:
        try:
            user_input = input(f'What is {question} ')
            if not user_input.strip():
                print("Please enter a number")
                continue
            num = int(user_input)
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer")


def get_right_answer(question_info):
    """Calculate the correct answer for a given question.

    Args:
        question_info (list): A list containing [num_one, num_two, operation]

    Returns:
        int: The correct answer to the question
    """
    num_one, num_two, operation = question_info[0], question_info[1], question_info[2]
    if operation == "+":
        return num_one + num_two
    elif operation == "-":
        return num_one - num_two
    elif operation == "*":
        return num_one * num_two
    else:
        return num_one // num_two


def main():
    """Run the math quiz game.

    The game will:
    1. Present 10 random math questions
    2. Accept and validate user input
    3. Check answers and keep score
    4. Display the final score
    """
    print("Welcome to the Math Quiz!")
    print("You will be asked 10 math questions to solve")
    score = 0
    for i in range(10):
        print(f"\nQuestion {i + 1}:")
        question_info = create_question()
        question = display_question(question_info)
        correct_answer = get_right_answer(question_info)

        user_answer = get_user_input(question)

        if check_answer(user_answer, correct_answer):
            print("Correct!")
            score += 1
        else:
            print(f'Incorrect, the correct answer was {correct_answer}')

    print(f'\nQuiz complete! Your score: {score}/10')


if __name__ == "__main__":
    main()
