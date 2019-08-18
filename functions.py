import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import re
import html5lib

# Check if the given word is bulgarian

def has_cyrillic(word):
    return bool(re.search("[а-яА-Я]", word))

# Bulgarian spellcheck

def bulgarian_check(word):

    response = requests.get("https://slovored.com/search/pravopisen-rechnik/" + word)

    if '<span class="error">' in response.text:
        print("\nНепозната дума: ", word, "\n\nMoже би имахте предвид:")

    response = BeautifulSoup(response.content, "html.parser")

    if response.find_all("pre"):
        output = response.find_all('pre')[0].get_text()
        print(output)
        return True
    else:
        print("\nНепозната дума: '{}'".format(word))
        return False

    meaning = requests.get("https://rechnik.chitanka.info/w/" + word)
    meaning = BeautifulSoup(meaning.content, "html.parser")

    if meaning.find(class_="meaning box"):
        print(meaning.find(class_="meaning box").get_text())


def get_synon_bg(word):

    # Get the synonyms

    result = requests.get("https://slovored.com/search/synonymous/" + word)
    result = BeautifulSoup(result.content, "html.parser").find(class_="translation").get_text()
    

    # Cleaning the output

    result = re.sub(r"[a-z]", "", result, flags=re.I)
    result = re.sub(r"\d", "", result)
    result = result.split(",")
    result = result[:-2]

    # Printing in human readable format

    print("Синоними:")

    for element in result:
        print(element)


def english_check(word):

    response = requests.get("https://www.lexico.com/en/definition/" + word)
    output = BeautifulSoup(response.content, "html.parser")
    mistake_detector = output.find(class_="searchHeading")
    word_type = output.find(class_='pos')

    if mistake_detector:

        similar = requests.get("https://www.collinsdictionary.com/spellcheck/english?q=" + word)
        similars = BeautifulSoup(similar.content, "html.parser").find(class_="columns2")
        

        print('\n[**]',mistake_detector.get_text())

        if similars:
            print("\nDid you mean:\n", similars.get_text())

        return False

    else:

        output = output.find(class_="trg")

        try:
            examples = output.find_all(class_="ex")
            word_explain = output.find(class_="ind").get_text()  # explanation
            phrases = output.find_all(class_="phrase")

        except AttributeError:
            # Form=Dict1&Query=program&Strategy=*&Database=wn&submit=Submit+query
            
            dict_org = requests.post('http://www.dict.org/bin/Dict',
                        data={'Form':'Dict1','Query':word,'Strategy':'*',
                        'Database':'wn','Sumbit':'Sumbit=query'})
                        
            dict_org = BeautifulSoup(dict_org.text,'html5lib').find_all('pre')[2].get_text()
            print(dict_org)
            
            return True

        else:
            print("\n[**] '{}' is spelled correctly\n\n[ {} ] {}\n".format(word,word_type.get_text(),word_explain))
            print("[-] Example sentens:\n")

        
            for pos, element in enumerate(examples):
                print(element.get_text())
                #We will print just 4 examples not all of what we scrape
                if pos > 2:    
                    break

            if phrases:
                print("Phrases:\n")
                for phrase in phrases:
                    print(phrase.get_text())

            print("\n")
            return True

def get_synon_en(word):

    
    syns = requests.get("https://www.lexico.com/en/synonym/" + word)
    syns = BeautifulSoup(syns.content, "html.parser").find_all(class_="syn")

    syns_string = ''

    for syn in syns:
        
        syns_string += (syn.get_text().replace(' ',""))

    syns_list = syns_string.split(',')
    print("[*] Synonyms:\n")

    for pos,element in enumerate(syns_list):
        if pos < 20:
            print(element)
        else:
            break



def translate(word, source):

    translator = Translator()

    if has_cyrillic(word):
        print("\nEnglish: ", translator.translate(word, src=source).text)
    else:
        print("\nBulgarian: ", translator.translate(word, src=source, dest="bg").text)

