import requests
from bs4 import BeautifulSoup
import html5lib


class English:
    ''' A class for validating and extending
    english words. The main goal of the project
    is to present the scrapped information as clear and
    readable as possible. As the project grows
    the idea behind is to add more complex features like
    localdatabase, text-analyse, grammar-mode in which
    the user can search for a specific grammar rule by
    given query.'''

    def __init__(self, word, details):

        self.word = word
        self.is_details = details
        self.error = ""  # fill if missspelled
        self.similars = ""
        self.sentences = ""
        self.synonyms = ""
        self.meaning = ""
        self.word_type = ""
        self.forms = ""
        self.is_correct = bool
        self.set_atributes()
        self.set_synonyms()



    def set_atributes(self):
        ''' Main logic in this complex method. The method
        will check which arguments are passed by the user
        and will follow the logic. Undesirable information
        will not be scrapped or saved.High working speed and
        memory effcient scripts are always good.'''

        spellcheck = requests.get("https://www.lexico.com/en/definition/" + self.word)
        spellcheck = BeautifulSoup(spellcheck.content, "html.parser")
        self.error = spellcheck.find(class_="searchHeading")

        if self.error:

            self.is_correct = False
            similars = requests.get(
                "https://www.collinsdictionary.com/spellcheck/english?q=" + self.word
            )
            similars = BeautifulSoup(similars.content, "html.parser").find(
                class_="columns2"
            )

            if similars:
                self.similars = similars.get_text()

        else:

            w_type = spellcheck.find(class_="pos").get_text()

            if "verb" == w_type[:4]:
                self.word_type = "verb"
                self.forms = w_type[4:]
            elif "adjective" in w_type:
                self.word_type = "adjective"
                self.forms = w_type[9:]
            elif "noun" in w_type and len(w_type) > 4:
                self.word_type = "noun"
                self.forms = w_type[4:]
            else:
                self.word_type = w_type

            if self.is_details:
                try:

                    sentences = requests.get(
                        "https://sentence.yourdictionary.com/" + self.word
                    )
                    sentences = BeautifulSoup(sentences.content, "html.parser"
                    ).find_all(class_="sentence component")[0:3]

                    if self.is_details:
                        for sentence in sentences:
                            self.sentences += sentence.get_text() + "\n\n"
                except:
                    self.sentences = None

                try:
                    dict_org = requests.post(
                        "http://www.dict.org/bin/Dict",
                        data={
                            "Form": "Dict1",
                            "Query": self.word,
                            "Strategy": "*",
                            "Database": "wn",
                            "Sumbit": "Sumbit=query",
                        },
                    )
                    dict_org = (
                        BeautifulSoup(dict_org.text, "html5lib")
                        .find_all("pre")[2]
                        .get_text()
                    )
                    self.meaning = dict_org
                except:
                    pass

    def set_synonyms(self):
         
        ''' Set the synonyms and write 5 words per line 
            for better looking output'''
            
        syns = requests.get("https://www.lexico.com/en/synonym/" + self.word)
        syns = BeautifulSoup(syns.content, "html.parser").find_all(class_="syn")

        synonyms = ""

        for syn in syns:

            synonyms += syn.get_text()

        synonyms = synonyms.split(",")

        for pos, syn in enumerate(synonyms, start=1):
            if pos % 5 == 0:
                self.synonyms += syn.strip(" ") + ",\n"
            else:
                self.synonyms += syn.strip(" ") + ", "
            if pos > 19:
                break


    def display(self):

        '''Check and validate the values from the
           first methods. Display the information
           in colorized human readable format. '''

        """ initializing color variables """

        reset = "\033[0m"
        yellow = "\033[93m"
        red = "\033[91m"
        cyan = "\033[36m"

        if self.is_correct:
            print(
                yellow,
                "\n[-{} ] [*{}]".format(self.word, self.word_type),
                reset + " is spelled correctly",
            )
            if self.forms:
                print(red, "({})".format(self.forms))

            # check if we have syns
            if not self.synonyms == ", ":
                print(yellow)
                print("[*] Synonyms:")
                print(cyan)
                print(self.synonyms)

            if self.is_details:

                if self.meaning:
                    print(yellow,"\n[*] Meaning:\n",reset)
                    print(self.meaning)

                if self.sentences:
                    print(yellow)
                    print("[-] Example sentens:\n", reset)
                    print(self.sentences)

        else:
            print(red, "\n[**]", yellow, self.error.get_text(), reset)
            if self.similars:
                print(yellow, "\n[--] Did you mean:", reset)
                print(cyan, self.similars, reset)


        ''' Methods to return back the scraped values.
            This is for later when the database
            idea becomes reality'''

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

    def get_forms(self):

        return self.forms
