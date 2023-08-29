import random
import hangman_graphics
import words

chosen_word = random.choice(words.countries)
end_of_game = False
lives = 6
compilation = set()

print(hangman_graphics.logo)
print("Guess the name of a country.")

display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    compilation.add(guess)

    if guess in display:
        print(f"You already guessed the letter {guess}. Try making another guess.")

    else:
        if guess not in chosen_word:
            lives -= 1
            print(f"The letter {guess} is not in the word. You now have {lives} lives remaining.")
            
        else:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
        
        print(" ".join(display))
        print(f"The letters you have guessed up to now are {compilation}.")
        print(hangman_graphics.stages[lives])

        if "_" not in display:
            end_of_game = True
            print("Congratulations! You have won the game.")
        
        if lives == 0:
            end_of_game = True
            print(f"You have lost the game. The answer was {chosen_word}.")