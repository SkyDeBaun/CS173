#Script used to find longest word in a text file (from hw#1 question 3e)

#from: https://followtutorials.com/2019/04/python-program-to-find-the-longest-words-in-a-file.html



def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_words('mobydick_snt/tokens.txt'))