import nltk
import sys

text = "I ate fruit the entire day. For breakfast, I had dates. For lunch, I had mangoes. For dinner, I had cantaloupe."

#test run----------------------------------------------- count sentences of a string var
#sentences = nltk.sent_tokenize(text)
#print("Test Count: ")
#print(len(sentences))


filename = sys.argv[1] #get the filename from user input (via terminal)

#print count of sentences from a given file--------------
def count_sentences(filename):
    with open(filename, 'r') as infile:
        text = infile.read()
        sentences = nltk.sent_tokenize(text)
        count = len(sentences)
        print("Sentence count of " + filename + ": " + str(count) + "\n")


count_sentences(filename)
