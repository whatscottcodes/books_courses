# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/Scott/Documents/Coursework/PS3MIT600/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    word_length = 0
    while word_length < len(secretWord):
        for c in secretWord:
            if c in lettersGuessed:
                word_length += 1
            else:
                return False
    if word_length == len(secretWord):
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_length = 0
    guessed_word = ''
    while word_length < len(secretWord):
        for c in secretWord:
            if c in lettersGuessed:
                word_length += 1
                guessed_word += c + " "
            else:
                guessed_word += '_ '
                word_length += 1
    return guessed_word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    all_letters = string.ascii_lowercase
    all_letter_list = list(all_letters)
    availableLetters = all_letter_list[:]
    for c in all_letter_list:
        if c in lettersGuessed:
            availableLetters.remove(c)
    letters = "".join(availableLetters)
    print("Available letters: " + letters)
    return letters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)), " letter(s) long.")
    guesses = 8
    lettersGuessed = []
    guessed_word = "_ " * len(secretWord)
    while guesses > 0:
        print("-------------")
        print('You have ', guesses, " guesses left.")
        getAvailableLetters(lettersGuessed)
        current_letter = input('Please guess a letter: ')
        guess = current_letter.lower()
        if len(guess) != 1:
            print("Oops! That isn't a single letter! Try again: " + guessed_word)
        elif current_letter in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + guessed_word)
        else:
            lettersGuessed.append(current_letter)
            if current_letter in secretWord:
                guessed_word = getGuessedWord(secretWord, lettersGuessed)
                print("Good guess: " + guessed_word)
            else:
                guessed_word = getGuessedWord(secretWord, lettersGuessed)
                print("Oops! That letter is not in my word: " + guessed_word)
                guesses -= 1
        if isWordGuessed(secretWord, lettersGuessed) is True:
            break
    if isWordGuessed(secretWord, lettersGuessed) is True:    
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord)




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
