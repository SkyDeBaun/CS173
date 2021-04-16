#cs173 spell checker
#sky debaun

import re
import nltk
from nltk.corpus import words #basis for our spell check dictionary
from nltk.corpus import brown #ammend the dictionary with more words
import time

##FUNCTIONS--------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#create set of valid words------------------------------------------- SET for fast lookups -->> idea.. use multiple nltk corpora for dictionary!!!!!
def create_dictionary_set(dictionary):
    #basis--------------------------------------
    for word in words.words():    
        dictionary.add(word.lower())    
    #brown--------------------------------------
    #add brown and others to dictionary    


#create list of words to validate (ie spelling check)---------------- LIST for sequential access
def create_word_list(filename, wordlist):
    with open(filename, 'r') as readfile:
        text = readfile.read()
        words = nltk.word_tokenize(text)
    
        for word in words:
            word = re.sub(r'[^a-zA-Z]', '', word)
            if word != '': #these aren't getting striped out
                wordlist.append(word.lower().strip())




def spell_check(dictionary, wordlist):    
    badwords = []
    for word in wordlist:
        if word not in dictionary:
            badwords.append(word)

    if len(badwords) > 0:
        print("Bad Words: ")
        for bad in badwords:
            print(bad)
            time.sleep(.25)





#POPULATE DATA STRUCTURES------------------------------------------------------------
#------------------------------------------------------------------------------------

dictionary = set()
create_dictionary_set(dictionary)
#print(dictionary)


wordlist = []
create_word_list('practice/mobydick.txt', wordlist)
#print(wordlist)


#SPELL CHECK-------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
spell_check(dictionary, wordlist)
