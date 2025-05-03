import random


def pick_numbers():
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    return num_one, num_two


def pick_operation():
    OPERATIONS = ['+', '-', '*', '/']
    operation = random.choice(OPERATIONS)
    return operation


def valid_division(num_one, num_two):
    return num_one % num_two == 0


def create_question():
    operation = pick_operation()
    num_one, num_two = pick_numbers()

    if operation == '/':
        while not valid_division(num_one, num_two):
            num_one, num_two = pick_numbers()
    return [num_one, num_two, operation]


def display_question(question_info):
    question_string = f'{question_info[0]} {question_info[2]} {question_info[1]} = ?'
    return question_string


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def get_user_input(question):
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
    num_one, num_two, operation = question_info[0], question_info[1], question_info[2]
    if operation == "+":
        return num_one + num_two
    elif operation == "-":
        return num_one - num_two
    elif operation == "*":
        return num_one * num_two
    else:
        return num_one // num_two

