import random as rand

# input first and last names below
first_name = "chistian"
last_name = "san roman"

# determine length of first + last name
max = len(first_name) + len(last_name)

# if length of names is less or equal to 15 set length to 20
if max <= 15:
	max = 20

# 5 unique numbers between 1 and max and ascending order
lucky = rand.sample(range(1,max),5) 

# sort the 5 digits in ascending order
lucky = sorted(lucky)

# 1 unique number between 1 and max*2
unlucky = rand.sample(range(1, max*2), 1) #cannot repeat


# output name, lucky and unlucky numbers
print("Hi, " + first_name + " " + last_name)
print("Your lucky numbers are between 1 and " + str(max))
print("Your lucky numbers are: " + str(lucky))
print("Your unlucky number is between 1 and " + str(max*2))
print("Your unlucky number is: " + str(unlucky)) 
