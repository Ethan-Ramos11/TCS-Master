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


def check_answer(user_answer, correct_answer):
    pass


def get_user_input(question):
    pass
