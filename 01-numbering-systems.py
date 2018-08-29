num = 54

#convert the int to hex
print ("------Dec to Hex-----")
print (num)
print (hex(num))


#convert base 10 to binary
print ("-----Dec to Bin----")
print (num)
print (bin(num))


#------------------------------------

print ("------Dec to Bin using format"------)
print (num)
print (format(num, "#010b"))


print ("-----Dec to Hex, Oct, and Bin! using format")
print (num)
print ("{0!s}{0:#04x}{0:#05o}{0:010b}".format(num))
