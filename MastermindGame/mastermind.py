import random

COLOURS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        colour = random.choice(COLOURS)
        code.append(colour)

    return code


def guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colours.")
            continue
        
        for color in guess:
            if color not in COLOURS:
                print(f"Invalid colour: {color}. Try again.")
                break
        else:
            break

    return guess

def check_code(guess, code):
    colour_counts = {}
    correct_positions = 0
    incorrect_positions = 0

    for colour in code:
        if colour not in colour_counts:
            colour_counts[colour] = 0
        colour_counts[colour]+=1
    
    for guess_colour, code_colour in zip(guess, code):
        if guess_colour == code_colour:
            correct_positions +=1
            colour_counts[guess_colour] -=1
    
    for guess_colour, code_colour in zip(guess, code):
        if guess_colour in colour_counts and colour_counts[guess_colour] > 0:
            incorrect_positions +=1
            colour_counts[guess_colour] -=1

    return correct_positions, incorrect_positions


def main():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code...")
    print("The valid colours are", *COLOURS)
    print("Write space after each code letter")
    code = generate_code()
    for attempts in range(1, TRIES+1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        
        print(f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")
    else:
        print("You ran out of tries, the code was: ", *code)

if __name__ == "__main__":
    main()