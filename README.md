# Bg-En-Spellcheck

#### Features

- Spellcheck
- Synonyms 
- Translate 
- 2 times faster than browser dictionaries
- No javascript, no ads 
- Terminal simplicity


#### Requirements

- Python 3
- beautifulsoup4
- googletrans
- html5lib

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

- -t --translate [optional] Translate from en to bg or backwards
- -s --synonyms [optional] Display synonyms 
- -i --input [required] Word to work with

#### TODO
- Bulgarian README
- More languages support 
- More dicts to scrape 




