import re

with open('mobydick.txt', 'r') as infile:
    text = infile.read()


    result = re.findall("Ishmael", text)
    print(result)
    print(len(result))



    count = len(re.findall("\bIshmael\b", text))
    print(count)