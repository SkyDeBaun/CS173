from nltk.corpus import names
from nltk.corpus import gazetteers
from nltk.corpus import wordnet

import re
import time


synonyms = []

for word in gazetteers.words():
    print(word)
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())

    print(set(synonyms))
    synonyms.clear()
    time.sleep(3)