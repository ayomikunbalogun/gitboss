import random
import sys

words = []
with open ("words.txt") as file:
    text = file.read()

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5:  (" o ",
                    "/|\\",
                    "/  "),
                6:  (" o ",
                    "/|\\",
                    "/ \\")}


words = [w.strip() for w in text.split(",") if w.strip()]

easy = [w for w in words if len(w)<=5]
intermediate =[w for w in words if 5 < len(w) <=8]
hard = [w for w in words if len(w) > 8]

levels = {
     "easy": easy,
     "medium": intermediate,
     "hard": hard,
}

def main():
     
     try: 
          
        word = choose_level()
        hint = ["_"] * len(word)
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True
        
        
        while is_running:
            hangman_image(wrong_guesses)
            display_hint(hint)
            
            guess = input("\nEnter a letter to guess: ").lower().strip()
            

            if len(guess) != 1 or not guess.isalpha():
                print("\nInvalid input")
                continue
            if guess in guessed_letters:
                print(f"\n{guess} has already been guessed")
                continue
            
            guessed_letters.add(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        hint[i] = guess
            else:
                print("\n")
                wrong_guesses += 1

            if "_" not in hint:
                hangman_image(wrong_guesses)
                display_answer(word)
                print("\n\nYOU WIN!")
                is_running = False

            if wrong_guesses >= len(hangman_art)-1:
                is_running = False
                print("\nYOU LOSE! ")
                print(f"\nthe correct answer was {word.upper()}\n")
                is_running = False
     except EOFError:
         sys.exit()

def choose_level():
    while True:
            level = input("Choose level (Easy, Medium, Hard): " ).strip().lower()

            if level in levels:
                #choose word based on the level
                word = random.choice(levels[level])
                break
            else:
                print("Please choose a valid level")
    return word

def hangman_image(wrong_guesses):
        print("**************") 
        for line in hangman_art[wrong_guesses]:
            print(line)
        print("**************")      

def display_hint(hint):
    print("")
    print("")        
    print(" ".join(hint))

def display_answer(word):
     print(" ".join(word))

if __name__ == "__main__":
    main()
    
