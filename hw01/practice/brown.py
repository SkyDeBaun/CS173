from nltk.corpus import brown
import re


for word in brown.words():
    word = re.sub(r'[^a-zA-Z]', '', word)
    print(word)