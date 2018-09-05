# import libaries------------------------------------------
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
import os, random, sys, pkg_resources


#encryptor---------------------------------------------------
def encrypt(key, filename):
	# chunks we pull out of the file
	chunksize = 64 * 1024
	# name of the file after it is encrypted
	outfile = "(encrypted)" + filename
	#outfile = os.path.join(os.path.dirname(filename), "(encrytped)" + os.path.basename(filename))
	# string and pad to 16 bytes	
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	# select which encryption algorithm, MODE_CBC = chained cypherblock
	encryptor = AES.new(key, AES.MODE_CBC, IV)

	# rb = read binary
	with open(filename, 'rb') as infile:
		# 'wb' = write binary
		with open(filename, 'wb') as outfile:
			outfile.write(filesize.encode('utf-8'))
			# use IV to decrypt
			outfile.write(IV)

			while True:
				chunk = infile.read(chunksize)

				# if there is nothing in chunk break out of while
				if len(chunk) == 0:
					break

				elif len(chunk) % 16 != 0:
					# pad the chunk with spaces of remainder
					chunk += ' ' * (16 - (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))


#decryptor--------------------------------------------------
def decrypt(key, filename):
	
	#outfile = os.path.join(os.path.dirname(filename), os.path.basename(filename[11:]))
	chunksize = 64 * 1024
	outfile = filename[11:]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		# encryption algorithm, CBC = chained cypherblock
		decrpytor = AES.new(key, AES.MODE_CBC, IV)

		with open(outfile, 'wb') as outfile:

			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))

			outfile.truncate(filesize)


#main program----------------------------------------------

def getKey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	# return the hashed result of our input
	return hasher.digest()

def Main():
	choice = input("Do you want to (E)ncrypt or (D)ecrypt? ")
	if choice == 'E':
		filename = input("File to encrypt: ")
		password = input("Password: ")
		encrypt(getKey(password), filename)
		print ("Done")

			
	if choice == 'D':
		filename = input("File to decrypt: ")
		password = input("Password: ")
		decrypt(getKey(password), filename)
		print ("Done")

	else: 
		print ("No option selected, closing...")




if __name__ == '__main__':
	Main()



		#for tfiles in encfiles:
		#	if os.path.basename(tfiles).startswith("(encrypted)"):
		#		print ("%s is alreat encrypted") %str(tfiles)
		#		pass
		
		#	elif tfiles == ps.path.join(os.getcwd(), sys.argv[0]):
		#		pass
		
		#	else: 
		#	encrypt(SHA256.new(password).digest(), str(tfiles))
		#	print ("Done encrypting %s") %str(tfiles)
		#	os.remove(tfiles)


#elif choice == 'D':
#	filename = raw_input("\nEnter the filename to decrypt:\n")
#	if not os.path.exists(filename):
#		print ("The file does not exist")
#		sys.exit(0)

#	elif not filename.startswith("(encrypted)"):
#		print ("%s is not encrypted") %filename
#		sys.exit(0)

#	else:
#		decrypt(SHA256.new(password).digest(), filename)
#		print ("Done decrypting %s") %filename
#		os.remove(filename)

#else:
#	print ("Please select a valid comment")
#	sys.exit(0) 	



#----------------
#def allfiles():
#	allfiles = []

#	for root, subfiles, files in os.walk(os.getcwd()):
#		for names in files:
#			allfiles.append(os.path.join(root, names))

#	return allfiles


#Resources
# https://null-byte.wonderhowto.com/how-to/create-encryption-program-with-python-0164249/
	
