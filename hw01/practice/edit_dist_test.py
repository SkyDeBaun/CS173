
import nltk

mistake = "unob"

words = ['nob', 'knob', 'unos', 'uno', 'snob']

for word in words:
    ed = nltk.edit_distance(mistake, word)
    print(word, ed)

myList = [1, 2, "MUO", "Google"]
thisset = set(("apple", "banana", "cherry"))
print(thisset)


thisset = set(myList)

for word in thisset:
	print(word)




