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
    if len(word) != len(guess):
        return False
    for i in range(len(guess)):
        if word[i] != guess[i]:
            return False
    return True


def get_user_input(word):
    guess_word = input("Do you want to guess the whole word? (y/n): ").lower()
    guess = input("Enter your guess: ")
    if guess_word == "y":
        return check_guess_letter(word, guess)
    else:
        return check_guess_letter(word, guess)
    
