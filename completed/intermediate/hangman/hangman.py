import random


def pick_word(words):
    return random.choice(words)


def display_game(tries, word, prior_letters):
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
    positions = []
    for i in range(len(word)):
        if word[i] == guess:
            positions.append(i)
    return positions


def check_guess_word(word, guess):
    return word == guess.lower()


def get_user_input(word, prior_letters):
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
    for idx in positions:
        working_word[idx] = guess
    return working_word


def play():
    words = ["coder", "javascript", "java", "rust", "golang"]

    word = pick_word(words)
    working_word = ["_"] * len(word)
    prior_letters = []
    print("Welcome to hangman. You will have 6 guesses to guess the right word")
    tries = 6
    word_guessed = False
    while tries > 0 and not word_guessed:
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
