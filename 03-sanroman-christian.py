import random as rand
import math

# find the number of # pads to add to name
numpads = 0

def findPadding(random_length, full_name):
	x = math.ceil(len(full_name) / random_length)
	numPads = len(full_name) - (x * random_length)
	return numPads

# input first and last name
first_name = "Christian"
last_name = "Sanroman"

# combines first and last name w/ a space
full_name = (first_name + " " + last_name)
print(len(full_name))

# outputs a randomly generated # between 1-5
random_length = rand.randint(1,5)
print(random_length)

# update string with # padding
findPadding(random_length, full_name)
padded_name = full_name.ljust(numPads,"#")

# output full name random length #s at a time
# range (), add '#' as padding
for i in range(0, padded_name, random_length):
	print(padded_name[i - random_length: i])
	
# print in lowercase first and last letters of names
print((first_name[0].lower())+(first_name[-1].lower()), last_name[0].lower()+last_name[-1].lower())

# print out the middle letters of first and last in uppercase
print((first_name[1:-1].upper()), (last_name[1:-1].upper()))

# print out every other letter in your name
print (full_name[::2])



#need to figure out the numPads to get it to work

