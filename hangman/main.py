import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
user_lives = 6

print(logo)

display = []
for i in chosen_word:
    display += "_"
print(' '.join(display))

end_of_game = False

previous_choices = []

while not end_of_game:
    guess = (input("Guess a letter: ")).lower()
    if guess in previous_choices:
        print(f"You have already guessed '{guess}'!")
    else:
        previous_choices += guess
    if guess in chosen_word:
        for position in range(0, word_len):
            if guess == chosen_word[position]:
                display[position] = chosen_word[position]
    else:
        print(f"'{guess}' is not in the word")
        user_lives -= 1
        if user_lives == 0:
            print("You lose!")
            end_of_game = True
    print(' '.join(display))
    print(stages[user_lives])
    if "_" not in display:
        print("You win!")
        end_of_game = True