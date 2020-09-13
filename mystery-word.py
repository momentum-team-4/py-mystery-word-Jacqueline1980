def display_game(attempts):
    mystery_game_pics = ["""
  + - - - +
          |
          |
          |
          |
        ===== """, """
   + - - - +
   O       |
           |
           |
           |
         ===== """, """
   + - - - +
   O       |
   |       |
           |
           |
         ===== """, """
   + - - - +
   O       |
   |       |
   |       |
           |
         ===== """, """
   + - - - +
   O       |
   |       |
   |       |
   |       |
         ===== """, """ 
   + - - - +
    O       |
   /|       |
    |       |
    |       |
         ===== """, """ 
   + - - - +
    O       |
   /|\\     |
    |       |
    |       |
          ===== """, """    
   + - - - +
   O       |
  /|\\     |
   |       |
   |       |
  /        |
         ===== """, """   
   + - - - +
   O       |
  /|\\     |
   |       |
   |       |
  / \\     |
         ===== """]
    
    return mystery_game_pics[attempts]


fileObject = open("words.txt", "r")
words = fileObject.read()
#print(words)

import random

word_choices = []


word_choices = words.upper()
random.choice(word_choices)
print(word_choices)













# def play(word):
#     word_complete = "_" * len(words)
#     guessed = False
#     guessed_letters = []
#     guessed_words = []
#     attempts = 8
#     print("Ready to Play?")
#     print(display_game(attempts))
#     print(word_complete)


#     while not guessed and attempts > 0:
#         guess = input("Guess a letter or solve the mystery word: ").upper()
#     print(guess) 
#     if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print("You have guessed this letter already", guess)
#             elif len(guess) > 1:
#                 print("You may only guess one letter, try again")
#             elif guess not in word:
#                 print("Incorrect choice, try again")
#                 attempts -= 1 
#                 guessed_letters.append(guess)
#                 print(attempts + "remain")
#             else: 
#                 print("You have guessed the word!")
#                 guessed_letters.append(guess)
#                 word_list = list(word_complete)
#                 indices = [i for i, letter in enumerate(word) if letter == guess]
#                 for index in indices:
#                     word_list[index] = guess
#                 word_complete = ''.join(word_list)
#                 if '_' not in word_complete:
#                     guessed = True

#     elif len(guess) == len(word_choices) and guess.isalpha():
#         if guessed in guessed_words:
#             print ("You have guessed this word already")
#         elif guess != word:
#             print(guess, "is incorrect")
#             attempts -= 1
#             guessed_words.append(guess)

    
#     else: 
#     print("Invalid guess")
#     print(display_game(attempts))
#     print(word_complete)

















# # def displayBoard():
# #     print(mystery_game_pics[len(missedLetters)])
# #     print()

# #     print('Missed Letters:', end=' ')
# #     for letter in missedLetters:
# #         print(letter,end=' ')
# #     print()

# #     blanks = '_' * len(secretWord)

# #     for i in range (len(secretWord)):
# #         if secretWord[i] in correctLetters:
# #             blanks= blanks[:1] + secretWord[i] + blanks[i+1:]

# #     for letter in blanks:
# #         print(letter, end=' ')
# #     print()

# # def getGuess(alreadyGuessed):
# #     while True:
# #         print('Guess a letter:')
# #         guess = input()
# #         guess = guess.upper
# #         if len(guess) != 1:
# #             print('Enter only one letter, please!')
# #         elif guess in alreadyGuessed:
# #             print('You have guessed this letter previously, guess again.')
# #         elif guess != guess.isalpha():
# #             print('Please guess only letters.')
# #         else:
# #             return guess

# # missedLetters = ''
# # correctLetters = ''
# # secretWord = word_choices
# # gameIsDone = False

# # while True:
# #     displayBoard(missedLetters, correctLetters, secretWord)

# #     guess = getGuess(missedLetters + correctLetters)

# #     if guess in secretWord:
# #         correctLetters = correctLetters + guess

# #         wordCorrect = True
# #         for i in range(len(secretWord)):
# #             if secretWord[i] not in correctLetters:
# #                 wordCorrect = False
# #             if wordCorrect:
# #                 print("Congratulations, you guessed the word!")
# #                 gameIsDone = True

# #     else:
# #         missedLetters = missedLetters + guess
        
# #         if len(missedLetters) == len(mystery_game_pics)  -  1:
# #             displayBoard(missedLetters, correctLetters, secretWord)
# #             print('You have zero guesses left.  The word was ' + secretWord + '.')
# #             gameIsDone = True

# # def playAgain():
# #     print('Would you like to play again? (yes or no)')
# #     return input().upper().startswith('y')

# #     if gameIsDone:
# #         if playAgain():
# #             missedLetters = ''
# #             correctLetters = ''
# #             gameIsDone = False
# #             secretWord = getRandomWords(words)

# #     else:


