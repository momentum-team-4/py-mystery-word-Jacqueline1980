import random 
#from words import words
import string

wordFile = open("words.txt", "r")
words = wordFile.read()
#print(words)

word_list = words.split()
wordFile.close()
#print(word_list)

def get_valid_word(words):
    word = random.choice(words) #choose a random word from the list
    while '-' in words or ' ' in words:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in this word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #user guesses will go in here

    attempts = 8

    #get the users input
    while len(word_letters) > 0 and attempts > 0:
        #letters used
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input("Choose a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                attempts = attempts - 1
                print('Incorrect letter, try again')

        elif user_letter in used_letters:
            print("You have guessed that letter, please guess again.")

        else: 
            print("Incorrect character. Please try again.")


    if attempts == 0:
        print('No more attempts left. The correct answer was', word)
    else:
        print('You guessed correctly!')






































#print (word_list)

# guessed = []
# wrong = []

# tries = 8

# while tries > 0:

#     out = ""
#     for letter in word:
#         if letter in guessed:
#             out = out + letter
#         else:
#             out = out + "_"

#     if out == word:
#         break

#     print("Guess the word:", out)
#     print(tries, "chances left")

#     guess = input()

#     if guess in guessed or guess in wrong:
#         print("Already guessed", guess)
#     elif guess in word:
#         print("Yay")
#         guessed.append(guess)
#     else:
#         print("Nope")
#         tries = tries - 1
#         wrong.append(guess)

#     print()

# if tries:
#     print("You guessed", word)
# else:
#     print("You didn't get", word)
# #         pass

# for letter in words_list:

#     out = out + '_'

# print("Guess a letter in the word:", out)

# guess = input()
# #what did the end user type

# if guess in word:
#     print("You found a letter")
# else:
#     print("Pick another letter")








