import argparse
import re
## Local imports 

from dicts.bg import Bulgarian
from dicts.en import English

# Check the input language

def is_cyrillic(word):
    return bool(re.search("[а-яА-Я]", word))

def main():
    
    parser = argparse.ArgumentParser(
        description='Termianl spell-check, word-meaning, synonyms, translate and many more')

    parser.add_argument(
        '--details',
        '-d',
        dest='details',
        help='Pass the argument to display examples and synonyms.',
        action='store_true'    
    )

    parser.add_argument(
        '--input',
        '-i',
        dest='word',
        help='Pass a word in bulgarian or in english. In english the word must be singular'
    )

    args=parser.parse_args()
    word = args.word
    details = args.details
    
    if not word:
        print('Please specify a word')
        exit()
        
    if is_cyrillic(word):
        new_word = Bulgarian(word,details)
        new_word.display()
    else:
        new_word = English(word,details)
        new_word.display()



if __name__ == "__main__":
    main()

