import random


def generate_secret_number(length=4):
    """Generates a unique secret number that doesn't start with 0."""
    digits = list("0123456789")
    while True:
        random.shuffle(digits)
        secret = digits[:length]
        if secret[0] != '0':
            return "".join(secret)


def validate_input(user_input, length=4):
    """Validates the user input based on game rules."""
    if not user_input.isdigit():
        return False, "Your input must contain only digits."
    if len(user_input) != length:
        return False, f"Your input must have exactly {length} digits."
    if user_input.startswith('0'):
        return False, "The number must not start with zero."
    if len(set(user_input)) != len(user_input):
        return False, "The digits must be unique (no duplicates)."
    return True, ""


def evaluate_guess(secret, guess):
    """Calculates the number of bulls and cows."""
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


def get_plural(count, singular, plural):
    """Returns correct singular or plural form based on count."""
    return singular if count == 1 else plural


def play_game():
    """Main game loop and logic."""
    line = "-" * 50
    secret_number = generate_secret_number()
    guesses_count = 0

    print("Hi there!")
    print(line)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(line)

    while True:
        user_guess = input("Enter a number: ").strip()
        guesses_count += 1
        
        is_valid, error_msg = validate_input(user_guess)
        if not is_valid:
            print(f"Invalid input: {error_msg}")
            print(line)
            continue

        bulls, cows = evaluate_guess(secret_number, user_guess)

        if bulls == 4:
            print(f"Correct, you've guessed the right number\nin {guesses_count} guesses!")
            print(line)
            print("That's amazing!")
            break

        b_text = get_plural(bulls, "bull", "bulls")
        c_text = get_plural(cows, "cow", "cows")
        
        print(f"{bulls} {b_text}, {cows} {c_text}")
        print(line)


if __name__ == "__main__":
    play_game()
