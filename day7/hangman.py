import random
from hangmanwords import word_list
word = random.choice(word_list)
word_length = len(word)
end_of_game = False
lives = 6
from hangman_art import logo
print(logo)
d = []
for _ in range(word_length):
    d += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in d:
        print(f"You've already guessed {guess}")
    for pos in range(word_length):
        letter = word[pos]
        if letter == guess:
            d[pos] = letter
    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(d)}")
    if "_" not in d:
        end_of_game = True
        print("You win.")
    from hangman_art import stages
    print(stages[lives])