# **grammatical-snake** :snake: :mortar_board:

Grammatical-snake is a simple terminal dictionary and spellcheck script with advanced futures for cool people. Priority over the browser dictionaries is the speed and simplicity. The main achievement is to return the scrapped information as precise and readable as possible. As the project grows, the idea behind is to add more complex features like local database, text analysis, grammar-mode in which the user can search for a specific grammar rule by a given query. IT terminology dictionary in separated mode with explanations translate is coming soon. Maybe a fancy GUI with a better experience for non-terminal-like people. So far supported languages are Bulgarian, and English.

### POWERED BY
:point_down:  
[Rechnik.info](http://rechnik.info) [Collinsdict](https://www.collinsdictionary.com)  
[Slovored](https://slovored.com/)  [Lexico](https://www.lexico.com)    
[Yourdict](https://sentence.yourdictionary.com)  [Dict.org](http://www.dict.org)


### FEATURES

- :white_check_mark: Spellcheck, Word Forms
- :closed_book: Word meaning, Sentence usage(example)
- :blue_book: Synonyms, Translate
- :fast_forward: Faster than browser dictionaries, no java-script, ads, cookies alert-dialogs or whatever you can imagine.
- :black_square_button: Terminal simplicity, Highlighted structured output.

#### INSTALL

### **Requirements**

- Python3
- beautifulsoup4
- html5lib
- **Terminal-Nature** :alien:

**The script require only 2 packages but it's good practice to create separate virtual environment. You can mess your existing versions if any!**

- **Windows**
```
git clone https://github.com/ihatemodels/grammatical-snake
pip install -r requirements.txt
```
- **Linux**
```
git clone https://github.com/ihatemodels/grammatical-snake
cd bg-en-spellcheck
pip3 install -r requirements.txt
chmod +x spellcheck.py  
```

## USAGE

**spellcheck.py [-h] --input -i [word] --details -d**

```
optional arguments:
  -h, --help            show this help message and exit

  --input WORD, -i WORD  
                        [*] required  
                        Word in Bulgarian or in English(singular). The script will  
                        detect the input language. If the word is correct and exists  
                        word forms will be returned. Else suggestions will be displayed.  

  --details, -d         Pass to display definition, examples,  
                        synonyms, translate (BG to EN only atm.)  
                        when available.**  

```
### Bugs Hugs & Drugs  

**The Bulgarian translated graph is looking ugly. TODO: Re-Construct**   
**The color schema is suitable under dark background color only.**  
**For windows users it's recommended to use terminal emulator like  
Terminus.**
**The new Windows Terminal must be fine as well, otherwise  
 powershell tweak
is required in order to display the colors**
**See more on: [StackOverflow](https://stackoverflow.com/questions/51680709/colored-text-output-in-powershell-console-using-ansi-vt100-codes)**

## IDEAS FOR LAZY DAYS :smoking:

- **1.(FIRST)** Add IT terminology dictionary from **[stelf/en2bg4term](https://github.com/stelf/en2bg4term)** as local (files/db.)
- **Bulgarian README.md**
- Add English to Bulgarian translate
- Add local database
- Grammar mode with menu and search mode (searchquery=='grammar-rule')
- Output the search to a csv
- **True mode** a.k.a waiting for another word without exiting the script
- Unit tests

#### SHOWTIME
- **count the second** :one: :two:

<div>
<img src="/img/mixed.gif"
 alt="mixed"
 />
</div>  

:three: :four:

<div>
<img src="/img/gif-bg.gif"
 alt="gif-bg"
 />
</div>

<div>
<img src="/img/gif-en.gif"
 alt="gif-en"
 />
</div>
