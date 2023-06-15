import random
import time
# starting initials
print("\n Welcome to hangman game")
name = input("\n Enter your name: ")
time.sleep(2)
print("\n Best of luck for the game " + name)
time.sleep(3)
# the main program
def main():
    global count
    global display
    global word
    global length
    global already_guessed
    global play_game
    words_to_guess = ["january", "march", "doll", "promise"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""
# loop for restarting the game if the first round ends.
def play_again():
    play_game = input("do you want to continue the game y = yes or n = no\n")
    while play_game not in ("Y", "y", "N", "n"):
        play_game = input("Do you want to continue the game y = yes or n = no\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing")
        exit()
def hangman():
    global count
    global play_game
    global word
    global display
    global already_guessed
    limit = 5
    guess = input("This is your word " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input, try again: \n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1
    if count == 1:
        time.sleep(1)
        print("  ___  \n"
            "   |     | \n"
            "   |       \n"
            "   |       \n"
            "   |       \n"
            "  _|_     \n")
        print("you guessed wrong, " + str(limit - count) + " try left")
    elif count == 2:
        time.sleep(1)
        print("  ___  \n"
            "   |     | \n"
            "   |     O \n"
            "   |       \n"
            "   |       \n"
            "  _|_     \n")
        print("you guessed wrong, " + str(limit - count) + " try left")
    elif count == 3:
        time.sleep(1)
        print("  ___  \n"
            "   |     | \n"
            "   |     O \n"
            "   |     |  \n"
            "   |       \n"
            "  _|_     \n")
        print("you guessed wrong, " + str(limit - count) + " try left")
    elif count == 4:
        time.sleep(1)
        print("  ___  \n"
            "   |     | \n"
            "   |     O \n"
            "   |    /|\ \n"
            "   |       \n"
            "  _|_     \n")
        print("you guessed wrong, " + str(limit - count) + " try left")
    elif count == 5:
        time.sleep(1)
        print("  ___  \n"
            "   |     | \n"
            "   |     O \n"
            "   |    /|\ \n"
            "   |    / \ \n"
            "  _|_     \n")
        print("You are hanged!!!\n")
        print("This was the word:\n" + already_guessed,word)
        play_again()
    if word == "_" * length:
        print("Congrates you have guessed correctly.")
        play_again()
    elif count != limit:
        hangman()
main()
hangman()
