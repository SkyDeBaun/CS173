#CS173 spell checker
#Sky DeBaun
#Spring 2021

'''
Instructions: execute file from command line with filename parameter (the file to spell check)
ex: python spellcheck.py mobydick.txt
'''


from os import system, name
import sys
import re
import nltk
from nltk.corpus import words #basis for our spell check dictionary
from nltk.corpus import brown #ammend the dictionary with more words
from nltk.corpus import gutenberg #ammend the dictionary with more words
from nltk.corpus import gazetteers

import itertools #speed up iterating through sets (my "dictionary")
import time


#missing words list contains names or other words not present in other sources used
missing_words = ["edinburgh", "moby", "ahab", "ramadan", "quarterdeck", "whales", "grammars", "lexicons", 
"psalms", "sylphs", "leviathans", "gills", "swims", "spouts", "trans", "asiatics", "comstock", "breaches","rainbows", "mightier", "spermacetti",
"chace", "cuvier", "cowper", "suspends", "herberts", "fuzzing", "elbe", "annus", "strafford", "spitzbergen", "kinross", "schouten", "shrouds",
"nightwatch", "loitering", "reveries", "harpooned", "mastheads", "lookouts", "entrances", "hussey", "etchings", "distended", "rears", "prairies", 
"quietest", "gazers", "pierheads", "shadiest", "woodlands", "toils", "tribulations", "tigerlilies", "bulwarks", "rebounds", "whalemen", "bakehouses",
"herrings", "queequeg","impregnated", "scribed", "contortions", "contortions", "nooses", "burghers", "oarsmen", "enveloped", "realise", "halters", 
"gunwales", "neighbouring", "sheaves", "naturalists", "outstretched", "wrecks", "overlays", "spawned", "terrors", "landsmen", "specialities", "elevations",
"soundings", "disentangling", "enjoining", "surrounds", "overruns", "pulverise", "scythes", "fibres", "adhering", "pequod", "harpoons", "hydras", 
"girdled", "surges", "intents", "whalers", "knockers", "cocks", "whalers", "forecastles", "slabs", "restores", "busks", "marvellous", "clearings", 
"smithies", "torments", "leviathanic", "subscribes", "facsimiles", "garnery", "grapnels", "narwhales", "draughtsmen", "centaurs", "marvellously", 
"pecking", "fowles", "barnacled",  "oars", "profundities", "parlour", "envelops", "undulations", "limbered", "mariners", "breakfasting", "tarts",
"humps", "systematised", "fisheries", "flukes", "delineations", "embellishments", "vignettes", "perseus", "avatar", "prefigured", "brahmins", "pedestals", 
"saladin", "panellings", "delusions", "steelkilt", "procuring", "chartering", "tahitians", "befriended", "lakeman", "yoked", "corals", "descried", 
"woollen", "spangling", "christenings", "spaniards", "ordaining", "infatuated",  "speediest",  "clamour", "vultures", "maddened", "rumours", "narrates"
"narhwal", "hippogriff", "bowsman", "famishing", "parisians", "canallers", "backstays", "maledictions", "bethinking", "charlemagne", "archipelagoes", 
"repartees", "swaths", "leuwenhoeck", "predestine", "bethinking", "radney", "thunderings", "interluding", "galapagos", "provincialisms", "gamming",
"spouters",  "bowings", "descrying", "voyagings", "fullers", "upheaving", "unstaked", "bivouacs", "capsizings","interblending", "headsmen",  "goadings",
"stowaways", "rapscallions", "soliloquised", "seychelle", "seychelle", "trenchers", "ramadan", "thews", "earthsman", "wights", "snortings", "hospitalities",
"deavoured","invokingly", "heeling", "farings", "cenotaphs", "mapple", "resurrections", "caanan", "beefsteaks", "lathering", "tattooings", "flourishings",
"dreadnaught", "harpooner", "wainscots", "bermuda", "looming", "tuileries" ] 



