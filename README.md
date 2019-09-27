#  :mortar_board: :snake: **grammatical-snake** :snake: :mortar_board:

Grammatical-snake is a simple terminal dictionary and spellcheck script with advanced features. Two main priorities over browser dictionaries: Speed and Simplicity. **The main achievement is to return the scrapped information as precise and readable as possible.** As the project grows, the idea behind is to add more complex features like, terms dictionary, text analysis, grammar-mode in which the user can search for a specific grammar rule by a given query. IT-Terms in separated mode with explanations, examples and translates will be added soon. At the end it could be fancy GUI with a better experience for non-terminal-like people. Who knows ?    

#### So far supported languages are **Bulgarian** & English.

 > **concept of adding more**

## **POWERED BY**

**:point_down:**

**[Rechnik.info](http://rechnik.info) [Collinsdict](https://www.collinsdictionary.com)**  
**[Slovored](https://slovored.com/)  [Lexico](https://www.lexico.com)**      
**[Yourdict](https://sentence.yourdictionary.com)  [Dict.org](http://www.dict.org)**  


## **FEATURES**

- **:white_check_mark:** Spellcheck, Word Forms, Transription
- **:closed_book:** Word meaning, Sentence usage(example)
- **:blue_book:** Synonyms, Translate
- **:fast_forward:** Faster than browser dictionaries, no JavaScript, ads, cookies alert-dialogs or whatever you can imagine.
- **:black_square_button:** Terminal simplicity, Highlighted structured output.

### **INSTALL**

#### Requirements

- Python3
> - beautifulsoup4  
> - html5lib
> - colorama
> - termcolor
- **Terminal-Nature :alien:**

**It's good practice to create separate virtual environment. You can mess your packages versions!**  
*Under windows it's better to use terminal emulator like Terminus,Moba X Term, etc..*

- **Windows**
```
git clone https://github.com/ihatemodels/grammatical-snake
pip install -r requirements.txt
```
- **Linux**
```
git clone https://github.com/ihatemodels/grammatical-snake
cd grammatical-snake/
pip3 install -r requirements.txt
chmod +x spellcheck.py  
```

## **USAGE**

[USAGE.md](/img/USAGE.md)  

**spellcheck.py [-h] --input -i [word] --details -d (optional)**  
**spellcheck.py book [-h] --details -d (optional)**
```
optional arguments:

positional arguments:

  {book}

    book                Pass to enter book mode.I.E: Spellcheck without exiting
                        the script. Like reading dictionary book. Choose 9 to
                        exit. Pass -d for details or leave empty for spellcheck
                        and forms only.

                        optional arguments: --details -d 

  -h, --help            show this help message and exit

  --input WORD, -i WORD  
                        [*] required  
                        Word in Bulgarian or in English(singular). The script will  
                        detect the input language. If the word is correct and exists  
                        word forms and transription will be returned. Else suggestions 
                        will be displayed.  

  --details, -d         Pass to display definition, examples,  
                        synonyms, translate (BG to EN only atm.)  
                        when available.  

```

### *BUGS* & **HUGS**  

**The Bulgarian translated graph is looking ugly.**  

> TODO: Re-Construct  

**The color schema is suitable under dark background color only.**   

> DONE: Add python package for managing colors   
> TODO: Add config file to choose between dark or white background color schema.

**For windows users it's recommended to use terminal emulator because of:**

- [x] Now PowerShell coloring is working fine.    
- [ ] PowerShell cyrillic:  
> Add this line to your PowerShell profile to set the right encoding for Input and Output streams.   
> ```$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding```   
> (By default the Output is working fine, but the input is not. I.E: You will not see what you type when using cyrillic.)     
> **See more on: [StackOverflow](https://stackoverflow.com/questions/39087491/powershell-replace-in-cyrillic-string)**
- [x] PowerShell is ready now!

### IDEAS FOR LAZY DAYS :smoking:

- **1.(FIRST)** Add IT terminology dictionary from **[stelf/en2bg4term](https://github.com/stelf/en2bg4term)** as local (files/db.)
- **Bulgarian README.md**
- Add English to Bulgarian translate
- Add local database
- **Grammar mode** with menu and search mode (searchquery=='grammar-rule')
- ~~Output the search to csv~~
- [x] **Book mode:**
> [x] I.E.: waiting for the next input(word) without exiting the script and save all searches from current session
- Unit tests

## **SHOWTIME**
- **Execute and count the second~~sss~~ :one: :two:**

<div>
<img src="/img/powershell-gо-gramoten.gif"
 alt="powershell"
 />
</div>  

**:three: :four:**

<div>
<img src="/img/powershell-grammatical.gif"
 alt="terminus"
 />
</div>

### **BOOK MODE**

<div>
<img src="/img/book-mode.gif"
 alt="book-mode"
 />
</div>

