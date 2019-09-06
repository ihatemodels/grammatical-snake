import argparse,textwrap,re
from argparse import RawTextHelpFormatter
from dicts.bg import Bulgarian
from dicts.en import English


__author__ = 'Gergin Darakov'
__version__ = 0.1
__credits__ = 'Credits for all scrapped dictionaries in README'
__status__ = 'Development'
__license__ = 'GPL-3.0'


def main():

    ''' The execution point of the script the --input argument
       isn't set as required via argparse, cuz it will conflict
       with other new args when the script becomes big  '''

    def is_cyrillic(word):
        '''Verify the input language '''
        return bool(re.search("[а-яА-Я]", word))

    parser = argparse.ArgumentParser(
        description='Simple terminal dictionary with advanced features',
        epilog=textwrap.dedent('''
        {}
        Author: {}
        Version: {}'''.format(__credits__,__author__,__version__)),
        formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        '--input',
        '-i',
        dest='word',
        type=str,
        help=textwrap.dedent('''\
        [*] required
        Word in Bulgarian or in English(singular). The script will
        detect the input language. If the word is correct and exists
        word forms will be returned. Else suggestions will be displayed.

        '''))

    parser.add_argument(
        '--details',
        '-d',
        dest='details',
        action='store_true',
        help=textwrap.dedent('''\
        Pass to display definition, examples,
        synonyms, translate (BG to EN only atm)
        when available.

        '''))

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
