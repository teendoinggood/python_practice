mySet = range(1,10)

newSet = [i+1 for i in mySet]
print newSet

newSet = [i+1 for i in mySet if i%3==0]
print newSet

newSet = [i**2 for i in mySet]
print newSet
