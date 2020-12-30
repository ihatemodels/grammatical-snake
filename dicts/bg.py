import colorama
import requests
from bs4 import BeautifulSoup
from termcolor import cprint

from .exceptions import DictConnectionError


class Bulgarian:
    """Bulgarian class, implement bulgarian words
    spellcheck, synonyms and meaning interfaces.

    Parameters:  
        word (str) Word to check on.  

        details (bool) If `True` word meaning, synonyms and english translate
        will be set during the init if any. 
    """

    def __init__(self, word=None, details=None):

        self.word = word
        self.is_details = details
        self.error = ""
        self.forms = ""
        self.synonyms = ""
        self.meaning = ""
        self.translated = ""
        self.is_correct = bool

        self.SPELL_CHECK_URL = "https://slovored.com/search/pravopisen-rechnik/"

        self._set_spellcheck()

        if self.is_details:
            self.DETAILS_URL = "http://rechnik.info/"
            self.details_error = False
            self._set_meaning_syns()

    def _set_spellcheck(self):
        """
        Spellcheck the `self.word` 

        Set `is_correct` and `forms` about the word
        """

        try:
            r = requests.get(self.SPELL_CHECK_URL + self.word)
        except requests.exceptions.RequestException as e:
            raise DictConnectionError(e)

        spellcheck = BeautifulSoup(r.content, "html.parser")

        try:
            error = spellcheck.find(class_="error")
            self.is_correct = False
            self.error = error.get_text()
            self.forms = spellcheck.find("pre").get_text()
        except:
            self.is_correct = True
            self.forms = spellcheck.find("pre").get_text()

    def _set_meaning_syns(self):
        """
        Set `meaning`, `synonyms` and `translated` if any
        """

        try:
            r = requests.get(self.DETAILS_URL + self.word)
        except requests.exceptions.RequestException:
            self.details_error = True
            return

        mistake = BeautifulSoup(r.content, "html.parser").find(
            class_="word_no_desc")
        headers = BeautifulSoup(r.content, "html.parser").find_all(
            class_="word_description_label"
        )

        data = BeautifulSoup(
            r.content, "html.parser").find_all(class_="defbox")

        if not mistake:

            for header, element in zip(headers, data):
                if "Тълковен речник" in header.get_text():
                    self.meaning = element.get_text()
                if "Синонимен речник" in header.get_text():
                    self.synonyms = element.get_text()
                if "Българо-Английски речник" in header.get_text():
                    self.translated = element.get_text()
        else:
            pass

    def display(self, colored=None):
        """
        Display scraped output as colored human readable format
        """

        colorama.init()

        if self.is_correct:

            cprint("\n[**] Думата '{}' е написана правилно\n".format(self.word),
                   'green', attrs=['bold'])
            print(self.forms.rstrip())

            if self.is_details:
                if self.details_error:
                    cprint(f"\n[---] Connection Error: Details can not be set. No connection \
                            can be established to {self.DETAILS_URL}",
                           'red', attrs=['bold'])
                    return
                if self.synonyms:
                    cprint("\n[-] Синоними:\n", 'yellow', attrs=['bold'])
                    cprint(self.synonyms, 'cyan', attrs=['bold'])
                if self.meaning:
                    cprint("\n[*] Tълковен речник:\n",
                           'yellow', attrs=['bold'])
                    print(self.meaning)
                if self.translated:
                    cprint("\n[+] Превод:\n", 'yellow', attrs=['bold'])
                    print(self.translated)
        else:
            cprint("[!!] {} [!!]".format(self.word), 'red', attrs=['bold'])
            cprint(self.error, 'yellow')

    def get_synonyms(self):

        return self.synonyms

    def get_forms(self):

        return self.forms

    def get_meaning(self):

        return self.meaning

    def get_translate(self):

        return self.translated

    def get_error(self):

        return self.error
