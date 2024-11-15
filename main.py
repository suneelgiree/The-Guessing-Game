import random

# Generate a random number between 1 and 99
n = random.randint(1, 99)
guessNumber = -1
count = 0

# Check if the user has entered a valid number
while( guessNumber != n ):
    count += 1
    guessNumber = int(input("Guess the number : "))
    if guessNumber < n:
        print("Too low")
    elif guessNumber > n:
        print("Too high")
    else:
        print("Congratulations! You guessed the number in", count, "attempts.")
