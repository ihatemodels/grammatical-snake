import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import sys
import re


# Check if the given word is bulgarian

def has_cyrillic(word):
    return bool(re.search('[а-яА-Я]', word))


def bulgarian_check(word):


    response = requests.get(
        'https://slovored.com/search/pravopisen-rechnik/' + word)

    if '<span class="error">' in response.text:
        print("\nНепозната дума: ", word,'\n\nMoже би имахте предвид:')


    response = BeautifulSoup(response.content, 'html.parser')
    output = response.find_all('pre')[0].get_text()
    print(output)

    meaning = requests.get("https://rechnik.chitanka.info/w/" + word)
    meaning = BeautifulSoup(meaning.content, 'html.parser')

    if not meaning.find(class_='meaning box') == None:
        print(meaning.find(class_='meaning box').get_text())


def get_synon_bg(word):

    output = ''
    print("Синоними:")
    response = requests.get('https://slovored.com/search/synonymous/' + word)
    soup = BeautifulSoup(response.content, 'html.parser')
    result = soup.find(class_='translation').get_text()

    # Cleaning the output

    result = re.sub(r"[a-z]", "", result, flags=re.I)
    result = re.sub(r"\d", "", result)
    result = result.split(',')

    # Printing in human readable format

    for pos, line in enumerate(result,start=1):

        if pos < (len(result) - 1):
            if pos % 5 == 0:
                output += line + ',\n'
            else:
                output += line + ','

    print(output)

def english_check(word):

    response = requests.get('https://www.lexico.com/en/definition/' + word )
    soup = BeautifulSoup(response.content, 'html.parser')
    mistake_detector = soup.find(class_='searchHeading')
    
    if not mistake_detector == None:
        
        similar = requests.get('https://www.collinsdictionary.com/spellcheck/english?q=' + word)
        similar_soup = BeautifulSoup(similar.content,'html.parser')
        similars = similar_soup.find(class_='columns2')
        
        print(mistake_detector.get_text())
        print("\nDid you mean:\n",similars.get_text())

    else:

        output = soup.find(class_='trg')
        human_read = output.find_all(class_='ex')
        noun = (output.find(class_='ind').get_text()) # noun explanation
        phrases = (soup.find_all(class_='phrase'))
        
        print('The word {} is spelled correctly\n\nNoun: {}\n'.format(word,noun))
        
        print ('Examples:\n')

        for pos,element in enumerate(human_read):
            print(element.get_text())
            if pos > 2: 
                print('\n')
                break
        
        if phrases:
            print('Phrases:\n')
            for phrase in phrases:
                print(phrase.get_text())

        print('\n')

def get_synon_en(word):

    output = ''
    response = requests.get('https://www.lexico.com/en/synonym/' + word)
    soup = BeautifulSoup(response.content, 'html.parser')
    syns = soup.find_all(class_='syn')
 
    for pos,syn in enumerate(syns):
        if pos > 10:
            break
        else:
            output += syn.get_text()
    
    print('Synonyms:\n\n/p ',output)

def translate(word,source):

    translator = Translator()

    if has_cyrillic(word):
        print('\nEnglish: ' ,translator.translate(word,src=source).text)
    else:
        print('\nBulgarian: ' ,translator.translate(word,src=source,dest='bg').text)


