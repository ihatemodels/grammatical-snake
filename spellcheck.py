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

    subparsers = parser.add_subparsers(dest='sub')

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

    book = subparsers.add_parser(
        'book',
        formatter_class=RawTextHelpFormatter,
        help=textwrap.dedent('''\
        Pass to enter book mode.I.E: Spellcheck without exiting
        the script. Like reading a dictionary book. Choose 9 to
        exit. Pass -d for details or leave empty for spellcheck 
        and forms only.'''))


    book.add_argument(
        '--details',
        '-d',
        dest='e_details',
        action='store_true',
        help=textwrap.dedent('''\
            
        Pass to display definition, examples,
        synonyms, translate (BG to EN only atm)
        when available.

        '''))

    args=parser.parse_args()

    if not args.sub:

        if not args.word:
            print('Please specify a word')
            exit()

        if is_cyrillic(args.word):
            new_word = Bulgarian(args.word,args.details)
            new_word.display()
        else:
            new_word = English(args.word,args.details)
            new_word.display()
    else:

        while True:
            word = input('Please specify a word:\n')
            if word == '9':
                exit()
            else:
                if is_cyrillic(word):
                    new_word = Bulgarian(word,args.e_details)
                    new_word.display()
                else:
                    new_word = English(word,args.e_details)
                    new_word.display()    
            


if __name__ == "__main__":
    main()
