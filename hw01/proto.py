#cs173 spell checker
#sky debaun

import re
import nltk
from nltk.corpus import words #basis for our spell check dictionary
from nltk.corpus import brown #ammend the dictionary with more words
from nltk.corpus import gutenberg #ammend the dictionary with more words
from nltk.corpus import gazetteers

from os import system, name
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
"dreadnaught", "harpooner", "wainscots", "bermuda" ] 

##FUNCTIONS--------------------------------------------------------------------------
#------------------------------------------------------------------------------------

#create set of valid words------------------------------------------- SET for fast lookups -->> idea.. use multiple nltk corpora for dictionary!!!!!
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
        #word = re.sub(r'[^a-zA-Z]', '', word)
        dictionary.add(word.lower()) 
    time.sleep(.5)

    #gutenberg-----------------------------------
    print("Processing NLTK Gutenberg...")
    for word in brown.words():
        #word = re.sub(r'[^a-zA-Z]', '', word)
        dictionary.add(word.lower()) 
    time.sleep(.5)

    #places--------------------------------------
    print("Processing NLTK Gazetteer(locations)...")
    for word in gazetteers.words():
        dictionary.add(word.lower())
    time.sleep(.5)

    #additional word list (https://github.com/dwyl/english-words)
    print("Ammending dictionary with 466,000 additional words...")
    with open("wordlist_large_english.txt", 'r') as readfile:
        text = readfile.read()
        tokens = nltk.word_tokenize(text)
        for word in tokens:
             dictionary.add(word.lower())
    time.sleep(.5)

    print("Ammending dictionary with hand-curated word list...")
    for word in missing_words:        
        dictionary.add(word)
    time.sleep(.5)

    print("\nDICTIONARY CREATION COMPLETE!\n")
    time.sleep(2)


#create list of words to validate (ie spelling check)---------------- LIST for sequential access
def create_word_list(filename, wordlist):
    with open(filename, 'r') as readfile:
        text = readfile.read()
        text = re.sub(r"""[-!?'".,<>(){}@%&*/[/]""", " ", text) #strip out all extraneous characters before tokenizing
        words = nltk.word_tokenize(text)
    
        for word in words:
            word = re.sub(r'[^a-zA-Z]', '', word) #strip extraneous chars, nums, etc
            if not re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",word, re.IGNORECASE) and word != '': #skip roman numerals                
                wordlist.append(word.lower().strip())




def spell_check(dictionary, wordlist):    
    badwords = []
    for word in wordlist:
        if word not in dictionary:
            badwords.append(word)

    count = len(badwords)
    if count > 0:
        print(str(count) +" bad Words Found --------------------")
        print("-----------------------------------------")
        time.sleep(2)

        for bad in badwords:
            #print(bad + ": " + spell(bad))
            print(bad)
            #time.sleep(.25)

#clear screen (https://www.geeksforgeeks.org/clear-screen-python/)
def clear():  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



#POPULATE DATA STRUCTURES------------------------------------------------------------
#------------------------------------------------------------------------------------
clear() #lets clear the screen

dictionary = set()
create_dictionary_set(dictionary)
#print(dictionary)


wordlist = []
create_word_list('practice/mobydick.txt', wordlist)
#print(wordlist)


#SPELL CHECK-------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
spell_check(dictionary, wordlist)
