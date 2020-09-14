import random 
#from words import words
import string

wordFile = open("words.txt", "r")
words = wordFile.read()
#print(words)

word_list = words.split()
wordFile.close()
#print(word_list)

word = random.choice(word_list)

start = input("Would you like to play hangman?")

print("Guess a letter")

guesses = ''

attempts = 8


while attempts > 0:
    failed = 0

    for letter in word:
        
        if letter in guesses:
            print(letter)
        else: 
            print('_')

            failed += 1

    if failed == 0 and attempts <= 8:
            print ("You win the game")
            print ("This word is ", word)
        
    guess = input ("Please guess a letter:")
    guesses += guess

    if guess not in word:   
        attempts -= 1
        print("Incorrect guess")
        print("You have", + attempts ,"guesses left.")
        #print("The correct answer was: ", + word)

        if attempts == 0:
            print("Game over, please try again")



