
import pybrary

import random
lst = []

for i in range (0,1000):
    lst.append(random.randint(0,100))

lst = pybrary.insertion(lst)
for i in range (0,len(lst)):
    print (lst[i])

lst = pybrary.insertion(lst, False)
for i in range (0,len(lst)):
    print (lst[i])

print ("ig-------------------------------------------ig")
print ("length of file")
print (pybrary.fileLen("fileToRead.md"))

lst = pybrary.shuffle(lst)
for i in range (0,len(lst)):
    print (lst[i])

array = [7,6,4,3,1,24,3,2,876]

var = "the quick brown fox jumped over the lazy doge"

var = pybrary.morse_from_eng(var)
print (var)

"""print (pybrary.isAscending(array))
array = pybrary.bubble(array)
print (pybrary.isAscending(array))"""
print (" ")
print (" ")
print (" ")
array = pybrary.bogo(array)
for i in range (0,len(array)):
    print (array[i])
"""
array = pybrary.readFile("fileToRead.md")
#print (array)
print ("over")
for i in range (0, len(array)):
    print (array[i])

pybrary.appArrayToFile("deletMe.txt",[0,2,4,3,4,5,6,7,987,32,123])

pybrary.appFile("file.txt", 5)
"""
