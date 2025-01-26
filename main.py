import random
import copy
from colorama import Fore, Style

valid_sols = []
valid_words = [] 

# read the files
with open("wordle-La.txt", "r") as file:
    for word in file:
        word = word.strip() # remove any whitespace
        valid_sols.append(word)
        valid_words.append(word)
   
with open("wordle-Ta.txt", "r") as file:
    for word in file:
        word = word.strip() # remove any whitespace
        valid_words.append(word)
        
# determine if valid 5-letter word
def not_valid_guess(word):
    if word not in valid_words or len(word) != 5:
        return True

# create letter frequency dict
def create_hash(solution):
    freq = {}
    for char in solution.lower():
        freq[char] = freq.get(char, 0) + 1 
    return freq


def letter_match(solution, guess, letter_freq):
    res = ""
    freq_copy = copy.deepcopy(letter_freq) # create a deep copy

    for i in range(len(guess)):
        
        if guess[i] == solution[i]:
            res += Fore.GREEN + guess[i] + Style.RESET_ALL
            freq_copy[guess[i]] -= 1
        elif guess[i] in solution and freq_copy[guess[i]] > 0:
            res += Fore.YELLOW + guess[i] + Style.RESET_ALL
            freq_copy[guess[i]] -= 1
        else:
            res += guess[i]
            
    return res


# main code
print("\nWelcome to Wordle! You have 6 guesses to guess the 5-letter word! Good luck!")

play_again = True

while play_again:
    solution = random.choice(valid_sols)
    solution = solution.lower()
    letter_freq = create_hash(solution)

    print("")
    finished = False
    num_guesses = 0

    while not finished and num_guesses < 6:
        guess = input("Please enter a guess: ")
        while not_valid_guess(guess):
            print("Invalid guess detected:", guess, "\n")
            guess = input("Please enter a valid guess (5 letters): ")

        if guess == solution:
            finished = True
            print(Fore.GREEN + solution + Style.RESET_ALL + "\n")
            print("Congrats! You have correctly guessed the word\n")
        else:
            res = letter_match(solution, guess, letter_freq)
            print("Guess " + str(num_guesses + 1) + "/6 :", res, "\n")
            
        num_guesses += 1

    if num_guesses == 6 and not finished:
        print("You have used up all your guesses. The word was: " + Fore.GREEN + solution + Style.RESET_ALL + "\n")

    choice = input("Would you like to play again? Please enter 'Y' for yes and 'N' for no:\n")
    while choice != "Y" and choice != "N":
        choice = input("Please enter 'Y' for yes and 'N' for no:\n")

    if choice == "Y":
        play_again = True
    elif choice == "N":
        play_again = False
        print("Thank you for playing!\n")
    
