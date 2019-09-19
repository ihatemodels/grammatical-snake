import re
from collections import Counter
from collections import OrderedDict

def is_cyrillic(word):
    '''Verify the input language '''
    return bool(re.search("[а-яА-Я]", word))

with open ('./docs/bg/grammar-rules/koito-kogoto.txt','r+',encoding='UTF-8') as f:
    data = f.read()

# Split the text into words without special character

def into_words(text):
    return re.findall(r'\w+',text)

# Count the words
countable_text = Counter(into_words(data))

# Clear the text from 2 letters based words 

spellcheck_words = []
word_freq = ''

for key,value in countable_text.items():
    if len(key) > 2:
        if is_cyrillic(key):
            spellcheck_words.append(key.lower())
    if len(key) > 2 and value > 5:
        word_freq += key + ' -> ' + str(value) + '\n'
       

print(spellcheck_words)
print(word_freq)