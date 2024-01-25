import random
import time

def generate_sequence(length, difficulty):

    if difficulty == 'easy':
        return [str(random.randint(1, 4)) for _ in range(length)]
    elif difficulty == 'medium':
        return [chr(random.randint(65, 68)) for _ in range(length)]
    elif difficulty == 'hard':
        return [chr(random.randint(97, 100)) for _ in range(length)]
    else:
        raise ValueError("Please choose a right difficulty level and correct spelling")

def display_sequence(sequence):

    print(" ".join(sequence))
    time.sleep(5)
    print('\n' * 100)


def get_player_guess(length):

    while True:
        guess = input(f"What was the correct order of the {length} items? Enter your guess separated by spaces: ").split()
        if len(guess) == length:
            return guess
        else:
            print(f"Please enter {length} items.")

def main():

    length = 4
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    original_sequence = generate_sequence(length, difficulty)
    display_sequence(original_sequence)

    while True:
        shuffled_sequence = original_sequence.copy()
        random.shuffle(shuffled_sequence)
        print("The sequence is now shuffled:", " ".join(shuffled_sequence))

        player_guess = get_player_guess(length)

        if player_guess == original_sequence:
            print("Congratulations! You guessed the correct sequence.")
            break
        else:
            print("Incorrect guess. Try again.")

main()
