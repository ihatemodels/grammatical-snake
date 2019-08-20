import requests
from bs4 import BeautifulSoup
import re
import html5lib

# Check if the given word is bulgarian

def is_cyrillic(word):
    return bool(re.search("[а-яА-Я]", word))

  
class Bulgarian:
   
    def __init__(self,word,details,translate):
       
        self.word = word
        self.is_details = details
        self.is_translate = translate
        self.error = str
        self.forms = str
        self.synonyms  = str
        self.meaning  = str
        self.translated  = str
        self.is_correct = bool
        self.set_spellcheck()
 
        if self.is_details:
            self.set_meaning_syns()
 
 
    ''' spellcheck the given word and set the is_correct and fill the self.forms'''
 
   
    def set_spellcheck(self):
 
        spellcheck = requests.get("https://slovored.com/search/pravopisen-rechnik/" + self.word)
        spellcheck = BeautifulSoup(spellcheck.content, "html.parser")
 
        try:
            error = spellcheck.find(class_='error')
            self.is_correct = False
            self.error = error.get_text()
            self.forms = spellcheck.find('pre').get_text()
        except:
            self.is_correct = True
            self.forms = spellcheck.find('pre').get_text()
           
    ''' setting the meaning, synonyms and the tranlasted form of the give word
       if there is no meaning or syns the variables will be empty '''
 
    def set_meaning_syns(self):
 
        data = requests.get('http://rechnik.info/' + self.word)
        mistake = BeautifulSoup(data.content,'html.parser').find(class_='word_no_desc')
        data = BeautifulSoup(data.content,'html.parser').find_all(class_='defbox')
 
        if not mistake:
           
            try:
                self.meaning = data[0].get_text()
                self.synonyms = data[1].get_text()
                self.translated = data[2].get_text()
            except IndexError:
                pass
        else:
            self.meaning = ''
            self.synonyms =''
            self.translated =''
 
    ''' Check which arguments are passed and
       display the variables in human readable format  '''
 
    def display(self):
 
        if self.is_correct:
            print("\nДумата '{}' е написана правилно\n".format(self.word))
            print(self.forms)
            if self.is_details:
                print("Tълковен речник: {} \n".format(self.meaning))
                print("Синоними: \n\n {} \n\n".format(self.synonyms))
            if self.is_translate:
                print("Превод с примери: \n\n {} \n ".format(self.translated))
        else:
            print(self.error)
            print(self.forms)
 
    ##########################################################
           
    ''' functions to return back the scraped values'''
 
    def get_synonyms(self):
 
        return self.synonyms
 
    def get_forms(self):
 
        return self.forms
 
    def get_meaning(self):
 
        return self.meaning
 
    def get_translate(self):
 
        return self.translated
   
 
 
class English():
 
    def __init__(self,word,details):
       
        self.word = word
        self.is_details = details
        self.error = str
        self.similars = str
        self.sentences = ''
        self.synonyms  = ''
        self.meaning  = str
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


                
                dict_org = requests.post('http://www.dict.org/bin/Dict',
                        data={'Form':'Dict1','Query':self.word,'Strategy':'*',
                        'Database':'wn','Sumbit':'Sumbit=query'})

                dict_org = BeautifulSoup(dict_org.text,'html5lib').find_all('pre')[2].get_text()

                self.meaning = dict_org

                sentences = requests.get('https://sentence.yourdictionary.com/' + self.word)
                sentences = BeautifulSoup(sentences.content,'html.parser').find_all(class_='sentence component')[0:3]

                if self.is_details:
                    for sentence in sentences:

                        self.sentences += (sentence.get_text() + '\n')

                
             
            except IndexError:
                pass
                        
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
            print("\n[**] '{}' is spelled correctly\n\n[ {} ]\n {}\n".format(self.word,self.word_type,self.meaning))
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



