# bg-en-spellcheck

The script is scraping the web at the moment, and you need an internet connection. So far supported languages are Bulgarian, and English. Тhe priority over the browser dictionaries is the speed and simplicity of how information is presenting. The goal of the project is to add more functionality like grammar rules, local database, sentence-translate, write style analysе, more languages support and many more.

## Features

- Spellcheck.
- Word meaning, Sentense usage
- Synonyms, Translate 
- Faster than browser dictionaries, no javascript, no ads. 
- Terminal simplicity.

### Requirements

- Python 3
- beautifulsoup4
- html5lib

### Install

**It is always good practice to create separate virtual env !** 

- **Windows**

```
git clone https://github.com/ihatemodels/bg-en-spellcheck
pip install -r requirements.txt 
```

- **Linux**

```
git clone https://github.com/ihatemodels/bg-en-spellcheck
cd bg-en-spellcheck
pip3 install -r requirements.txt 
chmod +x spellcheck.py  
```

### Usage

**python3 spellcheck.py -t -d -i [word]**

- **-t --translate [optional]** Translate from Bulgarian to English with examples.
  -    TODO: Add English to Bulgarian translate
- **-d- -details [optional]** Display synonyms and examples. 
- **-i --input [required]** Word to work with. ( *The script will detect the input language ! )*

<div>
<img src="/img/gif-en.gif"
 alt="en-spellcheck"
 />
</div>

<div>
<img src="/img/gif-bg.gif"
 alt="bg-spellcheck"
 />
</div>

#### Powered by:

[Rechnik.info](http://rechnik.info)
[Slovored](https://slovored.com/)
[Lexico](https://www.lexico.com) 
[Collinsdict](https://www.collinsdictionary.com)
[Yourdictionary](https://sentence.yourdictionary.com)
[Dict.org](http://www.dict.org)

#### TODO

- Bulgarian README.md
- More language support
- Add local database and save every search
- Unit tests
- Many more
