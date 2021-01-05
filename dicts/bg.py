import requests
from bs4 import BeautifulSoup
from rich.text import Text

from .exceptions import DictConnectionError
from core.styler import Styler, console


class Bulgarian(Styler):
    """Bulgarian class, implement bulgarian words
    spellcheck, synonyms and meaning interfaces via
    wep scrape.

    Args:
        word (str): Word to check on.
        details (Optional[bool], optional): Enable/disable synonyms, meaning and english translate.
    """

    def __init__(self, word: str = None, details: bool = False):

        self.word = word
        self.details = details
        self.is_correct = bool
        self.error = ""
        self.forms = []
        self.header_elements = []
        self.header = ""
        self.synonyms = ""
        self.meaning = ""
        self.translated = ""

        self.SPELL_CHECK_URL = "https://slovored.com/search/pravopisen-rechnik/"

        self._set_spellcheck()

        if self.details:
            self.DETAILS_URL = "http://rechnik.info/"
            self.details_error = False
            self._set_details()

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
        except:
            self.is_correct = True
            pre = spellcheck.find("pre").get_text().rstrip("\n").split("\n")
            for element in pre:
                if len(element) == 0:
                    continue
                elif element.startswith("   "):
                    if len(self.forms) < 15:
                        self.forms.append(str(element).lstrip())
                else:
                    self.header_elements.append(element)
                    self.header = self.header + element + "\n"

    def _set_details(self):
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

    def display(self):
        """
        Display scraped output as human readable format.
        """

        if self.is_correct:

            self.print(Text(self.header.rstrip('\n'), style="#00cc00", justify="left"))

            if self.details:

                if self.details_error:
                    # TODO: Add logging
                    print(
                        f"\n[---] Connection Error: Details can not be set. No connection \
                          can be established to {self.DETAILS_URL}"
                    )
                    return

                if self.synonyms:
                    console.print(f"\n+ Синоними\n+", style="bold yellow")
                    self.print(Text(self.synonyms, style="#00cc00", justify="left"))

                if self.meaning:
                    console.print(f"\n+ Значение\n+", style="bold yellow")
                    self.print(Text(self.meaning, style="#00cc00", justify="left"))

                if self.translated:
                    console.print(f"\n+ Превод \n+", style="bold yellow")
                    self.print(Text(self.translated, style="#00cc00", justify="left"))
        else:
            console.print(Text(f"\n- - - - - - {self.word} \n-", style="bold red"))
            console.print(Text(f"-{self.error}", style="bold yellow"))

    def get_synonyms(self) -> str:

        return self.synonyms

    def get_forms(self) -> list:

        return self.header_elements

    def get_meaning(self) -> str:

        return self.meaning

    def get_translate(self) -> str:

        return self.translated

    def get_error(self) -> str:

        return self.error
