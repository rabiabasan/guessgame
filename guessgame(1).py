def binary_search(lower, high):
    print("Welcome to the Number Guessing Number Game! ")
    print("Choose of a number between 0 and 100, and I will try to guess it in 5 questions!")
    
    attempts = 0
    
    while lower <= high and attempts < 6:
        guess = (lower + high) // 2
        attempts += 1
        response = input(f"Is your number {guess}? (yes/higher/lower): ").strip().lower()
        
        if response == 'yes':
            print("Wooahh! I guessed it! ")
            return guess
        elif response == 'higher':
            lower = guess + 1
            print("Okay, I’ll aim higher! ")
        elif response == 'lower':
            high = guess - 1
            print("Got it! Lower it is!")
        else:
            print("Oops! I didn’t understand that. Let’s keep going! ")

    print("I’ve used all my brainpower! Maybe your number is just too tricky... ")
    return None

def number_guessing_game():
    binary_search(0, 100)

if __name__ == "__main__":
    number_guessing_game()


