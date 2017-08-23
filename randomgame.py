import random
guess_count = 0
number = random.randint(1,50)
name = raw_input("wht is your name?")
print(name + " ,I am thinking a no. between 1 to 50 and hope u guess it..")

while guess_count < 5:
    guess=raw_input('guess a number=')
    guess=int(guess)

    guess_count = guess_count + 1
    guess_left = 5 - guess_count

    if guess > 50:
        guess_left = str(guess_left)
        print("Your guess is out of range! You have " + guess_left + " guesses left")

    elif guess < number:
        guess_left = str(guess_left)
        print("Your guess is too low! You have " + guess_left + " guesses left")

    elif guess > number:
        guess_left = str(guess_left)
        print("Your guess is too high! You have " + guess_left + " guesses left")

    elif guess == number:
        break

if guess==number:
    guess_count = str(guess_count)
    print("Good job! You guessed the number in " + guess_count + " tries :)")

if guess!=number:
    number = str(number)
    print("Sorry. The number I was thinking of was " + number + " :)")