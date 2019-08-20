import argparse
from functions import is_cyrillic,Bulgarian,English



def main():
    
    parser = argparse.ArgumentParser(
        description='Termianl spell-check, word-meaning, synonyms, translate and many more')

    parser.add_argument(
        '--details',
        '-d',
        dest='details',
        help='Pass the argument to display word meaning and synonyms.',
        action='store_true'    
    )

    parser.add_argument(
        '--input',
        '-i',
        dest='word',
        help='Pass a word in bulgarian or in english. In english the word must be singular',
        required=True
    )

    parser.add_argument(
        '--translate',
        '-t',
        dest='translate',
        help='Translate from bulgarian to english',
        action='store_true'
    )

    args=parser.parse_args()
    word = args.word
    details = args.details
    translate = args.translate
    

    if is_cyrillic(word):
        new_word = Bulgarian(word,details,translate)
        new_word.display()
    else:
        new_word = English(word,details)
        new_word.display()


if __name__ == "__main__":
    main()

