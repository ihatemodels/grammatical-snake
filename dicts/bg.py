import requests
from bs4 import BeautifulSoup

class Bulgarian:
    ''' A class for validating and extending
    bulgarian words. The main goal of the project
    is to present the scrapped information as clear and
    readable as possible. As the project grows
    the idea behind is to add more complex features like
    localdatabase, text-analyse, grammar-mode in which
    the user can search for a specific grammar rule by
    given query.'''

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

    def set_spellcheck(self):

        ''' spellcheck the word set the is_correct and
        fill the self.forms '''

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

    def set_meaning_syns(self):

        ''' setting the meaning, synonyms and
            the tranlasted form if there is no
            meaning or syns the variables will be empty '''

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

    def display(self):

        ''' Check which arguments are passed and
            display the variables in human readable
            format  '''

        ''' initializing color variables '''

        reset = "\033[0m"
        yellow = "\033[93m"
        red = "\033[91m"
        cyan = "\033[36m"

        if self.is_correct:
            print(yellow)
            print("[**] Думата '{}' е написана правилно\n".format(self.word),reset)
            print(self.forms.rstrip())

            if self.is_details:
                if self.synonyms:
                    print(yellow)
                    print("\n[-] Синоними:\n",cyan)
                    print(self.synonyms)
                if self.meaning:
                    print(yellow)
                    print("[*] Tълковен речник:\n",reset)
                    print(self.meaning)
                if self.translated:
                    print(yellow)
                    print("[+] Превод:\n",reset)
                    print(self.translated)
        else:
            print(red,"[!!]")
            print(yellow,self.error,reset)

    ''' Methods to return back the scraped values.
        This is for later when the database
        idea becomes reality '''

    def get_synonyms(self):

        return self.synonyms

    def get_forms(self):

        return self.forms

    def get_meaning(self):

        return self.meaning

    def get_translate(self):

        return self.translated

