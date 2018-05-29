"""
Date: 23042018
Programer: Willpiam
Description:

A library to do a tone of stuff. This way when I have tasks at school I don't have
to write code I already have.

Jokes will liely be made throughout the program in the form of comments

functions will be grouped into catagories (ie sorts, writing / readings)

"""
import random

#-----------sorting algorithums (and sort/array related functions)

def insertion(array, small_big = True):
    if (small_big == True):
        try:
            for i in range (1,len(array)):
                hold = array[i]
                j = i-1
                while (j >=0) and (hold < array[j]):
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = hold
        except IndexError:
            print ("SOMETHING WENT WRONG WHILE SORTING WITH INSERTION SORT")
    elif (small_big == False):
        try:
            for i in range (1,len(array)):
                hold = array[i]
                j = i-1
                while (j >=0) and (hold > array[j]):
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = hold
        except IndexError:
            print ("SOMETHING WENT WRONG WHILE SORTING WITH INSERTION SORT")        
    return array


def bubble(array):#bubble sort
    try:#using try we can make sure the list is viable
        lnth = len(array)#gets length of array
        temp = 0#declaring our tempary varable (needed for sort)
        for i in range (0,lnth):
            for k in range (0,lnth-1):
                if (array[k] > array[k+1]):
                    temp = array[k]
                    array[k] = array[k+1]
                    array[k+1] = temp
    except ValueError:
        print ("your list is bad. ¯\_(ツ)_/¯")
    return array

def shuffle(array):#shuffles array 
    random.shuffle(array)
    return array

def isDecending(array):
    fact = True
    for i in range (0, len(array)-1):
        if (array[i] < array[i+1]):
            fact = False
            break
    return fact

def isAscending(array):
    fact = True
    for i in range (0, len(array)-1):
        if (array[i] > array[i+1]):
            fact = False
            break
    return fact

def bogo(array):#just bogo sort (same as bogo_b_to_s)
    unsorted = True
    while (unsorted == True):
        if (isDecending(array) == True):
            break
        else:
            array = shuffle(array)
    return array

def bogo_b_to_s(array):#bogo sort to make big to small
    unsorted = True
    while (unsorted == True):
        if (isDecending(array) == True):
            break
        else:
            array = shuffle(array)
    return array

def bogo_s_to_b(array):#bogo sort to make small to big
    unsorted = True
    while (unsorted == True):
        if (isAscending(array) == True):
            break
        else:
            array = shuffle(array)
    return array


#----------------file related functions

def fileLen(fileName):#gets length of file
    with open(fileName) as f:
        for i, l in enumerate(f):
            pass
        return i +1
    #lifted from: https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python#1019572
    
    
def readFile(fileName):
    file = open(fileName, "r")
    array = []
    i = 0
    for i in range (0, fileLen(fileName)):
        array.append(file.readline())
        array[i] = array[i].rstrip()
    return array

def writeArray(fileName, array):#takes a filename and an array and writes each element of the array to the file (it may create a
    file = open(fileName, "w")#opens file with append premission
    for i in range (0, len(array)):
        file.write(str(array[i])+"\n")
    file.close()

def varToFile(fileName, var):#writes to file
    try:
        file = open(fileName, "w")#opens file with write premission
        file.write(str(var)+"\n")
        file.close()
    except:
        print ("something went wrong with function---> varToFile")
        
def appFile(fileName, var):#appends to file
    try:
        file = open(fileName, "a")#opens file with append premission
        file.write(str(var)+"\n")
        file.close()
    except:
        print ("something went wrong with function---> varToFile")

def appArrayToFile(fileName, array):#takes a filename and an array and writes each element of the array to the file (it may create a
    file = open(fileName, "a")#opens file with append premission
    for i in range (0, len(array)):
        file.write(str(array[i])+"\n")
    file.close()

#-----------------String stuff
def morse_from_eng(var):
    var = var.upper()
    var = var.replace("A", ".-")
    var = var.replace("B", "-...")
    var = var.replace("C", "-.-.")
    var = var.replace("D", "-..")
    var = var.replace("E", ".")
    var = var.replace("F", "..-.")
    var = var.replace("G", "--.")
    var = var.replace("I", "..")
    var = var.replace("H", "....")
    var = var.replace("J", ".---")
    var = var.replace("K", "-.-")
    var = var.replace("L", ".-..")
    var = var.replace("M", "--")
    var = var.replace("N", "-.")
    var = var.replace("O", "---")
    var = var.replace("P", ".--.")
    var = var.replace("Q", "--.-")
    var = var.replace("R", ".-.")
    var = var.replace("S", "...")
    var = var.replace("T", "-")
    var = var.replace("U", "..-")
    var = var.replace("V", "...-")
    var = var.replace("W", ".--")
    var = var.replace("X", "-..-")
    var = var.replace("Y", "-.--")
    var = var.replace("Z", "--..")
    var = var.replace("1", ".----")
    var = var.replace("2", "..---")
    var = var.replace("3", "...--")
    var = var.replace("4", "....-")
    var = var.replace("5", ".....")
    var = var.replace("6", "-....")
    var = var.replace("7", "--...")
    var = var.replace("8", "---..")
    var = var.replace("9", "----.")
    var = var.replace("0", "-----")    
    return var
    
    
        
