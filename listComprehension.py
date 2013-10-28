myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def display(myList):
	return ", ".join([str(i) for i in myList])
			
# add 1 to each elem
add1List = [i+1 for i in myList]
print "add 1 to each element of list: " +  display(add1List)

# minus 1 to each elem
minus1List = [i-1 for i in myList]
print "minus 1 to each element of list: " + display(minus1List)

# filter list to get odd numbers
oddList = [i for i in myList if i%2==1]
print "odd numbers are: " + display(oddList)

# filter list to get even numbers
evenList = [i for i in myList if i&1==0]
print "even numbers are: " + display(evenList)

# we can do the above in 1 line
import math
complexList = [(i+1, i-1, pow(2, i)) for i in myList]
print complexList
