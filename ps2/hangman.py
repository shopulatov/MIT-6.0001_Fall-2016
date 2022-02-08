# Problem Set 2, hangman.py
# Name: Abror Shopulatov
# Collaborators: Paulo Quilao
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    print('  ',len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    while True:
        for letter in secret_word:
            if letter not in letters_guessed:
                return False
                break
        return True
            

# secret_word = 'apple'
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    for n in range(len(secret_word)):
        if secret_word[n] not in letters_guessed:
            secret_word = secret_word[:n]+'_'+secret_word[n+1:]
    
    return secret_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    
    for letter in letters_guessed:
        for n in range(len(alphabet)):
            if alphabet[n] == letter:
                alphabet = alphabet[:n]+''+alphabet[(n+1):]
                break
    return alphabet    
    
    
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print("You have 3 warnings left")
    print('-------------')
    
    guesses = 6
    warnings = 3
    alphabet = string.ascii_lowercase
    
    letters_guessed = []
    
    while True:
         print(f'You have {guesses} guesses left.')
         print(f"Available letters: {alphabet}")
         letter = input('Please guess a letter: ​').lower()
         
         if letter not in string.ascii_lowercase:
             warnings -= 1
             if warnings < 0:
                 underscores = 0
                 for letter in get_guessed_word(secret_word, letters_guessed):
                      if letter == "_":
                          underscores +=1
                      
                 print(f"Oops! You have no warnings left so you lose {underscores} guess: {get_guessed_word(secret_word, letters_guessed)}")
                 break
              
             print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
         
         else:
             if letter in letters_guessed:
                 warnings -=1
                 if warnings < 0:
                     underscores = 0
                     for letter in get_guessed_word(secret_word, letters_guessed):
                          if letter == "_":
                              underscores +=1
                          
                     print(f"Oops! You've already guessed that letter. You have no warnings left so you lose {underscores} guess: {get_guessed_word(secret_word, letters_guessed)}")
                     break
                 print(f"Oops! You've already guessed that letter.You now have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
             else:
                 letters_guessed.append(letter)
                 alphabet = get_available_letters(letters_guessed)
                 
                 if is_word_guessed(secret_word, letters_guessed):
                     print('------------')
                     print("Congratulations, you won!")
                     print(f"Your total score for this game is: {guesses * len(set(secret_word))}")
                     break
                     
                 if letter in secret_word:
                     print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                 else:
                    guesses -= 1
                    if guesses == 0:
                        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
                        break
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    
                   
                    
         print('------------')
     
    # print(get_guessed_word(secret_word, letters_guessed))
         



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    test_word = ""
    #  test for similarity in length
    if len(other_word) == len(my_word):
       #  test for similarity in characters and character position
        for char in other_word:
            if char in my_word:
                test_word += char
            else:
                test_word += "_"
    else:
        return False
    #  test for similaroty between other_word and secret_word
    with_sim_char = False
    #  get the index of character "_"
    hidden_letter_index = [pos for pos,
                           char in enumerate(test_word) if char == "_"]
    #  if secret_word and other_word have the same unreaveled characters, not valid for possible matches
    for i in hidden_letter_index:
        if other_word[i] == secret_word[i]:
            with_sim_char = True
    #  test for similarity between my_word and other_word, and other_word and secret_word
    if test_word == my_word and with_sim_char == False:
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_words.append(word)
    
    if len(possible_words) == 0:
        print("No matches found")
    else:
        for pword in possible_words:
            print(pword, end= ' ')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print("You have 3 warnings left")
    print('-------------')
    
    guesses = 6
    warnings = 3
    alphabet = string.ascii_lowercase
    
    letters_guessed = []
    
    while True:
         print(f'You have {guesses} guesses left.')
         print(f"Available letters: {alphabet}")
         letter = input('Please guess a letter: ​').lower()
         
         if letter == "*":
             show_possible_matches(get_guessed_word(secret_word, letters_guessed))
             
         elif letter not in string.ascii_lowercase:
             warnings -= 1
             if warnings < 0:
                 
                  underscores = 0
                  for letter in get_guessed_word(secret_word, letters_guessed):
                      if letter == "_":
                          underscores +=1
                      
                  print(f"Oops! You've already guessed that letter. You have no warnings left so you lose {underscores} guess: {get_guessed_word(secret_word, letters_guessed)}")
                  break
              
             print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
         
         else:
             if letter in letters_guessed:
                 warnings -=1
                 if warnings < 0:
                     underscores = 0
                     for letter in get_guessed_word(secret_word, letters_guessed):
                          if letter == "_":
                              underscores +=1
                          
                     print(f"Oops! You've already guessed that letter. You have no warnings left so you lose {underscores} guess: {get_guessed_word(secret_word, letters_guessed)}")
                     break
                 print(f"Oops! You've already guessed that letter.You now have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
             else:
                 letters_guessed.append(letter)
                 alphabet = get_available_letters(letters_guessed)
                 
                 if is_word_guessed(secret_word, letters_guessed):
                     print('------------')
                     print("Congratulations, you won!")
                     print(f"Your total score for this game is: {guesses * len(set(secret_word))}")
                     break
                     
                 if letter in secret_word:
                     print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                 else:
                    guesses -= 1
                    if guesses == 0:
                        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
                        break
                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
                    
                   
                    
         print('------------')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
