import requests
from bs4 import BeautifulSoup


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
        headers = BeautifulSoup(data.content,'html.parser').find_all(class_='word_description_label')
        data = BeautifulSoup(data.content,'html.parser').find_all(class_='defbox')
        
 
        if not mistake:
           
            try:
                if len(headers) == 3:
                    self.meaning = data[0].get_text()
                    self.synonyms = 'Не бяха открити синоними'
                    self.translated = data[1].get_text()

                else:
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
           
    ''' methods to return back the scraped values'''
 
    def get_synonyms(self):
 
        return self.synonyms
 
    def get_forms(self):
 
        return self.forms
 
    def get_meaning(self):
 
        return self.meaning
 
    def get_translate(self):
 
        return self.translated