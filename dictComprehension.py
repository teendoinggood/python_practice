# initialize list
letters = ['a', 'b', 'c', 'd', 'e']

# dictionary, key is i, value is i.upper()
upperLetters = {i:i.upper() for i in letters}
print upperLetters

# print dictionary keys
print "keys are: " + ", ".join(upperLetters.keys())

# print dictionary values
print "values are: " + ", ".join(upperLetters.values())

for i in letters:
	print upperLetters[i]

# iterate using dictionary keys
for i in upperLetters.keys():
	print upperLetters[i]

# need to place : after for loop
# need identation in for loop
