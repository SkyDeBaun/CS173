import re 

f = open ("mobydick.txt", 'r')
data = f.readlines()
print(type(data))
print(data)




newdata = list(map(lambda x: x.strip(), data))
print(type(newdata))
print(newdata)

#alternate versions:
newdata = list()
for x in data:
    x = x.strip()
    newdata.append(x)

#or:
newdata = list(map(str.strip, data)) #using map

#or:
newdata = [x.strip() for x in data] #list comprehension?