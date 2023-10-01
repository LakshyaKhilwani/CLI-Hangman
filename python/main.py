import random
from time import sleep
from os import system,name
with open("words.txt") as f:
    words_list=f.read().split(" ")

word=random.choice(words_list)
print(word)
def clear(): 
  
    # for windows
    # clearscreen 
    if name == 'nt': 
        system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear') 
HANGMAN = (
    """
 ------
|     |
|
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|
|
|
|
|
----------
"""
   ,
"""
 ------
|     |
|     0
|     +
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\\
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\\
|     |
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\\
|     |
|     |
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\\
|     |
|     |
|    /
|   /
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-\\
|     |
|     |
|    / \\
|   /   \\
----------
"""
)

attemptLeft = len(HANGMAN)-1

correctGuesses=[]

def get_hangman():
    return HANGMAN[-1-attemptLeft]

def get_word_state():
    res=""
    for i in word:
        if i in correctGuesses:
            res+=i
        else:
            res+='_ '
    return res

def get_input():
    global attemptLeft
    guess=input("Guess your Letter: ")[0]
    if guess in word:
        correctGuesses.append(guess)
        print("You Guessed it correctly...")
        return True
    else:
        attemptLeft-=1
        print("You Couldn't guess the word..")
        return False

while "_ " in get_word_state() and attemptLeft:
    clear()
    print(get_hangman())
    print("Word:",get_word_state())
    correctGuess=get_input()
    sleep(1)

# clear()
print(get_hangman())
print("Word:",get_word_state())

if attemptLeft:
    print("Congratulations, You guessed the word ",word)
else:
    print("The word is:",word)

print("Press enter to exit..")
input()
