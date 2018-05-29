import pybrary

print ("welcome to the pybrary sort tester.")
print ("we will try and keep this program more organized")

array = [2,1,4,3,8,4,5,6,3,7,3,7,8,9,6,0,43,987,12,12,12,9876,232,12,43,567]

print (" ")
print ("Our unsorted array is as follows")
print (array)
print (" ")

print ("we will begin by bubbleing our array to a sort")

array = pybrary.bubble(array)

print ("our new array:")

print (array)

