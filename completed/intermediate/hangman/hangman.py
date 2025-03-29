import random


def pick_word(words):
    """
    Select a random word from the provided list of words.

    Args:
        words (list): List of words to choose from

    Returns:
        str: A randomly selected word from the list
    """
    return random.choice(words)


def display_game(tries, word, prior_letters):
    """
    Display the current state of the hangman game.

    Args:
        tries (int): Number of remaining tries
        word (list): Current state of the word with revealed letters
        prior_letters (list): List of previously guessed letters
    """
    stages = [  # final state: head, torso, both arms and legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                 """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                 """,
                # head, torso and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                 """,
                # head, torso and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                 """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                 """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                 """,
                # initial empty state
                """
                   --------
                   |      |
                   |    
                   |      
                   |      
                   |     
                   -
                 """
    ]
    w = "Word: "
    prior = "Guessed letters: "
    for char in word:
        w += f"{char} "
    for char in prior_letters:
        prior += f"{char}, "
    if len(prior_letters) == 0:
        prior += "None"
    print(stages[tries])
    print(w)
    print(prior)


def check_guess_letter(word, guess):
    """
    Check if a guessed letter appears in the word and find its positions.

    Args:
        word (str): The word to check
        guess (str): The guessed letter

    Returns:
        list: List of positions where the letter appears in the word
    """
    positions = []
    for i in range(len(word)):
        if word[i] == guess:
            positions.append(i)
    return positions


def check_guess_word(word, guess):
    """
    Check if the guessed word matches the target word.

    Args:
        word (str): The target word
        guess (str): The guessed word

    Returns:
        bool: True if the guess matches the word (case-insensitive)
    """
    return word == guess.lower()


def get_user_input(word, prior_letters):
    """
    Get and validate user input for guesses.

    Args:
        word (str): The word to guess
        prior_letters (list): List of previously guessed letters

    Returns:
        tuple: (guess, is_word_guess) where guess is the user's input and is_word_guess is a boolean
    """
    while True:
        check_word = input(
            "Do you want to guess the whole word? (y/n) ").lower()
        if check_word not in {"y", "n"}:
            print("Invalid response, please enter y or n")
            continue
        guess = input("Enter your guess: ").lower()
        if check_word == "y":
            if len(guess) != len(word):
                print("The length of your guess is incorrect try again")
                continue
        else:
            if len(guess) != 1:
                print("Too many letters try again")
                continue
            if guess in prior_letters:
                print("You guessed this letter already")
                continue
        return guess, check_word == "y"


def update_guess(working_word, guess, positions):
    """
    Update the working word with correctly guessed letters.

    Args:
        working_word (list): Current state of the word
        guess (str): The guessed letter
        positions (list): List of positions where the letter appears

    Returns:
        list: Updated working word with revealed letters
    """
    for idx in positions:
        working_word[idx] = guess
    return working_word


def play():
    """
    Main game loop for the Hangman game.

    This function handles the complete game flow including:
    - Word selection
    - Game state management
    - User interaction
    - Win/lose conditions
    """
    words = ["coder", "javascript", "java", "rust", "golang"]

    word = pick_word(words)
    working_word = ["_"] * len(word)
    prior_letters = []
    print("Welcome to hangman. You will have 6 guesses to guess the right word")
    tries = 6  # Incorrect Guesses
    attempts = 0  # Total attempts correct or incorrect
    word_guessed = False
    while tries > 0 and not word_guessed:
        attempts += 1
        print("\n" + "="*50)
        display_game(tries, working_word, prior_letters)
        guess, check_word = get_user_input(word, prior_letters)
        if check_word:
            result = check_guess_word(word, guess)
            if result:
                word_guessed = True
            else:
                tries -= 1
        else:
            positions = check_guess_letter(word, guess)
            if not positions:
                prior_letters.append(guess)
                tries -= 1
            else:
                working_word = update_guess(working_word, guess, positions)
                if "".join(working_word) == word:
                    word_guessed = True
    print("\n" + "="*50)
    display_game(tries, word, prior_letters)
    if word_guessed:
        print(f"Good job you guessed the word {word} in {attempts} attempts")
    else:
        print(f"Better luck next time. The right word was {word}")


if __name__ == "__main__":
    play()
