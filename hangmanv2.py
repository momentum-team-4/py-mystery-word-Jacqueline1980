import random 
#from words import words
import string

# wordFile = open("words.txt", "r")
# words = wordFile.read()
# #print(words)

# word_list = words.split()
# wordFile.close()
# #print(word_list)

#word = random.choice(word_list)

def open_file(file):
    with open(file, "r") as p:
        all_words = p.read()
    words = all_words.split().uppercase()
    return random.choice(words)

  


def play_game():
    word = open_file(file)
    print(word)
    print(f'Your word is {len(word)} letters long.')

    # attempts = 0
    # guessed_letters = set()

    # if letter_guessed in secret_word:
    #     print("You've guessed a letter")
    #     guessed_letters.add(letter_guessed)
    
    # else:
    #     print("Try again")
    #     attempts += 1
  



    # print("Do you want to play again: yes or no")
    # return input().lower().startswith('y')


    if __name__ == "__main__":
        import argparse
        from pathlib import Path

        parser = argparse.ArgumentParser(
            description='Get the word frequency in a text file.')
        parser.add_argument('file', help='file to read')
        args = parser.parse_args()

        file = Path(args.file)
        if file.is_file():
            play_game()
        else:
            print(f"{file} does not exist!")
            exit(1)





# start = input("Press enter to play hangman?")

# print("Guess a letter")

# guesses = ''

# attempts = 8

# def game_play(word):

#     guesses = ''
#     attempts = 8

#     while attempts > 0:
#         failed = 0

#         for letter in word:
        
#             if letter in guesses:
#                 print(letter)
#             else: 
#                 print('_')

#                 failed += 1

#         if failed == 0 and attempts <= 8:
#             print ("You win the game")
#             print ("This word is", + word)
        
#         guess = input ("Please guess a letter:")
#         guesses += guess

#         if guess not in word:   
#             attempts -= 1
#             print("Incorrect guess")
#             print("You have", + attempts ,"guesses left.")
#             #print("The correct answer was: ", + word)

#             if attempts == 0:
#                 print("Game over, please try again")