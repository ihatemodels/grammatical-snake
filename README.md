# Bg-En-Spellcheck

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

#### Features

- Spellcheck
- Word meaning, Sentense usage
- Synonyms, Translate 
- 2 times faster than browser dictionaries, no javascript, no ads 
- Terminal simplicity

#### Requirements

- Python 3
- beautifulsoup4
- googletrans
- html5lib

#### Install

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

- **-t --translate [optional]** Translate from en to bg or backwards
- **-s --synonyms [optional]** Display synonyms 
- **-i --input [required]** Word to work with ( *The script will detect the input language ! )*

#### TODO

- Bulgarian README
- More languages support 
- More dicts to scrape 
