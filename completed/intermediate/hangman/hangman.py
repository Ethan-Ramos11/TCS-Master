import random

# Word categories for different difficulty levels
WORDS = {
    "easy": ["cat", "dog", "sun", "moon", "star", "fish", "bird", "tree"],
    "medium": ["coder", "javascript", "java", "rust", "golang", "python", "ruby", "swift"],
    "hard": ["algorithm", "database", "framework", "developer", "programming", "computer"]
}


def pick_word(difficulty="medium"):
    """
    Pick a random word from the specified difficulty level.

    Args:
        difficulty (str): Difficulty level ('easy', 'medium', 'hard')

    Returns:
        str: Random word from the selected difficulty
    """
    return random.choice(WORDS.get(difficulty, WORDS["medium"]))


def display_game(tries, word, prior_letters):
    """
    Display the current game state including hangman, word, and guessed letters.

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

    # Display hangman
    print(stages[tries])

    # Display word with spaces
    print("Word:", " ".join(word))

    # Display guessed letters
    if prior_letters:
        print("Guessed letters:", ", ".join(sorted(prior_letters)))
    else:
        print("Guessed letters: None")

    # Display remaining tries
    print(f"Tries remaining: {tries}")


def check_guess_letter(word, guess):
    """
    Check if a guessed letter is in the word.

    Args:
        word (str): The word to check
        guess (str): The guessed letter

    Returns:
        list: Positions where the letter appears
    """
    return [i for i, letter in enumerate(word) if letter == guess]


def check_guess_word(word, guess):
    """
    Check if the guessed word matches the target word.

    Args:
        word (str): The target word
        guess (str): The guessed word

    Returns:
        bool: True if guess matches word
    """
    return word == guess.lower()


def get_user_input(word, prior_letters):
    """
    Get and validate user input for guesses.

    Args:
        word (str): The word to guess
        prior_letters (list): Previously guessed letters

    Returns:
        tuple: (guess, is_word_guess)
    """
    while True:
        check_word = input(
            "Do you want to guess the whole word? (y/n): ").lower()
        if check_word not in {"y", "n"}:
            print("Invalid response, please enter y or n")
            continue

        guess = input("Enter your guess: ").lower()
        if check_word == "y":
            if len(guess) != len(word):
                print(f"Your guess must be {len(word)} letters long")
                continue
        else:
            if len(guess) != 1:
                print("Please enter a single letter")
                continue
            if guess in prior_letters:
                print("You already guessed this letter")
                continue

        return guess, check_word == "y"


def update_guess(working_word, guess, positions):
    """
    Update the working word with correctly guessed letters.

    Args:
        working_word (list): Current state of the word
        guess (str): The guessed letter
        positions (list): Positions where the letter appears

    Returns:
        list: Updated working word
    """
    for idx in positions:
        working_word[idx] = guess
    return working_word


def play():
    """
    Main game loop for Hangman.
    """
    # Get difficulty level
    while True:
        difficulty = input("Select difficulty (easy/medium/hard): ").lower()
        if difficulty in WORDS:
            break
        print("Invalid difficulty. Please choose easy, medium, or hard.")

    # Initialize game
    word = pick_word(difficulty)
    working_word = ["_"] * len(word)
    prior_letters = []
    tries = 6
    attempts = 0
    word_guessed = False

    print(f"\nWelcome to Hangman! Difficulty: {difficulty}")
    print(f"The word is {len(word)} letters long.")

    while tries > 0 and not word_guessed:
        attempts += 1
        print("\n" + "="*50)
        display_game(tries, working_word, prior_letters)

        guess, check_word = get_user_input(word, prior_letters)

        if check_word:
            if check_guess_word(word, guess):
                word_guessed = True
            else:
                tries -= 1
                print("Incorrect word guess!")
        else:
            positions = check_guess_letter(word, guess)
            if not positions:
                prior_letters.append(guess)
                tries -= 1
                print(f"Sorry, the letter '{guess}' is not in the word")
            else:
                working_word = update_guess(working_word, guess, positions)
                print(
                    f"Good guess! The letter '{guess}' appears {len(positions)} time(s)")
                if "".join(working_word) == word:
                    word_guessed = True

    # Game end
    print("\n" + "="*50)
    display_game(tries, word, prior_letters)

    if word_guessed:
        print(
            f"\nCongratulations! You guessed the word '{word}' in {attempts} attempts!")
    else:
        print(f"\nGame Over! The word was '{word}'")


if __name__ == "__main__":
    while True:
        play()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            break
    print("\nThanks for playing!")
