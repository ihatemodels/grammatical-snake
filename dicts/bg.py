import requests
from bs4 import BeautifulSoup


class Bulgarian:
    def __init__(self, word, details):

        self.word = word
        self.is_details = details
        self.error = ""
        self.forms = ""
        self.synonyms = ""
        self.meaning = ""
        self.translated = ""
        self.is_correct = bool
        self.set_spellcheck()

        if self.is_details:
            self.set_meaning_syns()

    """ spellcheck the given word set the is_correct and fill the self.forms"""

    def set_spellcheck(self):

        spellcheck = requests.get(
            "https://slovored.com/search/pravopisen-rechnik/" + self.word
        )
        spellcheck = BeautifulSoup(spellcheck.content, "html.parser")

        try:
            error = spellcheck.find(class_="error")
            self.is_correct = False
            self.error = error.get_text()
            self.forms = spellcheck.find("pre").get_text()
        except:
            self.is_correct = True
            self.forms = spellcheck.find("pre").get_text()

    """ setting the meaning, synonyms and the tranlasted form of the given word
       if there is no meaning or syns the variables will be empty """

    def set_meaning_syns(self):

        data = requests.get("http://rechnik.info/" + self.word)
        mistake = BeautifulSoup(data.content, "html.parser").find(class_="word_no_desc")
        headers = BeautifulSoup(data.content, "html.parser").find_all(
            class_="word_description_label"
        )
        data = BeautifulSoup(data.content, "html.parser").find_all(class_="defbox")

        if not mistake:
            
            for header,element in zip(headers,data):
                if "Тълковен речник" in header.get_text():
                    self.meaning = element.get_text()
                if "Синонимен речник" in header.get_text():
                    self.synonyms = element.get_text()
                if "Българо-Английски речник" in header.get_text():
                    self.translated = element.get_text()
    
        else:
            pass


    """ Check which arguments are passed and
       display the variables in human readable format  """

    def display(self):

        """ initializing color variables """

        reset = "\033[0m"
        yellow = "\033[93m"
        red = "\033[91m"
        cyan = "\033[36m"


        if self.is_correct:
            print(yellow)
            print("[**] Думата '{}' е написана правилно\n".format(self.word),reset)
            print(self.forms.rstrip())

            if self.is_details:
                print(yellow)
                print("\n[-] Синоними:\n",cyan)
                print(self.synonyms)
                print(yellow)
                print("[*] Tълковен речник:\n",reset)
                print(self.meaning)
                print(yellow)
                print("[+] Превод:\n",reset)
                print(self.translated)
        else:
            print(red,"[!!]")
            print(yellow,self.error,reset)

    ##########################################################

    """ methods to return back the scraped values"""

    def get_synonyms(self):

        return self.synonyms

    def get_forms(self):

        return self.forms

    def get_meaning(self):

        return self.meaning

    def get_translate(self):

        return self.translated
