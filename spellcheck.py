import argparse
from functions import bulgarian_check,get_synon_bg,has_cyrillic,translate,english_check,get_synon_en



def main():
    
    parser = argparse.ArgumentParser(
        description='Termianl spell-check, synonyms and translate')

    parser.add_argument(
        '--synonyms',
        '-s',
        dest='synonyms',
        help='Pass the argument to display synonyms.',
        action='store_true'    
    )

    parser.add_argument(
        '--input',
        '-i',
        dest='word',
        help='Pass a word in bulgarian or in english',
        required=True
    )

    parser.add_argument(
        '--translate',
        '-t',
        dest='translate',
        help='Translate from bg to en or from en to bg',
        action='store_true'
    )

    args=parser.parse_args()
    word = args.word
    synonyms = args.synonyms
    tran = args.translate
    

    if has_cyrillic(word):
       if bulgarian_check(word):
          if synonyms:
            get_synon_bg(word)
          if tran:
            translate(word,'bg')
    else:
        if english_check(word):
            if synonyms:
                get_synon_en(word)
            if tran:
                translate(word,'en')


if __name__ == "__main__":
    main()

