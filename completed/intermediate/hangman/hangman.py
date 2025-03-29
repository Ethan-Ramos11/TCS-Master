import random
words = ["coder", "javascript", "java", "rust", "golang"]


def pick_word(words):
    return random.choice(words)


def display_hangman(tries):
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
    print(stages[tries])


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
        return guess, check_word
