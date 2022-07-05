import random
number = random.randint(1, 20)
name = input("Enter your name: ")
number_of_guess = 0
print(name + " I have selected a random num from 1 till 20, enter your guess: ")
while number_of_guess < 5:
    guess = int(input())
    number_of_guess += 1
    if guess > number:
        print("Your guess is too high")
    if guess < number:
        print("Your guess is too low")
    if guess == number:
        break
if guess == number:
    print("You guessed it rigth after " + str(number_of_guess))
else:
    print("You guessed it wrong, this was the correct answer: " + str(number))