import random 

computer_guess = random.randint(1,50)
user_guess = 0

while user_guess != computer_guess:
    user_guess = int(input("Guess a number between 1 and 50: "))

    if user_guess < computer_guess:
        print("Your guess is too low, try again!")

    elif user_guess > computer_guess:
        print("Your guess is too high, try again!")

print("Congratulations! You guessed the right number.")
print("Do you want to play more? ")
play_again = input("Enter 'yes' to play again or 'no' to quit: ")
if play_again == 'yes':
    computer_guess = random.randint(1,50)
    user_guess = 0
    while user_guess != computer_guess:
        user_guess = int(input("Guess a number between 1 and 50: "))
        if user_guess < computer_guess:
            print("Your guess is too low, try again!")
        elif user_guess > computer_guess:
            print("Your guess is too high, try again!")

print("Congratulations! You rock!  Again guessed the right number.")
