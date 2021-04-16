#cs173 spell checker
#sky debaun

import re
import nltk
from nltk.corpus import words #basis for our spell check dictionary
from nltk.corpus import brown #ammend the dictionary with more words
from nltk.corpus import gutenberg #ammend the dictionary with more words
from nltk.corpus import gazetteers
from nltk.corpus import wordnet


import time


missing_words = ["edinburgh", "moby", "ahab", "ramadan", "quarterdeck", "whales", "grammars", "lexicons", 
"psalms", "sylphs", "leviathans", "gills", "swims", "spouts", "trans", "asiatics", "comstock", "breaches","rainbows", "mightier", "spermacetti",
"chace", "cuvier", "cowper", "suspends", "herberts", "fuzzing", "elbe", "annus", "strafford", "spitzbergen", "kinross", "schouten", "shrouds",
"nightwatch", "loitering", "reveries", "harpooned", "mastheads", "lookouts", "entrances", "hussey", "etchings", "distended", "rears", "prairies", 
"quietest", "gazers", "pierheads", "shadiest", "woodlands", "toils", "tribulations", "tigerlilies", "bulwarks", "rebounds", "whalemen", "bakehouses",
"herrings", "queequeg",]

##FUNCTIONS--------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#create set of valid words------------------------------------------- SET for fast lookups -->> idea.. use multiple nltk corpora for dictionary!!!!!
def create_dictionary_set(dictionary):
    print("CREATING DICTIONARY-----------------")
    print("------------------------------------")

    #basis--------------------------------------
    print("Processing NLTK words...")
    for word in words.words():    
        dictionary.add(word.lower())    
    #brown--------------------------------------
    print("Processing NLTK brown...")
    for word in brown.words():   
        #word = re.sub(r'[^a-zA-Z]', '', word)
        dictionary.add(word.lower()) 
    #gutenberg-----------------------------------
    print("Processing NLTK gutenberg...")
    for word in brown.words():
        #word = re.sub(r'[^a-zA-Z]', '', word)
        dictionary.add(word.lower()) 
    #places--------------------------------------
    print("Processing NLTK gazetteer(locations)...")
    for word in gazetteers.words():
        dictionary.add(word.lower())

    print("Ammending dictionary with curated word list...")
    for word in missing_words:
        #print(word)
        dictionary.add(word)
        #time.sleep(.15)


    print("\nDictionary creation complete!\n")
    time.sleep(1)


#create list of words to validate (ie spelling check)---------------- LIST for sequential access
def create_word_list(filename, wordlist):
    with open(filename, 'r') as readfile:
        text = readfile.read()
        words = nltk.word_tokenize(text)
    
        for word in words:
            word = re.sub(r'[^a-zA-Z- ]', '', word)
            if not re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",word, re.IGNORECASE) and word != '': #skip roman numerals                
                wordlist.append(word.lower().strip())




def spell_check(dictionary, wordlist):    
    badwords = []
    for word in wordlist:
        if word not in dictionary:
            badwords.append(word)

    if len(badwords) > 0:
        print("Bad Words Found --------------------")
        print("------------------------------------")

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
