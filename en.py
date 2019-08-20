import requests
from bs4 import BeautifulSoup
import re
import html5lib
 
 
class English():
 
    def __init__(self,word,details):
       
        self.word = word
        self.is_details = details
        self.error = str
        self.similars = str
        self.sentences = ''
        self.synonyms  = ''
        self.meaning  = ''
        self.word_type  = str
        self.is_correct = bool
        self.set_atributes()

        if self.is_details:
            self.set_synonyms()
 
    def set_atributes(self):
 
        spellcheck = requests.get("https://www.lexico.com/en/definition/" + self.word)
        spellcheck = BeautifulSoup(spellcheck.content,'html.parser')
        self.error = spellcheck.find(class_='searchHeading')
 
        if self.error:

            self.is_correct = False
            similars = requests.get("https://www.collinsdictionary.com/spellcheck/english?q=" + self.word)
            similars = BeautifulSoup(similars.content, 'html.parser').find(class_='columns2')
            
            if similars:
                self.similars = similars.get_text()

        else:
            self.word_type = spellcheck.find(class_='pos').get_text()

            try:
                usage = requests.get("https://www.collinsdictionary.com/dictionary/english/" + self.word)
                example = BeautifulSoup(usage.content,'html.parser').find_all(class_='def')
                word_type1 = BeautifulSoup(usage.content,'html.parser').find_all(class_='pos')

                for definition,word in zip(word_type1,example):
                    self.meaning += ("\n[*{}]:\n{}\n".format(definition.get_text(),word.get_text()))

                sentences = requests.get('https://sentence.yourdictionary.com/' + self.word)
                sentences = BeautifulSoup(sentences.content,'html.parser').find_all(class_='sentence component')[0:3]

                if self.is_details:
                    for sentence in sentences:
                        self.sentences += (sentence.get_text() + '\n')

                ''' dict.org in case of any errors the reason its not used for main dict cuz of 
                html5lib is slower than html.parser and the post req also 
                '''

            except:
                
                dict_org = requests.post('http://www.dict.org/bin/Dict',
                        data={'Form':'Dict1','Query':self.word,'Strategy':'*',
                        'Database':'wn','Sumbit':'Sumbit=query'})

                dict_org = BeautifulSoup(dict_org.text,'html5lib').find_all('pre')[2].get_text()

                self.meaning = dict_org

                        
    ################################################
    
    ''' !!! Note the method will return the synonyms as a list '''
            
    def set_synonyms(self):

        syns = requests.get("https://www.lexico.com/en/synonym/" + self.word)
        syns = BeautifulSoup(syns.content, "html.parser").find_all(class_="syn") 

        

        for syn in syns:
            
            self.synonyms += (syn.get_text())

        self.synonyms = self.synonyms.split(',')
        

        
        ''' Check which arguments are passed and
       display the variables in human readable format  '''

    def display(self):
        if self.is_correct:
            print("\n[**] '{}' is spelled correctly\n\n {}\n".format(self.word,self.meaning))
            if self.is_details:
                print("[-] Example sentens:\n")
                print(self.sentences)
                print("[*] Synonyms:\n")
                for pos,syn in enumerate(self.synonyms):
                    if pos < 15:
                        print(syn.strip(' '))
                    else:
                        break

        else:
            print('\n[**]',self.error.get_text())
            if self.similars:
                print("\nDid you mean:\n {}".format(self.similars))

    ##########################################################
           
    ''' functions to return back the scraped values'''


    def get_similars(self):

        return self.similars

    def get_sentences(self):

        return self.sentences

    def get_synonyms(self):           

        return self.synonyms

    def get_meaning(self):

        return self.meaning

    def get_word_type(self):

        return self.word_type


