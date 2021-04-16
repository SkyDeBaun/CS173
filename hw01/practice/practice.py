#CS173 NTLK practice

#from: https://www.youtube.com/watch?v=WYge0KZBhe0

import nltk
text = "Hello world where isn't the corner store where they don't sell Mickey Mouse hats?"


#tokenize using regex----------------------------------
import regex
reg_result = regex.split("[\s\.\,]", text)
print("Tokenized using regex---------------------------")
print(type(reg_result))
print(reg_result)


#tokenize using nltk-------------------------------------
results = nltk.word_tokenize(text)
print("Tokenized using NLTK----------------------------")
print(type(results))
print(results)


#stemming------------------------------------------------- Porter
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

plurals = ['flies', 'dies', 'horses', 'houses', 'denies', 'agreed', 'owned', 'stating', 'itemization', 'traditional', 'colonizing', 'generously', 'spectacularly']
print("\nPorter------------------------------------------")
for word in plurals:
    print(f"{word} >>> {stemmer.stem(word)}")


#stemming------------------------------------------------- Snowball (better)
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english") #use SnowballStemmer.languages for list of applicable languages
print("\nSnowball-----------------------------------------")
for word in plurals:
    print(f"{word} >>> {stemmer.stem(word)}")


#lemmatizing------------------------------------------------ using Wordnet
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print("Lematizing------------------------------------------")
for word in plurals:
    print(f"{word} >>> {lemmatizer.lemmatize(word)}")




#from nltk.org----------------------------------------------------------------
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print ("Tagged tokens-----------------------------------------")
tagged = nltk.pos_tag(tokens)
print (type(tagged))
print(tagged[0:6])