##FUNCTIONS--------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#create set of valid words------------------------------------------- SET for fast lookups 
def create_dictionary_set(dictionary):
    print("CONSTRUCTING DICTIONARY-----------------")
    print("----------------------------------------")

    #basis--------------------------------------
    print("Processing NLTK Words...")
    for word in words.words():    
        dictionary.add(word.lower())   
    time.sleep(.5) 


    #brown--------------------------------------
    print("Processing NLTK Brown...")
    for word in brown.words():   
        dictionary.add(word.lower()) 
        pass
    time.sleep(.5)

    #gutenberg-----------------------------------
    print("Processing NLTK Gutenberg...")
    for word in brown.words():
        dictionary.add(word.lower()) 
        pass
    time.sleep(.5)

    #places--------------------------------------
    print("Processing NLTK Gazetteer...")
    for word in gazetteers.words():
        dictionary.add(word.lower())
        pass
    time.sleep(.5)

    #additional word list (https://github.com/dwyl/english-words)
    print("Ammending dictionary with 125,000 more words...")
    with open("wordlist_large_english.txt", 'r') as readfile:
        text = readfile.read()
        tokens = nltk.word_tokenize(text)
        for word in tokens:
             dictionary.add(word.lower())
             pass
    time.sleep(.5)
  

    print("Ammending dictionary with hand-curated word list...")
    for word in missing_words:        
        dictionary.add(word)
    time.sleep(.5)

    count = len(dictionary)
    print("\nDICTIONARY CREATION COMPLETE(" + format_value(count) + " words)!\n")
    time.sleep(2)



#create list of words to validate (ie spelling check)---------------- LIST for sequential access
def create_word_list(filename, wordlist):
    with open(filename, 'r') as readfile:
        text = readfile.read()
        text = re.sub(r"""[-!?'".,<>(){}@%&*/[/]""", " ", text) #strip out all extraneous characters before tokenizing
        words = nltk.word_tokenize(text)
    
        for word in words:
            word = re.sub(r'[^a-zA-Z]', '', word) #strip other extraneous nums, etc
            if not re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",word, re.IGNORECASE) and word != '': #skip roman numerals                
                wordlist.append(word.lower().strip())


#check wordlist (our text) using our dictionary------------------------
def spell_check(dictionary, wordlist):    
    badwords = set()
    for word in wordlist:
        if word not in dictionary:
            badwords.add(word)

    count = len(badwords)
    if count > 0:
        print(format_value(count) +" unknown words found --------------------")
        print("--------------------------------------------")
        time.sleep(1)

 

    for bad in iter(badwords):
        print(bad + ": ", end='', flush=True)        
        get_best_matches(bad, dictionary)


#collect set of best matches (dictionary method can not have duplicates...)
def get_best_matches(misspelling, dictionary):
    lowest = 1000 #arbitrarily high (insane) number ensures the first iteration will always change this
    candidates = set() #store set of spelling candidates

    for word in iter(dictionary):
            ed = nltk.edit_distance(misspelling, word)
            
            #if ed equal to existing lowest ed----
            if ed == lowest:
                lowest = ed
                candidates.add(word)
            #else if ed lower than existing lowest ed.. clean and start new set
            elif ed < lowest:
                lowest = ed
                candidates.clear()
                candidates.add(word)

    #print(candidates)-----------------------------
    length = len(candidates)
    count = 0
    for w in iter(candidates):
        print(w, end='')

        #print comma separators.. but not after last
        count +=1
        if count < length: 
            print(", ", end='') 

    print("\n\n", end='')
            


#clear screen (https://www.geeksforgeeks.org/clear-screen-python/)-----
def clear():  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#add commas to numeric output(https://www.geeksforgeeks.org/print-number-commas-1000-separators-python/)
def format_value(number):
    return ("{:,}".format(number))



#POPULATE DATA STRUCTURES------------------------------------------------------------
#------------------------------------------------------------------------------------

#user input-----------------------------------------------------------------------
filename = sys.argv[1] #get the filename from user input (via terminal)

clear() #lets clear the screen

dictionary = set()
create_dictionary_set(dictionary)

wordlist = []
create_word_list(filename, wordlist)


#SPELL CHECK-------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
spell_check(dictionary, wordlist)
