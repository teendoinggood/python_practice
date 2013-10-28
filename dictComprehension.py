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


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

powof2 = {i: pow(2, i) for i in digits if i%2 == 0}

print powof2

# why it has syntax error ?
# print "keys are: " + ", ".join([str(i) for i in powof2.keys()])
# print "values are: " + ", ".join(([str(i) for i in powof2.values()])
print "length is: " + str(len(powof2))

for i in digits:
	if i%2 == 0:
		print str(i) + "->" + str(powof2[i])

for i in powof2.keys():
	print str(i) + "->" + str(powof2[i])

print "using items()"
for key, value in powof2.items():
	print str(key) + "->" + str(value)
