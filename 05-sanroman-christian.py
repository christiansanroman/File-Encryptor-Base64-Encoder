# base 64 encoder using only the ord and bin functions

import numpy as np

# output should be bW91bnRhaW4=
base64_dict = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z",
26:"a",27:"b",28:"c",29:"d",30:"e",31:"f",32:"g",33:"h",34:"i",35:"j",36:"k",37:"l",38:"m",39:"n",40:"o",41:"p",42:"q",43:"r",44:"s",45:"t",46:"u",47:"v",48:"w",49:"x",50:"y",51:"z",52:"0",53:"1",54:"2",55:"3",56:"4",57:"5",58:"6",59:"7",60:"8",61:"9",62:"+",63:"/"}

# string to be converted
#input_str = ""
input_str = input("\nEnter the string to encode: ")

#1 string to ascii val
ascii_vals = []
#2 ascii value to 8bit binary
bin_arr = []
#3 8 bit binary to 6 bit
#4 6 bit to decimal
#5 use decimal to lookup base64 symbol

# for loop to get the 8 bit binary values
for i in input_str:
	# convert each letter to a decimal
	ascii_dec = ord(i)
	# add these to ascii array to check if inputs are correct
	ascii_vals.append(ascii_dec)
	# convert the decimal values calculated aboeve to binary
	binToAsc = bin(ascii_dec)[2:].zfill(8)
	bin_arr.append(binToAsc)

# check to ensure the values are correct	
#print(ascii_vals)
#print(bin_arr)

# breaking the 8 bit binary values into 6 bit
# convert the 8 bit binary values to one long string
bin_to_sixbit = ''.join(map(str, bin_arr))

# check to see if there 6 bit binary values can be created
# if 6 doesnt go the length of the long binary string- add 0s on the end until it does
while len(bin_to_sixbit) % 6 != 0:
	bin_to_sixbit = bin_to_sixbit + "0"

#print(bin_to_sixbit)

# loop to break up the long string into 6 bit parts
six_bit = []
for i in range(0, len(bin_to_sixbit), 6):
	sb = bin_to_sixbit[i:i+6]
	six_bit.append(sb)

#print(six_bit)

# convert the 6 bit binary numbers into decimals 
base_64 = []
# i is each 6 bit representation
for i in six_bit:
	# convert the 6 bit to str to get the length of characters
	str_sb = str(i)
	len_sb = len(str_sb)
	# j is each 0 or 1 in the 6 bit binary
	for j in str_sb:
		# count will be used to figure out the place value for base 2
		# initialize at -1 of the length of str since we need to find 2^0	
		count = len_sb - 1 
		# this is the calculation to find base 2 values. 2**count is 2 to power
		# multiple the base 2 value by the binary value
		baseTwo = (2**(count)) * int(j)
		base_64.append(baseTwo)
		#print (count, j)
		len_sb = len_sb - 1

#print (base_64)

# loop to find the sum of the 6 bit binary
b64_val = []
# use this loop to select 6 values at a time to take the sum of
for i in range(0, len(base_64),6):
	# this selects 6 values at a time- increasing by 6 every time
	six_sum = (base_64[i:i+6])
	#print(six_elem)
	# take the sum of the 6 values collected
	val = np.sum(six_sum)
	b64_val.append(val)
	
#print(b64_val)

end = []
# lookup in base64 dictionary and try to find matching values from decimals
for i in b64_val:
	for k, v in base64_dict.items():
		# if the key in the dictionary matches the decimal
		if k == i:
			# add the dictionary value (aka base64 symbol)
			end.append(v)

#print(end)

# print the base 64 encoded symbols as string using map for each value in the array
b64_end = ''.join(map(str, end)) + "="

print("\nBase 64 encoding:", b64_end)

