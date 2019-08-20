# bg-en-spellcheck

The script is scraping the web at the moment, so you need an internet connection. Тhe priority over the browser dictionaries is the speed and simplicity of how information is presenting. The goal of the project is to add more functionality like grammar rules, local database, sentence translate and analyse. 

#### Features

- Spellcheck
- Word meaning, Sentense usage
- Synonyms, Translate 
- 2 times faster than browser dictionaries, no javascript, no ads 
- Terminal simplicity

#### Requirements

- Python 3
- beautifulsoup4
- html5lib

#### Install

**It is always good practice to create separate virtual env !** 

**Windows**

```
git clone https://github.com/ihatemodels/bg-en-spellcheck
pip install -r requirements.txt 
```

**Linux**

```
git clone https://github.com/ihatemodels/bg-en-spellcheck
cd bg-en-spellcheck
pip3 install -r requirements.txt 
chmod +x spellcheck.py  
```

#### Usage

**python3 spellcheck.py -t -s -i [word]**

- **-t --translate [optional]** Translate from Bulgarian to English with examples
  -    TODO: Add English to Bulgarian translate
- **-d- -details [optional]** Display synonyms, word meaning, detailed information 
- **-i --input [required]** Word to work with ( *The script will detect the input language ! )*

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

#### TODO

- Bulgarian README.md
- More language support 
- Add local database and save every search 
- Unit tests
- Many more

#### TOFIX

the html5lib used to scrape dict.org is really slow




