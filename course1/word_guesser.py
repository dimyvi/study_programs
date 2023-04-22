from random import *

word_list = ['ненавижу', 'эту', 'угадайку']


def get_word():
    word = choice(word_list).upper()
    play(word)


def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / \
        |
        |

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    guessed = False
    tries = 6  # количество попыток
    sym = '!@#$%^&*()-=+/\\.?,'
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)


get_word()
