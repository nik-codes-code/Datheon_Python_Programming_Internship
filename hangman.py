import random

# ASCII stages for wrong guesses (0 to 6 mistakes)
HANGMAN_PICS = [
    """
      +---+
          |
          |
          |
         ==='
    """,
    """
      +---+
      O   |
          |
          |
         ==='
    """,
    """
      +---+
      O   |
      |   |
          |
         ==='
    """,
    """
      +---+
      O   |
     /|   |
          |
         ==='
    """,
    """
      +---+
      O   |
     /|\\  |
          |
         ==='
    """,
    """
      +---+
      O   |
     /|\\  |
     /    |
         ==='
    """,
    """
      +---+
      O   |
     /|\\  |
     / \\  |
         ==='
    """
]

# Word bank derived from standard English vocabulary
WORD_LIST = [
    "python", "developer", "internship", "automation", "programming", 
    "console", "terminal", "algorithm", "dataset", "repository"
]

def play_hangman():
    word = random.choice(WORD_LIST)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("=" * 40)
    print("      WELCOME TO HANGMAN (CONSOLE)      ")
    print("=" * 40)
    
    while incorrect_guesses < max_attempts:
        print(HANGMAN_PICS[incorrect_guesses])
        
        # Display current masked word progress (e.g., '_ A _ H E O N')
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"Word: {display_word}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Mistakes remaining: {max_attempts - incorrect_guesses}\n")
        
        # Check win condition
        if "_" not in display_word:
            print("=" * 40)
            print(f"🎉 CONGRATULATIONS! You guessed the word: {word}")
            print("=" * 40)
            break

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input. Please enter a single alphabetical letter.\n")
            continue

        # Prevent duplicate penalty deduction
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.add(guess)

        # Check correctness
        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Incorrect! '{guess}' is not in the word.\n")

    else:
        # Loss condition screen
        print(HANGMAN_PICS[6])
        print("=" * 40)
        print("💀 GAME OVER! You ran out of attempts.")
        print(f"The secret word was: {word}")
        print("=" * 40)

if __name__ == "__main__":
    play_hangman()