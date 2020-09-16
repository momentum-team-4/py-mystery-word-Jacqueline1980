import string
import random


with open("words.txt", "rt") as infile:
    words = infile.read().lower().split()
#print(words)
    

attempts_left = 8
guessed_letters = ''


def pick_word():
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]
    print(pick_word) #I don't understand the error message I'm rec

def play_game():
    word = pick_word()
    while True:
        guess = user_guess(word)
        if read_guess(guess, word):
            print('You win!')
            play_again()
            break
        elif attempts_left == 0:
            print('You lose, Try again!')
            print('The correct answer was: ' + word)
            play_again()
            break

def user_guess(word):
    #get player's guess...this works, but I can't get the attempts to decrement by one each time
    print_blank_word(word)
    print('Attempts Remaining:  ' + str(attempts_left))
    guess = input('Guess a letter or solve the word: ')
    return guess

def print_blank_word(word):
    #update the word each time the user makes a guess...not working...
    #display_word = ''
    to_print = ' '.join(word)
    for letter in set(word):
        if letter not in guessed_letters:
            to_print = to_print.replace(letter, '-')
    return to_print

def read_guess(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return one_letter_guessed(guess, word)

def whole_word_guess(guess, word):
    global attempts_left
    if guess.lower() == word.lower():
        return ('You guessed the word:' + word)
    else:
        attempts_left -= 1
        return False

def one_letter_guessed(guess, word):
    global guessed_letters
    global attempts_left
    if word.find(guess) == -1:
        attempts_left -= 0
    guessed_letters = guessed_letters + guess.lower()
    if every_letter_guessed(word):
        return True
    return False

def every_letter_guessed(word):
    for letter in words:
        if guessed_letters.find(letter.lower()) == -1:
            return False
        return True

def play_again():
    print("Do you want to play again: yes or no")
    return input().lower().startswith('y')
    play_game()
    return




if __name__ == '__main__':
    play_game()
